from itertools import chain
from typing import Any, List, Literal, Type, Union

from django.contrib.contenttypes.fields import (
    GenericForeignKey,
    GenericRel,
    GenericRelation,
)
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import (
    AutoField,
    BigAutoField,
    Field as DjangoField,
    ForeignKey,
    ManyToManyField,
    ManyToManyRel,
    ManyToOneRel,
    Model as DjangoModel,
    OneToOneField,
    OneToOneRel,
    Q,
    SmallAutoField,
)
from django.db.models.functions import Lower
from django.db.models.query import QuerySet as DjangoQuerySet
from django.forms.models import model_to_dict
from graphene_cruddals import (
    GRAPHENE_TYPE,
    RegistryGlobal,
    TypeRegistryForField,
    TypeRegistryForFieldEnum,
    TypesMutation,
    TypesMutationEnum,
)

import graphene
from graphene.utils.str_converters import to_camel_case, to_snake_case
from graphene_django_cruddals.converters.converter_filter_input import (
    convert_django_field_to_filter_input,
)
from graphene_django_cruddals.converters.converter_input import (
    GenericForeignKeyInput,
    convert_django_field_to_input,
)
from graphene_django_cruddals.converters.converter_order_by_input import (
    convert_django_field_to_order_by_input,
)
from graphene_django_cruddals.converters.converter_output import (
    convert_django_field_to_output,
)
from graphene_django_cruddals.converters.utils import (
    convert_choice_field_to_graphene_enum,
)


def get_field_name(field: DjangoField, for_queryset: bool) -> str:
    """Dado los siguientes modelos:
    class Author(models.Model):
        name = models.CharField(max_length=100)

    class Book(models.Model):
        title = models.CharField(max_length=100)
        author = models.ForeignKey(Author, on_delete=models.CASCADE)

    ========================================================================================================
    Usar solo related_name
        class Book(models.Model):
            title = models.CharField(max_length=100)
            author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
        Puedes acceder a los libros de un autor usando author.books.all().
        Las consultas inversas usarán books por defecto: Author.objects.filter(books__title='Some Title').
    ========================================================================================================
    Usar solo related_query_name
        class Book(models.Model):
            title = models.CharField(max_length=100)
            author = models.ForeignKey(Author, related_query_name='book', on_delete=models.CASCADE)
        No cambia el nombre del atributo inverso (será el nombre por defecto book_set).
        Las consultas inversas usarán book para filtros: Author.objects.filter(book__title='Some Title').
    ========================================================================================================
    Usar ambos related_name y related_query_name
        class Book(models.Model):
            title = models.CharField(max_length=100)
            author = models.ForeignKey(Author, related_name='books', related_query_name='book', on_delete=models.CASCADE)
        related_name='books' te permite acceder a los libros de un autor usando author.books.all().
        related_query_name='book' te permite usar filtros como Author.objects.filter(book__title='Some Title').
    ========================================================================================================
    No usar ninguno
        class Book(models.Model):
            title = models.CharField(max_length=100)
            author = models.ForeignKey(Author, on_delete=models.CASCADE)
        Django usará el nombre por defecto para el atributo inverso (book_set): author.book_set.all().
        Las consultas inversas usarán el nombre por defecto book_set: Author.objects.filter(book_set__title='Some Title').
    ========================================================================================================
    """
    if (
        for_queryset
        and isinstance(field, (OneToOneRel, ManyToManyRel, ManyToOneRel))
        and field.related_query_name is not None
    ):
        return field.related_query_name

    if (
        not for_queryset
        and isinstance(field, (ManyToManyRel, ManyToOneRel))
        and field.related_name is not None
    ):
        return field.related_name

    if not for_queryset and isinstance(field, (ManyToManyRel, ManyToOneRel)):
        accessor_name = field.get_accessor_name()
        if accessor_name is not None:
            return accessor_name
    return field.name


