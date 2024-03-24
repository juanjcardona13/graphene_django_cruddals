from functools import partial, singledispatch
from typing import Union

from django.db import models
from django.utils.functional import Promise
from graphene import (
    Dynamic,
    ObjectType,
)
import graphene
from graphql.pyutils import register_description

from graphene_django_cruddals.converters.for_fields.utils import get_django_field_description, django_field_is_required

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
)
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation, GenericRel
from graphene_django_cruddals.utils import transform_string
from django.db.models.manager import Manager
from .compat import ArrayField, HStoreField, JSONField, PGJSONField, RangeField


def get_unbound_function(func):
    if not getattr(func, "__self__", True):
        return func.__func__
    return func


def resolve_for_relation_field(field, model, _type, root, info, **args):
    from graphene_django_cruddals.operations_fields.utils import maybe_queryset
    queryset = None
    attname = field.name
    default_value = getattr(field, "default", None)
    instance = getattr(root, attname, default_value)
    if instance is None:
        return None
    elif isinstance(instance, Manager):
        queryset = instance.get_queryset()
    else:
        queryset = model.objects.filter(id=instance.id)
    queryset =  maybe_queryset(_type.get_queryset(queryset, info))
    try:
        return queryset.distinct().get()
    except model.DoesNotExist:
        return None


def get_function_for_type(graphene_type, func_name, name):
    """Gets a resolve function for a given ObjectType"""
    if not issubclass(graphene_type, ObjectType):
        return
    resolver = getattr(graphene_type, func_name, None)
    if not resolver:
        # If we don't find the resolver in the ObjectType class, then try to
        # find it in each of the interfaces
        interface_resolver = None
        for interface in graphene_type._meta.interfaces:
            if name not in interface._meta.fields:
                continue
            interface_resolver = getattr(interface, func_name, None)
            if interface_resolver:
                break
        resolver = interface_resolver

    # Only if is not decorated with classmethod
    if resolver:
        return get_unbound_function(resolver)


@singledispatch
def convert_django_field_to_output(field, registry: RegistryGlobal) -> Union[graphene.Field, graphene.List, Dynamic, None]:
    raise Exception(
        "Don't know how to convert the Django field {} ({})".format(
            field, field.__class__
        )
    )


@convert_django_field_to_output.register(models.BigAutoField)
@convert_django_field_to_output.register(models.AutoField)
@convert_django_field_to_output.register(models.SmallAutoField)
def convert_field_to_id(field, registry: RegistryGlobal):
    return graphene.Field(type_=graphene.ID, description=get_django_field_description(field), required=django_field_is_required(field))


@convert_django_field_to_output.register(models.CharField)
@convert_django_field_to_output.register(models.TextField)
@convert_django_field_to_output.register(models.FilePathField)
@convert_django_field_to_output.register(models.FileField)
@convert_django_field_to_output.register(models.ImageField)
def convert_field_to_string(field, registry: RegistryGlobal):
    return graphene.Field(type_=graphene.String, description=get_django_field_description(field), required=django_field_is_required(field))


@convert_django_field_to_output.register(models.PositiveSmallIntegerField)
@convert_django_field_to_output.register(models.SmallIntegerField)
@convert_django_field_to_output.register(models.IntegerField)
def convert_field_to_int(field, registry: RegistryGlobal):
    return graphene.Field(type_=graphene.Int, description=get_django_field_description(field), required=django_field_is_required(field))


# @convert_django_field_to_output.register(models.NullBooleanField)
@convert_django_field_to_output.register(models.BooleanField)
def convert_field_to_boolean(field, registry: RegistryGlobal):
    return graphene.Field(type_=graphene.Boolean, description=get_django_field_description(field), required=django_field_is_required(field))


@convert_django_field_to_output.register(models.BigIntegerField)
def convert_field_to_big_int(field, registry: RegistryGlobal):
    return graphene.Field(type_=graphene.BigInt, description=get_django_field_description(field), required=django_field_is_required(field))


