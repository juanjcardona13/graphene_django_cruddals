from functools import singledispatch
from typing import Union

from django.contrib.contenttypes.fields import (
    GenericForeignKey,
    GenericRel,
    GenericRelation,
)
from django.db import models
from django.utils.functional import Promise
from graphene_cruddals import RegistryGlobal
from graphql.pyutils import register_description

import graphene
from graphene import Dynamic
from graphene_django_cruddals.scalars_type import OrderEnum, OrderStringEnum

from .compat import HStoreField, JSONField, PGJSONField


def convert_django_field_to_order_by_input(name: str, field, model, registry):
    return _convert_field_dispatch(field, name, model, registry)


@singledispatch
def _convert_field_dispatch(
    field, name: str, model: models.Model, registry: RegistryGlobal
) -> Union[graphene.Enum, Dynamic, None]:
    raise ValueError(
        f"Don't know how to convert the Django field {field} ({field.__class__})"
    )


@_convert_field_dispatch.register(models.BigAutoField)
@_convert_field_dispatch.register(models.AutoField)
@_convert_field_dispatch.register(models.SmallAutoField)
@_convert_field_dispatch.register(models.FilePathField)
@_convert_field_dispatch.register(models.FileField)
@_convert_field_dispatch.register(models.ImageField)
@_convert_field_dispatch.register(models.PositiveSmallIntegerField)
@_convert_field_dispatch.register(models.SmallIntegerField)
@_convert_field_dispatch.register(models.IntegerField)
# @_convert_field_dispatch.register(models.NullBooleanField)
@_convert_field_dispatch.register(models.BooleanField)
@_convert_field_dispatch.register(models.BigIntegerField)
@_convert_field_dispatch.register(models.DateField)
@_convert_field_dispatch.register(models.TimeField)
@_convert_field_dispatch.register(models.DateTimeField)
@_convert_field_dispatch.register(models.DecimalField)
@_convert_field_dispatch.register(models.FloatField)
@_convert_field_dispatch.register(models.DurationField)
@_convert_field_dispatch.register(models.UUIDField)
@_convert_field_dispatch.register(models.PositiveIntegerField)
def convert_field_to_order_enum(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    return OrderEnum()


@_convert_field_dispatch.register(models.CharField)
@_convert_field_dispatch.register(models.TextField)
@_convert_field_dispatch.register(models.EmailField)
@_convert_field_dispatch.register(models.SlugField)
@_convert_field_dispatch.register(models.URLField)
@_convert_field_dispatch.register(models.GenericIPAddressField)
@_convert_field_dispatch.register(models.IPAddressField)
def convert_field_to_order_string_enum(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    return OrderStringEnum()


@_convert_field_dispatch.register(HStoreField)
@_convert_field_dispatch.register(models.BinaryField)
@_convert_field_dispatch.register(PGJSONField)
@_convert_field_dispatch.register(JSONField)
@_convert_field_dispatch.register(models.ManyToManyField)
@_convert_field_dispatch.register(models.ManyToManyRel)
@_convert_field_dispatch.register(models.ManyToOneRel)
@_convert_field_dispatch.register(GenericRelation)
def convert_pg_and_json_field_to_json_string(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    return None


@_convert_field_dispatch.register(models.OneToOneRel)
def convert_one_to_one_field_to_django_model(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    model = field.related_model

    def dynamic_type():
        registries_for_model = registry.get_registry_for_model(model)
        if (
            registries_for_model is not None
            and "input_object_type_for_order_by" in registries_for_model
        ):
            _input_type = registries_for_model["input_object_type_for_order_by"]
            return graphene.InputField(_input_type)

    return Dynamic(dynamic_type)


@_convert_field_dispatch.register(models.OneToOneField)
@_convert_field_dispatch.register(models.ForeignKey)
def convert_field_to_django_model(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
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
            and "input_object_type_for_order_by" in registries_for_model
        ):
            _input_type = registries_for_model["input_object_type_for_order_by"]
            return graphene.InputField(_input_type)

    return Dynamic(dynamic_type)


@_convert_field_dispatch.register(GenericForeignKey)
def convert_field_to_union_type(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    """TODO Add support"""
    return


@_convert_field_dispatch.register(GenericRel)  # Representa otro tipo OneToMany
def convert_field_to__type(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    """TODO Add support"""
    return


# Register Django lazy()-wrapped values as GraphQL description/help_text.
# This is needed for using lazy translations, see https://github.com/graphql-python/graphql-core-next/issues/58.
register_description(Promise)