def get_model_fields_for_input(
    model: DjangoModel,
    type_mutation: TypesMutation = TypesMutationEnum.CREATE_UPDATE.value,
):
    fields_for_mutation: List[DjangoField]
    sortable_private_fields = [
        f for f in model._meta.private_fields if isinstance(f, DjangoField)
    ]
    fields_for_mutation = list(
        chain(
            model._meta.concrete_fields,
            sortable_private_fields,
            model._meta.many_to_many,
        )
    )
    fields_for_mutation = [
        field
        for field in fields_for_mutation
        if getattr(field, "editable", True)
        and not isinstance(field, (AutoField, BigAutoField, SmallAutoField))
    ]
    local_fields_for_mutation = [
        (get_field_name(field, False), field) for field in fields_for_mutation
    ]
    final_fields = {}
    if (
        type_mutation == TypesMutationEnum.CREATE_UPDATE.value
        or type_mutation == TypesMutationEnum.UPDATE.value
    ):
        field_pk: DjangoField = model._meta.pk  # type: ignore
        final_fields[field_pk.name] = field_pk
    for name, field in local_fields_for_mutation:
        if not str(name).endswith("+"):
            final_fields[name] = field
    return final_fields


def get_model_fields_for_output(model: DjangoModel, for_object_type: bool = False):
    fields_for_query: List[DjangoField] = (
        list(model._meta.fields)
        + list(model._meta.many_to_many)
        + list(model._meta.private_fields)
        + list(model._meta.fields_map.values())
    )
    local_fields_for_query = [
        (get_field_name(field, True), field) for field in fields_for_query
    ]
    final_fields = {}
    for name, field in local_fields_for_query:
        if not str(name).endswith("+"):
            if (
                isinstance(
                    field,
                    (ManyToManyField, ManyToManyRel, ManyToOneRel, GenericRelation),
                )
                and not isinstance(field, OneToOneRel)
                and for_object_type
            ):
                final_fields[f"paginated_{name}"] = field
            else:
                final_fields[name] = field
    return final_fields


def nested_get(input_dict, nested_key):
    internal_dict_value = input_dict
    for k in nested_key:
        internal_dict_value = internal_dict_value.get(k, None)
        if internal_dict_value is None:
            return None
    return internal_dict_value


def get_paths(d):
    """Breadth-First Search"""
    queue = [(d, [])]
    while queue:
        actual_node, p = queue.pop(0)
        yield p
        if isinstance(actual_node, dict):
            for k, v in actual_node.items():
                queue.append((v, p + [k]))


def get_args(where):
    args = {}
    for path in get_paths(where):
        arg_value = nested_get(where, path)
        if not isinstance(arg_value, dict):
            arg_key = "__".join(path)
            if arg_key.endswith("__equals"):
                arg_key = arg_key[0:-8] + "__exact"
            args[arg_key] = arg_value
    return args


def where_input_to_Q(where):
    AND = Q()
    OR = Q(_connector=Q.OR)
    NOT = Q()

    if "OR" in where.keys():
        for w in where.pop("OR"):
            OR = OR | Q(where_input_to_Q(w))

    if "AND" in where.keys():
        for w in where.pop("AND"):
            AND = AND & Q(where_input_to_Q(w), _connector=Q.OR)

    if "NOT" in where.keys():
        NOT = NOT & ~Q(where_input_to_Q(where.pop("NOT")))

    f = (Q(**get_args(where)) | OR) & AND & NOT
    return f


def order_by_input_to_args(order_by):
    args = []
    for rule in order_by:
        for path in get_paths(rule):
            v = nested_get(rule, path)
            if not isinstance(v, dict):
                if v == "ASC":
                    args.append("__".join(path))
                elif v == "DESC":
                    args.append("-" + "__".join(path))
                elif v == "IASC":
                    args.append(Lower("__".join(path)).asc())
                elif v == "IDESC":
                    args.append(Lower("__".join(path)).desc())
    return args


