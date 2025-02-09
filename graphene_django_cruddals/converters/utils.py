import re
from collections import OrderedDict
from collections.abc import Callable
from enum import Enum as PyEnum
from functools import wraps
from typing import Callable as CallableType, Type, Union

from django.db.models import (
    Field as DjangoField,
)
from django.db.models.fields import NOT_PROVIDED
from django.db.models.manager import Manager
from django.db.models.query import QuerySet as DjangoQuerySet
from django.utils.encoding import force_str
from django.utils.functional import Promise
from django.utils.module_loading import import_string
from graphene_cruddals import TypesMutation, TypesMutationEnum
from graphene_django.settings import graphene_settings
from graphql import GraphQLError, Undefined, assert_name
from text_unidecode import unidecode

import graphene
from graphene import ObjectType
from graphene.utils.str_converters import to_camel_case
from graphene_django_cruddals.converters.compat import ChoicesMeta


def get_django_field_description(field: DjangoField):
    if hasattr(field, "help_text") and field.help_text:
        return str(field.help_text)


def get_django_field_is_required(field: DjangoField):
    try:
        blank = field.blank
        default = getattr(field, "default", None)
        if default is None:
            default = NOT_PROVIDED
        return not blank and default == NOT_PROVIDED
    except AttributeError:
        try:
            null = field.null
            default = getattr(field, "default", None)
            if default is None:
                default = NOT_PROVIDED
            return not null and default == NOT_PROVIDED
        except AttributeError:
            return False


def get_django_field_default(field: DjangoField):
    if isinstance(type(field.default), ChoicesMeta):
        return field.default.value
    if (
        isinstance(field.default, Promise)
        or callable(field.default)
        or field.default == NOT_PROVIDED
    ):
        return Undefined
    return field.default


class BlankValueField(graphene.Field):
    def wrap_resolve(self, parent_resolver):
        resolver = self.resolver or parent_resolver

        # create custom resolver
        def blank_field_wrapper(func):
            @wraps(func)
            def wrapped_resolver(*args, **kwargs):
                return_value = func(*args, **kwargs)
                if return_value == "":
                    return None
                return return_value

            return wrapped_resolver

        return blank_field_wrapper(resolver)


def to_const(string):
    return re.sub(r"[\W|^]+", "_", unidecode(string)).upper()


def convert_choice_name(name):
    name = to_const(force_str(name))
    try:
        assert_name(name)
    except GraphQLError:
        name = f"A_{name}"
    return name


def get_choices(choices):
    converted_names = []
    if isinstance(choices, (OrderedDict, dict)):
        choices = choices.items()
    elif isinstance(choices, ChoicesMeta):
        choices = choices.choices  # This is for the case of a Django Enum
    elif isinstance(choices, Callable):
        choices = choices()
    for value, help_text in choices:
        if isinstance(help_text, (tuple, list)):
            yield from get_choices(help_text)
        else:
            name = convert_choice_name(value)
            while name in converted_names:
                name += "_" + str(len(converted_names))
            converted_names.append(name)
            description = str(help_text)
            yield name, value, description


def convert_choices_to_named_enum_with_descriptions(
    name: str, choices
) -> Type[graphene.Enum]:
    choices = list(get_choices(choices))
    internal_name = 0
    value = 1
    description = 2
    named_choices = [(choice[internal_name], choice[value]) for choice in choices]
    named_choices_descriptions = {
        choice[internal_name]: choice[description] for choice in choices
    }

    class EnumWithDescriptionsType:
        name: str

        @property
        def description(self):
            return str(named_choices_descriptions[self.name])

    # graphene.Enum( name, named_choices, type=EnumWithDescriptionsType ) # the method __call__ of EnumMeta will be called and will return the Enum class, so for this reason return_type is a class and not an instance
    return graphene.Enum.from_enum(
        PyEnum(name, named_choices, type=EnumWithDescriptionsType)
    )


def generate_enum_name(django_model_meta, field):
    if graphene_settings.DJANGO_CHOICE_FIELD_ENUM_CUSTOM_NAME:
        custom_func = import_string(
            graphene_settings.DJANGO_CHOICE_FIELD_ENUM_CUSTOM_NAME  # type: ignore
        )
        name = custom_func(field)
    elif graphene_settings.DJANGO_CHOICE_FIELD_ENUM_V2_NAMING is True:
        name = to_camel_case(f"{django_model_meta.object_name}_{field.name}")
    else:
        name = f"{to_camel_case(django_model_meta.app_label.title())}{django_model_meta.object_name}{to_camel_case(field.name.title())}Choices"
    return name


def convert_choice_field_to_graphene_enum(
    field, name=None, type_mutation: Union[TypesMutation, None] = None
):
    if name is None:
        name = generate_enum_name(field.model._meta, field)
    choices = field.choices
    EnumCls = convert_choices_to_named_enum_with_descriptions(name, choices)

    if type_mutation is None:
        enum = EnumCls(
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
        ).mount_as(BlankValueField)
    elif type_mutation == TypesMutationEnum.CREATE.value:
        enum = EnumCls(
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
            default_value=get_django_field_default(field),
        ).InputField()
    elif (
        type_mutation == TypesMutationEnum.UPDATE.value
        or type_mutation == TypesMutationEnum.CREATE_UPDATE.value
    ):
        enum = EnumCls(description=get_django_field_description(field)).InputField()

    # I should know how this type that is mounted as a Field, work as Argument or InputField
    return enum


def get_unbound_function(func):
    if not getattr(func, "__self__", True):
        return func.__func__
    return func


def maybe_queryset(value: Union[DjangoQuerySet, Manager]) -> DjangoQuerySet:
    if isinstance(value, Manager):
        value = value.get_queryset()
    return value


def get_function_for_type(graphene_type, func_name, name) -> Union[CallableType, None]:
    """Gets a resolver function for a given ObjectType"""
    if not issubclass(graphene_type, ObjectType):
        return None

    resolver = getattr(graphene_type, func_name, None)
    if resolver:
        return get_unbound_function(resolver)

    for interface in graphene_type._meta.interfaces:
        interface_resolver = getattr(interface, func_name, None)
        if interface_resolver:
            return get_unbound_function(interface_resolver)

    return None


def resolve_for_relation_field(field, model, _type, root, info, **args):
    queryset = None
    attname = field.name
    default_value = getattr(field, "default", None)
    instance = getattr(root, attname, default_value)
    if instance is None:
        return None
    elif isinstance(instance, Manager):
        queryset = instance.get_queryset()
    else:
        queryset = model.objects.filter(id=instance.id)
    queryset = maybe_queryset(_type.get_objects(queryset, info))
    try:
        return queryset.distinct().get()
    except model.DoesNotExist:
        return None
