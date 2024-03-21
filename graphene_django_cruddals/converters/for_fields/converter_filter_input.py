from collections import OrderedDict
from functools import singledispatch
from typing import Type, Union

import graphene
from django.db import models
from django.db.models.fields import Field as DjangoField
from django.utils.functional import Promise
from graphene import (
    ID,
    UUID,
    BigInt,
    Boolean,
    Date,
    DateTime,
    Decimal,
    Dynamic,
    Float,
    Int,
    JSONString,
    String,
    Time,
    InputField
)
from graphql.pyutils import register_description

from graphene_django_cruddals.registry_global import RegistryGlobal
from graphene_django_cruddals.scalars_type import (
    IP,
    URL,
    Binary,
    Duration,
    Email,
    IPv4,
    PositiveInt,
    Slug,
)
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation, GenericRel

from .compat import HStoreField, JSONField, PGJSONField


def get_filter_input_object_type(django_field: DjangoField, type_of_field, name: str) -> Type[graphene.InputObjectType]:
    input_fields = OrderedDict()
    lookups = django_field.get_lookups()
    for name_lookup, lookup in lookups.items():
        if name_lookup == "regex" or name_lookup == "iregex":
            input_fields[name_lookup] = graphene.InputField(type_=graphene.String)
        elif name_lookup == "in":
            input_fields[name_lookup] = graphene.InputField(
                type_=graphene.List(of_type=type_of_field)
            )
        elif name_lookup == "isnull":
            input_fields[name_lookup] = graphene.InputField(type_=graphene.Boolean)
        else:
            input_fields[name_lookup] = graphene.InputField(type_=type_of_field)

    return type(name, (graphene.InputObjectType,), input_fields)


@singledispatch
def convert_django_field_to_filter_input( field: DjangoField, registry: RegistryGlobal) -> Union[graphene.InputObjectType, Dynamic, None]:
    raise Exception(
        "Don't know how to convert the Django field {} ({})".format(
            field, field.__class__
        )
    )


@convert_django_field_to_filter_input.register(models.BigAutoField)
@convert_django_field_to_filter_input.register(models.AutoField)
@convert_django_field_to_filter_input.register(models.SmallAutoField)
def convert_field_to_id(field, registry: RegistryGlobal):
    IDFilter = get_filter_input_object_type(field, ID, "IDFilter")
    return IDFilter()


@convert_django_field_to_filter_input.register(models.CharField)
@convert_django_field_to_filter_input.register(models.TextField)
@convert_django_field_to_filter_input.register(models.FilePathField)
def convert_field_to_string(field, registry: RegistryGlobal):
    StringFilter = get_filter_input_object_type(field, String, "StringFilter")
    return StringFilter()


@convert_django_field_to_filter_input.register(models.FileField)
@convert_django_field_to_filter_input.register(models.ImageField)
def convert_field_to_upload_or_string(field, registry: RegistryGlobal):
    StringFilter = get_filter_input_object_type(field, String, "StringFilter")
    return StringFilter()


@convert_django_field_to_filter_input.register(models.PositiveSmallIntegerField)
@convert_django_field_to_filter_input.register(models.SmallIntegerField)
@convert_django_field_to_filter_input.register(models.IntegerField)
def convert_field_to_int(field, registry: RegistryGlobal):
    IntFilter = get_filter_input_object_type(field, Int, "IntFilter")
    return IntFilter()


# @convert_django_field_to_filter_input.register(models.NullBooleanField)
@convert_django_field_to_filter_input.register(models.BooleanField)
def convert_field_to_boolean(field, registry: RegistryGlobal):
    BooleanFilter = get_filter_input_object_type(field, Boolean, "BooleanFilter")
    return BooleanFilter()


@convert_django_field_to_filter_input.register(models.BigIntegerField)
def convert_field_to_big_int(field, registry: RegistryGlobal):
    BigIntFilter = get_filter_input_object_type(field, BigInt, "BigIntFilter")
    return BigIntFilter()


@convert_django_field_to_filter_input.register(models.DateField)
def convert_field_to_date(field, registry: RegistryGlobal):
    DateFilter = get_filter_input_object_type(field, Date, "DateFilter")
    return DateFilter()


@convert_django_field_to_filter_input.register(models.TimeField)
def convert_field_to_time(field, registry: RegistryGlobal):
    TimeFilter = get_filter_input_object_type(field, Time, "TimeFilter")
    return TimeFilter()


@convert_django_field_to_filter_input.register(models.DateTimeField)
def convert_field_to_datetime(field, registry: RegistryGlobal):
    DateTimeFilter = get_filter_input_object_type(field, DateTime, "DateTimeFilter")
    return DateTimeFilter()


@convert_django_field_to_filter_input.register(models.DecimalField)
def convert_field_to_decimal(field, registry: RegistryGlobal):
    DecimalFilter = get_filter_input_object_type(field, Decimal, "DecimalFilter")
    return DecimalFilter()


@convert_django_field_to_filter_input.register(models.FloatField)
def convert_field_to_float(field, registry: RegistryGlobal):
    FloatFilter = get_filter_input_object_type(field, Float, "FloatFilter")
    return FloatFilter()