def exists_conversion_for_field(
    field: DjangoField, registry: RegistryGlobal, type_of_registry: TypeRegistryForField
) -> bool:
    registries_for_field = registry.get_registry_for_field(field)
    if registries_for_field is not None and type_of_registry in registries_for_field:
        return True
    return False


def get_converted_field(
    field, registry: RegistryGlobal, type_of_registry: TypeRegistryForField
):
    registries_for_field = registry.get_registry_for_field(field)
    if registries_for_field is not None and type_of_registry in registries_for_field:
        return registries_for_field[type_of_registry]


def convert_django_field_with_choices_to_output(
    name: str, field: DjangoField, model: DjangoModel, registry: RegistryGlobal
) -> GRAPHENE_TYPE:
    converted = get_converted_field(
        field, registry, TypeRegistryForFieldEnum.OUTPUT.value
    )
    if converted:
        return converted
    if getattr(field, "choices", None):
        converted = convert_choice_field_to_graphene_enum(field, None, None)
    else:
        converted = convert_django_field_to_output(name, field, model, registry)
    return converted  # type: ignore


def convert_django_field_with_choices_to_create_update_input(
    name: str,
    field: DjangoField,
    model: DjangoModel,
    registry: RegistryGlobal,
    type_mutation: TypesMutation = TypesMutationEnum.CREATE_UPDATE.value,
) -> GRAPHENE_TYPE:
    if type_mutation == TypesMutationEnum.UPDATE.value:
        type_of_registry = TypeRegistryForFieldEnum.INPUT_FOR_UPDATE.value
    elif type_mutation == TypesMutationEnum.CREATE.value:
        type_of_registry = TypeRegistryForFieldEnum.INPUT_FOR_CREATE.value
    else:
        type_of_registry = TypeRegistryForFieldEnum.INPUT_FOR_CREATE_UPDATE.value

    converted = get_converted_field(field, registry, type_of_registry)
    if converted:
        return converted

    if getattr(field, "choices", None):
        converted = converted = convert_choice_field_to_graphene_enum(
            field, None, type_mutation
        )
    else:
        converted = convert_django_field_to_input(
            name, field, model, registry, type_mutation
        )
    return converted  # type: ignore


def convert_django_field_without_choices_to_filter_input(
    name: str, field: DjangoField, model: DjangoModel, registry: RegistryGlobal
) -> GRAPHENE_TYPE:
    converted = get_converted_field(
        field, registry, TypeRegistryForFieldEnum.INPUT_FOR_SEARCH.value
    )
    if converted:
        return converted
    converted = convert_django_field_to_filter_input(name, field, model, registry)
    return converted  # type: ignore


def convert_django_field_without_choices_to_order_by_input(
    name: str, field: DjangoField, model: DjangoModel, registry: RegistryGlobal
) -> GRAPHENE_TYPE:
    converted = get_converted_field(
        field, registry, TypeRegistryForFieldEnum.INPUT_FOR_ORDER_BY.value
    )
    if converted:
        return converted
    converted = convert_django_field_to_order_by_input(name, field, model, registry)
    return converted  # type: ignore


