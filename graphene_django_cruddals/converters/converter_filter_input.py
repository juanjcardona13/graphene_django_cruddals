from collections import OrderedDict
from functools import singledispatch
from typing import Type, Union

from django.contrib.contenttypes.fields import (
    GenericForeignKey,
    GenericRel,
    GenericRelation,
)
from django.db import models
from django.db.models.fields import Field as DjangoField
from django.utils.functional import Promise
from graphene_cruddals import RegistryGlobal
from graphql.pyutils import register_description

import graphene
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
)
from graphene_django_cruddals.scalars_type import (
    IP,
    URL,
    Duration,
    Email,
    IPv4,
    PositiveInt,
    Slug,
)

from .compat import HStoreField, JSONField, PGJSONField


def get_filter_input_object_type(
    django_field: DjangoField, type_of_field, name: str
) -> Type[graphene.InputObjectType]:
    input_fields = OrderedDict()
    lookups = django_field.get_lookups()
    for name_lookup in lookups.keys():
        if name_lookup in ("regex", "iregex"):
            input_fields[name_lookup] = graphene.InputField(type_=graphene.String)
        elif name_lookup in ("in", "range"):
            input_fields[name_lookup] = graphene.InputField(
                type_=graphene.List(of_type=type_of_field)
            )
        elif name_lookup == "isnull":
            input_fields[name_lookup] = graphene.InputField(type_=graphene.Boolean)
        else:
            input_fields[name_lookup] = graphene.InputField(type_=type_of_field)

    return type(name, (graphene.InputObjectType,), input_fields)


def convert_django_field_to_filter_input(
    name: str, field, model: models.Model, registry: RegistryGlobal
) -> Union[graphene.InputObjectType, Dynamic, None]:
    return _convert_field_dispatch(field, name, model, registry)


@singledispatch
def _convert_field_dispatch(
    field, name: str, model: models.Model, registry: RegistryGlobal
) -> Union[graphene.InputObjectType, Dynamic, None]:
    raise ValueError(
        f"Don't know how to convert the Django field {field} ({field.__class__})"
    )


