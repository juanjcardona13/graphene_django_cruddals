from functools import singledispatch
from typing import Union

from django.contrib.contenttypes.fields import (
    GenericForeignKey,
    GenericRel,
    GenericRelation,
)
from django.db import models
from django.db.models.fields import Field as DjangoField
from django.utils.functional import Promise
from graphene_cruddals import (
    CruddalsRelationField,
    RegistryGlobal,
    TypesMutation,
    TypesMutationEnum,
)
from graphql.pyutils import register_description

import graphene
from graphene import (
    ID,
    Dynamic,
    InputField,
    List,
)
from graphene_django_cruddals.converters.converter_input_relation_nested import (
    GenericForeignKeyInput,
    convert_relation_field_to_input,
)
from graphene_django_cruddals.converters.utils import (
    get_django_field_default,
    get_django_field_description,
    get_django_field_is_required,
)
from graphene_django_cruddals.scalars_type import (
    IP,
    URL,
    Binary,
    Duration,
    Email,
    IPv4,
    PositiveInt,
    Slug,
    Upload,
)

from .compat import HStoreField, JSONField, PGJSONField


def convert_django_field_to_input(
    name: str,
    field: DjangoField,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation = TypesMutationEnum.CREATE_UPDATE.value,
):
    return _convert_field_dispatch(field, name, model, registry, type_mutation)


@singledispatch
def _convert_field_dispatch(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation = TypesMutationEnum.CREATE_UPDATE.value,
) -> Union[
    Dynamic, graphene.InputField, GenericForeignKeyInput, None
]:  # String, Upload, Int, Boolean, BigInt, Date, Time, DateTime, Decimal, Float, Duration, Binary, JSONString, UUID, Email, IPv4, IP, PositiveInt, Slug, URL
    raise ValueError(
        f"Don't know how to convert the Django field {field} ({field.__class__})"
    )


