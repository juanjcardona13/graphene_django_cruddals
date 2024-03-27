# # -*- coding: utf-8 -*-
from collections import OrderedDict
from enum import Enum
from typing import Any, Callable, Dict, Literal, NamedTuple, Optional, Tuple, Type, Union
import graphene
from graphene.utils.str_converters import to_snake_case
from graphene.utils.props import props
from graphene.utils.subclass_with_meta import SubclassWithMeta
from graphene.types.generic import GenericScalar

from django.apps import apps as django_apps
from django.db.models import Model as DjangoModel
from django.forms import ModelForm as DjangoModelForm


from graphene_django_cruddals.converters.django_types import DjangoObjectType
from graphene_django_cruddals.converters.for_entity.main import (
    convert_django_model_to_object_type,
    convert_django_model_to_paginated_object_type,
    convert_django_model_to_mutate_input_object_type,
    convert_django_model_to_filter_input_object_type,
    convert_django_model_to_order_by_input_object_type,
)
from graphene_django_cruddals.operations_fields.main import (
    DjangoCreateUpdateField,
    DjangoReadField,
    DjangoDeleteField,
    DjangoDeactivateField,
    DjangoActivateField,
    DjangoListField,
    DjangoSearchField,
)
from graphene_django_cruddals.operations_fields.default_resolvers import (
    default_create_update_resolver,
    default_read_field_resolver,
    default_delete_field_resolver,
    default_deactivate_field_resolver,
    default_activate_field_resolver,
    default_list_field_resolver,
    default_search_field_resolver,
    default_update_resolver,
)
from graphene_django_cruddals.registry_global import RegistryGlobal, TypeRegistryForModelEnum, get_global_registry
from graphene_django_cruddals.types import CamelFunctionType, FunctionType, InterfaceStructure, ListFieldStructure, NameCaseType, RootFieldsType
from graphene_django_cruddals.utils import (
    build_class,
    convert_model_to_model_form,
    delete_keys,
    get_name_of_model_in_different_case,
    merge_dict,
)


# For interfaces,
# is executed first AppInterface, after Model Interface, for both is executed in order of list
INTERFACE_META_CLASS_TYPE_NAMES = [
    "MetaObjectType",
    "MetaInputObjectType",
    "MetaCreateInputObjectType",
    "MetaUpdateInputObjectType",
    "MetaFilterInputObjectType",
    "MetaOrderByInputObjectType",
]
CLASS_INTERFACE_TYPE_NAMES = [
    "ObjectType",
    "InputObjectType",
    "CreateInputObjectType",
    "UpdateInputObjectType",
    "FilterInputObjectType",
    "OrderByInputObjectType",
]
CLASS_INTERFACE_FIELDS_NAMES = [
    "CreateField",
    "ReadField",
    "UpdateField",
    "DeleteField",
    "DeactivateField",
    "ActivateField",
    "ListField",
    "SearchField",
]
INTERFACES_NAME_CRUDDALS = CLASS_INTERFACE_FIELDS_NAMES + CLASS_INTERFACE_TYPE_NAMES

def validate_list_func_cruddals(functions:Tuple[FunctionType, ...], exclude_functions:Tuple[FunctionType, ...]) -> bool:
    valid_values = [
        "create",
        "read",
        "update",
        "delete",
        "deactivate",
        "activate",
        "list",
        "search",
    ]

    if functions and exclude_functions:
        raise ValueError(
            "You cannot provide both 'functions' and 'exclude_functions'. Please provide only one."
        )
    else:
        if functions:
            name_input = "functions"
            input_list = functions
        elif exclude_functions:
            name_input = "exclude_functions"
            input_list = exclude_functions
        else:
            return True

    if not isinstance(input_list, tuple) or len(input_list) == 0:
        raise ValueError(f"'{name_input}' must be a non-empty tuple.")

    invalid_values = [value for value in input_list if value not in valid_values]

    if invalid_values:
        raise ValueError(
            f"Expected in '{name_input}' a tuple with some of these values {valid_values}, but got these invalid values {invalid_values}"
        )

    return True

#from graphene_django_cruddals.operations_fields.main import DjangoReadField, DjangoCreateUpdateField, DjangoDeleteField, DjangoDeactivateField, DjangoActivateField, DjangoListField, DjangoSearchField
def get_schema_query_mutation(
        queries:Tuple[Type[graphene.ObjectType], ...]=(), 
        attrs_for_query:Dict[str, graphene.Field]={}, 
        mutations:Tuple[Type[graphene.ObjectType], ...]=(), 
        attrs_for_mutation:Union[Dict[str, graphene.Field], None]={}
    ) -> Tuple[graphene.Schema, Type[graphene.ObjectType], Union[Type[graphene.ObjectType], None]]:
    base = (graphene.ObjectType,)
    Query:Type[graphene.ObjectType] = build_class(name="Query", bases=(queries+base), attrs=attrs_for_query)
    
    dict_for_schema: RootFieldsType = {'query': Query, 'mutation': None}

    Mutation:Union[Type[graphene.ObjectType], None] = None
    if mutations or attrs_for_mutation:
        attrs_for_mutation = {} if attrs_for_mutation is None else attrs_for_mutation
        Mutation = build_class(name="Mutation", bases=(mutations+base), attrs=attrs_for_mutation)
        dict_for_schema.update({"mutation": Mutation})

    schema = graphene.Schema(**dict_for_schema)

    return schema, Query, Mutation


class CruddalsInterfaceNames(Enum):
    """
    An enumeration class that defines the names of the interfaces for CRUDDALS operations
    and object types in the Cruddals system.

    Attributes:
    - CREATE_FIELD: The name of the interface for creating a field.
    - READ_FIELD: The name of the interface for reading a field.
    - UPDATE_FIELD: The name of the interface for updating a field.
    - DELETE_FIELD: The name of the interface for deleting a field.
    - DEACTIVATE_FIELD: The name of the interface for deactivating a field.
    - ACTIVATE_FIELD: The name of the interface for activating a field.
    - LIST_FIELD: The name of the interface for listing fields.
    - SEARCH_FIELD: The name of the interface for searching fields.
    - OBJECT_TYPE: The name of the interface for object types.
    - INPUT_OBJECT_TYPE: The name of the interface for input object types.
    - CREATE_INPUT_OBJECT_TYPE: The name of the interface for creating input object types.
    - UPDATE_INPUT_OBJECT_TYPE: The name of the interface for updating input object types.
    - FILTER_INPUT_OBJECT_TYPE: The name of the interface for filtering input object types.
    - ORDER_BY_INPUT_OBJECT_TYPE: The name of the interface for ordering by input object types.
    """

    CREATE_FIELD = "CreateField"
    READ_FIELD = "ReadField"
    UPDATE_FIELD = "UpdateField"
    DELETE_FIELD = "DeleteField"
    DEACTIVATE_FIELD = "DeactivateField"
    ACTIVATE_FIELD = "ActivateField"
    LIST_FIELD = "ListField"
    SEARCH_FIELD = "SearchField"

    OBJECT_TYPE = "ObjectType"
    INPUT_OBJECT_TYPE = "InputObjectType"
    CREATE_INPUT_OBJECT_TYPE = "CreateInputObjectType"
    UPDATE_INPUT_OBJECT_TYPE = "UpdateInputObjectType"
    FILTER_INPUT_OBJECT_TYPE = "FilterInputObjectType"
    ORDER_BY_INPUT_OBJECT_TYPE = "OrderByInputObjectType"