def update_dict_with_model_instance(
    obj_to_update: Union[dict, object],
    instance: Union[Type[DjangoModel], None] = None,
    model: Union[Type[DjangoModel], None] = None,
) -> Union[dict, object]:
    """
    Updates a dictionary or an object's attributes with the values from a Django model instance, based on the provided ID.

    Args:
        obj_to_update (Union[dict, object]): Dictionary or object containing an 'id' key/attribute to match the model instance.
        instance (Type[models.Model], optional): Django model class. If not provided, the 'model' parameter must be used.
        model (Type[models.Model], optional): Django model instance. If not provided, the 'instance' parameter must be used.

    Returns:
        Union[dict, object]: Updated dictionary or object with the model instance's values.
    """
    obj_id = None

    if isinstance(obj_to_update, dict):
        obj_id = obj_to_update.get("id", None)
    elif hasattr(obj_to_update, "id"):
        obj_id = getattr(obj_to_update, "id", None)

    if obj_id is not None:
        if instance is not None:
            obj = instance._meta.model.objects.get(pk=obj_id)
        elif model is not None:
            obj = model.objects.get(pk=obj_id)
        else:
            raise ValueError(
                "Either 'instance' or 'model' parameters must be provided to update the dictionary with the model instance."
            )
        obj_original = model_to_dict(obj)
        for name_field, value_field in obj_original.items():
            if isinstance(obj_to_update, dict):
                if name_field not in obj_to_update:
                    obj_to_update.update({name_field: value_field})
            else:
                if not hasattr(obj_to_update, name_field):
                    setattr(obj_to_update, name_field, value_field)
    return obj_to_update


def toggle_active_status(
    option: Union[Literal["ACTIVATE", "DEACTIVATE"], Literal["activate", "deactivate"]],
    data: DjangoQuerySet,
    field: str = "is_active",
) -> DjangoQuerySet:
    """
    Activates or deactivates the state of the model instances based on the provided option.

    Args:
        option (str): Action to perform, 'ACTIVATE' or 'DEACTIVATE'.
        data (QuerySet): Data set to modify.
        ids (list): List of IDs to modify.
        field (str, optional): Field to update. By default, it is 'is_active'.

    Returns:
        QuerySet: Updated data.
    """
    if option.upper() == "ACTIVATE":
        data.update(**{field: True})
    elif option.upper() == "DEACTIVATE":
        data.update(**{field: False})
    return data


def paginate_queryset(
    qs: DjangoQuerySet,
    paginated_type: Type[graphene.ObjectType],
    items_per_page: Union[int, Literal["All"]] = "All",
    page: int = 1,
    **kwargs,
) -> graphene.ObjectType:
    """
    Paginate a queryset based on the specified parameters.

    Args:
        qs (QuerySet): The queryset to paginate.
        paginated_type (Type[graphene.ObjectType]): The pagination type to return. By default, it is None.
        items_per_page (Union[int, Literal['All']], optional): The number of items per page. By default, it is 'All'.
        page (int, optional): The current page number. By default, it is 1.
        **kwargs: Additional keyword arguments for the paginated_type.

    Returns:
        Type: An instance of paginated_type with pagination information and objects.
    """

    if items_per_page == "All":
        items_per_page = qs.count()

    try:
        page = int(page)
        items_per_page = int(items_per_page)
    except Exception:
        page = 1
        items_per_page = 1

    if page == 0:
        page = 1
    if items_per_page == 0:
        items_per_page = 1

    p = Paginator(qs, items_per_page)

    try:
        page_obj = p.page(page)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    return paginated_type(
        total=p.count,
        page=page_obj.number,
        pages=p.num_pages,
        has_next=page_obj.has_next(),
        has_prev=page_obj.has_previous(),
        index_start=page_obj.start_index(),
        index_end=page_obj.end_index(),
        objects=page_obj.object_list,
        **kwargs,
    )


def add_mutate_errors(responses, object_counter, internal_arr_errors, transaction=None):
    for name_related_field, obj in responses.items():
        for response in obj.values():
            if response:
                if response["errors_report"]:
                    for related_error in response["errors_report"]:
                        related_error.object_position = object_counter
                        for internal_related_error in related_error.errors:
                            internal_related_error.field = f"{to_camel_case(name_related_field)}.{internal_related_error.field}"
                    internal_arr_errors.extend(response["errors_report"])
                    if transaction is not None:
                        transaction.set_rollback(True)


def is_list_of_same_type(list_elements: List[Any], target_class: Type[Any]) -> bool:
    return all(isinstance(element, target_class) for element in list_elements)


