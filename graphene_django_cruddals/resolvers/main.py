from enum import Enum
from typing import Any, Dict, List, Set, Union

from django.db import transaction
from django.db.models import (
    Field as DjangoField,
    FileField,
    ForeignKey,
    ImageField,
    ManyToManyField,
    Model as DjangoModel,
    OneToOneField,
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
    FragmentSpreadNode,
    InlineFragmentNode,
    SelectionSetNode,
)

import graphene
from graphene.utils.str_converters import to_snake_case
from graphene_django_cruddals.converters.utils import maybe_queryset
from graphene_django_cruddals.utils.main import (
    add_mutate_errors,
    create_relation_model_objects,
    get_data_for_generic_foreign_key,
    obj_to_modify_have_generic_foreign_key_input,
    order_by_input_to_args,
    paginate_queryset,
    toggle_active_status,
    update_dict_with_model_instance,
    where_input_to_Q,
)


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
    django_object_type: ModelObjectType = registry.get_registry_for_model(model)[
        "object_type"
    ]
    queryset: Union[QuerySet, None] = None
    if "where" in args.keys():
        queryset = maybe_queryset(default_manager)
        where = args["where"]
        obj_q = where_input_to_Q(where)
        queryset = queryset.filter(obj_q)
        queryset = queryset.distinct()
    if isinstance(queryset, QuerySet):
        if hasattr(django_object_type, "get_objects"):
            if isinstance(django_object_type.get_objects, list):
                for get_objects_func in django_object_type.get_objects:
                    if isinstance(get_objects_func, classmethod):
                        queryset = maybe_queryset(
                            get_objects_func.__func__(
                                django_object_type, queryset, info
                            )
                        )
                    else:
                        queryset = maybe_queryset(get_objects_func(queryset, info))
            else:
                queryset = maybe_queryset(
                    django_object_type.get_objects(queryset, info)
                )
        else:
            raise ValueError("The get_objects method is not defined.")
    if queryset is None:
        raise ValueError(
            "The queryset is None. Ensure that the 'where' clause is correct and the default manager returns a valid queryset."
        )
    return queryset.distinct().get()


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
        queryset = model.objects.filter(obj_q)
        queryset = queryset.distinct()
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
        queryset = model.objects.filter(obj_q)
        queryset = queryset.distinct()
        queryset = toggle_active_status(
            "ACTIVATE", queryset, field_for_activate_deactivate
        )
        return {"objects": queryset}


def default_list_field_resolver(resolver, default_manager, root, info, **args):
    queryset = None
    if resolver is not None and hasattr(resolver, "args"):
        queryset = maybe_queryset(
            resolver(root, info, **args)
        )  # Por lo general este resolver es el resolver por defecto, en este caso es el dict_or_attr_resolver, y va usar el atr_resolver, y va a traer el attr 'objects' del obj, y este 'objects' es un queryset
    if queryset is None:
        queryset = maybe_queryset(default_manager)
    return queryset


def extract_requested_fields_from_graphql_query(info) -> Set[str]:
    """
    Extrae los campos solicitados en la consulta GraphQL de forma recursiva.
    Retorna un set con todos los nombres de campos que se están solicitando.

    Maneja:
    - FragmentSpread: Resuelve fragmentos definidos
    - InlineFragment: Maneja fragmentos inline con condiciones de tipo
    - PaginatedType: Extrae campos del campo 'objects' cuando el tipo es paginado
    """
    requested_fields = set()

    def is_paginated_type(selection_set: SelectionSetNode) -> tuple[bool, FieldNode]:
        """
        Determina si un campo es de tipo PaginatedType verificando si tiene
        el campo 'objects' en su selection_set.
        """
        if not selection_set:
            return False, None
        for selection in selection_set.selections:
            # TODO: Debo de encontrar una mejor manera de verificar si es un PaginatedType, por que si alguien usa el campo 'objects' en otro lugar, se va a tomar como un PaginatedType
            if isinstance(selection, FieldNode) and hasattr(selection, "name"):
                if selection.name.value == "objects":
                    return True, selection
        return False, None

    def extract_from_selection_set(selection_set: SelectionSetNode, path: str = ""):
        if not selection_set:
            return
        selections = selection_set.selections
        for field in selections:
            if isinstance(field, FragmentSpreadNode):
                fragment_name = field.name.value
                fragment_definition = info.fragments.get(fragment_name)
                if fragment_definition and hasattr(
                    fragment_definition, "selection_set"
                ):
                    extract_from_selection_set(fragment_definition.selection_set, path)

            elif isinstance(field, InlineFragmentNode):
                if hasattr(field, "selection_set") and field.selection_set:
                    extract_from_selection_set(field.selection_set, path)

            elif (
                isinstance(field, FieldNode)
                and hasattr(field, "name")
                and hasattr(field, "selection_set")
            ):
                field_name = (
                    field.name.value
                    if hasattr(field.name, "value")
                    else str(field.name)
                )

                if field_name.startswith("__"):
                    continue

                field_name = to_snake_case(field_name)

                is_paginated, paginated_field = is_paginated_type(field.selection_set)
                if is_paginated:
                    field = paginated_field
                    if field_name.startswith("paginated_"):
                        field_name = field_name.replace("paginated_", "", 1)

                current_path = field_name if not path else f"{path}.{field_name}"
                requested_fields.add(current_path)
                if hasattr(field, "selection_set") and field.selection_set:
                    extract_from_selection_set(field.selection_set, current_path)

    if hasattr(info, "field_nodes") and info.field_nodes:
        for field_node in info.field_nodes:
            if hasattr(field_node, "selection_set"):
                is_paginated, paginated_field = is_paginated_type(
                    field_node.selection_set
                )
                if is_paginated:
                    extract_from_selection_set(paginated_field.selection_set)
                else:
                    extract_from_selection_set(field_node.selection_set)

    return requested_fields


