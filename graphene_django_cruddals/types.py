from enum import Enum
from typing import Any, Dict, Literal, Optional, Protocol, Tuple, Type, TypedDict, Union
import graphene
from django.db.models.query import QuerySet as DjangoQuerySet


GRAPHENE_TYPE = Union[
    graphene.Scalar,
    graphene.String,
    graphene.ID,
    graphene.Int,
    graphene.Float,
    graphene.Boolean,
    graphene.Date,
    graphene.DateTime,
    graphene.Time,
    graphene.Decimal,
    graphene.JSONString,
    graphene.UUID,
    graphene.List,
    graphene.NonNull,
    graphene.Enum,
    graphene.Argument,
    graphene.Dynamic
]

class MetaTypeStructure(Protocol):
    only_fields: Union[Tuple[str, ...], Literal["__all__"]]
    exclude_fields: Tuple[str]


class ObjectTypeStructure(Protocol):
    Meta: MetaTypeStructure

    # TODO: Missing the resolvers for the fields

    def __getattr__(self, item: str) -> GRAPHENE_TYPE:
        ...

    def __setattr__(self, key: str, value: GRAPHENE_TYPE) -> None:
        ...

    def __delattr__(self, item: str) -> None:
        ...

    @classmethod
    def get_queryset(cls, queryset:DjangoQuerySet, info) -> DjangoQuerySet:
        ...


class InputObjectTypeStructure(Protocol):
    Meta: MetaTypeStructure

    # exist_field_type_relation = CruddalsRelationField() => For relations

    def __getattr__(self, item: str) -> GRAPHENE_TYPE:
        ...

    def __setattr__(self, key: str, value: GRAPHENE_TYPE) -> None:
        ...

    def __delattr__(self, item: str) -> None:
        ...


class CreateInputObjectTypeStructure(Protocol):
    Meta: MetaTypeStructure

    # exist_field_type_relation = CruddalsRelationField() => For relations

    def __getattr__(self, item: str) -> GRAPHENE_TYPE:
        ...

    def __setattr__(self, key: str, value: GRAPHENE_TYPE) -> None:
        ...

    def __delattr__(self, item: str) -> None:
        ...


class UpdateInputObjectTypeStructure(Protocol):
    Meta: MetaTypeStructure

    # exist_field_type_relation = CruddalsRelationField() => For relations

    def __getattr__(self, item: str) -> GRAPHENE_TYPE:
        ...

    def __setattr__(self, key: str, value: GRAPHENE_TYPE) -> None:
        ...

    def __delattr__(self, item: str) -> None:
        ...


class FilterInputObjectTypeStructure(Protocol):
    Meta: MetaTypeStructure

    def __getattr__(self, item: str) -> GRAPHENE_TYPE:
        ...

    def __setattr__(self, key: str, value: GRAPHENE_TYPE) -> None:
        ...

    def __delattr__(self, item: str) -> None:
        ...


class OrderByInputObjectTypeStructure(Protocol):
    Meta: MetaTypeStructure

    def __getattr__(self, item: str) -> GRAPHENE_TYPE:
        ...

    def __setattr__(self, key: str, value: GRAPHENE_TYPE) -> None:
        ...

    def __delattr__(self, item: str) -> None:
        ...


class ModifyArgument(TypedDict):
    name: str
    required: bool
    description: str
    hidden: bool


class CreateFieldStructure(Protocol):
    class Meta:
        modify_input_argument: ModifyArgument
        extra_arguments: Dict[str, GRAPHENE_TYPE]
    
    def pre_mutate(self, info, *args, **kwargs) -> Tuple:
        ...

    def mutate(self, info, *args, **kwargs) -> Any:
        ...

    def override_total_mutate(self, info, *args, **kwargs) -> Any:
        ...

    def post_mutate(self, info, response, *args, **kwargs) -> Any:
        ...


class ReadFieldStructure(Protocol):
    class Meta:
        modify_where_argument: ModifyArgument
        extra_arguments: Dict[str, GRAPHENE_TYPE]

    def pre_resolve(self, info, *args, **kwargs) -> Tuple:
        ...

    def resolve(self, info, *args, **kwargs) -> Any:
        ...

    def override_total_resolve(self, info, *args, **kwargs) -> Any:
        ...

    def post_resolve(self, info, response, *args, **kwargs) -> Any:
        ...


class UpdateFieldStructure(Protocol):
    class Meta:
        modify_input_argument: ModifyArgument
        extra_arguments: Dict[str, GRAPHENE_TYPE]

    def pre_mutate(self, info, *args, **kwargs) -> Tuple:
        ...

    def mutate(self, info, *args, **kwargs) -> Any:
        ...

    def override_total_mutate(self, info, *args, **kwargs) -> Any:
        ...

    def post_mutate(self, info, response, *args, **kwargs) -> Any:
        ...