def value_is_input_object_type(value: Any) -> bool:
    if isinstance(value, list):
        return is_list_of_same_type(value, graphene.InputObjectType)
    else:
        return isinstance(value, graphene.InputObjectType)


def get_field_values_from_instances(instance_list, field_name):
    field_values = []
    for instance in instance_list:
        if hasattr(instance, field_name):
            field_values.append(getattr(instance, field_name))
        else:
            raise ValueError(
                f"The field '{field_name}' does not exist in the model {type(instance).__name__}"
            )
    return field_values


def get_list_input_object_type(value_of_field_to_convert, model: DjangoModel):
    is_generic_foreign_key = isinstance(
        value_of_field_to_convert, GenericForeignKeyInput
    )
    if is_generic_foreign_key:
        value_of_field_to_convert = {
            to_snake_case(key): value
            for key, value in value_of_field_to_convert.object.items()
        }

    list_values = []
    list_values_to_modify = []
    list_values_to_connect = []
    list_values = (
        [value_of_field_to_convert]
        if not isinstance(value_of_field_to_convert, list)
        else value_of_field_to_convert
    )
    pk_field_name = model._meta.pk.name

    if (
        is_list_of_same_type(list_values, graphene.InputObjectType)
        or is_generic_foreign_key
    ):
        list_values_to_modify = [
            value for value in list_values if pk_field_name not in value
        ]
        list_values_to_connect = [
            value for value in list_values if pk_field_name in value
        ]

    return list_values_to_modify, list_values_to_connect


def get_resolvers_for_field(model, registry):
    registries_for_model = registry.get_registry_for_model(model)
    if registries_for_model:
        cruddals_for_related_model = registries_for_model.get("cruddals", None)
        if cruddals_for_related_model:
            create_field_resolver = (
                cruddals_for_related_model.meta.create_field.resolver
            )
            update_field_resolver = (
                cruddals_for_related_model.meta.update_field.resolver
            )
            return create_field_resolver, update_field_resolver


def create_direct_relation_model_objects(
    obj_to_relate,
    list_objects_to_relate,
    name_field_relate,
    field_relation,
    direct_field_detail,
    mutate,
    root,
    info,
):
    response_direct_objs = mutate(root, info, **{"input": list_objects_to_relate})
    if response_direct_objs["objects"]:
        reverse_pks = get_field_values_from_instances(
            response_direct_objs["objects"], "pk"
        )
        if isinstance(field_relation, (ForeignKey, OneToOneField)):
            obj_to_relate[name_field_relate] = reverse_pks[0]
        elif isinstance(field_relation, (ManyToManyField)):
            actual_reverse_pks_of_direct_obj = []
            if direct_field_detail["pk_field_name"] in obj_to_relate:
                direct_pk_value = obj_to_relate[direct_field_detail["pk_field_name"]]
                direct_actual_obj = direct_field_detail["model"].objects.get(
                    pk=direct_pk_value
                )
                query_set_actual_objs_related: DjangoQuerySet = getattr(
                    direct_actual_obj, direct_field_detail["name_field"]
                ).all()
                actual_reverse_pks_of_direct_obj = list(
                    query_set_actual_objs_related.values_list("pk", flat=True)
                )
            if isinstance(obj_to_relate.get(name_field_relate), list):
                obj_to_relate[name_field_relate] += (
                    reverse_pks + actual_reverse_pks_of_direct_obj
                )
            else:
                obj_to_relate[name_field_relate] = (
                    reverse_pks + actual_reverse_pks_of_direct_obj
                )
    return response_direct_objs


