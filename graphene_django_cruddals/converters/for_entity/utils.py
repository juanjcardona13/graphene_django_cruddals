from collections import OrderedDict
from typing import Dict, List, Literal, Tuple, Type, Union
import warnings
from itertools import chain

import graphene
from django.db.models import Model as DjangoModel
from django.db.models import ManyToManyField, ManyToManyRel, ManyToOneRel, OneToOneRel
from django.db.models import AutoField, BigAutoField
from django.db.models import Field as DjangoField
from django.db.models import ManyToManyRel, ManyToOneRel
from django.db.models import OneToOneRel, SmallAutoField
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

from graphene_django_cruddals.converters.for_fields.main import (
    convert_django_field_with_choices_to_create_update_input,
    convert_django_field_with_choices_to_output,
    convert_django_field_without_choices_to_filter_input,
    convert_django_field_without_choices_to_order_by_input,
)
from graphene_django_cruddals.registry_global import RegistryGlobal
from graphene_django_cruddals.types import TypeRegistryForModel, TypesMutation, TypesMutationEnum


class CruddalsRelationField:
    """Mark to field for convert field to relation field"""


def convert_args_type_relation( model: DjangoModel, args_final, registry: RegistryGlobal, type_mutation_input: TypesMutation):
    from graphene_django_cruddals.converters.for_fields.converter_input import convert_relation_field_to_input

    for arg, value in args_final.items():
        if isinstance(value, CruddalsRelationField):
            django_field = model._meta.get_field(arg)

            if isinstance(django_field, GenericForeignKey):
                ct_field = django_field.ct_field
                fk_field = django_field.fk_field
                if ct_field in args_final or fk_field in args_final:
                    raise Exception( f"If you convert field {arg} of type GenericForeignKey, you can't use {ct_field} or {fk_field} in args, please exclude this fields" )
            
            relation_input_object_type = convert_relation_field_to_input( django_field, registry=registry, type_mutation_input=type_mutation_input, )
            args_final[arg] = relation_input_object_type
    return args_final


def converter_pk_field(pk_field:DjangoField, registry:RegistryGlobal, type_mutation:TypesMutation=TypesMutationEnum.CREATE_UPDATE.value):
    converted_pk = convert_django_field_with_choices_to_create_update_input( pk_field, registry, True )
    if type_mutation == TypesMutationEnum.UPDATE.value:
        if isinstance(converted_pk, graphene.InputField) and not isinstance(converted_pk.type, graphene.NonNull):
            converted_pk = graphene.InputField(
                type_=converted_pk.type,
                required=True,
                description=converted_pk.description,
                default_value=converted_pk.default_value,
            )
    elif type_mutation == TypesMutationEnum.CREATE_UPDATE.value:
        if isinstance(converted_pk, graphene.InputField) and isinstance(converted_pk.type, graphene.NonNull):
            converted_pk = graphene.InputField(
                type_=converted_pk.type.of_type,
                required=False,
                description=converted_pk.description,
                default_value=converted_pk.default_value,
            )
    return converted_pk


def exists_conversion_for_model( model: DjangoModel, registry: RegistryGlobal, type_of_registry: TypeRegistryForModel ):
    registries_for_model = registry.get_registry_for_model(model)
    if registries_for_model is not None and type_of_registry in registries_for_model:
        return True


def get_converted_model(model: DjangoModel, registry: RegistryGlobal, type_of_registry: TypeRegistryForModel): #TODO: Falta tipar el retorno
    registries_for_model = registry.get_registry_for_model(model)
    if registries_for_model is not None and type_of_registry in registries_for_model:
        return registries_for_model[type_of_registry]
    else:
        raise Exception(f"The model {model} has not been converted to {type_of_registry}")


# region ==== get_model_fields
def is_included(name:str, only_fields:Union[Literal["__all__"], Tuple[str, ...]], exclude_fields:Tuple[str, ...]):
    return (
        only_fields == "__all__" and name not in exclude_fields or name in only_fields
    )


def get_reverse_fields(model: DjangoModel) -> list[tuple[str, DjangoField]]:
    reverse_fields = {
        field.name: field
        for field in model._meta.get_fields()
        if field.auto_created and not field.concrete
    }

    for name, field in reverse_fields.items():
        # Django =>1.9 uses 'rel', django <1.9 uses 'related'
        related = getattr(field, "rel", None) or getattr(field, "related", None)
        if isinstance(related, ManyToOneRel) or ( isinstance(related, ManyToManyRel) and not related.symmetrical ):
            yield name, related


def get_field_name(field:DjangoField, for_queryset:bool) -> str:
    # Si el campo es un tipo de relación y se está consultando para un queryset,
    # se usa el nombre de la consulta relacionada si está disponible.
    if ( for_queryset and isinstance(field, (OneToOneRel, ManyToManyRel, ManyToOneRel)) and field.related_query_name is not None ):
        return field.related_query_name

    # Si el campo es una relación ManyToMany o ManyToOne, y no se está consultando para un queryset,
    # se usa el nombre relacionado si está disponible, de lo contrario, se usa el nombre de accessor.
    if ( not for_queryset and isinstance(field, (ManyToManyRel, ManyToOneRel)) and field.related_name is not None ):
        return field.related_name
    if not for_queryset and isinstance(field, (ManyToManyRel, ManyToOneRel)):
        accessor_name = field.get_accessor_name()
        if accessor_name is not None:
            return accessor_name
        else:
            warnings.warn(
                f"El campo {field.name} no tiene un nombre de accessor, se usará el nombre del campo."
            )

    # En todos los demás casos, se usa el nombre del campo.
    return field.name