class _MetaCruddalsInterfaceNames(Enum):
    META_OBJECT_TYPE = "MetaObjectType"
    META_INPUT_OBJECT_TYPE = "MetaInputObjectType"
    META_CREATE_INPUT_OBJECT_TYPE = "MetaCreateInputObjectType"
    META_UPDATE_INPUT_OBJECT_TYPE = "MetaUpdateInputObjectType"
    META_FILTER_INPUT_OBJECT_TYPE = "MetaFilterInputObjectType"
    META_ORDER_BY_INPUT_OBJECT_TYPE = "MetaOrderByInputObjectType"


class BuilderBase:
    """
    A base class providing common methods for building resolvers and managing interfaces.

    Attributes:
        model_as_object_type: The GraphQL object type for the model.
        model_as_paginated_object_type: The GraphQL paginated object type for the model.
        model_as_input_object_type: The GraphQL input object type for the model.
        model_as_create_input_object_type: The GraphQL input object type for create operations.
        model_as_update_input_object_type: The GraphQL input object type for update operations.
        model_as_filter_input_object_type: The GraphQL input object type for filtering operations.
        model_as_order_by_input_object_type: The GraphQL input object type for ordering operations.
        
        read_field: The read field (or also called operation) for the model.
        list_field: The list field (or also called operation) for the model.
        search_field: The search field (or also called operation) for the model.
        create_field: The create field (or also called operation) for the model.
        update_field: The update field (or also called operation) for the model.
        activate_field: The activate field (or also called operation) for the model.
        deactivate_field: The deactivate field (or also called operation) for the model.
        delete_field: The delete field (or also called operation) for the model.

    Methods:
        wrap_resolver_with_pre_post_resolvers: Wrap resolver with pre and post resolvers.
        get_resolve_for_operation_field: Get the resolver for an operation field.
        get_interface_attrs: Get attributes for an interface.
        get_interface_meta_attrs: Get meta attributes for an interface.
        validate_attrs: Validate attributes for a function.
        get_function_lists: Get lists of functions.
        get_last_element: Get the last element from a list or a default value.
        get_extra_arguments: Get extra arguments.
        save_pre_post_how_list: Save pre and post functions as lists.
        get_pre_and_post_resolves: Get pre and post resolves.

    """
    model_as_object_type:Type[DjangoObjectType]
    model_as_paginated_object_type:Type[graphene.ObjectType]
    model_as_input_object_type:Type[graphene.InputObjectType]
    model_as_create_input_object_type:Type[graphene.InputObjectType]
    model_as_update_input_object_type:Type[graphene.InputObjectType]
    model_as_filter_input_object_type:Type[graphene.InputObjectType]
    model_as_order_by_input_object_type:Type[graphene.InputObjectType]

    read_field:DjangoReadField
    list_field:Union[DjangoListField,None] = None
    search_field:Union[DjangoSearchField,None] = None
    create_field:Union[DjangoCreateUpdateField,None] = None
    update_field:Union[DjangoCreateUpdateField,None] = None
    activate_field:Union[DjangoActivateField,None] = None
    deactivate_field:Union[DjangoDeactivateField,None] = None
    delete_field:Union[DjangoDeleteField,None] = None

    @staticmethod #TODO: Change to a class method
    def get_where_arg(model_as_filter_input_object_type, kw={}, default_required=False):
        attrs_for_input_arg = kw.get("modify_where_argument", {})
        default_values_for_where = {
            "type_": model_as_filter_input_object_type,
            "name": "where",
            "required": default_required,
            "description": "",
        }
        for key in default_values_for_where.keys():
            if key in attrs_for_input_arg:
                default_values_for_where[key] = attrs_for_input_arg[key]
        if default_values_for_where.get("hidden", False):
            return {}
        else:
            return {"where": graphene.Argument(**default_values_for_where)}

    @staticmethod #TODO: Change to a class method
    def add_cruddals_model_to_request(info, cruddals_model):
        try:
            if info.context is None:
                class Context:
                    pass
                setattr(info, "context", Context())
            setattr(info.context, "CruddalsModel", cruddals_model)
        except Exception as e:
            raise e


    def wrap_resolver_with_pre_post_resolvers( self, kwargs, name_function, default_resolver ):
        pre_resolves, post_resolves = self.get_pre_and_post_resolves(
            kwargs, name_function
        )
        default_resolver = self.get_last_element(
            name_function, kwargs, default_resolver
        )

        def default_final_resolver_with_pre_and_post(root, info, **kwargs):
            self.add_cruddals_model_to_request(info, self)
            for pre_resolve in pre_resolves:
                root, info, kwargs = pre_resolve(root, info, **kwargs)
            response = default_resolver(root, info, **kwargs)
            for post_resolve in post_resolves:
                response = post_resolve(root, info, response, **kwargs)
            return response

        return self.get_last_element(
            f"override_total_{name_function}",
            kwargs,
            default_final_resolver_with_pre_and_post,
        )

    def get_resolve_for_operation_field( self, kwargs, name_function: str, default_resolver ):
        return self.wrap_resolver_with_pre_post_resolvers( kwargs, name_function, default_resolver )

    def get_interface_attrs(self, Interface, include_meta_attrs=True):
        if Interface is not None:
            attrs_internal_cls_meta = {}
            if getattr(Interface, "Meta", None) is not None and include_meta_attrs:
                attrs_internal_cls_meta = props(Interface.Meta)
            props_function = delete_keys(props(Interface), ["Meta"])
            return {**props_function, **attrs_internal_cls_meta}
        return {}

    def get_interface_meta_attrs(self, InterfaceType):
        if InterfaceType is not None:
            if getattr(InterfaceType, "Meta", None) is not None:
                p = props(InterfaceType.Meta)

                fields = p.get("fields", p.get("only_fields", p.get("only", [])))
                exclude = p.get(
                    "exclude", p.get("exclude_fields", p.get("exclude", []))
                )
                assert not (
                    fields and exclude
                ), f"Cannot set both 'fields' and 'exclude' options on Type {self.model_name_in_different_case['camel_case']}."
                return p
        return {}

    def validate_attrs(self, props, function_name, operation_name, class_name=None):
        class_name = class_name or self.model_name_in_different_case["camel_case"]
        function_name_without = function_name.replace("override_total_", "")
        model_pre = props.get(f"pre_{function_name_without}")
        model_function = props.get(f"{function_name_without}")
        model_override_function = props.get(f"{function_name}")
        model_post = props.get(f"post_{function_name_without}")

        assert not (
            model_pre and model_override_function
        ), f"Cannot set both 'pre_{function_name_without}' and '{function_name}' options on {operation_name} {class_name}."
        assert not (
            model_function and model_override_function
        ), f"Cannot set both '{function_name_without}' and '{function_name}' options on {operation_name} {class_name}."
        assert not (
            model_post and model_override_function
        ), f"Cannot set both 'post_{function_name_without}' and '{function_name}' options on {operation_name} {class_name}."

    def get_function_lists(self, key, kwargs, func_default):
        functions = kwargs.get(key, [func_default])
        if not callable(func_default):
            raise ValueError(
                f"func_default must be a function, but got {type(func_default)}"
            )
        if not isinstance(functions, list):
            functions = [functions]
        return functions

    def get_last_element(self, key, kwargs, default=None) -> Any:
        if key in kwargs:
            element = kwargs[key]
            if isinstance(element, list):
                return element[-1]
            return element
        return default

    def get_extra_arguments(self, kwargs):
        return kwargs.get("extra_arguments", {})

    def save_pre_post_how_list(self, kwargs):
        for attr, value in kwargs.items():
            if "pre" in attr or "post" in attr:
                if not isinstance(kwargs[attr], list):
                    kwargs[attr] = [value]

    def get_pre_and_post_resolves(self, kwargs, name_function: str):
        pre_default = lambda *args, **kwargs: (*args, kwargs)
        post_default = (
            lambda root, info, default_response=None, **kwargs: default_response
        )

        pre_resolves_model = self.get_function_lists(
            f"pre_{name_function}", kwargs, pre_default
        )
        post_resolves_model = self.get_function_lists(
            f"post_{name_function}", kwargs, post_default
        )
        return pre_resolves_model, post_resolves_model


