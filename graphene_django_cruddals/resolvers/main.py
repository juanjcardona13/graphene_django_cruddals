from enum import Enum
from typing import Union

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
    info, selection_set, is_connection, model, registry, suffix=""
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
                        related_queryset = related_model.objects.all()
                        order_by_list = ["pk"]
                        if hasattr(field, "arguments"):
                            field_args = parse_arguments_ast(
                                field.arguments,
                                variable_values=info.variable_values
                                if hasattr(info, "variable_values")
                                else {},
                            )
                            order_by_list = get_order_by_list_from_arguments(
                                field_args,
                                registries_for_model["input_object_type_for_order_by"],
                            )

                            if "where" in field_args.keys():
                                where = resolve_argument(
                                    registries_for_model[
                                        "input_object_type_for_search"
                                    ],
                                    field_args.get("where", {}),
                                )
                                related_queryset = related_queryset.filter(
                                    where_input_to_Q(where)
                                )

                        related_ret = _queryset_factory_analyze(
                            info,
                            field.selection_set,
                            True,
                            related_model,
                            registry,
                            "",
                        )

                        related_queryset = related_queryset.select_related(
                            *related_ret["select_related"]
                        )
                        related_queryset = related_queryset.only(*related_ret["only"])
                        related_queryset = related_queryset.prefetch_related(
                            *related_ret["prefetch_related"]
                        )
                        related_queryset = related_queryset.order_by(*order_by_list)

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
                    queryset = maybe_queryset(get_objects_func(queryset, info))
            elif callable(django_object_type.get_objects):
                queryset = maybe_queryset(
                    django_object_type.get_objects(queryset, info)
                )
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
    field_name_for_prefetch = None
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

    if queryset is None:
        queryset = maybe_queryset(default_manager)

    if queryset is None:
        raise ValueError(
            "The queryset is None. Ensure that the resolver or default manager returns a valid queryset."
        )

    is_prefetched = isinstance(queryset, list) or (
        hasattr(queryset, "_result_cache") and queryset._result_cache is not None
    )

    if not is_prefetched and not is_nested_paginated_field:
        queryset_factory = _queryset_factory_analyze(
            info,
            selection_set=info.field_nodes[0].selection_set,
            is_connection=True,
            model=model,
            registry=registry,
        )
        if queryset_factory["select_related"]:
            queryset = queryset.select_related(*queryset_factory["select_related"])
        if queryset_factory["only"]:
            queryset = queryset.only(*queryset_factory["only"])
        if queryset_factory["prefetch_related"]:
            queryset = queryset.prefetch_related(*queryset_factory["prefetch_related"])

    if "where" in args and not is_prefetched:
        obj_q = where_input_to_Q(args.get("where", {}))
        queryset = queryset.filter(obj_q)

    if not isinstance(queryset, list):
        order_by_list = get_order_by_list_from_arguments(args)
        if "order_by" in args or "orderBy" in args:
            queryset = queryset.order_by(*order_by_list)
        elif not is_prefetched:
            queryset = queryset.order_by(*order_by_list)

    pagination_config = args.get("pagination_config", {}) or args.get(
        "paginationConfig", {}
    )
    if not is_prefetched and not isinstance(queryset, list):
        queryset = queryset.distinct()

    if isinstance(queryset, QuerySet):
        if hasattr(django_object_type, "get_objects"):
            if isinstance(django_object_type.get_objects, list):
                for get_objects_func in django_object_type.get_objects:
                    queryset = maybe_queryset(get_objects_func(queryset, info))
            elif callable(django_object_type.get_objects):
                queryset = maybe_queryset(
                    django_object_type.get_objects(queryset, info)
                )
            else:
                raise ValueError(
                    "The get_objects method is not a list of functions or a callable."
                )
        else:
            raise ValueError("The get_objects method is not defined.")
    return paginate_queryset(
        queryset,
        paginated_object_type,  # type: ignore
        pagination_config.get("items_per_page", "All"),
        pagination_config.get("page", 1),
    )
