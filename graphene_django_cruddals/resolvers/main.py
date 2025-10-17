from enum import Enum
from typing import Any, Dict, Optional, Union

from django.db import transaction
from django.db.models import (
    Field as DjangoField,
    FileField,
    ForeignKey,
    ImageField,
    ManyToManyField,
    ManyToManyRel,
    ManyToOneRel,
    Model as DjangoModel,
    OneToOneField,
    OneToOneRel,
    Prefetch,
    QuerySet,
)
from django.forms import ModelForm as DjangoModelForm
from django.utils.datastructures import MultiValueDict
from graphene_cruddals import (
    ErrorCollectionType,
    ErrorType,
    ModelObjectType,
    ModelPaginatedObjectType,
    RegistryGlobal,
)
from graphql.language.ast import (
    FieldNode,
    FragmentSpreadNode as FragmentSpread,
    InlineFragmentNode as InlineFragment,
)

import graphene
from graphene_django_cruddals.converters.utils import maybe_queryset
from graphene_django_cruddals.utils.main import (
    add_mutate_errors,
    create_relation_model_objects,
    get_data_for_generic_foreign_key,
    get_model_fields_for_output,
    get_order_by_list_from_arguments,
    get_type_field,
    obj_to_modify_have_generic_foreign_key_input,
    paginate_queryset,
    parse_arguments_ast,
    resolve_argument,
    toggle_active_status,
    update_dict_with_model_instance,
    where_input_to_Q,
)


def _queryset_factory_analyze(
    info,
    selection_set,
    is_connection,
    model,
    registry,
    suffix="",
    computed_field_hints=None,
):
    def fusion_ret(a, b):
        [
            a["select_related"].append(x)
            for x in b["select_related"]
            if x not in a["select_related"]
        ]
        [a["prefetch_related"].append(x) for x in b["prefetch_related"]]
        [a["only"].append(x) for x in b["only"] if x not in a["only"]]
        return a

    if suffix == "":
        new_suffix = ""
    else:
        new_suffix = suffix + "__"

    ret = {
        "select_related": [],
        "only": [new_suffix + model._meta.pk.name],
        "prefetch_related": [],
    }

    model_fields = get_model_fields_for_output(model)

    if computed_field_hints is None:
        computed_field_hints = get_computed_field_hints(registry, model)

    for field in selection_set.selections:
        field_name = field.name.value

        if isinstance(field, FragmentSpread):
            new_ret = _queryset_factory_analyze(
                info,
                info.fragments[field_name].selection_set,
                is_connection,
                model,
                registry,
                suffix,
            )
            ret = fusion_ret(ret, new_ret)
            continue

        if isinstance(field, InlineFragment):
            # TODO: Handle this case
            # if field.type_condition.name.value == cls.__name__:
            print("Warning: InlineFragment not implemented")
            new_ret = _queryset_factory_analyze(
                info, field.selection_set, is_connection, model, registry, suffix
            )
            ret = fusion_ret(ret, new_ret)
            # continue

        if field_name.startswith("__"):
            continue

        if is_connection:
            if field_name in ["objects"]:
                new_ret = _queryset_factory_analyze(
                    info, field.selection_set, False, model, registry, new_suffix
                )
                ret = fusion_ret(ret, new_ret)
        else:
            registries_for_model = registry.get_registry_for_model(model)
            django_object_type: ModelObjectType = registries_for_model["object_type"]
            real_name, _type_field = get_type_field(django_object_type, field_name)

            if real_name.startswith("paginated_"):
                real_name = real_name.replace("paginated_", "", 1)

            try:
                model_field = model_fields[real_name]
            except KeyError:
                if real_name in computed_field_hints:
                    hints = computed_field_hints[real_name]
                    for sr in hints["select_related"]:
                        prefixed_sr = new_suffix + sr if new_suffix else sr
                        if prefixed_sr not in ret["select_related"]:
                            ret["select_related"].append(prefixed_sr)

                    for pr in hints["prefetch_related"]:
                        prefixed_pr = new_suffix + pr if new_suffix else pr
                        if prefixed_pr not in [
                            p.prefetch_to if isinstance(p, Prefetch) else p
                            for p in ret["prefetch_related"]
                        ]:
                            ret["prefetch_related"].append(prefixed_pr)

                    for only_field in hints["only"]:
                        prefixed_only = (
                            new_suffix + only_field if new_suffix else only_field
                        )
                        if prefixed_only not in ret["only"]:
                            ret["only"].append(prefixed_only)
                continue

            if getattr(field, "selection_set", None):
                if isinstance(
                    model_field,
                    (
                        OneToOneField,
                        OneToOneRel,
                        ForeignKey,
                        ManyToManyField,
                        ManyToManyRel,
                        ManyToOneRel,
                    ),
                ):
                    related_model = model_field.remote_field.model
                    registries_for_model = registry.get_registry_for_model(
                        related_model
                    )

                    if isinstance(
                        model_field, (OneToOneField, OneToOneRel, ForeignKey)
                    ):
                        ret["select_related"].append(new_suffix + real_name)
                        new_ret = _queryset_factory_analyze(
                            info,
                            field.selection_set,
                            False,
                            related_model,
                            registry,
                            new_suffix + real_name,
                        )
                        ret = fusion_ret(ret, new_ret)

                    elif isinstance(
                        model_field, (ManyToManyField, ManyToManyRel, ManyToOneRel)
                    ):
                        related_queryset = _queryset_factory(
                            model=related_model,
                            registry=registry,
                            info=info,
                            field_ast=field,  # Incluye arguments del nested field
                            is_connection=True,
                        )
                        if hasattr(model_field, "get_attname"):
                            real_name = model_field.get_attname()
                        elif hasattr(model_field, "get_accessor_name"):
                            real_name = model_field.get_accessor_name()
                        ret["prefetch_related"].append(
                            Prefetch(
                                new_suffix + real_name,
                                queryset=related_queryset,
                            )
                        )

                elif isinstance(model_field, FileField):
                    ret["only"].append(new_suffix + real_name)

            else:
                ret["only"].append(new_suffix + real_name)

    return ret