class BuilderQuery(BuilderBase):
    """
    A class for building query operations.

    Inherits from:
        BuilderBase

    """
    pass


class BuilderMutation(BuilderBase):
    """
    A class for building mutation operations.

    Inherits from:
        BuilderBase

    Methods:
        get_state_controller_field: Get the state controller field.

    """
    def get_state_controller_field(self, kwargs) -> str:
        return self.get_last_element(
            "state_controller_field", kwargs, "is_active"
        )  # TODO- Debo de mirar esto donde lo voy a cuadrar para que sea global

    @staticmethod #TODO: Change to a class method
    def get_input_arg(model_as_input_object_type, kw={}):
        attrs_for_input_arg = kw.get("modify_input_argument", {})
        default_values_for_input = {
            "type_": graphene.List(graphene.NonNull(model_as_input_object_type)),
            "name": "input",
            "required": False,
            "description": "",
        }
        for key in default_values_for_input.keys():
            if key in attrs_for_input_arg:
                default_values_for_input[key] = attrs_for_input_arg[key]
        if default_values_for_input.get("hidden", False):
            return {}
        else:
            return {"input": graphene.Argument(**default_values_for_input)}


class BuilderCreate(BuilderMutation):
    """
    A class to build the field (or also called OPERATION) "Create" for the model.

    Inherits from:
        BuilderMutation

    """
    def validate_props_create_field(self, props, name=None):
        self.validate_attrs(props, "override_total_mutate", "Create", name)

    #TODO: I should change to class method
    def build_create(self, **kwargs) -> DjangoCreateUpdateField:
        extra_args = self.get_extra_arguments(kwargs)
        input_arg = self.get_input_arg(self.model_as_create_input_object_type, kwargs)

        name_function = "mutate"
        default_resolver = lambda root, info, **args: default_create_update_resolver(
            self.model, self.model_as_form, self.registry, root, info, **args
        )
        resolver = self.get_resolve_for_operation_field( kwargs, name_function, default_resolver )

        create_field = DjangoCreateUpdateField(
            _type=self.model_as_object_type,
            name_for_output_type=f"Create{self.model_name_in_different_case['plural_camel_case']}Payload",
            args={**input_arg, **extra_args},
            resolver=resolver,
            name=f"create{self.model_name_in_different_case['plural_camel_case']}",
        )
        return create_field


class BuilderRead(BuilderQuery):
    """
    A class to build the field (or also called OPERATION) "Read" for the model.

    Inherits from:
        BuilderQuery

    """
    def validate_props_read_field(self, props, name=None):
        self.validate_attrs(props, "override_total_resolve", "Read", name)

    #TODO: I should change to class method
    def build_read(self, **kwargs) -> DjangoReadField:
        extra_args = self.get_extra_arguments(kwargs)
        where_arg = self.get_where_arg(self.model_as_filter_input_object_type, kwargs, True)

        name_function = "resolve"
        default_resolver = lambda root, info, **args: default_read_field_resolver(
            self.model_as_object_type, self.model._default_manager, root, info, **args
        )
        resolver = self.get_resolve_for_operation_field( kwargs, name_function, default_resolver )

        read_field = DjangoReadField(
            _type=self.model_as_object_type,
            args={**where_arg, **extra_args},
            resolver=resolver,
            name=f"read{self.model_name_in_different_case['camel_case']}",
        )
        return read_field


class BuilderUpdate(BuilderMutation):
    """
    A class to build the field (or also called OPERATION) "Update" for the model.

    Inherits from:
        BuilderMutation

    """
    def validate_props_update_field(self, props, name=None):
        self.validate_attrs(props, "override_total_mutate", "Update", name)

    #TODO: I should change to class method
    def build_update(self, **kwargs) -> DjangoCreateUpdateField:
        extra_args = self.get_extra_arguments(kwargs)
        input_arg = self.get_input_arg(self.model_as_update_input_object_type, kwargs)

        name_function = "mutate"
        default_resolver = lambda root, info, **args: default_update_resolver(
            self.model, self.model_as_form, self.registry, root, info, **args
        )
        resolver = self.get_resolve_for_operation_field(
            kwargs, name_function, default_resolver
        )

        update_field = DjangoCreateUpdateField(
            _type=self.model_as_object_type,
            name_for_output_type=f"Update{self.model_name_in_different_case['plural_camel_case']}Payload",
            args={**input_arg, **extra_args},
            resolver=resolver,
            name=f"update{self.model_name_in_different_case['plural_camel_case']}",
        )
        return update_field


class BuilderDelete(BuilderMutation):
    """
    A class to build the field (or also called OPERATION) "Delete" for the model.

    Inherits from:
        BuilderMutation

    """
    def validate_props_delete_field(self, props, name=None):
        self.validate_attrs(props, "override_total_mutate", "Delete", name)

    #TODO: I should change to class method
    def build_delete(self, **kwargs) -> DjangoDeleteField:
        extra_args = self.get_extra_arguments(kwargs)
        where_arg = self.get_where_arg(self.model_as_filter_input_object_type, kwargs, True)

        name_function = "mutate"
        default_resolver = lambda root, info, **args: default_delete_field_resolver(
            self.model, root, info, **args
        )
        resolver = self.get_resolve_for_operation_field(
            kwargs, name_function, default_resolver
        )

        delete_field = DjangoDeleteField(
            _type=self.model_as_object_type,
            name_for_output_type=f"Delete{self.model_name_in_different_case['plural_camel_case']}Payload",
            args={**where_arg, **extra_args},
            resolver=resolver,
            name=f"delete{self.model_name_in_different_case['plural_camel_case']}",
        )
        return delete_field


class BuilderDeactivate(BuilderMutation):
    """
    A class to build the field (or also called OPERATION) "Deactivate" for the model.

    Inherits from:
        BuilderMutation

    """
    def validate_props_deactivate_field(self, props, name=None):
        self.validate_attrs(props, "override_total_mutate", "Deactivate", name)

    #TODO: I should change to class method
    def build_deactivate(self, **kwargs) -> DjangoDeactivateField:
        extra_args = self.get_extra_arguments(kwargs)
        where_arg = self.get_where_arg(self.model_as_filter_input_object_type, kwargs, True)

        name_function = "mutate"
        field_for_activate_deactivate: str = self.get_state_controller_field(kwargs)
        default_resolver = lambda root, info, **args: default_deactivate_field_resolver(
            self.model, field_for_activate_deactivate, root, info, **args
        )
        resolver = self.get_resolve_for_operation_field(
            kwargs, name_function, default_resolver
        )

        deactivate_field = DjangoDeactivateField(
            _type=self.model_as_object_type,
            name_for_output_type=f"Deactivate{self.model_name_in_different_case['plural_camel_case']}Payload",
            args={**where_arg, **extra_args},
            resolver=resolver,
            name=f"deactivate{self.model_name_in_different_case['plural_camel_case']}",
        )
        return deactivate_field


