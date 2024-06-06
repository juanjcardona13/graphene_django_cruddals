from functools import partial, singledispatch
from typing import Type, Union

from django.contrib.contenttypes.fields import (
    GenericForeignKey,
    GenericRel,
    GenericRelation,
)
from django.db import models
from django.utils.functional import Promise
from graphene_cruddals import ModelSearchField, RegistryGlobal, transform_string
from graphql.pyutils import register_description

import graphene
from graphene import Dynamic
from graphene.types.resolver import dict_or_attr_resolver
from graphene_django_cruddals.converters.utils import (
    get_django_field_description,
    get_django_field_is_required,
    get_function_for_type,
    resolve_for_relation_field,
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
)

from .compat import (
    HStoreField,
    JSONField,
    PGJSONField,
)


def convert_django_field_to_output(
    name: str, field, model: models.Model, registry: "RegistryGlobal"
) -> Union[graphene.Field, graphene.List, Dynamic, None]:
    return _convert_field_dispatch(field, name, model, registry)


@singledispatch
def _convert_field_dispatch(
    field, name: str, model: models.Model, registry: "RegistryGlobal"
) -> Union[graphene.Field, graphene.List, Dynamic, None]:
    raise ValueError(
        f"Don't know how to convert the Django field {field} ({field.__class__})"
    )


