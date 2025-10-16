"""
Extensions to ModelObjectType to add _queryset_factory functionality.

This module extends the base ModelObjectType from graphene_cruddals to add
centralized query optimization logic similar to graphene-django-crud.
"""
from typing import Any, Dict, Optional, Union
from django.db import models
from django.db.models import Prefetch, QuerySet
from graphene_cruddals.types.main import ModelObjectType
from graphene_cruddals import RegistryGlobal
from graphql.language.ast import FieldNode

def get_dependencies():
    """Lazy import of dependencies to avoid circular imports."""
    from graphene_django_cruddals.resolvers.main import (
        _queryset_factory_analyze as _analyze,
        get_computed_field_hints as _get_hints,
    )
    from graphene_django_cruddals.utils.main import (
        parse_arguments_ast as _parse_args,
        where_input_to_Q as _where_to_q,
        get_order_by_list_from_arguments as _get_order_by,
        resolve_argument as _resolve_arg,
    )
    return {
        '_queryset_factory_analyze': _analyze,
        'get_computed_field_hints': _get_hints,
        'parse_arguments_ast': _parse_args,
        'where_input_to_Q': _where_to_q,
        'get_order_by_list_from_arguments': _get_order_by,
        'resolve_argument': _resolve_arg,
    }


def _queryset_factory(cls, info, field_ast: Optional[FieldNode] = None, is_connection: bool = True, **kwargs) -> QuerySet:
    """
    Punto de entrada único para crear y optimizar querysets.

    Este método centraliza toda la lógica de optimización:
    - Análisis del AST de GraphQL para detectar campos solicitados
    - Aplicación de select_related, prefetch_related, only
    - Procesamiento de argumentos WHERE y ORDER BY
    - Aplicación del hook get_objects si existe

    Args:
        info: GraphQL ResolveInfo
        field_ast: Nodo AST del field (para obtener arguments y selection_set)
        is_connection: Si el queryset es para una conexión/lista o un objeto individual
        **kwargs: Argumentos adicionales

    Returns:
        QuerySet optimizado y filtrado
    """
    deps = get_dependencies()

    queryset = cls._meta.model.objects.all()

    selection_set = field_ast.selection_set if field_ast else info.field_nodes[0].selection_set

    queryset_factory = deps['_queryset_factory_analyze'](
        info=info,
        selection_set=selection_set,
        is_connection=is_connection,
        model=cls._meta.model,
        registry=cls._meta.registry,
        suffix="",
        computed_field_hints=None,
    )

    if queryset_factory["select_related"]:
        queryset = queryset.select_related(*queryset_factory["select_related"])
    if queryset_factory["only"]:
        queryset = queryset.only(*queryset_factory["only"])
    if queryset_factory["prefetch_related"]:
        queryset = queryset.prefetch_related(*queryset_factory["prefetch_related"])

    if field_ast and hasattr(field_ast, 'arguments'):
        arguments = deps['parse_arguments_ast'](
            field_ast.arguments,
            variable_values=info.variable_values if hasattr(info, 'variable_values') else {}
        )

        registries_for_model = cls._meta.registry.get_registry_for_model(cls._meta.model)

        if "where" in arguments:
            where_input_type = registries_for_model.get("input_object_type_for_search")

            if where_input_type:
                where = deps['resolve_argument'](where_input_type, arguments["where"])
                queryset = queryset.filter(deps['where_input_to_Q'](where))

        if "order_by" in arguments or "orderBy" in arguments:
            order_by_input_type = registries_for_model.get("input_object_type_for_order_by")
            order_by_list = deps['get_order_by_list_from_arguments'](arguments, order_by_input_type)
            if order_by_list:
                queryset = queryset.order_by(*order_by_list)

    queryset = queryset.distinct()

    # Aplicar get_objects después de WHERE para que reciba un queryset filtrado
    if hasattr(cls, 'get_objects'):
        get_objects = cls.get_objects

        if isinstance(get_objects, list):
            for func in get_objects:
                if callable(func):
                    queryset = func(queryset, info)
        elif callable(get_objects):
            queryset = get_objects(queryset, info)

    return queryset


def get_objects_queryset(cls, info) -> QuerySet:
    """
    Hook para obtener el queryset base y aplicar get_objects personalizado.

    Este método:
    1. Obtiene el queryset inicial del modelo
    2. Aplica el hook get_objects si existe (puede ser función única o lista)

    Args:
        info: GraphQL ResolveInfo

    Returns:
        QuerySet base (posiblemente modificado por get_objects)
    """
    # Obtener queryset base del modelo
    queryset = cls._meta.model.objects.all()

    # Aplicar hook get_objects si existe
    # IMPORTANTE: get_objects en cruddals tiene firma (cls, objects, info, **kwargs)
    # Como es un @classmethod, cuando lo obtenemos ya está bound, así que pasamos (objects, info)
    if hasattr(cls, 'get_objects'):
        get_objects = cls.get_objects

        if isinstance(get_objects, list):
            # Lista de funciones
            for func in get_objects:
                if callable(func):
                    # Cada función debería ser un bound classmethod
                    queryset = func(queryset, info)
        elif callable(get_objects):
            # Función única - ya es un bound classmethod, así que solo pasamos (objects, info)
            # El primer parámetro 'cls' ya está incluido en el bound method
            queryset = get_objects(queryset, info)

    return queryset


# Monkey-patch ModelObjectType para agregar los métodos
ModelObjectType._queryset_factory = classmethod(_queryset_factory)
ModelObjectType.get_objects_queryset = classmethod(get_objects_queryset)
