from functools import singledispatch
from typing import Literal, Type, Union

from django.db import models
from django.db.models import Model as DjangoModel
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
    InputField,
    InputObjectType,
    Int,
    JSONString,
    List,
    NonNull,
    String,
    Time,
)
import graphene
from graphql.pyutils import register_description
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation, GenericRel

from graphene_django_cruddals.converters.for_fields.utils import django_field_get_default, get_django_field_description, django_field_is_required
from graphene_django_cruddals.types import TypesMutation, TypesMutationEnum
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
    Upload,
)

from .compat import HStoreField, JSONField, PGJSONField
from graphene.types.generic import GenericScalar


@singledispatch
def convert_django_field_to_input(field: DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation=TypesMutationEnum.CREATE_UPDATE.value) -> Union[graphene.InputField, None]: #String, Upload, Int, Boolean, BigInt, Date, Time, DateTime, Decimal, Float, Duration, Binary, JSONString, UUID, Email, IPv4, IP, PositiveInt, Slug, URL
    raise Exception(
        "Don't know how to convert the Django field {} ({})".format(
            field, field.__class__
        )
    )


@convert_django_field_to_input.register(models.BigAutoField)
@convert_django_field_to_input.register(models.AutoField)
@convert_django_field_to_input.register(models.SmallAutoField)
def convert_field_to_id(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(type_=graphene.ID, description=get_django_field_description(field), required=django_field_is_required(field), default_value=django_field_get_default(field))
    else:
        # If type_mutation is for create_update 
        # is best to not have default value because 
        # is not possible after make a update the value 
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=graphene.ID, description=get_django_field_description(field))
    


@convert_django_field_to_input.register(models.CharField)
@convert_django_field_to_input.register(models.TextField)
@convert_django_field_to_input.register(models.FilePathField)
def convert_field_to_string(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(type_=graphene.String, description=get_django_field_description(field), required=django_field_is_required(field), default_value=django_field_get_default(field))
    else:
        # If type_mutation is for create_update 
        # is best to not have default value because 
        # is not possible after make a update the value 
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=graphene.String, description=get_django_field_description(field))
    


@convert_django_field_to_input.register(models.FileField)
@convert_django_field_to_input.register(models.ImageField)
def convert_field_to_upload_or_string(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(type_=Upload, description=get_django_field_description(field), required=django_field_is_required(field), default_value=django_field_get_default(field))
    else:
        # If type_mutation is for create_update 
        # is best to not have default value because 
        # is not possible after make a update the value 
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=Upload, description=get_django_field_description(field))
    


@convert_django_field_to_input.register(models.PositiveSmallIntegerField)
@convert_django_field_to_input.register(models.SmallIntegerField)
@convert_django_field_to_input.register(models.IntegerField)
def convert_field_to_int(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(type_=graphene.Int, description=get_django_field_description(field), required=django_field_is_required(field), default_value=django_field_get_default(field))
    else:
        # If type_mutation is for create_update 
        # is best to not have default value because 
        # is not possible after make a update the value 
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=graphene.Int, description=get_django_field_description(field))
    


# @convert_django_field_to_input.register(models.NullBooleanField)
@convert_django_field_to_input.register(models.BooleanField)
def convert_field_to_boolean(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(type_=graphene.Boolean, description=get_django_field_description(field), required=django_field_is_required(field), default_value=django_field_get_default(field))
    else:
        # If type_mutation is for create_update 
        # is best to not have default value because 
        # is not possible after make a update the value 
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=graphene.Boolean, description=get_django_field_description(field))
    


@convert_django_field_to_input.register(models.BigIntegerField)
def convert_field_to_big_int(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(type_=graphene.BigInt, description=get_django_field_description(field), required=django_field_is_required(field), default_value=django_field_get_default(field))
    else:
        # If type_mutation is for create_update 
        # is best to not have default value because 
        # is not possible after make a update the value 
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=graphene.BigInt, description=get_django_field_description(field))
    
@convert_django_field_to_input.register(models.DateField)
def convert_field_to_date(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(type_=graphene.Date, description=get_django_field_description(field), required=django_field_is_required(field), default_value=django_field_get_default(field))
    else:
        # If type_mutation is for create_update 
        # is best to not have default value because 
        # is not possible after make a update the value 
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=graphene.Date, description=get_django_field_description(field))
    