def get_relation_fields_for_model(model: DjangoModel) -> Dict[str, Any]:
    """
    Obtiene todos los campos de relación (ForeignKey, OneToOneField, ManyToManyField)
    de un modelo Django de forma agnóstica.
    """
    relation_fields = {}

    for field in model._meta.get_fields():
        # TODO: Revisar si para los campos ManyToOneRel, OneToOneRel, ManyToManyRel, GenericRelation tambien se agregan
        if isinstance(field, (ForeignKey, OneToOneField, ManyToManyField)):
            relation_fields[field.name] = {
                "field": field,
                "related_model": field.related_model,
                "field_type": type(field).__name__,
                "is_many_to_many": field.many_to_many,
                "is_one_to_one": field.one_to_one,
                "is_foreign_key": isinstance(field, ForeignKey),
            }

    return relation_fields


def build_optimization_paths(
    requested_fields: Set[str], model: DjangoModel
) -> Dict[str, List[str]]:
    """
    Construye los paths de optimización (select_related y prefetch_related)
    basándose en los campos solicitados en la consulta GraphQL.

    Esta función es robusta y recursiva, validando que solo se incluyan
    campos relacionales en los paths de optimización.
    """
    relation_fields = get_relation_fields_for_model(model)
    select_related_paths = []
    prefetch_related_paths = []

    def is_relational_field(field_name: str, current_model: DjangoModel) -> bool:
        """Verifica si un campo es relacional en el modelo dado."""
        try:
            field = current_model._meta.get_field(field_name)
            return isinstance(field, (ForeignKey, OneToOneField, ManyToManyField))
        except Exception:
            return False

    def get_related_model(field_name: str, current_model: DjangoModel):
        """Obtiene el modelo relacionado para un campo dado."""
        try:
            field = current_model._meta.get_field(field_name)
            if isinstance(field, (ForeignKey, OneToOneField, ManyToManyField)):
                return field.related_model
        except Exception:
            pass
        return None

    def build_path_recursively(
        path_parts: List[str], current_model: DjangoModel, current_path: str = ""
    ) -> List[str]:
        """
        Construye paths de optimización de forma recursiva, validando
        que cada nivel del path sea un campo relacional válido.
        """
        if not path_parts:
            return []

        current_field = path_parts[0]
        remaining_parts = path_parts[1:]

        # Verificar si el campo actual es relacional
        if not is_relational_field(current_field, current_model):
            return []

        # Construir el path actual
        if current_path:
            full_path = f"{current_path}__{current_field}"
        else:
            full_path = current_field

        # Obtener el modelo relacionado
        related_model = get_related_model(current_field, current_model)
        if not related_model:
            return []

        result_paths = []

        # Si hay más partes en el path, continuar recursivamente
        if remaining_parts:
            nested_paths = build_path_recursively(
                remaining_parts, related_model, full_path
            )
            result_paths.extend(nested_paths)
            # También agregar el path actual si es relacional
            result_paths.append(full_path)
        else:
            # Si no hay más partes, agregar el path actual
            result_paths.append(full_path)

        return result_paths

    def categorize_path(path: str, model: DjangoModel) -> str:
        """
        Categoriza un path como select_related o prefetch_related
        basándose en el tipo de relación del primer campo.
        """
        first_field = path.split("__")[0]
        if first_field in relation_fields:
            field_info = relation_fields[first_field]
            if field_info["is_many_to_many"]:
                return "prefetch_related"
            elif field_info["is_one_to_one"] or field_info["is_foreign_key"]:
                return "select_related"
        return None

    # Procesar cada campo solicitado
    for field_path in requested_fields:
        path_parts = field_path.split(".")

        # Solo procesar paths con al menos 2 partes (relación + campo)
        if len(path_parts) >= 2:
            # Construir paths recursivamente
            built_paths = build_path_recursively(path_parts, model)

            # Categorizar cada path construido
            for path in built_paths:
                category = categorize_path(path, model)
                if category == "select_related":
                    select_related_paths.append(path)
                elif category == "prefetch_related":
                    prefetch_related_paths.append(path)

    return {
        "select_related": list(set(select_related_paths)),
        "prefetch_related": list(set(prefetch_related_paths)),
    }


