from enum import Enum

from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from django.db.models import (
    Field as DjangoField,
    FileField,
    ImageField,
    QuerySet,
)
from django.forms import ModelForm as DjangoModelForm
from django.utils.datastructures import MultiValueDict

import graphene
from graphene_django_cruddals.converters.django_types import (
    ErrorCollectionType,
    ErrorType,
)
from graphene_django_cruddals.converters.for_fields.converter_input import (
    GenericForeignKeyInput,
)
from graphene_django_cruddals.operations_fields.utils import (
    add_mutate_errors,
    create_relation_model_objects,
    maybe_queryset,
    order_by_input_to_args,
    paginate_queryset,
    toggle_active_status,
    update_dict_with_model_instance,
    where_input_to_Q,
)


def obj_to_modify_have_generic_foreign_key_input(obj_to_modify):
    for value in obj_to_modify.values():
        if isinstance(value, GenericForeignKeyInput):
            return True
    return False


def get_data_for_generic_foreign_key(obj_to_modify, model, responses):
    data = {}
    for key, value in obj_to_modify.items():
        if isinstance(value, GenericForeignKeyInput):
            field_foreign_key = model._meta.get_field(key)
            ct_field = field_foreign_key.ct_field
            fk_field = field_foreign_key.fk_field
            if key in responses:
                for response in responses[key].values():
                    if response:
                        if response["objects"]:
                            obj_contenttype = ContentType.objects.get_or_create(
                                app_label=value.app_label, model=value.model
                            )[0]
                            data[fk_field] = response["objects"][0].pk
                            data[ct_field] = obj_contenttype.pk
    return data


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
                    if issubclass(type(value), (graphene.Enum, Enum)):
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
                    e = ErrorCollectionType.from_errors(i, errors)
                    arr_errors.append(e)
                    transaction.set_rollback(True)

        if len(arr_obj) == 0:
            arr_obj = None
        if len(arr_errors) == 0:
            arr_errors = None

        return {"objects": arr_obj, "errors_report": arr_errors}


def default_read_field_resolver(
    django_object_type, default_manager, root, info, **args
):
    if "where" in args.keys():
        queryset: QuerySet = maybe_queryset(default_manager)
        where = args["where"]
        obj_q = where_input_to_Q(where)
        queryset = queryset.filter(obj_q)
        queryset = queryset.distinct()
    if isinstance(queryset, QuerySet):
        queryset = maybe_queryset(django_object_type.get_queryset(queryset, info))
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


def default_delete_field_resolver(model, root, info, **args):
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


def default_list_field_resolver(
    django_object_type, resolver, default_manager, root, info, **args
):
    queryset = None
    if resolver is not None and hasattr(resolver, "args"):
        queryset = maybe_queryset(
            resolver(root, info, **args)
        )  # Por lo general este resolver es el resolver por defecto, en este caso es el dict_or_attr_resolver, y va usar el atr_resolver, y va a traer el attr 'objects' del obj, y este 'objects' es un queryset
    if queryset is None:
        queryset = maybe_queryset(default_manager)

    # TODO: Se comentan estas lineas ya que se esta presentando un problema en el search
    # el field objects del search es un DjangoFieldList, entonces después de entrar en el default resolver del search
    # el field objects entra aca y por ende vuelve y llama el
    # get_queryset, entonces como ya va slice, no puede modificarlo (y no debería para eso esta el get_queryset, antes de ser paginado)

    #! if isinstance(queryset, QuerySet):
    #!     queryset = maybe_queryset(django_object_type.get_queryset(queryset, info))
    return queryset


def default_search_field_resolver(
    paginated_object_type,
    django_object_type,
    resolver,
    default_manager,
    root,
    info,
    **args,
):
    queryset = None
    if resolver is not None and hasattr(resolver, "args"):
        maybe_manager = resolver(root, info, **args)
        attname, default_value = resolver.args
        if attname.startswith("paginated_"):
            posible_field = attname.replace("paginated_", "", 1)
            if hasattr(root, posible_field):
                maybe_manager = getattr(root, posible_field, default_value)

        queryset: QuerySet = maybe_queryset(maybe_manager)

    if queryset is None:
        queryset = maybe_queryset(default_manager)

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

    paginated = args.get("paginated", {})
    queryset = queryset.distinct()

    if isinstance(queryset, QuerySet):
        queryset = maybe_queryset(django_object_type.get_queryset(queryset, info))
    return paginate_queryset(
        queryset,
        paginated_object_type,
        paginated.get("items_per_page", "All"),
        paginated.get("page", 1),
    )