@convert_django_field_to_input.register(models.TimeField)
def convert_field_to_time(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(type_=graphene.Time, description=get_django_field_description(field), required=django_field_is_required(field), default_value=django_field_get_default(field))
    else:
        # If type_mutation is for create_update 
        # is best to not have default value because 
        # is not possible after make a update the value 
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=graphene.Time, description=get_django_field_description(field))
    


@convert_django_field_to_input.register(models.DateTimeField)
def convert_field_to_datetime(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(type_=graphene.DateTime, description=get_django_field_description(field), required=django_field_is_required(field), default_value=django_field_get_default(field))
    else:
        # If type_mutation is for create_update 
        # is best to not have default value because 
        # is not possible after make a update the value 
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=graphene.DateTime, description=get_django_field_description(field))
    


@convert_django_field_to_input.register(models.DecimalField)
def convert_field_to_decimal(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(type_=graphene.Decimal, description=get_django_field_description(field), required=django_field_is_required(field), default_value=django_field_get_default(field))
    else:
        # If type_mutation is for create_update 
        # is best to not have default value because 
        # is not possible after make a update the value 
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=graphene.Decimal, description=get_django_field_description(field))
    


@convert_django_field_to_input.register(models.FloatField)
def convert_field_to_float(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(type_=graphene.Float, description=get_django_field_description(field), required=django_field_is_required(field), default_value=django_field_get_default(field))
    else:
        # If type_mutation is for create_update 
        # is best to not have default value because 
        # is not possible after make a update the value 
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=graphene.Float, description=get_django_field_description(field))
    


@convert_django_field_to_input.register(models.DurationField)
def convert_field_to_duration(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(type_=Duration, description=get_django_field_description(field), required=django_field_is_required(field), default_value=django_field_get_default(field))
    else:
        # If type_mutation is for create_update 
        # is best to not have default value because 
        # is not possible after make a update the value 
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=Duration, description=get_django_field_description(field))
    


@convert_django_field_to_input.register(models.BinaryField)
def convert_field_to_binary(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(type_=Binary, description=get_django_field_description(field), required=django_field_is_required(field), default_value=django_field_get_default(field))
    else:
        # If type_mutation is for create_update 
        # is best to not have default value because 
        # is not possible after make a update the value 
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=Binary, description=get_django_field_description(field))
    #https://docs.djangoproject.com/en/3.2/ref/models/fields/#binaryfield
    #https://stackoverflow.com/questions/40800941/how-to-make-a-binaryfield-editable-in-django
    #https://stackoverflow.com/questions/59213498/binary-in-graphql


@convert_django_field_to_input.register(HStoreField)
@convert_django_field_to_input.register(PGJSONField)
@convert_django_field_to_input.register(JSONField)
def convert_pg_and_json_field_to_json_string(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(type_=graphene.JSONString, description=get_django_field_description(field), required=django_field_is_required(field), default_value=django_field_get_default(field))
    else:
        # If type_mutation is for create_update 
        # is best to not have default value because 
        # is not possible after make a update the value 
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=graphene.JSONString, description=get_django_field_description(field))
    


@convert_django_field_to_input.register(models.UUIDField)
def convert_field_to_uuid(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(type_=graphene.UUID, description=get_django_field_description(field), required=django_field_is_required(field), default_value=django_field_get_default(field))
    else:
        # If type_mutation is for create_update 
        # is best to not have default value because 
        # is not possible after make a update the value 
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=graphene.UUID, description=get_django_field_description(field))
    


@convert_django_field_to_input.register(models.EmailField)
def convert_field_to_email(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(type_=Email, description=get_django_field_description(field), required=django_field_is_required(field), default_value=django_field_get_default(field))
    else:
        # If type_mutation is for create_update 
        # is best to not have default value because 
        # is not possible after make a update the value 
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=Email, description=get_django_field_description(field))
    


@convert_django_field_to_input.register(models.GenericIPAddressField)
def convert_field_to_ipv4(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(type_=IPv4, description=get_django_field_description(field), required=django_field_is_required(field), default_value=django_field_get_default(field))
    else:
        # If type_mutation is for create_update 
        # is best to not have default value because 
        # is not possible after make a update the value 
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=IPv4, description=get_django_field_description(field))
    