def _queryset_factory(
    model,
    registry,
    info,
    field_ast: Optional[FieldNode] = None,
    is_connection: bool = True,
    **kwargs,
) -> QuerySet:
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
    queryset = model.objects.all()

    selection_set = (
        field_ast.selection_set if field_ast else info.field_nodes[0].selection_set
    )

    queryset_factory = _queryset_factory_analyze(
        info=info,
        selection_set=selection_set,
        is_connection=is_connection,
        model=model,
        registry=registry,
        suffix="",
        computed_field_hints=None,
    )

    if queryset_factory["select_related"]:
        queryset = queryset.select_related(*queryset_factory["select_related"])
    if queryset_factory["only"]:
        queryset = queryset.only(*queryset_factory["only"])
    if queryset_factory["prefetch_related"]:
        queryset = queryset.prefetch_related(*queryset_factory["prefetch_related"])

    obj_where_q = None
    if "where" in kwargs and kwargs["where"]:
        obj_where_q = where_input_to_Q(kwargs["where"])
    elif field_ast and hasattr(field_ast, "arguments"):
        arguments = parse_arguments_ast(
            field_ast.arguments,
            variable_values=info.variable_values
            if hasattr(info, "variable_values")
            else {},
        )
        registries_for_model = registry.get_registry_for_model(model)
        where_input_type = registries_for_model.get("input_object_type_for_search")

        if where_input_type and "where" in arguments and arguments["where"]:
            where = resolve_argument(where_input_type, arguments["where"])
            obj_where_q = where_input_to_Q(where)
    if obj_where_q:
        queryset = queryset.filter(obj_where_q)

    order_by_list = None
    if "order_by" in kwargs or "orderBy" in kwargs:
        order_by_list = get_order_by_list_from_arguments(kwargs)
    elif field_ast and hasattr(field_ast, "arguments"):
        arguments = parse_arguments_ast(
            field_ast.arguments,
            variable_values=info.variable_values
            if hasattr(info, "variable_values")
            else {},
        )
        registries_for_model = registry.get_registry_for_model(model)
        order_by_input_type = registries_for_model.get("input_object_type_for_order_by")
        order_by_list = get_order_by_list_from_arguments(arguments, order_by_input_type)

    if order_by_list:
        queryset = queryset.order_by(*order_by_list)

    queryset = queryset.distinct()

    # TODO: REVISAR
    # Aplicar get_objects después de WHERE para que reciba un queryset filtrado
    # if hasattr(cls, 'get_objects'):
    #     get_objects = cls.get_objects

    #     if isinstance(get_objects, list):
    #         for func in get_objects:
    #             if callable(func):
    #                 queryset = func(queryset, info)
    #     elif callable(get_objects):
    #         queryset = get_objects(queryset, info)

    return queryset