class BuilderActivate(BuilderMutation):
    """
    A class to build the field (or also called OPERATION) "Activate" for the model.

    Inherits from:
        BuilderMutation

    """
    def validate_props_activate_field(self, props, name=None):
        self.validate_attrs(props, "override_total_mutate", "Activate", name)

    #TODO: I should change to class method
    def build_activate(self, **kwargs) -> DjangoActivateField:
        extra_args = self.get_extra_arguments(kwargs)
        where_arg = self.get_where_arg(self.model_as_filter_input_object_type, kwargs, True)

        name_function = "mutate"
        field_for_activate_deactivate: str = self.get_state_controller_field(kwargs)
        default_resolver = lambda root, info, **args: default_activate_field_resolver(
            self.model, field_for_activate_deactivate, root, info, **args
        )
        resolver = self.get_resolve_for_operation_field(
            kwargs, name_function, default_resolver
        )

        activate_field = DjangoActivateField(
            _type=self.model_as_object_type,
            name_for_output_type=f"Activate{self.model_name_in_different_case['plural_camel_case']}Payload",
            args={**where_arg, **extra_args},
            resolver=resolver,
            name=f"activate{self.model_name_in_different_case['plural_camel_case']}",
        )
        return activate_field


class BuilderList(BuilderQuery):
    """
    A class to build the field (or also called OPERATION) "List" for the model.

    Inherits from:
        BuilderQuery

    """
    def validate_props_list_field(self, props, name=None):
        self.validate_attrs(props, "override_total_resolve", "List", name)

    #TODO: I should change to class method
    def build_list(self, **kwargs) -> DjangoListField:
        extra_args = self.get_extra_arguments(kwargs)

        name_function = "resolve"
        default_resolver = lambda root, info, **args: default_list_field_resolver(
            self.model_as_object_type,
            None,
            self.model._default_manager,
            root,
            info,
            **args,
        )
        resolver = self.get_resolve_for_operation_field(
            kwargs, name_function, default_resolver
        )

        list_field = DjangoListField(
            _type=self.model_as_object_type,
            args={**extra_args},
            resolver=resolver,
            name=f"list{self.model_name_in_different_case['plural_camel_case']}",
        )
        return list_field


class IntOrAll(GenericScalar):
    class Meta:
        description = "The page size can be int or 'All'"

class PaginationConfigInput(graphene.InputObjectType):
    page = graphene.InputField(type_=graphene.Int, default_value=1)
    items_per_page = graphene.InputField(type_=IntOrAll, default_value="All")


class BuilderSearch(BuilderQuery):
    """
    A class to build the field (or also called OPERATION) "Search" for the model.

    Inherits from:
        BuilderQuery

    """
    @staticmethod #TODO: Change to a class method
    def get_order_by_arg(model_as_order_by_input_object_type, kw={}):
        attrs_for_order_by_arg = kw.get("modify_order_by_argument", {})
        default_values_for_order_by = {
            "type_": model_as_order_by_input_object_type,
            "name": "orderBy",
            "required": False,
            "description": "",
        }
        for key in default_values_for_order_by.keys():
            if key in attrs_for_order_by_arg:
                default_values_for_order_by[key] = attrs_for_order_by_arg[key]
        if default_values_for_order_by.get("hidden", False):
            return {}
        else:
            return {"order_by": graphene.Argument(**default_values_for_order_by)}

    @staticmethod #TODO: Change to a class method
    def get_pagination_config_arg(kw={}):
        default_values_for_paginated = {
            "type_": PaginationConfigInput,
            "name": "paginated",
            "required": False,
            "description": "",
        }
        attrs_for_pagination_config_arg = kw.get("modify_pagination_config_argument", {})
        attrs_for_pagination_config_arg = default_values_for_paginated | attrs_for_pagination_config_arg
        if default_values_for_paginated.get("hidden", False):
            return {}
        else:
            return {"paginated": graphene.Argument(**default_values_for_paginated)}

    def validate_props_search_field(self, props, name=None):
        self.validate_attrs(props, "override_total_resolve", "Search", name)

    #TODO: I should change to class method
    def build_search(self, **kwargs) -> DjangoSearchField:
        extra_arg_for_search = self.get_extra_arguments(kwargs)
        where_arg = self.get_where_arg(self.model_as_filter_input_object_type, kwargs, False)
        order_by_arg = self.get_order_by_arg(
            self.model_as_order_by_input_object_type, kw=kwargs
        )
        pagination_config_arg = self.get_pagination_config_arg(kw=kwargs)

        name_function = "resolve"
        default_resolver = lambda root, info, **args: default_search_field_resolver(
            self.model_as_paginated_object_type,
            self.model_as_object_type,
            None,
            self.model._default_manager,
            root,
            info,
            **args,
        )
        resolver = self.get_resolve_for_operation_field(
            kwargs, name_function, default_resolver
        )

        search_field = DjangoSearchField(
            _type=self.model_as_paginated_object_type,
            args={**where_arg, **order_by_arg, **pagination_config_arg, **extra_arg_for_search},
            resolver=resolver,
            name=f"search{self.model_name_in_different_case['plural_camel_case']}",
        )
        return search_field