@convert_django_field_to_output.register(models.DateField)
def convert_field_to_date(field, registry: RegistryGlobal):
    return graphene.Field(type_=graphene.Date, description=get_django_field_description(field), required=django_field_is_required(field))


@convert_django_field_to_output.register(models.TimeField)
def convert_field_to_time(field, registry: RegistryGlobal):
    return graphene.Field(type_=graphene.Time, description=get_django_field_description(field), required=django_field_is_required(field))


@convert_django_field_to_output.register(models.DateTimeField)
def convert_field_to_datetime(field, registry: RegistryGlobal):
    return graphene.Field(type_=graphene.DateTime, description=get_django_field_description(field), required=django_field_is_required(field))


@convert_django_field_to_output.register(models.DecimalField)
def convert_field_to_decimal(field, registry: RegistryGlobal):
    return graphene.Field(type_=graphene.Decimal, description=get_django_field_description(field), required=django_field_is_required(field))


@convert_django_field_to_output.register(models.FloatField)
def convert_field_to_float(field, registry: RegistryGlobal):
    return graphene.Field(type_=graphene.Float, description=get_django_field_description(field), required=django_field_is_required(field))


@convert_django_field_to_output.register(models.DurationField)
def convert_field_to_duration(field, registry: RegistryGlobal):
    return graphene.Field(type_=Duration, description=get_django_field_description(field), required=django_field_is_required(field))


@convert_django_field_to_output.register(models.BinaryField)
def convert_field_to_binary(field, registry: RegistryGlobal):
    return graphene.Field(type_=Binary, description=get_django_field_description(field), required=django_field_is_required(field))


@convert_django_field_to_output.register(HStoreField)
@convert_django_field_to_output.register(PGJSONField)
@convert_django_field_to_output.register(JSONField)
def convert_pg_and_json_field_to_json_string(field, registry: RegistryGlobal):
    return graphene.Field(type_=graphene.JSONString, description=get_django_field_description(field), required=django_field_is_required(field))


@convert_django_field_to_output.register(models.UUIDField)
def convert_field_to_uuid(field, registry: RegistryGlobal):
    return graphene.Field(type_=graphene.UUID, description=get_django_field_description(field), required=django_field_is_required(field))


@convert_django_field_to_output.register(models.EmailField)
def convert_field_to_email(field, registry: RegistryGlobal):
    return graphene.Field(type_=Email, description=get_django_field_description(field), required=django_field_is_required(field))


@convert_django_field_to_output.register(models.GenericIPAddressField)
def convert_field_to_ipv4(field, registry: RegistryGlobal):
    return graphene.Field(type_=IPv4, description=get_django_field_description(field), required=django_field_is_required(field))


@convert_django_field_to_output.register(models.IPAddressField)
def convert_field_to_ip(field, registry: RegistryGlobal):
    return graphene.Field(type_=IP, description=get_django_field_description(field), required=django_field_is_required(field))


@convert_django_field_to_output.register(models.PositiveIntegerField)
def convert_field_to_positive_int(field, registry: RegistryGlobal):
    return graphene.Field(type_=PositiveInt, description=get_django_field_description(field), required=django_field_is_required(field))


@convert_django_field_to_output.register(models.SlugField)
def convert_field_to_slug(field, registry: RegistryGlobal):
    return graphene.Field(type_=Slug, description=get_django_field_description(field), required=django_field_is_required(field))


@convert_django_field_to_output.register(models.URLField)
def convert_field_to_url(field, registry: RegistryGlobal):
    return graphene.Field(type_=URL, description=get_django_field_description(field), required=django_field_is_required(field))


@convert_django_field_to_output.register(models.OneToOneRel)
def convert_onetoone_field_to_djangomodel(field, registry: RegistryGlobal):
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

        return graphene.Field(related_type, required=django_field_is_required(field), resolver=default_resolver)

    return Dynamic(dynamic_type)