def get_computed_field_hints(
    registry: RegistryGlobal,
    model: DjangoModel,
) -> Dict[str, Dict[str, Any]]:
    """
    Extrae hints de optimización de computed fields decorados con @resolver_hints.

    Args:
        registry: Registro global de graphene-django-cruddals
        model: Modelo Django del cual extraer computed fields

    Returns:
        Diccionario con hints por campo:
        {
            "field_name": {
                "select_related": [...],
                "prefetch_related": [...],
                "only": [...]
            }
        }
    """
    computed_field_hints = {}

    try:
        registries_for_model = registry.get_registry_for_model(model)
        object_type = registries_for_model.get("object_type")
        cruddals_class = registries_for_model.get("cruddals")

        type_to_inspect = cruddals_class if cruddals_class else object_type

        if not type_to_inspect:
            return computed_field_hints

        model_fields_names = get_model_fields_for_output(
            model=model,
            for_object_type=True,
        )

        if (
            cruddals_class
            and hasattr(cruddals_class, "meta")
            and hasattr(cruddals_class.meta, "model_as_object_type")
        ):
            actual_object_type = cruddals_class.meta.model_as_object_type
        else:
            actual_object_type = type_to_inspect

        if cruddals_class:
            for attr_name in dir(cruddals_class):
                if attr_name.startswith("resolve_") and not attr_name.startswith(
                    "resolve__"
                ):
                    field_name = attr_name[8:]

                    if field_name in model_fields_names:
                        continue

                    resolver = getattr(cruddals_class, attr_name)

                    if resolver and hasattr(resolver, "have_resolver_hints"):
                        computed_field_hints[field_name] = {
                            "select_related": getattr(resolver, "select_related", []),
                            "prefetch_related": getattr(
                                resolver, "prefetch_related", []
                            ),
                            "only": getattr(resolver, "only", []),
                        }

            for base_class in [cruddals_class] + list(cruddals_class.__mro__):
                if not hasattr(base_class, "__dict__"):
                    continue

                for attr_name, attr_value in base_class.__dict__.items():
                    if attr_name.startswith("_"):
                        continue

                    if (
                        attr_value
                        and hasattr(attr_value, "__class__")
                        and "Field" in str(attr_value.__class__)
                    ):
                        if attr_name in model_fields_names:
                            continue

                        if (
                            hasattr(attr_value, "resolver")
                            and attr_value.resolver is not None
                        ):
                            resolver = attr_value.resolver
                            if hasattr(resolver, "have_resolver_hints"):
                                computed_field_hints[attr_name] = {
                                    "select_related": getattr(
                                        resolver, "select_related", []
                                    ),
                                    "prefetch_related": getattr(
                                        resolver, "prefetch_related", []
                                    ),
                                    "only": getattr(resolver, "only", []),
                                }

        if hasattr(actual_object_type, "_meta") and hasattr(
            actual_object_type._meta, "fields"
        ):
            for field_name, field_obj in actual_object_type._meta.fields.items():
                if (
                    field_name in computed_field_hints
                    or field_name in model_fields_names
                ):
                    continue

                resolver = None
                if hasattr(field_obj, "resolver") and field_obj.resolver is not None:
                    resolver = field_obj.resolver
                elif hasattr(actual_object_type, f"resolve_{field_name}"):
                    resolver = getattr(actual_object_type, f"resolve_{field_name}")

                if resolver and hasattr(resolver, "have_resolver_hints"):
                    computed_field_hints[field_name] = {
                        "select_related": getattr(resolver, "select_related", []),
                        "prefetch_related": getattr(resolver, "prefetch_related", []),
                        "only": getattr(resolver, "only", []),
                    }

    except Exception:
        pass

    return computed_field_hints


def apply_query_arguments(
    queryset: Union[QuerySet, list, None],
    args: dict,
    model: DjangoModel,
    registry: RegistryGlobal,
    apply_where: bool = True,
    apply_order_by: bool = True,
    apply_distinct: bool = True,
) -> Union[QuerySet, list, None]:
    """
    Función centralizada para aplicar argumentos de query (where, order_by, distinct).

    Esta función procesa los argumentos comunes de GraphQL y los aplica al queryset de forma consistente.

    Args:
        queryset: El queryset a procesar
        args: Diccionario con los argumentos de GraphQL (where, order_by, orderBy, etc.)
        model: El modelo Django asociado
        registry: El registro global
        apply_where: Si aplicar filtros WHERE
        apply_order_by: Si aplicar ORDER BY
        apply_distinct: Si aplicar DISTINCT

    Returns:
        El queryset con los argumentos aplicados
    """
    if queryset is None:
        return None

    is_prefetched = isinstance(queryset, list) or (
        isinstance(queryset, QuerySet)
        and hasattr(queryset, "_result_cache")
        and queryset._result_cache is not None
    )

    if isinstance(queryset, QuerySet) and not is_prefetched:
        if apply_where and "where" in args:
            where = args["where"]
            if where and any(where.values()):
                obj_q = where_input_to_Q(where)
                queryset = queryset.filter(obj_q)

        if apply_order_by and not isinstance(queryset, list):
            order_by_list = get_order_by_list_from_arguments(args)
            if "order_by" in args or "orderBy" in args:
                queryset = queryset.order_by(*order_by_list)
            elif order_by_list and order_by_list != ["pk"]:
                queryset = queryset.order_by(*order_by_list)

        if apply_distinct:
            queryset = queryset.distinct()

    return queryset


