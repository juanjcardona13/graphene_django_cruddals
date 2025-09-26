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
    BooleanValueNode,
    EnumValueNode,
    FloatValueNode,
    FragmentSpreadNode as FragmentSpread,
    InlineFragmentNode as InlineFragment,
    IntValueNode,
    ListValueNode,
    ObjectValueNode,
    StringValueNode,
    VariableNode,
)

import graphene
from graphene import Dynamic, List
from graphene.types.scalars import MAX_INT, MIN_INT
from graphene.utils.str_converters import to_camel_case
from graphene_django_cruddals.converters.utils import maybe_queryset
from graphene_django_cruddals.utils.main import (
    add_mutate_errors,
    create_relation_model_objects,
    get_data_for_generic_foreign_key,
    get_model_fields_for_output,
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


def parse_ast(ast, variable_values=None):
    if variable_values is None:
        variable_values = {}
    if isinstance(ast, VariableNode):
        var_name = ast.name.value
        value = variable_values.get(var_name)
        return value
    elif isinstance(ast, (StringValueNode, BooleanValueNode)):
        return ast.value
    elif isinstance(ast, IntValueNode):
        num = int(ast.value)
        if MIN_INT <= num <= MAX_INT:
            return num
    elif isinstance(ast, FloatValueNode):
        return float(ast.value)
    elif isinstance(ast, EnumValueNode):
        return ast.value
    elif isinstance(ast, ListValueNode):
        ret = []
        for ast_value in ast.values:
            value = parse_ast(ast_value, variable_values=variable_values)
            if value is not None:
                ret.append(value)
        return ret
    elif isinstance(ast, ObjectValueNode):
        ret = {}
        for field in ast.fields:
            value = parse_ast(field.value, variable_values=variable_values)
            if value is not None:
                ret[field.name.value] = value
        return ret
    else:
        return None


def parse_arguments_ast(arguments, variable_values=None):
    if variable_values is None:
        variable_values = {}
    ret = {}
    for argument in arguments:
        value = parse_ast(argument.value, variable_values=variable_values)
        if value is not None:
            ret[argument.name.value] = value
    return ret


def _queryset_factory(
    model, info, field_ast=None, is_connection=True, registry=None, **kwargs
):
    queryset = model.objects.all()
    arguments = parse_arguments_ast(
        field_ast.arguments, variable_values=info.variable_values
    )
    queryset_factory = _queryset_factory_analyze(
        info,
        field_ast.selection_set,
        is_connection=is_connection,
        model=model,
        registry=registry,
    )
    print("========")
    print("queryset_factory", queryset_factory)
    print("========")
    queryset = queryset.select_related(*queryset_factory["select_related"])
    queryset = queryset.only(*queryset_factory["only"])
    queryset = queryset.prefetch_related(*queryset_factory["prefetch_related"])

    if "where" in arguments.keys():
        where = arguments["where"]
        obj_q = where_input_to_Q(where)
        queryset = queryset.filter(obj_q)

    if "order_by" in arguments.keys() or "orderBy" in arguments.keys():
        order_by = arguments.get("order_by") or arguments.get("orderBy")
        if isinstance(order_by, dict):
            order_by = [order_by]
        list_for_order = order_by_input_to_args(order_by)
        queryset = queryset.order_by(*list_for_order)
    else:
        queryset = queryset.order_by("pk")

    queryset = queryset.distinct()
    return queryset


def get_type_field(gql_type, gql_name):
    fields = gql_type._meta.fields
    for name, field in fields.items():
        if to_camel_case(gql_name) == to_camel_case(name):
            if isinstance(field, Dynamic):
                field = field.get_type()
            else:
                field = field
            if isinstance(field, List):
                field_type = field.of_type
            else:
                field_type = field.type
            if isinstance(field_type, List):
                field_type = field_type.of_type
            return name, field_type


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
            # TODO: Entender este caso
            # if field.type_condition.name.value == cls.__name__:
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
            except KeyError as e:
                print(f"KeyError: {real_name}")
                print(e)
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
                        qs = _queryset_factory(
                            related_model,
                            info,
                            field_ast=field,
                            is_connection=True,
                            registry=registry,
                        )
                        ret["prefetch_related"].append(
                            Prefetch(
                                new_suffix + real_name,
                                queryset=qs,
                            )
                        )
                elif isinstance(model_field, FileField):
                    ret["only"].append(new_suffix + real_name)
            else:
                ret["only"].append(new_suffix + real_name)
    return ret


def default_search_field_resolver(
    model: DjangoModel,
    registry: RegistryGlobal,
    resolver,
    default_manager,
    root,
    info,
    **args,
):
    print("default_search_field_resolver")
    print("model", model)
    print("registry", registry)
    print("resolver", resolver)
    print("default_manager", default_manager)
    print("root", root)
    print("info", info)
    print("args", args)
    print("========")

    registries_for_model = registry.get_registry_for_model(model)
    django_object_type: ModelObjectType = registries_for_model["object_type"]
    paginated_object_type: ModelPaginatedObjectType = registries_for_model[
        "paginated_object_type"
    ]

    queryset = maybe_queryset(default_manager)

    if queryset is None:
        raise ValueError(
            "The queryset is None. Ensure that the resolver or default manager returns a valid queryset."
        )

    queryset_factory = _queryset_factory_analyze(
        info,
        selection_set=info.field_nodes[0].selection_set,
        is_connection=True,  # supongo que es por el paginado, como alla es un batch,
        model=model,
        registry=registry,
    )
    print("========")
    print("queryset_factory", queryset_factory)
    print("========")

    queryset = queryset.select_related(*queryset_factory["select_related"])
    queryset = queryset.only(*queryset_factory["only"])
    queryset = queryset.prefetch_related(*queryset_factory["prefetch_related"])

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

    if isinstance(queryset, QuerySet):
        if hasattr(django_object_type, "get_objects"):
            if isinstance(django_object_type.get_objects, list):
                for get_objects_func in django_object_type.get_objects:
                    queryset = maybe_queryset(get_objects_func(queryset, info))
            elif callable(django_object_type.get_objects):
                queryset = maybe_queryset(
                    django_object_type.get_objects(queryset, info)
                )

    queryset = queryset.distinct()

    pagination_config = args.get("pagination_config", {}) or args.get(
        "paginationConfig", {}
    )
    return paginate_queryset(
        queryset,
        paginated_object_type,  # type: ignore
        pagination_config.get("items_per_page", "All"),
        pagination_config.get("page", 1),
    )
