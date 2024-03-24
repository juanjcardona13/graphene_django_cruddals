from django.db.models import Field as DjangoField

from graphene_django_cruddals.converters.for_fields.converter_filter_input import (
    convert_django_field_to_filter_input,
)
from graphene_django_cruddals.converters.for_fields.converter_input import (
    convert_django_field_to_input,
)
from graphene_django_cruddals.converters.for_fields.converter_order_by_input import (
    convert_django_field_to_order_by_input,
)
from graphene_django_cruddals.converters.for_fields.converter_output import (
    convert_django_field_to_output,
)
from graphene_django_cruddals.converters.for_fields.utils import (
    convert_choice_field_to_graphene_enum,
    exists_conversion_for_field,
    get_converted_field,
)
from graphene_django_cruddals.registry_global import RegistryGlobal, TypeRegistryForFieldEnum
from graphene_django_cruddals.types import TypesMutation, TypesMutationEnum


def convert_django_field_with_choices_to_output( field: DjangoField, registry: RegistryGlobal, convert_choices_to_enum=True ):
    converted = get_converted_field(field, registry, TypeRegistryForFieldEnum.OUTPUT.value)
    if converted:
        return converted
    if getattr(field, "choices", None) and convert_choices_to_enum:
        converted = convert_choice_field_to_graphene_enum(field, None, None)
    else:
        converted = convert_django_field_to_output(field, registry)
    registry.register_field(field, TypeRegistryForFieldEnum.OUTPUT.value, converted)
    return converted


def convert_django_field_with_choices_to_create_update_input( field: DjangoField, registry: RegistryGlobal, convert_choices_to_enum=True, type_mutation:TypesMutation=TypesMutationEnum.CREATE_UPDATE.value ):
    if type_mutation == TypesMutationEnum.UPDATE.value:
        type_of_registry = TypeRegistryForFieldEnum.INPUT_FOR_UPDATE.value
    elif type_mutation == TypesMutationEnum.CREATE.value:
        type_of_registry = TypeRegistryForFieldEnum.INPUT_FOR_CREATE.value
    else:
        type_of_registry = TypeRegistryForFieldEnum.INPUT_FOR_CREATE_UPDATE.value
    
    
    converted = get_converted_field(field, registry, type_of_registry)
    if converted:
        return converted
    if getattr(field, "choices", None) and convert_choices_to_enum:
        converted = converted = convert_choice_field_to_graphene_enum(field, None, type_mutation)
    else:
        converted = convert_django_field_to_input(field, registry, type_mutation)
    registry.register_field(field, type_of_registry, converted)
    return converted


def convert_django_field_without_choices_to_filter_input( field: DjangoField, registry: RegistryGlobal, convert_choices_to_enum=True ):
    converted = get_converted_field(field, registry, TypeRegistryForFieldEnum.INPUT_FOR_SEARCH.value)
    if converted:
        return converted 
    converted = convert_django_field_to_filter_input(field, registry)
    registry.register_field(field, TypeRegistryForFieldEnum.INPUT_FOR_SEARCH.value, converted)
    return converted


def convert_django_field_without_choices_to_order_by_input( field: DjangoField, registry: RegistryGlobal ):
    converted = get_converted_field(field, registry, TypeRegistryForFieldEnum.INPUT_FOR_ORDER_BY.value)
    if converted:
        return converted
    converted = convert_django_field_to_order_by_input(field, registry)
    registry.register_field(field, TypeRegistryForFieldEnum.INPUT_FOR_ORDER_BY.value, converted)
    return converted