class BuilderCruddalsModel(
    BuilderCreate,
    BuilderRead,
    BuilderUpdate,
    BuilderDelete,
    BuilderDeactivate,
    BuilderActivate,
    BuilderList,
    BuilderSearch,
):
    """
    A class for building CRUDDALS operations for a Django model.
        C = "Create"
        R = "Read"
        U = "Update"
        D = "Delete"
        D = "Deactivate"
        A = "Activate"
        L = "List"
        S = "Search"

    Inherits from:
        BuilderCreate, BuilderRead, BuilderUpdate, BuilderDelete,
        BuilderDeactivate, BuilderActivate, BuilderList, BuilderSearch

    Attributes:
        model: The Django model for which operations are being built.
        prefix: Prefix for the model's schema.
        suffix: Suffix for the model's schema.
        model_name_in_different_case: Dictionary containing the model name in different cases.
        model_as_form: The Django model form.
        registry: The registry for schema registration.

    Methods:
        __init__: Initialize the BuilderCruddalsModel class.
        get_dict_of_interface_attr: Get a dictionary of interface attributes.

    """

    model:DjangoModel
    prefix:str = ""
    suffix:str = ""

    model_name_in_different_case:NameCaseType
    model_as_form:DjangoModelForm
    registry:RegistryGlobal

    def __init__(
        self,
        Model:DjangoModel,
        prefix:str="",
        suffix:str="",
        interfaces:Tuple[InterfaceStructure, ...]=tuple(),
        exclude_interfaces:Tuple[str, ...]=tuple(),
        registry:Union[RegistryGlobal,None]=None,
    ) -> None:
        assert Model, "Model is required for BuilderCruddalsModel"

        attrs_for_child = [ "model", "prefix", "suffix", "model_as_form", "model_name_in_different_case", "registry", "model_as_object_type", "model_as_paginated_object_type", "model_as_input_object_type", "model_as_filter_input_object_type", "model_as_order_by_input_object_type", "read_field", "list_field", "search_field", "create_field", "update_field", "activate_field", "deactivate_field", "delete_field", ]
        [setattr(self, attr, None) for attr in attrs_for_child]

        if not registry:
            self.registry = get_global_registry(f"{prefix}{suffix}")
        else:
            self.registry = registry

        self.model = Model
        self.prefix = prefix
        self.suffix = suffix
        self.model_name_in_different_case = get_name_of_model_in_different_case(
            Model, prefix, suffix
        )

        assert isinstance(
            interfaces, (tuple,)
        ), f"'interfaces' should be tuple received {type(interfaces)}"
        assert isinstance(
            exclude_interfaces, (tuple,)
        ), f"'exclude_interfaces' should be tuple received {type(exclude_interfaces)}"

        dict_of_interface_attr = self.get_dict_of_interface_attr( interfaces, exclude_interfaces )

        self.model_as_object_type = convert_django_model_to_object_type(
            model=self.model,
            registry=self.registry,
            meta_attrs=dict_of_interface_attr[
                _MetaCruddalsInterfaceNames.META_OBJECT_TYPE.value
            ],
            extra_attrs=dict_of_interface_attr[
                CruddalsInterfaceNames.OBJECT_TYPE.value
            ],
        )
        self.model_as_paginated_object_type = (
            convert_django_model_to_paginated_object_type(
                model=self.model,
                registry=self.registry,
                model_as_object_type=self.model_as_object_type,
                extra_attrs={},
            )
        )
        self.model_as_input_object_type = (
            convert_django_model_to_mutate_input_object_type(
                model=self.model,
                registry=self.registry,
                type_mutation="create_update",
                meta_attrs=dict_of_interface_attr[
                    _MetaCruddalsInterfaceNames.META_INPUT_OBJECT_TYPE.value
                ],
                extra_attrs=dict_of_interface_attr[
                    CruddalsInterfaceNames.INPUT_OBJECT_TYPE.value
                ],
            )
        )
        self.model_as_create_input_object_type = (
            convert_django_model_to_mutate_input_object_type(
                model=self.model,
                registry=self.registry,
                type_mutation="create",
                meta_attrs=dict_of_interface_attr[
                    _MetaCruddalsInterfaceNames.META_CREATE_INPUT_OBJECT_TYPE.value
                ],
                extra_attrs=dict_of_interface_attr[
                    CruddalsInterfaceNames.CREATE_INPUT_OBJECT_TYPE.value
                ],
            )
        )
        self.model_as_update_input_object_type = (
            convert_django_model_to_mutate_input_object_type(
                model=self.model,
                registry=self.registry,
                type_mutation="update",
                meta_attrs=dict_of_interface_attr[
                    _MetaCruddalsInterfaceNames.META_UPDATE_INPUT_OBJECT_TYPE.value
                ],
                extra_attrs=dict_of_interface_attr[
                    CruddalsInterfaceNames.UPDATE_INPUT_OBJECT_TYPE.value
                ],
            )
        )
        self.model_as_filter_input_object_type = (
            convert_django_model_to_filter_input_object_type(
                model=self.model,
                registry=self.registry,
                meta_attrs=dict_of_interface_attr[
                    _MetaCruddalsInterfaceNames.META_FILTER_INPUT_OBJECT_TYPE.value
                ],
                extra_attrs=dict_of_interface_attr[
                    CruddalsInterfaceNames.FILTER_INPUT_OBJECT_TYPE.value
                ],
            )
        )
        self.model_as_order_by_input_object_type = (
            convert_django_model_to_order_by_input_object_type(
                model=self.model,
                registry=self.registry,
                meta_attrs=dict_of_interface_attr[
                    _MetaCruddalsInterfaceNames.META_ORDER_BY_INPUT_OBJECT_TYPE.value
                ],
                extra_attrs=dict_of_interface_attr[
                    CruddalsInterfaceNames.ORDER_BY_INPUT_OBJECT_TYPE.value
                ],
            )
        )

        self.model_as_form = convert_model_to_model_form(
            model=self.model,
            prefix_for_name=prefix,
            suffix_for_name=suffix,
        )

        builders: Dict[CamelFunctionType, Callable[..., Any]] = {
            "Read": self.build_read,
            "Search": self.build_search,
            "List": self.build_list,
            "Create": self.build_create,
            "Update": self.build_update,
            "Activate": self.build_activate,
            "Deactivate": self.build_deactivate,
            "Delete": self.build_delete,
        }

        for prop_name, builder in builders.items():
            operation_field = builder(**dict_of_interface_attr[f"{prop_name}Field"])
            attr_name = f"{prop_name.lower()}_field"
            setattr(self, attr_name, operation_field)

    def get_dict_of_interface_attr(self, interfaces:Tuple[InterfaceStructure, ...], exclude_interfaces:Tuple[str, ...]) -> Dict[str, OrderedDict[str, Any]]:

        dict_of_interface_attr = {
            interface_name: OrderedDict() for interface_name in INTERFACES_NAME_CRUDDALS
        }
        dict_of_interface_attr.update(
            {
                meta_interface_name: OrderedDict()
                for meta_interface_name in INTERFACE_META_CLASS_TYPE_NAMES
            }
        )

        for interface in interfaces:
            if interface.__name__ in exclude_interfaces:
                continue
            for interface_field_name in CLASS_INTERFACE_FIELDS_NAMES:
                interface_attrs = {}
                current_interface = getattr(interface, interface_field_name, None)
                if current_interface is not None:
                    interface_attrs = self.get_interface_attrs(current_interface)
                    self.save_pre_post_how_list(interface_attrs)
                    validation_func = getattr(
                        self, f"validate_props_{to_snake_case(interface_field_name)}"
                    )
                    validation_func(interface_attrs, interface.__name__)
                dict_of_interface_attr[interface_field_name] = merge_dict(
                    destination=dict_of_interface_attr[interface_field_name],
                    source=interface_attrs,
                    keep_both=True,
                )
            for interface_type_name in CLASS_INTERFACE_TYPE_NAMES:
                interface_attrs = {}
                current_interface = getattr(interface, interface_type_name, None)
                if current_interface is not None:
                    interface_attrs = self.get_interface_attrs(current_interface, False)
                    interface_meta_attrs = self.get_interface_meta_attrs(
                        current_interface
                    )
                    dict_of_interface_attr[f"Meta{interface_type_name}"] = merge_dict(
                        destination=dict_of_interface_attr[
                            f"Meta{interface_type_name}"
                        ],
                        source=interface_meta_attrs,
                        keep_both=True,
                    )
                dict_of_interface_attr[interface_type_name] = merge_dict(
                    destination=dict_of_interface_attr[interface_type_name],
                    source=interface_attrs,
                    keep_both=True,
                )

        return dict_of_interface_attr


