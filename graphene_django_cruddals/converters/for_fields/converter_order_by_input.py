from functools import singledispatch
from typing import Union
import graphene
from django.db import models
from django.db.models.fields import Field as DjangoField
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation, GenericRel

from django.utils.functional import Promise
from graphene import Dynamic
from graphql.pyutils import register_description

from graphene_django_cruddals.registry_global import RegistryGlobal
from graphene_django_cruddals.scalars_type import OrderEnum, OrderStringEnum

from .compat import HStoreField, JSONField, PGJSONField


@singledispatch
def convert_django_field_to_order_by_input( field: DjangoField, registry: RegistryGlobal ) -> Union[graphene.Enum, Dynamic, None]:
    raise Exception(
        "Don't know how to convert the Django field {} ({})".format(
            field, field.__class__
        )
    )


@convert_django_field_to_order_by_input.register(models.BigAutoField)
@convert_django_field_to_order_by_input.register(models.AutoField)
@convert_django_field_to_order_by_input.register(models.SmallAutoField)
@convert_django_field_to_order_by_input.register(models.FilePathField)
@convert_django_field_to_order_by_input.register(models.FileField)
@convert_django_field_to_order_by_input.register(models.ImageField)
@convert_django_field_to_order_by_input.register(models.PositiveSmallIntegerField)
@convert_django_field_to_order_by_input.register(models.SmallIntegerField)
@convert_django_field_to_order_by_input.register(models.IntegerField)
# @convert_django_field_to_order_by_input.register(models.NullBooleanField)
@convert_django_field_to_order_by_input.register(models.BooleanField)
@convert_django_field_to_order_by_input.register(models.BigIntegerField)
@convert_django_field_to_order_by_input.register(models.DateField)
@convert_django_field_to_order_by_input.register(models.TimeField)
@convert_django_field_to_order_by_input.register(models.DateTimeField)
@convert_django_field_to_order_by_input.register(models.DecimalField)
@convert_django_field_to_order_by_input.register(models.FloatField)
@convert_django_field_to_order_by_input.register(models.DurationField)
@convert_django_field_to_order_by_input.register(models.UUIDField)
@convert_django_field_to_order_by_input.register(models.PositiveIntegerField)
def convert_field_to_order_enum(field, registry: RegistryGlobal):
    return OrderEnum()


@convert_django_field_to_order_by_input.register(models.CharField)
@convert_django_field_to_order_by_input.register(models.TextField)
@convert_django_field_to_order_by_input.register(models.EmailField)
@convert_django_field_to_order_by_input.register(models.SlugField)
@convert_django_field_to_order_by_input.register(models.URLField)
@convert_django_field_to_order_by_input.register(models.GenericIPAddressField)
@convert_django_field_to_order_by_input.register(models.IPAddressField)
def convert_field_to_order_string_enum(field, registry: RegistryGlobal):
    return OrderStringEnum()


@convert_django_field_to_order_by_input.register(HStoreField)
@convert_django_field_to_order_by_input.register(models.BinaryField)
@convert_django_field_to_order_by_input.register(PGJSONField)
@convert_django_field_to_order_by_input.register(JSONField)
@convert_django_field_to_order_by_input.register(models.ManyToManyField)
@convert_django_field_to_order_by_input.register(models.ManyToManyRel)
@convert_django_field_to_order_by_input.register(models.ManyToOneRel)
@convert_django_field_to_order_by_input.register(GenericRelation)
def convert_pg_and_json_field_to_json_string(field, registry: RegistryGlobal):
    return None


@convert_django_field_to_order_by_input.register(models.OneToOneRel)
def convert_one_to_one_field_to_django_model(field, registry: RegistryGlobal):
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


@convert_django_field_to_order_by_input.register(models.OneToOneField)
@convert_django_field_to_order_by_input.register(models.ForeignKey)
def convert_field_to_django_model(field, registry: RegistryGlobal):
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


@convert_django_field_to_order_by_input.register(GenericForeignKey)
def convert_field_to_union_type(field, registry: RegistryGlobal):
    #TODO-Podría ser un GenericForeignKeyOrderByInput, Similar a como se crea con el GenericForeignKeyInput
    return


@convert_django_field_to_order_by_input.register(GenericRel) # Representa otro tipo OneToMany
def convert_field_to__type(field, registry: RegistryGlobal):
    """TODO Add support"""
    return

# Register Django lazy()-wrapped values as GraphQL description/help_text.
# This is needed for using lazy translations, see https://github.com/graphql-python/graphql-core-next/issues/58.
register_description(Promise)