def apply_get_objects_hook(
    queryset: Union[QuerySet, list, None],
    django_object_type: ModelObjectType,
    info,
) -> Union[QuerySet, list, None]:
    """
    Función centralizada para aplicar el hook get_objects de los ModelObjectType.

    Args:
        queryset: El queryset a procesar
        django_object_type: El tipo de objeto Django con posible hook get_objects
        info: GraphQL info object

    Returns:
        El queryset procesado por el hook get_objects
    """
    if not isinstance(queryset, QuerySet):
        return queryset

    if not hasattr(django_object_type, "get_objects"):
        return queryset

    get_objects = django_object_type.get_objects

    if isinstance(get_objects, list):
        for get_objects_func in get_objects:
            queryset = maybe_queryset(get_objects_func(queryset, info))
    elif callable(get_objects):
        queryset = maybe_queryset(get_objects(queryset, info))
    else:
        raise ValueError(
            "The get_objects attribute must be a callable or a list of callables."
        )

    return queryset


def default_create_update_resolver(
    model, model_form_class, registry, root, info, **args
):
    if "input" in args:
        arr_obj = []
        arr_errors = []
        for i, obj_to_modify in enumerate(args["input"]):
            with transaction.atomic():
                internal_arr_errors = []
                responses_direct = create_relation_model_objects(
                    "field_direct", model, registry, obj_to_modify, None, root, info
                )
                add_mutate_errors(responses_direct, i, internal_arr_errors)
                arr_errors.extend(internal_arr_errors)
                if len(internal_arr_errors) > 0:
                    continue

                if obj_to_modify_have_generic_foreign_key_input(obj_to_modify):
                    data_for_generic_foreign_key = get_data_for_generic_foreign_key(
                        obj_to_modify, model, responses_direct
                    )
                    obj_to_modify.update(data_for_generic_foreign_key)

                form_kwargs = {"data": obj_to_modify, "files": MultiValueDict()}
                obj_to_modify_copy = obj_to_modify.copy()
                for key, value in obj_to_modify_copy.items():
                    django_field: DjangoField = model._meta.get_field(key)
                    if isinstance(
                        django_field, (FileField, ImageField)
                    ) and not isinstance(value, str):
                        form_kwargs["files"].setlist(key, [value])
                    if (
                        issubclass(type(value), (graphene.Enum, Enum))
                        and hasattr(value, "value")
                        and not isinstance(value, str)
                    ):
                        obj_to_modify[key] = value.value
                pk = obj_to_modify.get("id", None)
                if pk:
                    instance = model.objects.get(pk=pk)
                    form_kwargs["instance"] = instance
                form: DjangoModelForm = model_form_class(**form_kwargs)
                if form.is_valid():
                    instance = form.save()
                    responses_reverse = create_relation_model_objects(
                        "field_inverse",
                        model,
                        registry,
                        obj_to_modify,
                        instance,
                        root,
                        info,
                    )
                    add_mutate_errors(
                        responses_reverse, i, internal_arr_errors, transaction
                    )
                    arr_errors.extend(internal_arr_errors)
                    if len(internal_arr_errors) > 0:
                        continue
                    arr_obj.append(instance)
                else:
                    errors = ErrorType.from_errors(form.errors)
                    e = ErrorCollectionType.from_errors(str(i), errors)
                    arr_errors.append(e)
                    transaction.set_rollback(True)

        if len(arr_obj) == 0:
            arr_obj = None
        if len(arr_errors) == 0:
            arr_errors = None

        return {"objects": arr_obj, "errors_report": arr_errors}


def default_read_field_resolver(
    model: DjangoModel,
    registry: RegistryGlobal,
    default_manager,
    root,
    info,
    **args,
):
    registries_for_model = registry.get_registry_for_model(model)
    django_object_type: ModelObjectType = registries_for_model["object_type"]

    queryset = _queryset_factory(
        model=model,
        registry=registry,
        info=info,
        field_ast=info.field_nodes[0],
        is_connection=False,
        **args,
    )

    queryset = apply_get_objects_hook(
        queryset=queryset,
        django_object_type=django_object_type,
        info=info,
    )

    if queryset is None:
        raise ValueError(
            "The queryset is None. Ensure that the 'where' clause is correct and the default manager returns a valid queryset."
        )
    return queryset.get()