def create_reverse_relation_model_objects(
    related_obj,
    list_objects_to_relate,
    name_field_relate,
    field_relation,
    direct_field_detail,
    mutate,
    root,
    info,
):
    pk_obj_to_relate = related_obj.pk
    for obj_to_relate in list_objects_to_relate:
        if isinstance(field_relation, (ManyToOneRel, OneToOneRel)):
            obj_to_relate[name_field_relate] = pk_obj_to_relate

        elif isinstance(field_relation, (ManyToManyRel)):
            actual_pks_of_obj_to_relate = []
            if getattr(obj_to_relate, direct_field_detail["pk_field_name"], None):
                reverse_pk_value = getattr(
                    obj_to_relate, direct_field_detail["pk_field_name"]
                )
                reverse_actual_obj = direct_field_detail["model"].objects.get(
                    pk=reverse_pk_value
                )
                query_set_reverse_actual_objs: DjangoQuerySet = getattr(
                    reverse_actual_obj, direct_field_detail["name_field"]
                ).all()
                actual_pks_of_obj_to_relate = list(
                    query_set_reverse_actual_objs.values_list("pk", flat=True)
                )

            obj_to_relate[name_field_relate] = [
                pk_obj_to_relate
            ] + actual_pks_of_obj_to_relate

        elif isinstance(field_relation, (GenericRelation)):
            model_inverse = field_relation.model
            name_model_inverse = model_inverse._meta.model_name
            name_app_inverse = model_inverse._meta.app_label
            content_type = ContentType.objects.get(
                app_label=name_app_inverse, model=name_model_inverse
            )

            ct_field = field_relation.content_type_field_name
            fk_field = field_relation.object_id_field_name

            obj_to_relate[ct_field] = content_type.pk
            obj_to_relate[fk_field] = pk_obj_to_relate

    return mutate(related_obj, info, **{"input": list_objects_to_relate})


def apply_relation_mutations(
    type_field_relation,
    original_field,
    direct_field_detail,
    list_input_objects,
    mutate,
    direct_obj_to_modify,
    obj_modified,
    root,
    info,
):
    response = None
    if list_input_objects:
        if mutate:
            if type_field_relation == "field_direct":
                response = create_direct_relation_model_objects(
                    direct_obj_to_modify,
                    list_input_objects,
                    direct_field_detail["name_field"],
                    original_field,
                    direct_field_detail,
                    mutate,
                    root,
                    info,
                )
            elif type_field_relation == "field_inverse":
                if obj_modified:
                    response = create_reverse_relation_model_objects(
                        obj_modified,
                        list_input_objects,
                        direct_field_detail["name_field"],
                        original_field,
                        direct_field_detail,
                        mutate,
                        root,
                        info,
                    )
    return response


def handle_disconnect_objs_related(
    direct_field_detail, model, value_of_field, obj_to_modify
):
    list_values_to_disconnect = []
    if "disconnect" in value_of_field:
        for value_to_disconnect in value_of_field["disconnect"]:
            obj_q = where_input_to_Q(value_to_disconnect)
            final_data = model.objects.filter(obj_q)
            final_data = list(final_data.distinct())
            list_values_to_disconnect = list_values_to_disconnect + final_data

    if list_values_to_disconnect:
        if isinstance(direct_field_detail["field"], (ManyToManyField, ManyToManyRel)):
            direct_pk_value = obj_to_modify[direct_field_detail["pk_field_name"]]
            direct_actual_obj = direct_field_detail["model"].objects.get(
                pk=direct_pk_value
            )
            getattr(direct_actual_obj, direct_field_detail["name_field"]).remove(
                *list_values_to_disconnect
            )

        elif isinstance(direct_field_detail["field"], (ManyToOneRel)):
            direct_pk_value = obj_to_modify[direct_field_detail["pk_field_name"]]
            direct_actual_obj = direct_field_detail["model"].objects.get(
                pk=direct_pk_value
            )
            for obj_to_disconnect in list_values_to_disconnect:
                if direct_field_detail["field"].field.null:
                    obj_to_disconnect.__setattr__(
                        direct_field_detail["field"].field.attname, None
                    )
                    obj_to_disconnect.save()
                elif direct_field_detail["field"].field.blank:
                    obj_to_disconnect.__setattr__(
                        direct_field_detail["field"].field.attname, ""
                    )
                    obj_to_disconnect.save()
                else:
                    # raise Exception("No se puede desconectar el objeto relacionado")
                    obj_to_disconnect.delete()

        elif isinstance(direct_field_detail["field"], (ForeignKey)):
            for obj_to_disconnect in list_values_to_disconnect:
                obj_to_disconnect.__setattr__(direct_field_detail["name_field"], None)
                obj_to_disconnect.save()

        elif isinstance(direct_field_detail["field"], (GenericRel)):
            direct_pk_value = obj_to_modify[direct_field_detail["pk_field_name"]]
            direct_actual_obj = direct_field_detail["field"].related_model.objects.get(
                pk=direct_pk_value
            )
            name_field_generic_relation = direct_field_detail["field"].field.name
            getattr(direct_actual_obj, name_field_generic_relation).remove(
                *list_values_to_disconnect
            )

        elif isinstance(direct_field_detail["field"], (GenericRelation)):
            direct_pk_value = obj_to_modify[direct_field_detail["pk_field_name"]]
            direct_actual_obj = direct_field_detail["model"].objects.get(
                pk=direct_pk_value
            )
            name_field_generic_relation = direct_field_detail["name_field"]
            getattr(direct_actual_obj, name_field_generic_relation).remove(
                *list_values_to_disconnect
            )