@_convert_field_dispatch.register(models.BigAutoField)
@_convert_field_dispatch.register(models.AutoField)
@_convert_field_dispatch.register(models.SmallAutoField)
def convert_field_to_id(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    IDFilter = get_filter_input_object_type(field, ID, "IDFilter")
    return IDFilter()


@_convert_field_dispatch.register(models.CharField)
@_convert_field_dispatch.register(models.TextField)
@_convert_field_dispatch.register(models.FilePathField)
def convert_field_to_string(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    StringFilter = get_filter_input_object_type(field, String, "StringFilter")
    return StringFilter()


@_convert_field_dispatch.register(models.FileField)
@_convert_field_dispatch.register(models.ImageField)
def convert_field_to_upload_or_string(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    StringFilter = get_filter_input_object_type(field, String, "StringFilter")
    return StringFilter()


@_convert_field_dispatch.register(models.PositiveSmallIntegerField)
@_convert_field_dispatch.register(models.SmallIntegerField)
@_convert_field_dispatch.register(models.IntegerField)
def convert_field_to_int(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    IntFilter = get_filter_input_object_type(field, Int, "IntFilter")
    return IntFilter()


# @_convert_field_dispatch.register(models.NullBooleanField)
@_convert_field_dispatch.register(models.BooleanField)
def convert_field_to_boolean(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    BooleanFilter = get_filter_input_object_type(field, Boolean, "BooleanFilter")
    return BooleanFilter()


@_convert_field_dispatch.register(models.BigIntegerField)
def convert_field_to_big_int(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    BigIntFilter = get_filter_input_object_type(field, BigInt, "BigIntFilter")
    return BigIntFilter()


@_convert_field_dispatch.register(models.DateField)
def convert_field_to_date(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    DateFilter = get_filter_input_object_type(field, Date, "DateFilter")
    return DateFilter()


@_convert_field_dispatch.register(models.TimeField)
def convert_field_to_time(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    TimeFilter = get_filter_input_object_type(field, Time, "TimeFilter")
    return TimeFilter()


@_convert_field_dispatch.register(models.DateTimeField)
def convert_field_to_datetime(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    DateTimeFilter = get_filter_input_object_type(field, DateTime, "DateTimeFilter")
    return DateTimeFilter()


@_convert_field_dispatch.register(models.DecimalField)
def convert_field_to_decimal(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    DecimalFilter = get_filter_input_object_type(field, Decimal, "DecimalFilter")
    return DecimalFilter()


@_convert_field_dispatch.register(models.FloatField)
def convert_field_to_float(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    FloatFilter = get_filter_input_object_type(field, Float, "FloatFilter")
    return FloatFilter()


@_convert_field_dispatch.register(models.DurationField)
def convert_field_to_duration(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    DurationFilter = get_filter_input_object_type(field, Duration, "DurationFilter")
    return DurationFilter()


@_convert_field_dispatch.register(models.BinaryField)
def convert_field_to_binary(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    return


@_convert_field_dispatch.register(HStoreField)
@_convert_field_dispatch.register(PGJSONField)
@_convert_field_dispatch.register(JSONField)
def convert_pg_and_json_field_to_json_string(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    JSONStringFilter = get_filter_input_object_type(
        field, JSONString, "JSONStringFilter"
    )
    return JSONStringFilter()


@_convert_field_dispatch.register(models.UUIDField)
def convert_field_to_uuid(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    UUIDFilter = get_filter_input_object_type(field, UUID, "UUIDFilter")
    return UUIDFilter()


@_convert_field_dispatch.register(models.EmailField)
def convert_field_to_email(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    EmailFilter = get_filter_input_object_type(field, Email, "EmailFilter")
    return EmailFilter()


@_convert_field_dispatch.register(models.GenericIPAddressField)
def convert_field_to_ipv4(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    IPFilter = get_filter_input_object_type(field, IP, "IPFilter")
    return IPFilter()


@_convert_field_dispatch.register(models.IPAddressField)
def convert_field_to_ip(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    IPv4Filter = get_filter_input_object_type(field, IPv4, "IPv4Filter")
    return IPv4Filter()


@_convert_field_dispatch.register(models.PositiveIntegerField)
def convert_field_to_positive_int(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    PositiveIntFilter = get_filter_input_object_type(
        field, PositiveInt, "PositiveIntFilter"
    )
    return PositiveIntFilter()


@_convert_field_dispatch.register(models.SlugField)
def convert_field_to_slug(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    SlugFilter = get_filter_input_object_type(field, Slug, "SlugFilter")
    return SlugFilter()


@_convert_field_dispatch.register(models.URLField)
def convert_field_to_url(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    URLFilter = get_filter_input_object_type(field, URL, "URLFilter")
    return URLFilter()


@_convert_field_dispatch.register(models.OneToOneRel)
def convert_onetoone_field_to_djangomodel(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    model = field.related_model

    def dynamic_type():
        registries_for_model = registry.get_registry_for_model(model)
        if (
            registries_for_model is not None
            and "input_object_type_for_search" in registries_for_model
        ):
            _input_type = registries_for_model["input_object_type_for_search"]
            return graphene.InputField(_input_type)
        return None

    return Dynamic(dynamic_type)


@_convert_field_dispatch.register(models.ManyToManyField)
@_convert_field_dispatch.register(models.ManyToManyRel)
@_convert_field_dispatch.register(models.ManyToOneRel)
@_convert_field_dispatch.register(GenericRelation)
def convert_field_to_list_or_connection(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    model = field.related_model

    def dynamic_type():
        registries_for_model = registry.get_registry_for_model(model)
        if (
            registries_for_model is not None
            and "input_object_type_for_search" in registries_for_model
        ):
            _input_type = registries_for_model["input_object_type_for_search"]
            return graphene.InputField(_input_type)
        return None

    return Dynamic(dynamic_type)


@_convert_field_dispatch.register(models.OneToOneField)
@_convert_field_dispatch.register(models.ForeignKey)
def convert_field_to_djangomodel(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    model = field.related_model

    def dynamic_type():
        # Avoid create field for auto generate OneToOneField product of an inheritance
        if isinstance(field, models.OneToOneField) and issubclass(
            field.model, field.related_model
        ):
            return None
        registries_for_model = registry.get_registry_for_model(model)
        if (
            registries_for_model is not None
            and "input_object_type_for_search" in registries_for_model
        ):
            _input_type = registries_for_model["input_object_type_for_search"]
            return graphene.InputField(_input_type)
        return None

    return Dynamic(dynamic_type)


@_convert_field_dispatch.register(GenericForeignKey)
def convert_field_to_union_type(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    """TODO Add support"""


@_convert_field_dispatch.register(GenericRel)
def convert_field_to__type(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    """TODO Add support"""


# Register Django lazy()-wrapped values as GraphQL description/help_text.
# This is needed for using lazy translations, see https://github.com/graphql-python/graphql-core-next/issues/58.
register_description(Promise)