class CruddalsModel(SubclassWithMeta):
    """
    A base class for defining GraphQL schemas for Django models using Cruddals.

    This class provides methods to dynamically create GraphQL schemas for Django models,
    along with query and mutation operation fields.

    Attributes:
        Query (Type[graphene.ObjectType]): The GraphQL Query object for the model.
        Mutation (Union[Type[graphene.ObjectType], None]): The GraphQL Mutation object for the model.
        schema (graphene.Schema): The GraphQL schema for the model.
        query_operation_fields (Dict[str, Union[graphene.Field, DjangoReadField, DjangoListField, DjangoSearchField]]):
            The query operation fields for the model.
        mutation_operation_fields (Union[Dict[str, Union[graphene.Field, DjangoCreateUpdateField, DjangoDeleteField,
            DjangoDeactivateField, DjangoActivateField]], None]): The mutation operation fields for the model.
        meta (BuilderCruddalsModel): An instance of BuilderCruddalsModel containing metadata about the model.

    Methods:
        __init_subclass_with_meta__: Initialize the subclass with meta settings and dynamically create GraphQL schemas.
        _initialize_attributes: Initialize attributes to None.
        _build_cruddals_model: Build the CruddalsModel using BuilderCruddalsModel.
        _build_dict_for_operation_fields: Build dictionaries for query and mutation operation fields.
        _build_schema_query_mutation: Build the schema, Query, and Mutation objects.

    """

    Query:Type[graphene.ObjectType]
    Mutation:Union[Type[graphene.ObjectType], None] = None
    schema:graphene.Schema
    query_operation_fields:Dict[str, graphene.Field | DjangoReadField | DjangoListField | DjangoSearchField]
    mutation_operation_fields:Union[Dict[str, graphene.Field | DjangoCreateUpdateField | DjangoDeleteField | DjangoDeactivateField | DjangoActivateField ], None] = None
    meta:BuilderCruddalsModel

    @classmethod
    def __init_subclass_with_meta__(
        cls,
        model:Union[DjangoModel, None]=None,
        prefix:str="",
        suffix:str="",
        interfaces:Tuple[InterfaceStructure, ...]=tuple(),
        exclude_interfaces:Tuple[str, ...]=tuple(),
        functions:Tuple[FunctionType, ...]=tuple(),
        exclude_functions:Tuple[FunctionType, ...]=tuple(),
        registry:Union[RegistryGlobal,None]=None,
        **kwargs,
    ):
        """
        Initialize the subclass with meta settings and dynamically create GraphQL schemas.

        Args:
            model (Union[DjangoModel, None]): The Django model for which the schema is to be generated.
            prefix (str): Prefix for the model's schema.
            suffix (str): Suffix for the model's schema.
            interfaces (Tuple[InterfaceStructure, ...]): Additional GraphQL interfaces to include in the schema.
            exclude_interfaces (Tuple[str, ...]): Interfaces to exclude from the schema.
            functions (Tuple[FunctionType, ...]): Additional functions to include in the schema.
            exclude_functions (Tuple[FunctionType, ...]): Functions to exclude from the schema.
            registry (Union[RegistryGlobal, None]): The registry to use for schema registration.
            **kwargs: Additional keyword arguments.
        """
        
        assert model, "model is required for CruddalsModel"
        validate_list_func_cruddals(functions, exclude_functions)

        if not registry:
            registry = get_global_registry(f"{prefix}{suffix}")

        cls._initialize_attributes()
        cls._build_cruddals_model(model, prefix, suffix, interfaces, exclude_interfaces, registry)
        cls._build_dict_for_operation_fields(functions, exclude_functions)
        cls._build_schema_query_mutation()
        registry.register_model(model, TypeRegistryForModelEnum.CRUDDALS.value, cls)

        super(CruddalsModel, cls).__init_subclass_with_meta__(**kwargs)

    @classmethod
    def _initialize_attributes(cls):
        """
        Initialize attributes to None for the child class.
        """
        attrs_for_child = [ "Query", "Mutation", "schema", "query_operation_fields", "mutation_operation_fields", "meta", ]
        [setattr(cls, attr, None) for attr in attrs_for_child]

    @classmethod
    def _build_cruddals_model(cls, model, prefix, suffix, interfaces, exclude_interfaces, registry):
        """
        Build the CruddalsModel using BuilderCruddalsModel.

        Args:
            model (DjangoModel): The Django model for which the schema is to be generated.
            prefix (str): Prefix for the model's schema.
            suffix (str): Suffix for the model's schema.
            interfaces (Tuple[InterfaceStructure, ...]): Additional GraphQL interfaces to include in the schema.
            exclude_interfaces (Tuple[str, ...]): Interfaces to exclude from the schema.
            registry (Union[RegistryGlobal, None]): The registry to use for schema registration.
        """
        cruddals_of_model = BuilderCruddalsModel(
            Model=model,
            prefix=prefix,
            suffix=suffix,
            interfaces=interfaces,
            exclude_interfaces=exclude_interfaces,
            registry=registry,
        )
        cls.meta = cruddals_of_model

    @classmethod
    def _build_dict_for_operation_fields(cls, functions, exclude_functions):
        """
        Build dictionaries for query and mutation operation fields based on the given functions and exclude_functions..

        Args:
            functions (Tuple[FunctionType, ...]): Functions to include in the schema.
            exclude_functions (Tuple[FunctionType, ...]): Functions to exclude from the schema.
        """
        functions_type_query = ("read", "list", "search")
        functions_type_mutation = (
            "create",
            "update",
            "activate",
            "deactivate",
            "delete",
        )
        final_functions = ( functions if functions else tuple( set(functions_type_query + functions_type_mutation) - set(exclude_functions) ) )

        cls.query_operation_fields = {}
        cls.mutation_operation_fields = {}

        for function in final_functions:
            key = f"{function}_{cls.meta.model_name_in_different_case['plural_snake_case']}"
            if function == "read":
                key = f"{function}_{cls.meta.model_name_in_different_case['snake_case']}"
            attr_field:Dict[str, graphene.Field] = {key: getattr(cls.meta, f"{function}_field")}
            if function in functions_type_query:
                cls.query_operation_fields.update(attr_field)
            elif function in functions_type_mutation:
                cls.mutation_operation_fields.update(attr_field)

        if not cls.query_operation_fields:
            cls.query_operation_fields.update(
                {
                    f"read_{cls.meta.model_name_in_different_case['snake_case']}": getattr(
                        cls.meta, "read_field"
                    )
                }
            )

    @classmethod
    def _build_schema_query_mutation(cls):
        """
        Build the schema, Query, and Mutation objects.
        """
        cls.schema, cls.Query, cls.Mutation = get_schema_query_mutation( 
            (), 
            cls.query_operation_fields, 
            (), 
            cls.mutation_operation_fields 
        )


class BuilderCruddalsApp:
    app_name = None
    app_config = None
    models = None
    cruddals_of_models = dict()

    queries = tuple()
    mutations = tuple()

    def __init__(
        self,
        app_name,
        exclude_models=None,
        models=None,
        prefix="",
        suffix="",
        interfaces=tuple(),
        exclude_interfaces=tuple(),
        functions=tuple(),
        exclude_functions=tuple(),
        settings_for_model=dict(),
    ) -> None:
        assert app_name, "app_name is required for BuilderCruddalsApp"
        validate_list_func_cruddals(functions, exclude_functions)

        [setattr(self, attr, None) for attr in ["app_name", "app_config", "models"]]
        [setattr(self, attr, tuple()) for attr in ["queries", "mutations"]]
        setattr(self, "cruddals_of_models", dict())

        self.validate_variables_of_cruddals_app(
            exclude_models,
            models,
            interfaces,
            exclude_interfaces,
            functions,
            exclude_functions,
            settings_for_model,
            app_name,
        )

        self.app_name = app_name
        self.app_config = django_apps.get_app_config(app_name)
        self.models = tuple(self.app_config.get_models())

        if exclude_models is not None:
            models_to_exclude = set()
            for exclude_model in exclude_models:
                model_to_exclude = self.app_config.get_model(model_name=exclude_model)
                models_to_exclude.add(model_to_exclude)
            self.models = tuple(set(self.models) - models_to_exclude)
        elif models is not None:
            models_to_include = []
            for include_model in models:
                model_to_include = self.app_config.get_model(model_name=include_model)
                models_to_include.append(model_to_include)
            self.models = models_to_include

        for Model in self.models:
            settings_model = settings_for_model.get(Model.__name__, dict())

            settings_model["interfaces"] = interfaces + settings_model.get(
                "interfaces", ()
            )
            settings_model["exclude_interfaces"] = (
                exclude_interfaces + settings_model.get("exclude_interfaces", ())
            )

            settings_model["functions"] = functions + settings_model.get(
                "functions", ()
            )
            settings_model["exclude_functions"] = (
                exclude_functions + settings_model.get("exclude_functions", ())
            )

            settings_model["prefix"] = settings_model.get("prefix", prefix)
            settings_model["suffix"] = settings_model.get("suffix", suffix)

            cruddals_model_meta = build_class(
                name="Meta", attrs={"model": Model, **settings_model}
            )
            cruddals_model = build_class(
                name=f"{Model.__name__}Cruddals",
                bases=(CruddalsModel,),
                attrs={"Meta": cruddals_model_meta},
            )

            self.cruddals_of_models.update(
                {
                    f"{cruddals_model.meta.model_name_in_different_case['camel_case']}": cruddals_model
                }
            )
            self.queries = self.queries + (cruddals_model.Query,)
            if cruddals_model.Mutation:
                self.mutations = self.mutations + (cruddals_model.Mutation,)

    @staticmethod #TODO: Change to a class method
    def validate_variables_of_cruddals_app(exclude_models, include_models, interfaces_app, exclude_interfaces_app, functions_app, exclude_functions_app, settings_for_model, app_name):
        assert not ( exclude_models and include_models ), f"Cannot set both 'exclude_models' and 'models' options on {app_name}."
        assert isinstance( interfaces_app, (tuple,) ), f"'interfaces' should be tuple received {type(interfaces_app)}"
        assert isinstance( exclude_interfaces_app, (tuple,) ), f"'exclude_interfaces' should be tuple received {type(exclude_interfaces_app)}"
        assert isinstance( functions_app, (tuple,) ), f"'functions' should be tuple received {type(functions_app)}"
        assert isinstance( exclude_functions_app, (tuple,) ), f"'exclude_functions' should be tuple received {type(exclude_functions_app)}"
        assert isinstance( settings_for_model, dict ), f"'settings_for_model' should be dict, received {type(settings_for_model)}"

        if exclude_models is not None:
            assert isinstance( exclude_models, (tuple,) ), f"'exclude_models' should be tuple received {type(exclude_models)}"
        if include_models is not None:
            assert isinstance( include_models, (tuple,) ), f"'models' should be tuple received {type(include_models)}"