def get_model_fields( model: DjangoModel, for_queryset:bool=False, for_mutation:bool=False, only_fields:Union[Literal["__all__"], Tuple[str, ...]]="__all__", exclude_fields:Tuple[str, ...]=() ) -> list[tuple[str, DjangoField]]:
    all_fields_list:List[DjangoField]
    if for_mutation:
        sortable_private_fields = [ f for f in model._meta.private_fields if isinstance(f, DjangoField) ]
        all_fields_list = list( chain( model._meta.concrete_fields, sortable_private_fields, model._meta.many_to_many, ) )
        all_fields_list = [ field for field in all_fields_list if getattr(field, "editable", True) and not isinstance(field, (AutoField, BigAutoField, SmallAutoField)) ]
    else:
        all_fields_list = ( list(model._meta.fields) + list(model._meta.many_to_many) + list(model._meta.private_fields) + list(model._meta.fields_map.values()) )

    reverse_fields = list(get_reverse_fields(model))
    invalid_fields = [field[1] for field in reverse_fields]
    local_fields = [ (get_field_name(field, for_queryset), field) for field in all_fields_list if field not in invalid_fields ]

    all_fields = local_fields + reverse_fields

    return [ (name, field) for name, field in all_fields if not str(name).endswith("+") and is_included(name, only_fields, exclude_fields) ]
# endregion


def get_output_fields( model: DjangoModel, registry: RegistryGlobal, meta_attrs: Dict = {}, ):
    fields = OrderedDict()

    model_fields = get_model_fields(
        model=model,
        only_fields=meta_attrs.get( "only_fields", meta_attrs.get("only", meta_attrs.get("fields", "__all__")) ),
        exclude_fields=meta_attrs.get("exclude_fields", meta_attrs.get("exclude", ())),
    )
    for name, field in model_fields:
        _convert_choices_to_enum = meta_attrs.get("convert_choices_to_enum", True)
        if not isinstance(_convert_choices_to_enum, bool):
            _convert_choices_to_enum = True if name in _convert_choices_to_enum else False

        converted = convert_django_field_with_choices_to_output( field, registry, convert_choices_to_enum=_convert_choices_to_enum )

        if isinstance( field, (ManyToManyField, ManyToManyRel, ManyToOneRel, GenericRelation) ) and not isinstance( field, OneToOneRel ):
            fields[f"paginated_{name}"] = converted
        else:
            fields[name] = converted

    return fields


def get_input_fields_for_create_update( model: DjangoModel, registry: RegistryGlobal, type_mutation: TypesMutation = TypesMutationEnum.CREATE_UPDATE.value, meta_attrs: Dict = {}, ):
    input_fields = OrderedDict()
    model_fields = get_model_fields( model=model, for_mutation=True, only_fields=meta_attrs.get( "only_fields", meta_attrs.get("only", meta_attrs.get("fields", "__all__")) ), exclude_fields=meta_attrs.get("exclude_fields", meta_attrs.get("exclude", ())), )
    field_pk = model._meta.pk
    if not field_pk:
        raise Exception("The model does not have a primary key")
    
    converted_pk = converter_pk_field(field_pk, registry, type_mutation)
    if converted_pk:
        if ( type_mutation == TypesMutationEnum.UPDATE.value or type_mutation == TypesMutationEnum.CREATE_UPDATE.value ):
            input_fields[field_pk.name] = converted_pk
    else:
        if type_mutation == TypesMutationEnum.UPDATE.value:
            input_fields[field_pk.name] = graphene.InputField(type_=graphene.ID, required=True)
        elif type_mutation == TypesMutationEnum.CREATE_UPDATE.value:
            input_fields[field_pk.name] = graphene.InputField(type_=graphene.ID, required=False)

    for name, field in model_fields:
        converted_field = convert_django_field_with_choices_to_create_update_input(
            field=field,
            registry=registry,
            convert_choices_to_enum=True,
            type_mutation=type_mutation,
        )
        input_fields[name] = converted_field
    return input_fields


def get_input_fields_for_filter(
    model: DjangoModel, registry: RegistryGlobal, meta_attrs: Dict = {}
):
    input_fields = OrderedDict()
    model_fields = get_model_fields(
        model=model,
        for_queryset=True,
        only_fields=meta_attrs.get( "only_fields", meta_attrs.get("only", meta_attrs.get("fields", "__all__")) ),
        exclude_fields=meta_attrs.get("exclude_fields", meta_attrs.get("exclude", ())),
    )
    for name, field in model_fields:
        converted_field = convert_django_field_without_choices_to_filter_input(
            field=field, registry=registry, convert_choices_to_enum=True
        )
        input_fields[name] = converted_field
    return input_fields


def get_input_fields_for_order_by(
    model: DjangoModel, registry: RegistryGlobal, meta_attrs: Dict = {}
):
    input_fields = OrderedDict()
    model_fields = get_model_fields(
        model=model,
        for_queryset=True,
        only_fields=meta_attrs.get( "only_fields", meta_attrs.get("only", meta_attrs.get("fields", "__all__")) ),
        exclude_fields=meta_attrs.get("exclude_fields", meta_attrs.get("exclude", ())),
    )
    for name, field in model_fields:
        converted_field = convert_django_field_without_choices_to_order_by_input(
            field=field, registry=registry
        )
        input_fields[name] = converted_field
    return input_fields