@_convert_field_dispatch.register(models.BigAutoField)
@_convert_field_dispatch.register(models.AutoField)
@_convert_field_dispatch.register(models.SmallAutoField)
def convert_field_to_id(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(
            type_=graphene.ID,
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
            default_value=get_django_field_default(field),
        )
    elif type_mutation == TypesMutationEnum.UPDATE.value:
        return InputField(
            type_=graphene.ID,
            description=get_django_field_description(field),
            required=True,
            default_value=get_django_field_default(field),
        )
    else:
        # If type_mutation is for create_update
        # is best to not have default value because
        # is not possible after make a update the value
        # because the default value always is provided in the schema
        return InputField(
            type_=graphene.ID, description=get_django_field_description(field)
        )


@_convert_field_dispatch.register(models.CharField)
@_convert_field_dispatch.register(models.TextField)
@_convert_field_dispatch.register(models.FilePathField)
def convert_field_to_string(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(
            type_=graphene.String,
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
            default_value=get_django_field_default(field),
        )
    else:
        # If type_mutation is for create_update
        # is best to not have default value because
        # is not possible after make a update the value
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(
            type_=graphene.String, description=get_django_field_description(field)
        )


@_convert_field_dispatch.register(models.FileField)
@_convert_field_dispatch.register(models.ImageField)
def convert_field_to_upload_or_string(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(
            type_=Upload,
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
            default_value=get_django_field_default(field),
        )
    else:
        # If type_mutation is for create_update
        # is best to not have default value because
        # is not possible after make a update the value
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=Upload, description=get_django_field_description(field))


@_convert_field_dispatch.register(models.PositiveSmallIntegerField)
@_convert_field_dispatch.register(models.SmallIntegerField)
@_convert_field_dispatch.register(models.IntegerField)
def convert_field_to_int(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(
            type_=graphene.Int,
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
            default_value=get_django_field_default(field),
        )
    else:
        # If type_mutation is for create_update
        # is best to not have default value because
        # is not possible after make a update the value
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(
            type_=graphene.Int, description=get_django_field_description(field)
        )


# @_convert_field_dispatch.register(models.NullBooleanField)
@_convert_field_dispatch.register(models.BooleanField)
def convert_field_to_boolean(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(
            type_=graphene.Boolean,
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
            default_value=get_django_field_default(field),
        )
    else:
        # If type_mutation is for create_update
        # is best to not have default value because
        # is not possible after make a update the value
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(
            type_=graphene.Boolean, description=get_django_field_description(field)
        )


@_convert_field_dispatch.register(models.BigIntegerField)
def convert_field_to_big_int(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(
            type_=graphene.BigInt,
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
            default_value=get_django_field_default(field),
        )
    else:
        # If type_mutation is for create_update
        # is best to not have default value because
        # is not possible after make a update the value
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(
            type_=graphene.BigInt, description=get_django_field_description(field)
        )


@_convert_field_dispatch.register(models.DateField)
def convert_field_to_date(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(
            type_=graphene.Date,
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
            default_value=get_django_field_default(field),
        )
    else:
        # If type_mutation is for create_update
        # is best to not have default value because
        # is not possible after make a update the value
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(
            type_=graphene.Date, description=get_django_field_description(field)
        )


@_convert_field_dispatch.register(models.TimeField)
def convert_field_to_time(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(
            type_=graphene.Time,
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
            default_value=get_django_field_default(field),
        )
    else:
        # If type_mutation is for create_update
        # is best to not have default value because
        # is not possible after make a update the value
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(
            type_=graphene.Time, description=get_django_field_description(field)
        )


@_convert_field_dispatch.register(models.DateTimeField)
def convert_field_to_datetime(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(
            type_=graphene.DateTime,
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
            default_value=get_django_field_default(field),
        )
    else:
        # If type_mutation is for create_update
        # is best to not have default value because
        # is not possible after make a update the value
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(
            type_=graphene.DateTime, description=get_django_field_description(field)
        )


@_convert_field_dispatch.register(models.DecimalField)
def convert_field_to_decimal(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(
            type_=graphene.Decimal,
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
            default_value=get_django_field_default(field),
        )
    else:
        # If type_mutation is for create_update
        # is best to not have default value because
        # is not possible after make a update the value
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(
            type_=graphene.Decimal, description=get_django_field_description(field)
        )


@_convert_field_dispatch.register(models.FloatField)
def convert_field_to_float(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(
            type_=graphene.Float,
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
            default_value=get_django_field_default(field),
        )
    else:
        # If type_mutation is for create_update
        # is best to not have default value because
        # is not possible after make a update the value
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(
            type_=graphene.Float, description=get_django_field_description(field)
        )


@_convert_field_dispatch.register(models.DurationField)
def convert_field_to_duration(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(
            type_=Duration,
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
            default_value=get_django_field_default(field),
        )
    else:
        # If type_mutation is for create_update
        # is best to not have default value because
        # is not possible after make a update the value
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(
            type_=Duration, description=get_django_field_description(field)
        )


@_convert_field_dispatch.register(models.BinaryField)
def convert_field_to_binary(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(
            type_=Binary,
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
            default_value=get_django_field_default(field),
        )
    else:
        # If type_mutation is for create_update
        # is best to not have default value because
        # is not possible after make a update the value
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=Binary, description=get_django_field_description(field))
    # https://docs.djangoproject.com/en/3.2/ref/models/fields/#binaryfield
    # https://stackoverflow.com/questions/40800941/how-to-make-a-binaryfield-editable-in-django
    # https://stackoverflow.com/questions/59213498/binary-in-graphql


@_convert_field_dispatch.register(HStoreField)
@_convert_field_dispatch.register(PGJSONField)
@_convert_field_dispatch.register(JSONField)
def convert_pg_and_json_field_to_json_string(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(
            type_=graphene.JSONString,
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
            default_value=get_django_field_default(field),
        )
    else:
        # If type_mutation is for create_update
        # is best to not have default value because
        # is not possible after make a update the value
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(
            type_=graphene.JSONString, description=get_django_field_description(field)
        )


@_convert_field_dispatch.register(models.UUIDField)
def convert_field_to_uuid(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(
            type_=graphene.UUID,
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
            default_value=get_django_field_default(field),
        )
    else:
        # If type_mutation is for create_update
        # is best to not have default value because
        # is not possible after make a update the value
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(
            type_=graphene.UUID, description=get_django_field_description(field)
        )


@_convert_field_dispatch.register(models.EmailField)
def convert_field_to_email(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(
            type_=Email,
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
            default_value=get_django_field_default(field),
        )
    else:
        # If type_mutation is for create_update
        # is best to not have default value because
        # is not possible after make a update the value
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=Email, description=get_django_field_description(field))


@_convert_field_dispatch.register(models.GenericIPAddressField)
def convert_field_to_ipv4(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(
            type_=IPv4,
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
            default_value=get_django_field_default(field),
        )
    else:
        # If type_mutation is for create_update
        # is best to not have default value because
        # is not possible after make a update the value
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=IPv4, description=get_django_field_description(field))


@_convert_field_dispatch.register(models.IPAddressField)
def convert_field_to_ip(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(
            type_=IP,
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
            default_value=get_django_field_default(field),
        )
    else:
        # If type_mutation is for create_update
        # is best to not have default value because
        # is not possible after make a update the value
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=IP, description=get_django_field_description(field))


@_convert_field_dispatch.register(models.PositiveIntegerField)
def convert_field_to_positive_int(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(
            type_=PositiveInt,
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
            default_value=get_django_field_default(field),
        )
    else:
        # If type_mutation is for create_update
        # is best to not have default value because
        # is not possible after make a update the value
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(
            type_=PositiveInt, description=get_django_field_description(field)
        )


@_convert_field_dispatch.register(models.SlugField)
def convert_field_to_slug(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(
            type_=Slug,
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
            default_value=get_django_field_default(field),
        )
    else:
        # If type_mutation is for create_update
        # is best to not have default value because
        # is not possible after make a update the value
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=Slug, description=get_django_field_description(field))


@_convert_field_dispatch.register(models.URLField)
def convert_field_to_url(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(
            type_=URL,
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
            default_value=get_django_field_default(field),
        )
    else:
        # If type_mutation is for create_update
        # is best to not have default value because
        # is not possible after make a update the value
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=URL, description=get_django_field_description(field))


@_convert_field_dispatch.register(models.ManyToManyField)
@_convert_field_dispatch.register(models.ManyToManyRel)
@_convert_field_dispatch.register(models.ManyToOneRel)
def convert_field_to_list_or_connection(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(
            type_=List(ID),
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
        )
    else:
        return InputField(
            type_=List(ID), description=get_django_field_description(field)
        )


@_convert_field_dispatch.register(models.OneToOneField)
@_convert_field_dispatch.register(models.ForeignKey)
def convert_field_to_djangomodel(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(
            type_=ID,
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
        )
    else:
        return InputField(type_=ID, description=get_django_field_description(field))


@_convert_field_dispatch.register(GenericForeignKey)
def convert_field_to_union_type(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    """TODO Add support"""
    return


@_convert_field_dispatch.register(GenericRelation)
def convert_relation_field_to_union_type(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    """TODO Add support"""
    return


@_convert_field_dispatch.register(GenericRel)
def convert_field_to__type(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    """TODO Add support"""
    return


@_convert_field_dispatch.register(CruddalsRelationField)
def convert_field_to_relation(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation: TypesMutation,
):
    django_field = model._meta.get_field(name)
    return convert_relation_field_to_input(
        name, django_field, model, registry, type_mutation
    )


"""TODO"""
# @_convert_field_dispatch.register(ArrayField)
# @_convert_field_dispatch.register(RangeField)

# Register Django lazy()-wrapped values as GraphQL description/help_text.
# This is needed for using lazy translations, see https://github.com/graphql-python/graphql-core-next/issues/58.
register_description(Promise)