class CruddalsApp(SubclassWithMeta):
    Query = None
    Mutation = None
    schema = None

    meta = None

    @classmethod
    def __init_subclass_with_meta__(
        cls,
        app_name,
        models=None,
        exclude_models=None,
        prefix="",
        suffix="",
        interfaces=tuple(),
        exclude_interfaces=tuple(),
        functions=tuple(),
        exclude_functions=tuple(),
        settings_for_model=dict(),
    ):
        assert app_name, "app_name is required for CruddalsApp"
        validate_list_func_cruddals(functions, exclude_functions)

        [setattr(cls, attr, None) for attr in ["Query", "Mutation", "schema", "meta"]]

        cruddals_of_app = BuilderCruddalsApp(
            app_name=app_name,
            exclude_models=exclude_models,
            models=models,
            prefix=prefix,
            suffix=suffix,
            interfaces=interfaces,
            exclude_interfaces=exclude_interfaces,
            functions=functions,
            exclude_functions=exclude_functions,
            settings_for_model=settings_for_model,
        )
        cls.meta = cruddals_of_app

        cls.schema, cls.Query, cls.Mutation = get_schema_query_mutation(
            cruddals_of_app.queries, {}, cruddals_of_app.mutations, {}
        )

        super(CruddalsApp, cls).__init_subclass_with_meta__()


class AppSettings(NamedTuple):
    exclude_models: tuple = None
    models: tuple = None
    interfaces: tuple = ()
    exclude_interfaces: tuple = ()
    functions: tuple = ()
    exclude_functions: tuple = ()
    settings_for_model: dict = {}


class CruddalsProject(SubclassWithMeta):
    """
    A base class for defining GraphQL schemas for Django apps in a project using Cruddals.

    This class provides methods to dynamically create GraphQL schemas for each app in the project
    based on provided settings.

    Attributes:
        apps (str or tuple or dict): Names of Django apps for which schemas will be generated.
            Defaults to "__all__", meaning all apps in the project.
        schema: The generated GraphQL schema for the project.
        Query: The combined Query object for the project.
        Mutation: The combined Mutation object for the project.
    """
    apps: Union[Literal["__all__"], Tuple[str, ...]] = "__all__"
    schema: graphene.Schema = None

    Query = None #TODO: Type
    Mutation = None #TODO: Type

    @classmethod
    def __init_subclass_with_meta__(
        cls,
        apps: Union[Literal["__all__"], Tuple[str, ...]] = "__all__",
        exclude_apps: Tuple[str, ...] = (),
        interfaces: Tuple[str, ...] = (),
        settings_for_app: Optional[Dict[str, Any]] = None,
        functions: Tuple[str] = (),
        exclude_functions: Tuple[str] = (),
        **kwargs: Any,
    ):
        """
        Initialize the subclass with meta settings and dynamically create GraphQL schemas for apps.

        Args:
            apps (str or tuple): Names of Django apps for which schemas will be generated.
                Defaults to "__all__", meaning all apps in the project.
            exclude_apps (tuple): Names of apps to exclude from schema generation.
            interfaces (tuple): Additional GraphQL interfaces to include in the schemas.
            settings_for_app (dict): Settings specific to each app for schema generation.
            functions (tuple): Functions to include in the schemas can be "create", "read", "update", "delete", "deactivate", "activate", "list", "search" . #TODO: Should name "functions" be changed to "operations" or "fields"?
            exclude_functions (tuple): Functions to exclude from schema generation.
            **kwargs: Additional keyword arguments.
        """
        if settings_for_app is None:
            settings_for_app = {}

        default_exclude_apps = (
            "graphene_django",
            "messages",
            "staticfiles",
            "corsheaders",
            "graphene_django_cruddals",
        )
        exclude_apps = exclude_apps + default_exclude_apps

        interfaces_for_project = interfaces

        apps_name = cls._get_apps_name(apps, exclude_apps)
        cls._validate_apps(apps_name)
        cls._validate_apps(settings_for_app.keys())

        queries = ()
        mutations = ()

        for _app_name in apps_name:
            settings_of_app = settings_for_app.get(_app_name, {})

            final_models, final_exclude_models = cls._get_final_models(apps, _app_name, settings_of_app)
            final_interfaces, final_exclude_interfaces = cls._get_final_interfaces(interfaces_for_project, settings_of_app)
            final_functions, final_exclude_functions = cls._get_final_functions(functions, exclude_functions, settings_of_app)

            final_settings_for_model = settings_of_app.get("settings_for_model", {})

            AppSchema = cls._create_app_schema(
                _app_name,
                final_models,
                final_exclude_models,

                final_interfaces,
                final_exclude_interfaces,

                final_functions,
                final_exclude_functions,
                final_settings_for_model,
            )

            queries = queries + (AppSchema.Query,)
            if AppSchema.Mutation:
                mutations = mutations + (AppSchema.Mutation,)

        cls.schema, cls.Query, cls.Mutation = get_schema_query_mutation(
            queries, {}, mutations, {}
        )

    @classmethod
    def _get_apps_name(cls, apps, exclude_apps):
        apps_name = ()
        if apps == "__all__":
            apps_name = django_apps.app_configs.keys()
        elif isinstance(apps, tuple):
            apps_name = apps
        else:
            raise ValueError("apps should be '__all__' or tuple")
        
        apps_name = [item for item in apps_name if item not in exclude_apps]
        return apps_name

    @classmethod
    def _validate_apps(cls, apps_name):
        [django_apps.get_app_config(app_name) for app_name in apps_name]

    @classmethod
    def _get_final_models(cls, apps, _app_name, settings_of_app):
        exclude_models = settings_of_app.get("exclude_models", None)
        if exclude_models is None:
            _models = apps.get(_app_name, None) if isinstance(apps, dict) else None
            return (settings_of_app.get("models", _models), None)
        else:
            return (None, exclude_models)

    @classmethod
    def _get_final_interfaces(cls, interfaces_for_project, settings_of_app):
        interfaces_for_app = settings_of_app.get("interfaces", ())
        return (interfaces_for_project + interfaces_for_app, settings_of_app.get("exclude_interfaces", ()))

    @classmethod
    def _get_final_functions(cls, functions, exclude_functions, settings_of_app):
        functions_of_app = settings_of_app.get("functions", ())
        exclude_functions_of_app = settings_of_app.get("exclude_functions", ())
        return (functions + functions_of_app, exclude_functions + exclude_functions_of_app)

    @classmethod
    def _create_app_schema(
        cls,
        _app_name,
        final_models,
        final_exclude_models,
        final_interfaces,
        exclude_interfaces_of_app,
        final_functions,
        final_exclude_functions,
        final_settings_for_model,
    ):
        class AppSchema(CruddalsApp):
            class Meta:
                app_name = _app_name

                models = final_models
                exclude_models = final_exclude_models

                interfaces = final_interfaces
                exclude_interfaces = exclude_interfaces_of_app

                functions = final_functions
                exclude_functions = final_exclude_functions

                settings_for_model = final_settings_for_model

        return AppSchema