@convert_django_field_to_input.register(models.IPAddressField)
def convert_field_to_ip(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(type_=IP, description=get_django_field_description(field), required=django_field_is_required(field), default_value=django_field_get_default(field))
    else:
        # If type_mutation is for create_update 
        # is best to not have default value because 
        # is not possible after make a update the value 
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=IP, description=get_django_field_description(field))
    


@convert_django_field_to_input.register(models.PositiveIntegerField)
def convert_field_to_positive_int(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(type_=PositiveInt, description=get_django_field_description(field), required=django_field_is_required(field), default_value=django_field_get_default(field))
    else:
        # If type_mutation is for create_update 
        # is best to not have default value because 
        # is not possible after make a update the value 
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=PositiveInt, description=get_django_field_description(field))
    


@convert_django_field_to_input.register(models.SlugField)
def convert_field_to_slug(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(type_=Slug, description=get_django_field_description(field), required=django_field_is_required(field), default_value=django_field_get_default(field))
    else:
        # If type_mutation is for create_update 
        # is best to not have default value because 
        # is not possible after make a update the value 
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=Slug, description=get_django_field_description(field))
    


@convert_django_field_to_input.register(models.URLField)
def convert_field_to_url(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(type_=URL, description=get_django_field_description(field), required=django_field_is_required(field), default_value=django_field_get_default(field))
    else:
        # If type_mutation is for create_update 
        # is best to not have default value because 
        # is not possible after make a update the value 
        # because the default value always is provided in the schema
        # and the attr required is not necessary
        return InputField(type_=URL, description=get_django_field_description(field))
    


@convert_django_field_to_input.register(models.OneToOneRel)
def convert_onetoone_field_to_djangomodel(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(type_=ID, description=get_django_field_description(field), required=django_field_is_required(field))
    else:
        return InputField(type_=ID, description=get_django_field_description(field))
    # from graphene_django_cruddals.converters.for_entity.utils import converter_pkk_field
    # if not field.related_model:
    #     return ID(required=not field.null)
    # model:DjangoModel = field.related_model
    # pk_field = model._meta.pk
    # if not pk_field:
    #     return ID(required=not field.null)
    # converted_pk_field = converter_pkk_field(pk_field, registry)
    # if not converted_pk_field:
    #     return ID(required=not field.null)
    # return converted_pk_field


@convert_django_field_to_input.register(models.ManyToManyField)
@convert_django_field_to_input.register(models.ManyToManyRel)
@convert_django_field_to_input.register(models.ManyToOneRel)
def convert_field_to_list_or_connection(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(type_=List(ID), description=get_django_field_description(field), required=django_field_is_required(field))
    else:
        return InputField(type_=List(ID), description=get_django_field_description(field))
    # model = field.related_model
    # from graphene_django_cruddals.converters.for_entity.utils import converter_pkk_field

    # pk_field = model._meta.pk
    # converted_pk_field = converter_pkk_field(pk_field, registry)
    # if not converted_pk_field:
    #     return List(ID, required=django_field_is_required(field))
    # return List(converted_pk_field.__class__, required=django_field_is_required(field))


@convert_django_field_to_input.register(models.OneToOneField)
@convert_django_field_to_input.register(models.ForeignKey)
def convert_field_to_djangomodel(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    if type_mutation == TypesMutationEnum.CREATE.value:
        return InputField(type_=ID, description=get_django_field_description(field), required=django_field_is_required(field))
    else:
        return InputField(type_=ID, description=get_django_field_description(field))
    # model = field.related_model
    # pk_field = model._meta.pk
    # converted_pk_field = converter_pkk_field(pk_field, registry)
    # if not converted_pk_field:
    #     return ID(required=django_field_is_required(field))
    # return converted_pk_field => This old code is if maybe the pk is not a ID




@convert_django_field_to_input.register(GenericForeignKey)
def convert_field_to_union_type(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    """TODO Add support"""
    return


@convert_django_field_to_input.register(GenericRelation)
def convert_relation_field_to_union_type(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    """TODO Add support"""
    return


@convert_django_field_to_input.register(GenericRel) # Representa otro tipo OneToMany
def convert_field_to__type(field:DjangoField, registry: RegistryGlobal, type_mutation:TypesMutation):
    """TODO Add support"""
    return

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@ FOR RELATION FIELDS NESTED @@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


@singledispatch
def convert_relation_field_to_input(
    field: DjangoField,
    registry: RegistryGlobal,
    type_mutation_input: TypesMutation  = TypesMutationEnum.CREATE.value,
):
    raise Exception(
        "Don't know how to convert the Django field {} ({}), please check if is relation Field".format(
            field, field.__class__
        )
    )


@convert_relation_field_to_input.register(models.ManyToManyField)
@convert_relation_field_to_input.register(models.ManyToManyRel)
@convert_relation_field_to_input.register(models.ManyToOneRel)
@convert_relation_field_to_input.register(GenericRelation) # Representa otro tipo ManyToOne
def convert_field_to_list(
    field: DjangoField,
    registry: RegistryGlobal,
    type_mutation_input: TypesMutation = TypesMutationEnum.CREATE.value,
):
    model = field.related_model

    def dynamic_type():
        model_input_object_type = None
        registries_for_model = registry.get_registry_for_model(model)
        if (
            registries_for_model is not None
            and "input_object_type" in registries_for_model
        ):
            model_input_object_type = registries_for_model["input_object_type"]

        if not model_input_object_type:
            return
        from graphene_django_cruddals.utils import build_class

        if type_mutation_input == TypesMutationEnum.CREATE.value:
            connect_model_input = build_class( 
                name=f"{model.__name__}ConnectInput", 
                bases=(InputObjectType,), 
                attrs={ "connect": List(NonNull(model_input_object_type)) }
            )

            registry.register_model(
                model,
                "input_object_type_for_connect",
                connect_model_input,
            )

            return InputField(connect_model_input)
            # return InputField(List(NonNull(model_input_object_type)))
        else:  # update, create_update
            

            model_where_input_object_type = None
            if (
                registries_for_model is not None
                and "input_object_type_for_search" in registries_for_model
            ):
                model_where_input_object_type = registries_for_model[
                    "input_object_type_for_search"
                ]
            if not model_where_input_object_type:
                return

            connect_disconnect_model_input = build_class(
                name=f"{model.__name__}ConnectDisconnectInput",
                bases=(InputObjectType,),
                attrs={
                    "connect": List(NonNull(model_input_object_type)),
                    "disconnect": List(NonNull(model_where_input_object_type)),
                },
            )

            registry.register_model(
                model,
                "input_object_type_for_connect_disconnect",
                connect_disconnect_model_input,
            )

            return InputField(connect_disconnect_model_input)

    return Dynamic(dynamic_type)


@convert_relation_field_to_input.register(models.OneToOneField)
@convert_relation_field_to_input.register(models.ForeignKey)
@convert_relation_field_to_input.register(models.OneToOneRel)
def convert_field_to_input_django_model(
    field: DjangoField,
    registry: RegistryGlobal,
    type_mutation_input: TypesMutation = TypesMutationEnum.CREATE.value,
):
    model = field.related_model

    def dynamic_type():
        model_input_object_type = None
        registries_for_model = registry.get_registry_for_model(model)
        if (
            registries_for_model is not None
            and "input_object_type" in registries_for_model
        ):
            model_input_object_type = registries_for_model["input_object_type"]
        if not model_input_object_type:
            return

        # Avoid create field for auto generate OneToOneField product of an inheritance
        if isinstance(field, models.OneToOneField) and issubclass(
            field.model, field.related_model
        ):
            return

        return InputField(model_input_object_type)

    return Dynamic(dynamic_type)



class GenericForeignKeyInput(InputObjectType):
    app_label = String(required=True)
    model = String(required=True)
    object = GenericScalar()



@convert_relation_field_to_input.register(GenericForeignKey)
def convert_generic_field_to_input_django_model( field: DjangoField, registry: RegistryGlobal, type_mutation_input: TypesMutation = TypesMutationEnum.CREATE.value, ):
    
    return GenericForeignKeyInput()



@convert_relation_field_to_input.register(GenericRel) # Representa otro tipo OneToMany
def convert_relation_field_to__type(field:DjangoField, registry: RegistryGlobal):
    """TODO Add support"""
    return

"""TODO"""
# @convert_django_field_to_input.register(ArrayField)
# @convert_django_field_to_input.register(RangeField)

# Register Django lazy()-wrapped values as GraphQL description/help_text.
# This is needed for using lazy translations, see https://github.com/graphql-python/graphql-core-next/issues/58.
register_description(Promise)