@convert_django_field_to_filter_input.register(models.DurationField)
def convert_field_to_duration(field, registry: RegistryGlobal):
    DurationFilter = get_filter_input_object_type(field, Duration, "DurationFilter")
    return DurationFilter()


@convert_django_field_to_filter_input.register(models.BinaryField)
def convert_field_to_binary(field, registry: RegistryGlobal):
    return


@convert_django_field_to_filter_input.register(HStoreField)
@convert_django_field_to_filter_input.register(PGJSONField)
@convert_django_field_to_filter_input.register(JSONField)
def convert_pg_and_json_field_to_json_string(field, registry: RegistryGlobal):
    JSONStringFilter = get_filter_input_object_type( field, JSONString, "JSONStringFilter" )
    return JSONStringFilter()


@convert_django_field_to_filter_input.register(models.UUIDField)
def convert_field_to_uuid(field, registry: RegistryGlobal):
    UUIDFilter = get_filter_input_object_type(field, UUID, "UUIDFilter")
    return UUIDFilter()


@convert_django_field_to_filter_input.register(models.EmailField)
def convert_field_to_email(field, registry: RegistryGlobal):
    EmailFilter = get_filter_input_object_type(field, Email, "EmailFilter")
    return EmailFilter()


@convert_django_field_to_filter_input.register(models.GenericIPAddressField)
def convert_field_to_ipv4(field, registry: RegistryGlobal):
    IPv4Filter = get_filter_input_object_type(field, IPv4, "IPv4Filter")
    return IPv4Filter()


@convert_django_field_to_filter_input.register(models.IPAddressField)
def convert_field_to_ip(field, registry: RegistryGlobal):
    IPFilter = get_filter_input_object_type(field, IP, "IPFilter")
    return IPFilter()


@convert_django_field_to_filter_input.register(models.PositiveIntegerField)
def convert_field_to_positive_int(field, registry: RegistryGlobal):
    PositiveIntFilter = get_filter_input_object_type( field, PositiveInt, "PositiveIntFilter" )
    return PositiveIntFilter()


@convert_django_field_to_filter_input.register(models.SlugField)
def convert_field_to_slug(field, registry: RegistryGlobal):
    SlugFilter = get_filter_input_object_type(field, Slug, "SlugFilter")
    return SlugFilter()


@convert_django_field_to_filter_input.register(models.URLField)
def convert_field_to_url(field, registry: RegistryGlobal):
    URLFilter = get_filter_input_object_type(field, URL, "URLFilter")
    return URLFilter()


@convert_django_field_to_filter_input.register(models.OneToOneRel)
def convert_onetoone_field_to_djangomodel(field, registry: RegistryGlobal):
    model = field.related_model

    def dynamic_type():
        registries_for_model = registry.get_registry_for_model(model)
        if (
            registries_for_model is not None
            and "input_object_type_for_search" in registries_for_model
        ):
            _input_type = registries_for_model["input_object_type_for_search"]
            return graphene.InputField(_input_type)

    return Dynamic(dynamic_type)


@convert_django_field_to_filter_input.register(models.ManyToManyField)
@convert_django_field_to_filter_input.register(models.ManyToManyRel)
@convert_django_field_to_filter_input.register(models.ManyToOneRel)
@convert_django_field_to_filter_input.register(GenericRelation) # Representa otro tipo ManyToOne
def convert_field_to_list_or_connection(field, registry: RegistryGlobal):
    model = field.related_model

    def dynamic_type():
        registries_for_model = registry.get_registry_for_model(model)
        if (
            registries_for_model is not None
            and "input_object_type_for_search" in registries_for_model
        ):
            _input_type = registries_for_model["input_object_type_for_search"]
            return graphene.InputField(_input_type)

    return Dynamic(dynamic_type)


@convert_django_field_to_filter_input.register(models.OneToOneField)
@convert_django_field_to_filter_input.register(models.ForeignKey)
def convert_field_to_djangomodel(field, registry: RegistryGlobal):
    model = field.related_model

    def dynamic_type():
        # Avoid create field for auto generate OneToOneField product of an inheritance
        if isinstance(field, models.OneToOneField) and issubclass(
            field.model, field.related_model
        ):
            return
        registries_for_model = registry.get_registry_for_model(model)
        if (
            registries_for_model is not None
            and "input_object_type_for_search" in registries_for_model
        ):
            _input_type = registries_for_model["input_object_type_for_search"]
            return graphene.InputField(_input_type)

    return Dynamic(dynamic_type)


@convert_django_field_to_filter_input.register(GenericForeignKey)
def convert_field_to_union_type(field, registry: RegistryGlobal):
    #TODO-Podría ser un GenericForeignKeyFilterInput, Similar a como se crea con el GenericForeignKeyInput
    return


@convert_django_field_to_filter_input.register(GenericRel) # Representa otro tipo OneToMany
def convert_field_to__type(field, registry: RegistryGlobal):
    """TODO Add support"""
    return

# Register Django lazy()-wrapped values as GraphQL description/help_text.
# This is needed for using lazy translations, see https://github.com/graphql-python/graphql-core-next/issues/58.
register_description(Promise)