def get_relation_field_details(
    type_field_relation, django_relation_field, value_of_field
):
    direct_model = None
    direct_field = None
    direct_name_field = None
    direct_pk_field_name = None
    reverse_model = None
    reverse_field = None
    reverse_name_field = None
    reverse_pk_field_name = None
    if type_field_relation == "field_direct":
        direct_model = django_relation_field.model  # Model of field
        direct_field = (
            django_relation_field  # ManyToManyField, ForeignKey, OneToOneField
        )
        direct_name_field = django_relation_field.name  # name of field what is direct
        direct_pk_field_name = direct_model._meta.pk.name  # pk

        if isinstance(django_relation_field, GenericForeignKey):
            generic_type = ContentType.objects.get(
                app_label=value_of_field.app_label, model=value_of_field.model
            )
            reverse_model = generic_type.model_class()
            reverse_field = None
            reverse_name_field = None
            reverse_pk_field_name = None
        else:
            reverse_model = django_relation_field.related_model  # QuestionDetail
            reverse_field = (
                django_relation_field.remote_field
            )  # ManyToManyRel, ManyToOneRel, OneToOneRel
            reverse_name_field = (
                django_relation_field.related_query_name()
                if hasattr(django_relation_field, "related_query_name")
                else None
            )
            reverse_pk_field_name = (
                reverse_model._meta.pk.name if reverse_model else None
            )

    elif type_field_relation == "field_inverse":
        direct_model = django_relation_field.related_model  # QuestionDetail
        direct_field = (
            django_relation_field.remote_field
        )  # ManyToManyField, ForeignKey, OneToOneField
        direct_name_field = direct_field.name  # questions,     question,    question
        direct_pk_field_name = direct_model._meta.pk.name  # pk

        reverse_model = django_relation_field.model  # Question
        reverse_field = (
            django_relation_field  # ManyToManyRel, ManyToOneRel, OneToOneRel )
        )
        reverse_name_field = (
            django_relation_field.name
        )  # question_details, question_details, question_detail
        reverse_pk_field_name = reverse_model._meta.pk.name  # pk

    return {
        "direct": {
            "model": direct_model,
            "field": direct_field,
            "name_field": direct_name_field,
            "pk_field_name": direct_pk_field_name,
        },
        "reverse": {
            "model": reverse_model,
            "field": reverse_field,
            "name_field": reverse_name_field,
            "pk_field_name": reverse_pk_field_name,
        },
    }


