from typing import Literal, Type, Union
import graphene
from django.db.models import Model as DjangoModel

from graphene_django_cruddals.converters.for_entity.utils import (
    exists_conversion_for_model,
    get_converted_model,
    get_input_fields_for_create_update,
    get_input_fields_for_filter,
    get_input_fields_for_order_by,
    get_output_fields,
    convert_args_type_relation,
)
from graphene_django_cruddals.operations_fields.main import DjangoListField
from graphene_django_cruddals.registry_global import RegistryGlobal, TypeRegistryForModelEnum
from graphene_django_cruddals.converters.django_types import DjangoObjectType
from graphene_django_cruddals.types import TypesMutation, TypesMutationEnum
from graphene_django_cruddals.utils import (
    build_class,
    get_name_of_model_in_different_case,
)

class PaginationInterface(graphene.Interface):
    total = graphene.Field(type_=graphene.Int)
    page = graphene.Field(type_=graphene.Int)
    pages = graphene.Field(type_=graphene.Int)
    has_next = graphene.Field(type_=graphene.Boolean)
    has_prev = graphene.Field(type_=graphene.Boolean)
    index_start_obj = graphene.Field(type_=graphene.Int)
    index_end_obj = graphene.Field(type_=graphene.Int)

def convert_django_model_to_object_type( model: DjangoModel, registry: RegistryGlobal, meta_attrs={}, extra_attrs={} ) -> Type[DjangoObjectType]:
    """TODO: Mejorar esto
    Los meta_attrs que espera recibir son los que permite Django Object Type en su clase interna `Meta`
    la doc encuentran en: https://docs.graphene-python.org/projects/django/en/latest/queries/
    y son:
        "model"
        "registry"
        "skip_registry"
        "fields"
        "exclude"
        "filter_fields"
        "filterset_class"
        "connection"
        "connection_class"
        "use_connection"
        "interfaces"
        "convert_choices_to_enum"
        "_meta"
        **options

    Los extra_attrs que espera recibir son los que permite Django Object Type los cuales son para custom types con sus resolves
    la doc encuentran en: https://docs.graphene-python.org/projects/django/en/latest/queries/#customising-fields
    y son:
        cualquier atributo con un valor valido de tipo graphene y su función resolve
    """

    names_of_model = get_name_of_model_in_different_case(model)
    singular_camel_case_name = names_of_model["camel_case"]
    if exists_conversion_for_model(model, registry, TypeRegistryForModelEnum.OBJECT_TYPE.value):
        return get_converted_model(model, registry, TypeRegistryForModelEnum.OBJECT_TYPE.value)
    
    attr_output_fields = get_output_fields(model, registry, meta_attrs=meta_attrs)

    MetaType = build_class( name="Meta", attrs={"model": model, "registry": registry, **meta_attrs} )
    ModelObjectType = build_class( name=f"{singular_camel_case_name}Type", bases=(DjangoObjectType,), attrs={"Meta": MetaType, **attr_output_fields, **extra_attrs}, )

    registry.register_model(model, TypeRegistryForModelEnum.OBJECT_TYPE.value, ModelObjectType)
    return ModelObjectType


def convert_django_model_to_paginated_object_type( model: DjangoModel, registry: RegistryGlobal, model_as_object_type=None, extra_attrs={} ):
    if exists_conversion_for_model(model, registry, TypeRegistryForModelEnum.PAGINATED_OBJECT_TYPE.value):
        return get_converted_model(model, registry, TypeRegistryForModelEnum.PAGINATED_OBJECT_TYPE.value)

    if model_as_object_type is None:
        model_as_object_type = convert_django_model_to_object_type( model=model, registry=registry )

    names_of_model = get_name_of_model_in_different_case(model)
    singular_camel_case_name = names_of_model["camel_case"]

    MetaPaginatedType = build_class( name="Meta", attrs={ "interfaces": (PaginationInterface,), "name": f"{singular_camel_case_name}PaginatedType", }, )
    ModelPaginatedType = build_class( name=f"{singular_camel_case_name}PaginatedType", bases=(graphene.ObjectType,), attrs={ "Meta": MetaPaginatedType, "objects": DjangoListField(model_as_object_type), **extra_attrs, }, )
    registry.register_model(model, TypeRegistryForModelEnum.PAGINATED_OBJECT_TYPE.value, ModelPaginatedType)
    return ModelPaginatedType