def optimize_queryset_for_graphql_query(
    queryset: QuerySet, model: DjangoModel, info
) -> QuerySet:
    """
    Optimiza un queryset aplicando select_related y prefetch_related
    basándose en los campos solicitados en la consulta GraphQL.
    Esta función es completamente agnóstica y funciona con cualquier modelo Django.
    """
    try:
        # Extraer campos solicitados de la consulta GraphQL
        requested_fields = extract_requested_fields_from_graphql_query(info)

        # Construir paths de optimización
        optimization_paths = build_optimization_paths(requested_fields, model)

        # Aplicar select_related
        if optimization_paths["select_related"]:
            queryset = queryset.select_related(*optimization_paths["select_related"])

        # Aplicar prefetch_related
        if optimization_paths["prefetch_related"]:
            queryset = queryset.prefetch_related(
                *optimization_paths["prefetch_related"]
            )

        return queryset

    except Exception as e:
        # Si hay algún error en la optimización, retornar el queryset original
        # Esto asegura que la funcionalidad básica no se rompa
        print(f"Warning: Error in query optimization: {e}")
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
    # print("-------------Aca comienza la query------------")
    # print("model", model)
    # print("registry", registry)
    # print("resolver", resolver)
    # print("default_manager", default_manager)
    # print("root", root)
    # print("info", info)
    # print("args", args)
    # print("-------------Aca termina la query------------")
    registries_for_model = registry.get_registry_for_model(model)
    django_object_type: ModelObjectType = registries_for_model["object_type"]
    paginated_object_type: ModelPaginatedObjectType = registries_for_model[
        "paginated_object_type"
    ]

    queryset = maybe_queryset(default_manager)

    if resolver is not None and hasattr(resolver, "args"):
        maybe_manager = resolver(root, info, **args)
        attname, default_value = resolver.args
        if attname.startswith("paginated_"):
            posible_field = attname.replace("paginated_", "", 1)
            posible_field_with_default_set = posible_field + "_set"
            posible_field = (
                posible_field
                if hasattr(root, posible_field)
                else posible_field_with_default_set
            )
            if hasattr(root, posible_field):
                maybe_manager = getattr(root, posible_field, default_value)

        queryset: QuerySet = maybe_queryset(maybe_manager)

    if queryset is None:
        raise ValueError(
            "The queryset is None. Ensure that the resolver or default manager returns a valid queryset."
        )

    if "where" in args:
        where = args["where"]
        obj_q = where_input_to_Q(where)
        queryset = queryset.filter(obj_q)

    if "order_by" in args or "orderBy" in args:
        order_by = args.get("order_by") or args.get("orderBy")
        if isinstance(order_by, dict):
            order_by = [order_by]
        list_for_order = order_by_input_to_args(order_by)
        queryset = queryset.order_by(*list_for_order)
    else:
        queryset = queryset.order_by("pk")

    pagination_config = args.get("pagination_config", {}) or args.get(
        "paginationConfig", {}
    )
    queryset = queryset.distinct()

    queryset = optimize_queryset_for_graphql_query(queryset, model, info)

    if isinstance(queryset, QuerySet):
        if hasattr(django_object_type, "get_objects"):
            if isinstance(django_object_type.get_objects, list):
                for get_objects_func in django_object_type.get_objects:
                    if isinstance(get_objects_func, classmethod):
                        queryset = maybe_queryset(
                            get_objects_func.__func__(
                                django_object_type, queryset, info
                            )
                        )
                    else:
                        queryset = maybe_queryset(get_objects_func(queryset, info))
            else:
                queryset = maybe_queryset(
                    django_object_type.get_objects(queryset, info)
                )
        else:
            raise ValueError("The get_objects method is not defined.")
    return paginate_queryset(
        queryset,
        paginated_object_type,  # type: ignore
        pagination_config.get("items_per_page", "All"),
        pagination_config.get("page", 1),
    )