def create_relation_model_objects(
    type_field_relation,
    model: DjangoModel,
    registry: RegistryGlobal,
    obj_to_modify,
    obj_modified,
    root,
    info,
):
    all_model_fields = get_model_fields_for_output(model)
    valid_relations = (
        (ManyToManyField, ForeignKey, OneToOneField, GenericForeignKey)
        if type_field_relation == "field_direct"
        else (ManyToManyRel, ManyToOneRel, OneToOneRel, GenericRelation)
    )
    fields_to_remove = []
    responses = {}
    for name_field, value_of_field in obj_to_modify.items():
        django_field = all_model_fields.get(name_field, None)
        if (
            django_field
            and django_field.is_relation
            and isinstance(django_field, valid_relations)
            and value_is_input_object_type(value_of_field)
        ):
            relation_field_details = get_relation_field_details(
                type_field_relation, django_field, value_of_field
            )
            model_of_django_field = (
                relation_field_details["reverse"]["model"]
                if type_field_relation == "field_direct"
                else relation_field_details["direct"]["model"]
            )
            mutate_for_create, mutate_for_update = get_resolvers_for_field(
                model_of_django_field, registry
            ) or (None, None)
            registries_for_model_of_django_field = registry.get_registry_for_model(
                model_of_django_field
            )
            if (
                "input_object_type_for_connect_disconnect"
                in registries_for_model_of_django_field
            ):
                input_object_type_for_connect_disconnect = (
                    registries_for_model_of_django_field[
                        "input_object_type_for_connect_disconnect"
                    ]
                )
                if (
                    isinstance(value_of_field, input_object_type_for_connect_disconnect)
                    or value_of_field.__class__.__name__
                    == input_object_type_for_connect_disconnect.__name__
                ):
                    field_details = (
                        relation_field_details["direct"]
                        if type_field_relation == "field_direct"
                        else relation_field_details["reverse"]
                    )
                    handle_disconnect_objs_related(
                        field_details,
                        model_of_django_field,
                        value_of_field,
                        obj_to_modify,
                    )
                    if "connect" in value_of_field and value_of_field["connect"]:
                        value_of_field = value_of_field["connect"]
                    else:
                        fields_to_remove.append(
                            relation_field_details["direct"]["name_field"]
                        )
                        continue
            if "input_object_type_for_connect" in registries_for_model_of_django_field:
                input_object_type_for_connect = registries_for_model_of_django_field[
                    "input_object_type_for_connect"
                ]
                if (
                    isinstance(value_of_field, input_object_type_for_connect)
                    or value_of_field.__class__.__name__
                    == input_object_type_for_connect.__name__
                ):
                    if "connect" in value_of_field and value_of_field["connect"]:
                        value_of_field = value_of_field["connect"]
            (
                list_input_objects_to_create,
                list_input_objects_to_connect,
            ) = get_list_input_object_type(value_of_field, model_of_django_field)
            response_create = apply_relation_mutations(
                type_field_relation,
                django_field,
                relation_field_details["direct"],
                list_input_objects_to_create,
                mutate_for_create,
                obj_to_modify,
                obj_modified,
                root,
                info,
            )
            response_update = apply_relation_mutations(
                type_field_relation,
                django_field,
                relation_field_details["direct"],
                list_input_objects_to_connect,
                mutate_for_update,
                obj_to_modify,
                obj_modified,
                root,
                info,
            )
            responses[name_field] = {
                "create": response_create,
                "update": response_update,
            }
    for field_to_remove in fields_to_remove:
        if field_to_remove in obj_to_modify:
            del obj_to_modify[field_to_remove]

    return responses


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
                    if response and response["objects"]:
                        obj_contenttype = ContentType.objects.get_or_create(
                            app_label=value.app_label, model=value.model
                        )[0]
                        data[fk_field] = response["objects"][0].pk
                        data[ct_field] = obj_contenttype.pk
    return data
