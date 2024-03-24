import re
from collections import OrderedDict
from functools import wraps

import graphene
from django.utils.encoding import force_str
from django.utils.module_loading import import_string
from graphene.utils.str_converters import to_camel_case
from graphql import GraphQLError, assert_name
from text_unidecode import unidecode

from graphene_django_cruddals.registry_global import RegistryGlobal
from graphene_django.settings import graphene_settings
from django.db.models import Field as DjangoField
from django.db.models.fields import NOT_PROVIDED

from graphene_django_cruddals.types import TypeRegistryForField


# region === CONVERTER FOR FIELD WITH CHOICES
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


def get_django_field_description(field):
    if hasattr(field, "help_text") and field.help_text:
        return str(field.help_text)


def convert_choice_name(name):
    name = to_const(force_str(name))
    try:
        assert_name(name)
    except GraphQLError:
        name = "A_%s" % name
    return name


def get_choices(choices):
    converted_names = []
    if isinstance(choices, OrderedDict):
        choices = choices.items()
    for value, help_text in choices:
        if isinstance(help_text, (tuple, list)):
            yield from get_choices(help_text)
        else:
            name = convert_choice_name(value)
            while name in converted_names:
                name += "_" + str(len(converted_names))
            converted_names.append(name)
            description = str(
                help_text
            )  # TODO: translatable description: https://github.com/graphql-python/graphql-core-next/issues/58
            yield name, value, description


def convert_choices_to_named_enum_with_descriptions(name:str, choices) -> graphene.Enum:
    choices = list(get_choices(choices))
    # 0 = name, 1 = value, 2 = description
    named_choices = [(choice[0], choice[1]) for choice in choices]
    named_choices_descriptions = {choice[0]: choice[2] for choice in choices}

    class EnumWithDescriptionsType:
        name:str
        @property
        def description(self):
            return str(named_choices_descriptions[self.name])

    return_type = graphene.Enum(
        name,
        named_choices,
        type=EnumWithDescriptionsType,
        description="An enumeration.",
    )
    return return_type


def generate_enum_name(django_model_meta, field):
    if graphene_settings.DJANGO_CHOICE_FIELD_ENUM_CUSTOM_NAME:
        # Try and import custom function
        custom_func = import_string(
            graphene_settings.DJANGO_CHOICE_FIELD_ENUM_CUSTOM_NAME
        )
        name = custom_func(field)
    elif graphene_settings.DJANGO_CHOICE_FIELD_ENUM_V2_NAMING is True:
        name = to_camel_case(f"{django_model_meta.object_name}_{field.name}")
    else:
        name = "{app_label}{object_name}{field_name}Choices".format(
            app_label=to_camel_case(django_model_meta.app_label.title()),
            object_name=django_model_meta.object_name,
            field_name=to_camel_case(field.name.title()),
        )
    return name


def convert_choice_field_to_graphene_enum(field, name=None):
    if name is None:
        name = generate_enum_name(field.model._meta, field)
    choices = field.choices
    EnumCls = convert_choices_to_named_enum_with_descriptions(name, choices)
    return EnumCls( description=get_django_field_description(field), required=is_required(field) ).mount_as(BlankValueField)


# endregion


def is_required(field:DjangoField):
    try:
        blank = getattr(field, "blank", False)
        default = getattr(field, "default", None)
        # null = getattr(field, "null", False)
        if default is None:
            default = NOT_PROVIDED
    except AttributeError:
        return False

    return not blank and default == NOT_PROVIDED


def exists_conversion_for_field( field:DjangoField, registry: RegistryGlobal, type_of_registry: TypeRegistryForField ) -> bool:
    registries_for_field = registry.get_registry_for_field(field)
    if registries_for_field is not None and type_of_registry in registries_for_field:
        return True
    return False


def get_converted_field( field, registry: RegistryGlobal, type_of_registry: TypeRegistryForField ):
    registries_for_field = registry.get_registry_for_field(field)
    if registries_for_field is not None and type_of_registry in registries_for_field:
        return registries_for_field[type_of_registry]
