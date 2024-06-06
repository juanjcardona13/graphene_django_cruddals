from functools import singledispatch
from typing import Union

from django.contrib.contenttypes.fields import (
    GenericForeignKey,
    GenericRel,
    GenericRelation,
)
from django.db import models
from django.db.models.fields import Field as DjangoField
from graphene_cruddals import (
    RegistryGlobal,
    TypesMutation,
    TypesMutationEnum,
    build_class,
)

from graphene import (
    Dynamic,
    InputField,
    InputObjectType,
    List,
    NonNull,
    String,
)
from graphene.types.generic import GenericScalar

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@ FOR RELATION FIELDS NESTED @@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


class GenericForeignKeyInput(InputObjectType):
    app_label = String(required=True)
    model = String(required=True)
    object = GenericScalar()


def convert_relation_field_to_input(name: str, field, model, registry, type_mutation):
    return _convert_field_dispatch_relation(field, name, model, registry, type_mutation)


@singledispatch
def _convert_field_dispatch_relation(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation_input: TypesMutation = TypesMutationEnum.CREATE.value,
) -> Union[Dynamic, GenericForeignKeyInput, None]:
    raise ValueError(
        f"Don't know how to convert the Django field {field} ({field.__class__}), please check if it is a relation Field"
    )


@_convert_field_dispatch_relation.register(models.ManyToManyField)
@_convert_field_dispatch_relation.register(models.ManyToManyRel)
@_convert_field_dispatch_relation.register(models.ManyToOneRel)
@_convert_field_dispatch_relation.register(GenericRelation)
def convert_field_to_list(
    field: DjangoField,
    name: str,
    model: models.Model,
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

        if type_mutation_input == TypesMutationEnum.CREATE.value:
            connect_model_input = build_class(
                name=f"{model.__name__}ConnectInput",
                bases=(InputObjectType,),
                attrs={"connect": List(NonNull(model_input_object_type))},
            )

            registry.register_model(
                model,
                "input_object_type_for_connect",
                connect_model_input,
            )

            return InputField(connect_model_input)

        # update, create_update
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


@_convert_field_dispatch_relation.register(models.OneToOneField)
@_convert_field_dispatch_relation.register(models.ForeignKey)
@_convert_field_dispatch_relation.register(models.OneToOneRel)
def convert_field_to_input_django_model(
    field: DjangoField,
    name: str,
    model: models.Model,
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
            return None

        # Avoid create field for auto generate OneToOneField product of an inheritance
        if isinstance(field, models.OneToOneField) and issubclass(
            field.model, field.related_model
        ):
            return None

        return InputField(model_input_object_type)

    return Dynamic(dynamic_type)


@_convert_field_dispatch_relation.register(GenericForeignKey)
def convert_generic_field_to_input_django_model(
    field: DjangoField,
    name: str,
    model: models.Model,
    registry: RegistryGlobal,
    type_mutation_input: TypesMutation = TypesMutationEnum.CREATE.value,
):
    return GenericForeignKeyInput()


@_convert_field_dispatch_relation.register(GenericRel)  # Representa otro tipo OneToMany
def convert_relation_field_to__type(
    field: DjangoField, name: str, model: models.Model, registry: RegistryGlobal
):
    """TODO Add support"""
    return