@_convert_field_dispatch.register(models.BigAutoField)
@_convert_field_dispatch.register(models.AutoField)
@_convert_field_dispatch.register(models.SmallAutoField)
def convert_field_to_id(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    return graphene.Field(
        type_=graphene.ID,
        description=get_django_field_description(field),
        required=get_django_field_is_required(field),
    )


@_convert_field_dispatch.register(models.CharField)
@_convert_field_dispatch.register(models.TextField)
@_convert_field_dispatch.register(models.FilePathField)
@_convert_field_dispatch.register(models.FileField)
@_convert_field_dispatch.register(models.ImageField)
def convert_field_to_string(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    return graphene.Field(
        type_=graphene.String,
        description=get_django_field_description(field),
        required=get_django_field_is_required(field),
    )


@_convert_field_dispatch.register(models.PositiveSmallIntegerField)
@_convert_field_dispatch.register(models.SmallIntegerField)
@_convert_field_dispatch.register(models.IntegerField)
def convert_field_to_int(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    return graphene.Field(
        type_=graphene.Int,
        description=get_django_field_description(field),
        required=get_django_field_is_required(field),
    )


# @_convert_field_dispatch.register(models.NullBooleanField)
@_convert_field_dispatch.register(models.BooleanField)
def convert_field_to_boolean(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    return graphene.Field(
        type_=graphene.Boolean,
        description=get_django_field_description(field),
        required=get_django_field_is_required(field),
    )


@_convert_field_dispatch.register(models.BigIntegerField)
def convert_field_to_big_int(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    return graphene.Field(
        type_=graphene.BigInt,
        description=get_django_field_description(field),
        required=get_django_field_is_required(field),
    )


@_convert_field_dispatch.register(models.DateField)
def convert_field_to_date(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    return graphene.Field(
        type_=graphene.Date,
        description=get_django_field_description(field),
        required=get_django_field_is_required(field),
    )


@_convert_field_dispatch.register(models.TimeField)
def convert_field_to_time(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    return graphene.Field(
        type_=graphene.Time,
        description=get_django_field_description(field),
        required=get_django_field_is_required(field),
    )


@_convert_field_dispatch.register(models.DateTimeField)
def convert_field_to_datetime(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    return graphene.Field(
        type_=graphene.DateTime,
        description=get_django_field_description(field),
        required=get_django_field_is_required(field),
    )


@_convert_field_dispatch.register(models.DecimalField)
def convert_field_to_decimal(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    return graphene.Field(
        type_=graphene.Decimal,
        description=get_django_field_description(field),
        required=get_django_field_is_required(field),
    )


@_convert_field_dispatch.register(models.FloatField)
def convert_field_to_float(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    return graphene.Field(
        type_=graphene.Float,
        description=get_django_field_description(field),
        required=get_django_field_is_required(field),
    )


@_convert_field_dispatch.register(models.DurationField)
def convert_field_to_duration(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    return graphene.Field(
        type_=Duration,
        description=get_django_field_description(field),
        required=get_django_field_is_required(field),
    )


@_convert_field_dispatch.register(models.BinaryField)
def convert_field_to_binary(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    return graphene.Field(
        type_=Binary,
        description=get_django_field_description(field),
        required=get_django_field_is_required(field),
    )


@_convert_field_dispatch.register(HStoreField)
@_convert_field_dispatch.register(PGJSONField)
@_convert_field_dispatch.register(JSONField)
def convert_pg_and_json_field_to_json_string(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    """TODO Add support"""
    return graphene.Field(
        type_=graphene.JSONString,
        description=get_django_field_description(field),
        required=get_django_field_is_required(field),
    )


@_convert_field_dispatch.register(models.UUIDField)
def convert_field_to_uuid(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    return graphene.Field(
        type_=graphene.UUID,
        description=get_django_field_description(field),
        required=get_django_field_is_required(field),
    )


@_convert_field_dispatch.register(models.EmailField)
def convert_field_to_email(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    return graphene.Field(
        type_=Email,
        description=get_django_field_description(field),
        required=get_django_field_is_required(field),
    )


@_convert_field_dispatch.register(models.GenericIPAddressField)
def convert_field_to_ipv4(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    return graphene.Field(
        type_=IPv4,
        description=get_django_field_description(field),
        required=get_django_field_is_required(field),
    )


@_convert_field_dispatch.register(models.IPAddressField)
def convert_field_to_ip(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    return graphene.Field(
        type_=IP,
        description=get_django_field_description(field),
        required=get_django_field_is_required(field),
    )


@_convert_field_dispatch.register(models.PositiveIntegerField)
def convert_field_to_positive_int(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    return graphene.Field(
        type_=PositiveInt,
        description=get_django_field_description(field),
        required=get_django_field_is_required(field),
    )


@_convert_field_dispatch.register(models.SlugField)
def convert_field_to_slug(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    return graphene.Field(
        type_=Slug,
        description=get_django_field_description(field),
        required=get_django_field_is_required(field),
    )


@_convert_field_dispatch.register(models.URLField)
def convert_field_to_url(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    return graphene.Field(
        type_=URL,
        description=get_django_field_description(field),
        required=get_django_field_is_required(field),
    )


@_convert_field_dispatch.register(models.OneToOneRel)
def convert_onetoone_field_to_djangomodel(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    related_model = field.related_model
    direct_model = field.model

    def dynamic_type():
        related_type = None
        direct_type = None

        registries_for_related_model = registry.get_registry_for_model(related_model)
        if (
            registries_for_related_model is not None
            and "object_type" in registries_for_related_model
        ):
            related_type = registries_for_related_model["object_type"]

        registries_for_direct_model = registry.get_registry_for_model(direct_model)
        if (
            registries_for_direct_model is not None
            and "object_type" in registries_for_direct_model
        ):
            direct_type = registries_for_direct_model["object_type"]

        if not related_type:
            return

        default_resolver = partial(
            resolve_for_relation_field, field, related_model, related_type
        )

        if direct_type:
            default_resolver = get_function_for_type(
                direct_type, f"resolve_{field.name}", field.name
            )

        return graphene.Field(
            related_type,
            required=get_django_field_is_required(field),
            resolver=default_resolver,
        )

    return Dynamic(dynamic_type)


@_convert_field_dispatch.register(models.OneToOneField)
@_convert_field_dispatch.register(models.ForeignKey)
@_convert_field_dispatch.register(GenericRel)
def convert_field_to_djangomodel(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    related_model = field.related_model
    direct_model = field.model

    def dynamic_type():
        related_type = None
        direct_type = None

        registries_for_related_model = registry.get_registry_for_model(related_model)
        if (
            registries_for_related_model is not None
            and "object_type" in registries_for_related_model
        ):
            related_type = registries_for_related_model["object_type"]

        registries_for_direct_model = registry.get_registry_for_model(direct_model)
        if (
            registries_for_direct_model is not None
            and "object_type" in registries_for_direct_model
        ):
            direct_type = registries_for_direct_model["object_type"]

        if not related_type:
            return

        default_resolver = partial(
            resolve_for_relation_field, field, related_model, related_type
        )

        if direct_type:
            """Esta parte es importante por si en el TypeParent se define un resolver para el campo relacionado"""
            custom_resolver = get_function_for_type(
                direct_type, f"resolve_{field.name}", field.name
            )
            if custom_resolver:
                default_resolver = custom_resolver

        return graphene.Field(
            related_type,
            description=get_django_field_description(field),
            required=get_django_field_is_required(field),
            resolver=default_resolver,
        )

    return Dynamic(dynamic_type)


@_convert_field_dispatch.register(GenericForeignKey)
def convert_field_to_union_type(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    direct_model = field.model

    def dynamic_type():
        all_models_registered = registry.get_all_models_registered()

        types_for_union = ()

        for registries_for_model in all_models_registered.values():
            if (
                registries_for_model is not None
                and "object_type" in registries_for_model
            ):
                types_for_union += (registries_for_model["object_type"],)

        if not types_for_union:
            return

        name = f"{direct_model.__name__}{transform_string(field.name, 'PascalCase')}UnionType"

        meta_class = type("Meta", (), {"types": types_for_union, "name": name})

        union_type = type(name, (graphene.Union,), {"Meta": meta_class})

        return graphene.Field(union_type)

    return Dynamic(dynamic_type)


@_convert_field_dispatch.register(models.ManyToManyField)
@_convert_field_dispatch.register(models.ManyToManyRel)
@_convert_field_dispatch.register(models.ManyToOneRel)
@_convert_field_dispatch.register(GenericRelation)  # Representa otro tipo ManyToOne
def convert_field_to_list_or_connection(
    field, name: str, model: models.Model, registry: RegistryGlobal
):
    model = field.related_model

    def dynamic_type():
        if isinstance(field, (models.ManyToManyField, GenericRelation)):
            description = get_django_field_description(field)
        else:
            description = get_django_field_description(field.field)

        _type = None

        registries_for_model = registry.get_registry_for_model(model)
        if registries_for_model is not None and "object_type" in registries_for_model:
            _type = registries_for_model["object_type"]

        if not _type:
            return

        if registries_for_model is not None and "cruddals" in registries_for_model:
            cruddals_of_model = registries_for_model["cruddals"]

            search_field = cruddals_of_model.meta.search_field

            django_search_field: Type[ModelSearchField] = search_field.__class__

            from graphene_django_cruddals.main import (
                default_search_field_resolver,  # TODO: Esto es un parche, se debe buscar una mejor solución
            )

            # a este no le pongo esta función => "resolve_for_relation_field"
            # por que esa función solo es para cuando se tiene un campo OneToOneField o ForeignKey
            # es decir solo devuelve un obj y no tiene en cuenta el orderBy, Where y pagination
            # por eso este debe de llamar el default_search_field_resolver, pero también debe
            # de llamar la función dict_or_attr_resolver, para que traiga primero los
            # objs relacionados con el root (parent)
            old_resolver = partial(dict_or_attr_resolver, name, None)
            new_resolver = partial(
                default_search_field_resolver,
                model,
                registry,
                old_resolver,
                model._default_manager,
            )

            instance_search_field = django_search_field(
                model=model,
                plural_model_name=transform_string(
                    model._meta.verbose_name_plural, "PascalCase"
                ),
                registry=registry,
                resolver=new_resolver,
                **{
                    "description": description,
                    "name": transform_string(name, "camelCase"),
                },
            )
            return instance_search_field

    return Dynamic(dynamic_type)


# Register Django lazy()-wrapped values as GraphQL description/help_text.
# This is needed for using lazy translations, see https://github.com/graphql-python/graphql-core-next/issues/58.
register_description(Promise)

"""Add Support"""
# CommaSeparatedIntegerField