def default_update_resolver(model, model_form_class, registry, root, info, **args):
    if "input" in args:
        new_input = [
            update_dict_with_model_instance(old_input, model=model)
            for old_input in args["input"]
        ]
        args["input"] = new_input
        return default_create_update_resolver(
            model, model_form_class, registry, root, info, **args
        )


def default_delete_field_resolver(model: DjangoModel, root, info, **args):
    if "where" in args.keys():
        where = args["where"]
        for value in where.values():
            if not value:
                return {"objects": []}
        obj_q = where_input_to_Q(where)
        queryset = model.objects.filter(obj_q)
        queryset.delete()
        return {"success": True}


def default_deactivate_field_resolver(
    model, field_for_activate_deactivate, root, info, **args
):
    if "where" in args.keys():
        where = args["where"]
        for value in where.values():
            if not value:
                return {"objects": []}
        obj_q = where_input_to_Q(where)
        queryset = model.objects.filter(obj_q).distinct()
        queryset = toggle_active_status(
            "DEACTIVATE", queryset, field_for_activate_deactivate
        )
        return {"objects": queryset}


def default_activate_field_resolver(
    model, field_for_activate_deactivate, root, info, **args
):
    if "where" in args.keys():
        where = args["where"]
        for value in where.values():
            if not value:
                return {"objects": []}
        obj_q = where_input_to_Q(where)
        queryset = model.objects.filter(obj_q).distinct()
        queryset = toggle_active_status(
            "ACTIVATE", queryset, field_for_activate_deactivate
        )
        return {"objects": queryset}


def default_list_field_resolver(
    model: DjangoModel,
    registry: RegistryGlobal,
    resolver,
    default_manager,
    root,
    info,
    **args,
):
    queryset = _queryset_factory(
        model=model,
        registry=registry,
        info=info,
        field_ast=info.field_nodes[0],
        is_connection=False,
        **args,
    )
    return queryset


def default_search_field_resolver(
    model: DjangoModel,
    registry: RegistryGlobal,
    resolver,
    default_manager,
    root,
    info,
    **args,
):
    registries_for_model = registry.get_registry_for_model(model)
    django_object_type: ModelObjectType = registries_for_model["object_type"]
    paginated_object_type: ModelPaginatedObjectType = registries_for_model[
        "paginated_object_type"
    ]

    queryset = None
    is_nested_paginated_field = False

    if resolver is not None and hasattr(resolver, "args"):
        attname, default_value = resolver.args
        if attname.startswith("paginated_"):
            is_nested_paginated_field = True
            posible_field = attname.replace("paginated_", "", 1)
            posible_field_with_default_set = posible_field + "_set"
            field_name_for_prefetch = (
                posible_field
                if hasattr(root, posible_field)
                else posible_field_with_default_set
            )

            if (
                hasattr(root, "_prefetched_objects_cache")
                and field_name_for_prefetch in root._prefetched_objects_cache
            ):
                queryset = list(root._prefetched_objects_cache[field_name_for_prefetch])
            else:
                maybe_manager = resolver(root, info, **args)
                if hasattr(root, field_name_for_prefetch):
                    maybe_manager = getattr(
                        root, field_name_for_prefetch, default_value
                    )
                queryset = maybe_queryset(maybe_manager)

    if not is_nested_paginated_field:
        queryset = _queryset_factory(
            model=model,
            registry=registry,
            info=info,
            field_ast=info.field_nodes[0],
            is_connection=True,
            **args,
        )
    elif queryset is None:
        queryset = maybe_queryset(default_manager)

        if queryset is None:
            raise ValueError(
                "The queryset is None. Ensure that the resolver or default manager returns a valid queryset."
            )

        queryset = apply_query_arguments(
            queryset=queryset,
            args=args,
            model=model,
            registry=registry,
            apply_where=True,
            apply_order_by=True,
            apply_distinct=True,
        )

    queryset = apply_get_objects_hook(
        queryset=queryset,
        django_object_type=django_object_type,
        info=info,
    )

    pagination_config = args.get("pagination_config", {}) or args.get(
        "paginationConfig", {}
    )

    return paginate_queryset(
        queryset,
        paginated_object_type,  # type: ignore
        pagination_config.get("items_per_page", "All"),
        pagination_config.get("page", 1),
    )