class DeleteFieldStructure(Protocol):
    class Meta:
        modify_where_argument: ModifyArgument
        extra_arguments: Dict[str, GRAPHENE_TYPE]

    def pre_mutate(self, info, *args, **kwargs) -> Tuple:
        ...

    def mutate(self, info, *args, **kwargs) -> Any:
        ...

    def override_total_mutate(self, info, *args, **kwargs) -> Any:
        ...

    def post_mutate(self, info, response, *args, **kwargs) -> Any:
        ...


class DeactivateFieldStructure(Protocol):
    class Meta:
        modify_where_argument: ModifyArgument
        extra_arguments: Dict[str, GRAPHENE_TYPE]

    def pre_mutate(self, info, *args, **kwargs) -> Tuple:
        ...

    def mutate(self, info, *args, **kwargs) -> Any:
        ...

    def override_total_mutate(self, info, *args, **kwargs) -> Any:
        ...

    def post_mutate(self, info, response, *args, **kwargs) -> Any:
        ...


class ActivateFieldStructure(Protocol):
    class Meta:
        modify_where_argument: ModifyArgument
        extra_arguments: Dict[str, GRAPHENE_TYPE]

    def pre_mutate(self, info, *args, **kwargs) -> Tuple:
        ...

    def mutate(self, info, *args, **kwargs) -> Any:
        ...

    def override_total_mutate(self, info, *args, **kwargs) -> Any:
        ...

    def post_mutate(self, info, response, *args, **kwargs) -> Any:
        ...


class ListFieldStructure(Protocol):
    class Meta:
        modify_order_by_argument: ModifyArgument
        modify_pagination_config_argument: ModifyArgument
        extra_arguments: Dict[str, GRAPHENE_TYPE]

    def pre_resolve(self, info, *args, **kwargs) -> Tuple:
        ...

    def resolve(self, info, *args, **kwargs) -> Any:
        ...

    def override_total_resolve(self, info, *args, **kwargs) -> Any:
        ...

    def post_resolve(self, info, response, *args, **kwargs) -> Any:
        ...


class SearchFieldStructure(Protocol):
    class Meta:
        modify_where_argument: ModifyArgument
        modify_order_by_argument: ModifyArgument
        modify_pagination_config_argument: ModifyArgument
        extra_arguments: Dict[str, GRAPHENE_TYPE]

    def pre_resolve(self, info, *args, **kwargs) -> Tuple:
        ...

    def resolve(self, info, *args, **kwargs) -> Any:
        ...

    def override_total_resolve(self, info, *args, **kwargs) -> Any:
        ...

    def post_resolve(self, info, response, *args, **kwargs) -> Any:
        ...


class InterfaceStructure(Protocol):
    ObjectType: ObjectTypeStructure
    InputObjectType: InputObjectTypeStructure
    CreateInputObjectType: CreateInputObjectTypeStructure
    UpdateInputObjectType: UpdateInputObjectTypeStructure
    FilterInputObjectType: FilterInputObjectTypeStructure
    OrderByInputObjectType: OrderByInputObjectTypeStructure
    CreateField: CreateFieldStructure
    ReadField: ReadFieldStructure
    UpdateField: UpdateFieldStructure
    DeleteField: DeleteFieldStructure
    DeactivateField: DeactivateFieldStructure
    ActivateField: ActivateFieldStructure
    ListField: ListFieldStructure
    SearchField: SearchFieldStructure


FunctionType = Literal['create', 'read', 'update', 'delete', 'deactivate', 'activate', 'list', 'search']

CamelFunctionType = Literal['Create', 'Read', 'Update', 'Delete', 'Deactivate', 'Activate', 'List', 'Search']

TypesMutation = Literal['create_update', 'create', 'update']

TypeRegistryForModel = Literal['object_type', 'paginated_object_type', 'input_object_type', 'input_object_type_for_create', 'input_object_type_for_update', 'input_object_type_for_search', 'input_object_type_for_order_by', 'input_object_type_for_connect', 'input_object_type_for_connect_disconnect', 'cruddals']

TypeRegistryForField = Literal['output', 'input_for_create_update', 'input_for_create', 'input_for_update', 'input_for_search', 'input_for_order_by']

class NameCaseType(TypedDict):
    snake_case: str
    plural_snake_case: str
    camel_case: str
    plural_camel_case: str
    pascal_case: str
    plural_pascal_case: str

class RootFieldsType(TypedDict):
    query: Type[graphene.ObjectType]
    mutation: Optional[Type[graphene.ObjectType]]
    # subscription: Optional[Type[graphene.ObjectType]]

class TypesMutationEnum(Enum):
    CREATE = "create"
    UPDATE = "update"
    CREATE_UPDATE = "create_update"