@convert_django_field_to_output.register(models.OneToOneField)
@convert_django_field_to_output.register(models.ForeignKey)
@convert_django_field_to_output.register(GenericRel) # Representa otro tipo OneToMany, Lo que seria un ForeignKey
def convert_field_to_djangomodel(field, registry: RegistryGlobal):
    related_model = field.related_model
    direct_model = field.model

    def dynamic_type():
        related_type = None
        direct_type = None

        registries_for_related_model = registry.get_registry_for_model(related_model)
        if ( registries_for_related_model is not None and "object_type" in registries_for_related_model ):
            related_type = registries_for_related_model["object_type"]

        registries_for_direct_model = registry.get_registry_for_model(direct_model)
        if ( registries_for_direct_model is not None and "object_type" in registries_for_direct_model ):
            direct_type = registries_for_direct_model["object_type"]

        if not related_type:
            return

        default_resolver = partial( resolve_for_relation_field, field, related_model, related_type )

        if direct_type:
            """Esta parte es importante por si en el TypeParent se define un resolve para el campo relacionado"""
            custom_resolver = get_function_for_type( direct_type, f"resolve_{field.name}", field.name )
            if custom_resolver:
                default_resolver = custom_resolver

        return graphene.Field(
            related_type,
            description=get_django_field_description(field),
            required=django_field_is_required(field),
            resolver=default_resolver,
        )

    return Dynamic(dynamic_type)


@convert_django_field_to_output.register(GenericForeignKey)
def convert_field_to_union_type(field, registry: RegistryGlobal):
    direct_model = field.model
    def dynamic_type():
        all_models_registered = registry.get_all_models_registered()

        types_for_union = tuple()

        for registries_for_model in all_models_registered.values():
            if registries_for_model is not None and "object_type" in registries_for_model:
                types_for_union += (registries_for_model["object_type"],)

        if not types_for_union:
            return
        
        #TODO: Al igual que para el ForeignKey, se debe buscar si el TypeParent tiene un resolve para el campo relacionado

        name = f"{direct_model.__name__}{transform_string(field.name, 'PascalCase')}UnionType"

        meta_class = type("Meta", (), {"types": types_for_union, "name": name})

        union_type = type(name, (graphene.Union,), {"Meta": meta_class})

        return graphene.Field(union_type)

    return Dynamic(dynamic_type)


@convert_django_field_to_output.register(models.ManyToManyField)
@convert_django_field_to_output.register(models.ManyToManyRel)
@convert_django_field_to_output.register(models.ManyToOneRel)
@convert_django_field_to_output.register(GenericRelation) # Representa otro tipo ManyToOne
def convert_field_to_list_or_connection(field, registry: RegistryGlobal):
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
            django_search_field = search_field.__class__
            return django_search_field(_type=search_field._type, args=search_field.args, description=description)

    return Dynamic(dynamic_type)


@convert_django_field_to_output.register(ArrayField)
def convert_postgres_array_to_list(field, registry: RegistryGlobal):
    inner_type = convert_django_field_to_output(field.base_field)
    if not isinstance(inner_type, (graphene.List, graphene.NonNull)):
        inner_type = (
            graphene.NonNull(type(inner_type))
            if inner_type.kwargs["required"]
            else type(inner_type)
        )
    return graphene.List(
        inner_type,
        description=get_django_field_description(field),
        required=django_field_is_required(field),
    )


@convert_django_field_to_output.register(RangeField)
def convert_postgres_range_to_string(field, registry: RegistryGlobal):
    inner_type = convert_django_field_to_output(field.base_field)
    if not isinstance(inner_type, (graphene.List, graphene.NonNull)):
        inner_type = (
            graphene.NonNull(type(inner_type))
            if inner_type.kwargs["required"]
            else type(inner_type)
        )
    return graphene.List(
        inner_type,
        description=get_django_field_description(field),
        required=django_field_is_required(field),
    )


# Register Django lazy()-wrapped values as GraphQL description/help_text.
# This is needed for using lazy translations, see https://github.com/graphql-python/graphql-core-next/issues/58.
register_description(Promise)