def convert_django_model_to_mutate_input_object_type( model: DjangoModel, registry: RegistryGlobal, type_mutation:TypesMutation=TypesMutationEnum.CREATE_UPDATE.value, meta_attrs={}, extra_attrs={} ) -> Type[graphene.InputObjectType]:
    names_of_model = get_name_of_model_in_different_case(model)
    singular_camel_case_name = names_of_model["camel_case"]

    if type_mutation == "create_update":
        type_of_registry = TypeRegistryForModelEnum.INPUT_OBJECT_TYPE.value #"input_object_type"
        name_input_object_type = f"{singular_camel_case_name}Input"
    elif type_mutation == "create":
        type_of_registry = TypeRegistryForModelEnum.INPUT_OBJECT_TYPE_FOR_CREATE.value #"input_object_type_for_create"
        name_input_object_type = f"Create{singular_camel_case_name}Input"
    elif type_mutation == "update":
        type_of_registry = TypeRegistryForModelEnum.INPUT_OBJECT_TYPE_FOR_UPDATE.value #"input_object_type_for_update"
        name_input_object_type = f"Update{singular_camel_case_name}Input"

    if exists_conversion_for_model(model, registry, type_of_registry):
        return get_converted_model(model, registry, type_of_registry)

    attr_input_fields = get_input_fields_for_create_update( model, registry, type_mutation, meta_attrs )
    attrs_final = convert_args_type_relation( model, {**attr_input_fields, **extra_attrs}, registry, type_mutation )

    ModelInputObjectType = build_class( name=name_input_object_type, bases=(graphene.InputObjectType,), attrs=attrs_final, )

    registry.register_model(model, type_of_registry, ModelInputObjectType)
    return ModelInputObjectType


def convert_django_model_to_filter_input_object_type( model: DjangoModel, registry: RegistryGlobal, meta_attrs={}, extra_attrs={} ):
    names_of_model = get_name_of_model_in_different_case(model)
    singular_camel_case_name = names_of_model["camel_case"]
    if exists_conversion_for_model(model, registry, TypeRegistryForModelEnum.INPUT_OBJECT_TYPE_FOR_SEARCH.value):
        return get_converted_model(model, registry, TypeRegistryForModelEnum.INPUT_OBJECT_TYPE_FOR_SEARCH.value)
    attr_input_fields = get_input_fields_for_filter( model, registry, meta_attrs=meta_attrs )
    attr_input_fields.update( { "AND": graphene.Dynamic( lambda: graphene.InputField( graphene.List( convert_django_model_to_filter_input_object_type( model, registry ) ) ) ), "OR": graphene.Dynamic( lambda: graphene.InputField( graphene.List( convert_django_model_to_filter_input_object_type( model, registry ) ) ) ), "NOT": graphene.Dynamic( lambda: graphene.InputField( convert_django_model_to_filter_input_object_type(model, registry) ) ), } )
    ModelInputObjectType = build_class( name=f"{singular_camel_case_name}FilterInput", bases=(graphene.InputObjectType,), attrs={**attr_input_fields, **extra_attrs}, )
    registry.register_model(model, TypeRegistryForModelEnum.INPUT_OBJECT_TYPE_FOR_SEARCH.value, ModelInputObjectType)
    return ModelInputObjectType


def convert_django_model_to_order_by_input_object_type( model: DjangoModel, registry: RegistryGlobal, meta_attrs={}, extra_attrs={} ):
    names_of_model = get_name_of_model_in_different_case(model)
    singular_camel_case_name = names_of_model["camel_case"]
    if exists_conversion_for_model(model, registry, TypeRegistryForModelEnum.INPUT_OBJECT_TYPE_FOR_ORDER_BY.value):
        return get_converted_model(model, registry, TypeRegistryForModelEnum.INPUT_OBJECT_TYPE_FOR_ORDER_BY.value)
    attr_input_fields = get_input_fields_for_order_by( model, registry, meta_attrs=meta_attrs )
    ModelInputObjectType = build_class( name=f"{singular_camel_case_name}OrderByInput", bases=(graphene.InputObjectType,), attrs={**attr_input_fields, **extra_attrs}, )
    registry.register_model( model, TypeRegistryForModelEnum.INPUT_OBJECT_TYPE_FOR_ORDER_BY.value, ModelInputObjectType )
    return ModelInputObjectType