class ExampleModelInterface:
    
    class ObjectType: # This is the class that will be used to modify the ObjectType of the model
        
        class Meta: # This is the class that will be used to modify the Meta class of the ObjectType
            only_fields = "__all__" # Tuple of str or "__all__"
            exclude_fields = () # Tuple of str

        new_field = graphene.String() # Graphene => Scalar, String, ID, Int, Float, Boolean, Date, DateTime, Time, Decimal, JSONString, UUID, List, NonNull, Enum, Argument, Dynamic

        def resolve_new_field(self, info): # Resolver for new_field should be a function with the same name as the field prefixed by "resolve_" and receive 2 arguments (self, info), return the value of the field same type as the field
            return "new_field"

        # another fields with their resolvers

        @classmethod
        def get_queryset(cls, queryset, info): # This method is special and is used to modify the queryset before it is returned, receives 3 arguments (cls, queryset:QuerySet de Django, info), return queryset
            return queryset

    class InputObjectType:
        class Meta:
            only_fields = "__all__"
            exclude_fields = ()
            #(deprecated)hold_required_in_fields = False  # Podría ser también reemplazar esto por required_fields = "__all__" y not_required_fields = ()

        new_field = graphene.String()
        # exist_field = CruddalsRelationField() => For relations

        # Implícitamente si pone un campo que ya estaba en el ModelInputObjectType, sera sobrescrito por el que ponga de ultimo
        # y ya todos los otros nuevos serán nuevos campos como tal

    class CreateInputObjectType:
        class Meta:
            only_fields = "__all__"
            exclude_fields = ()
            #(deprecated)hold_required_in_fields = False  # Podría ser también reemplazar esto por required_fields = "__all__" y not_required_fields = ()

        new_field = graphene.String()
        # exist_field = CruddalsRelationField() => For relations

        # Implícitamente si pone un campo que ya estaba en el ModelInputObjectType, sera sobrescrito por el que ponga de ultimo
        # y ya todos los otros nuevos serán nuevos campos como tal

    class UpdateInputObjectType:
        class Meta:
            only_fields = "__all__"
            exclude_fields = ()
            #(deprecated)hold_required_in_fields = False  # Podría ser también reemplazar esto por required_fields = "__all__" y not_required_fields = ()

        new_field = graphene.String()
        # exist_field = CruddalsRelationField() => For relations

        # Implícitamente si pone un campo que ya estaba en el ModelInputObjectType, sera sobrescrito por el que ponga de ultimo
        # y ya todos los otros nuevos serán nuevos campos como tal

    class FilterInputObjectType:
        class Meta:
            only_fields = "__all__"
            exclude_fields = ()

        new_field = graphene.String()

        # Implícitamente si pone un campo que ya estaba en el ModelInputObjectType, sera sobrescrito por el que ponga de ultimo
        # y ya todos los otros nuevos serán nuevos campos como tal

    class OrderByInputObjectType:
        class Meta:
            only_fields = "__all__"
            exclude_fields = ()

        new_field = graphene.String()

        # Implícitamente si pone un campo que ya estaba en el ModelInputObjectType, sera sobrescrito por el que ponga de ultimo
        # y ya todos los otros nuevos serán nuevos campos como tal

    class CreateField:
        class Meta:
            modify_input_argument = {
                "name": "input",
                "required": True,
                "description": "",
                "hidden": False,
            }
            extra_arguments = {}

        def pre_mutate(*args, **kwargs):
            return (*args, kwargs)

        def mutate(*args, **kwargs):
            return "object_create"

        def override_total_mutate(*args, **kwargs):
            return "object_create"

        def post_mutate(*args, **kwargs):
            return "object_create"

    class ReadField:
        class Meta:
            modify_where_argument = {
                "name": "where",
                "required": True,
                "description": "",
                "hidden": False,
            }
            extra_arguments = {}

        def pre_resolve(*args, **kwargs):
            return (*args, kwargs)

        def resolve(*args, **kwargs):
            return "object_read"

        def override_total_resolve(*args, **kwargs):
            return "object_read"

        def post_resolve(*args, **kwargs):
            return "object_read"

    class UpdateField:
        class Meta:
            modify_input_argument = {
                "name": "input",
                "required": True,
                "description": "",
                "hidden": False,
            }
            extra_arguments = {}

        def pre_mutate(*args, **kwargs):
            return (*args, kwargs)

        def mutate(*args, **kwargs):
            return "object_update"

        def override_total_mutate(*args, **kwargs):
            return "object_update"

        def post_mutate(*args, **kwargs):
            return "object_update"

    class DeleteField:
        class Meta:
            modify_where_argument = {
                "name": "where",
                "required": True,
                "description": "",
                "hidden": False,
            }
            extra_arguments = {}

        def pre_mutate(*args, **kwargs):
            return (*args, kwargs)

        def mutate(*args, **kwargs):
            return "object_read"

        def override_total_mutate(*args, **kwargs):
            return "object_read"

        def post_mutate(*args, **kwargs):
            return "object_read"

    class DeactivateField:
        class Meta:
            modify_where_argument = {
                "name": "where",
                "required": True,
                "description": "",
                "hidden": False,
            }
            extra_arguments = {}

        def pre_mutate(*args, **kwargs):
            return (*args, kwargs)

        def mutate(*args, **kwargs):
            return "list_objects_deactivates"

        def override_total_mutate(*args, **kwargs):
            return "list_objects_deactivates"

        def post_mutate(*args, **kwargs):
            return "list_objects_deactivates"

    class ActivateField:
        class Meta:
            modify_where_argument = {
                "name": "where",
                "required": True,
                "description": "",
                "hidden": False,
            }
            extra_arguments = {}

        def pre_mutate(*args, **kwargs):
            return (*args, kwargs)

        def mutate(*args, **kwargs):
            return "list_objects_actives"

        def override_total_mutate(*args, **kwargs):
            return "list_objects_actives"

        def post_mutate(*args, **kwargs):
            return "list_objects_actives"

    class ListField:
        class Meta:
            modify_order_by_argument = {
                "name": "orderBy",
                "required": False,
                "description": "",
                "hidden": False,
            }
            modify_pagination_config_argument = {
                "name": "paginated",
                "required": False,
                "description": "",
                "hidden": False,
            }
            extra_arguments = {}

        def pre_resolve(*args, **kwargs):
            return (*args, kwargs)

        def resolve(*args, **kwargs):
            return "paginated_objects"

        def override_total_resolve(*args, **kwargs):
            return "paginated_objects"

        def post_resolve(*args, **kwargs):
            return "paginated_objects"

    class SearchField:
        class Meta:
            modify_where_argument = {
                "name": "where",
                "required": False,
                "description": "",
                "hidden": False,
            }
            modify_order_by_argument = {
                "name": "orderBy",
                "required": False,
                "description": "",
                "hidden": False,
            }
            modify_pagination_config_argument = {
                "name": "paginated",
                "required": False,
                "description": "",
                "hidden": False,
            }
            extra_arguments = {}

        def pre_resolve(*args, **kwargs):
            return (*args, kwargs)

        def resolve(*args, **kwargs):
            return "paginated_objects"

        def override_total_resolve(*args, **kwargs):
            return "paginated_objects"

        def post_resolve(*args, **kwargs):
            return "paginated_objects"
