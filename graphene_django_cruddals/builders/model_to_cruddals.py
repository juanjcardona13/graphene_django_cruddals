from collections import OrderedDict
from enum import Enum
from typing import Any, Callable, Dict, Tuple, Type, Union

from django.db.models import Model as DjangoModel
from django.forms import ModelForm as DjangoModelForm

import graphene
from graphene.types.generic import GenericScalar
from graphene.utils.props import props
from graphene.utils.str_converters import to_snake_case
from graphene.utils.subclass_with_meta import SubclassWithMeta
from graphene_django_cruddals.converters.django_types import DjangoObjectType
from graphene_django_cruddals.converters.for_entity.main import (
    convert_django_model_to_filter_input_object_type,
    convert_django_model_to_mutate_input_object_type,
    convert_django_model_to_object_type,
    convert_django_model_to_order_by_input_object_type,
    convert_django_model_to_paginated_object_type,
)
from graphene_django_cruddals.operations_fields.default_resolvers import (
    default_activate_field_resolver,
    default_create_update_resolver,
    default_deactivate_field_resolver,
    default_delete_field_resolver,
    default_list_field_resolver,
    default_read_field_resolver,
    default_search_field_resolver,
    default_update_resolver,
)
from graphene_django_cruddals.operations_fields.main import (
    DjangoActivateField,
    DjangoCreateUpdateField,
    DjangoDeactivateField,
    DjangoDeleteField,
    DjangoListField,
    DjangoReadField,
    DjangoSearchField,
)
from graphene_django_cruddals.python_types import (
    CamelFunctionType,
    FunctionType,
    InterfaceStructure,
    NameCaseType,
)
from graphene_django_cruddals.registry_global import (
    RegistryGlobal,
    TypeRegistryForModelEnum,
    get_global_registry,
)
from graphene_django_cruddals.utils.utils import (
    convert_model_to_model_form,
    delete_keys,
    get_name_of_model_in_different_case,
    get_schema_query_mutation,
    merge_dict,
    validate_list_func_cruddals,
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

    model_as_object_type: Type[DjangoObjectType]
    model_as_paginated_object_type: Type[graphene.ObjectType]
    model_as_input_object_type: Type[graphene.InputObjectType]
    model_as_create_input_object_type: Type[graphene.InputObjectType]
    model_as_update_input_object_type: Type[graphene.InputObjectType]
    model_as_filter_input_object_type: Type[graphene.InputObjectType]
    model_as_order_by_input_object_type: Type[graphene.InputObjectType]

    read_field: DjangoReadField
    list_field: Union[DjangoListField, None] = None
    search_field: Union[DjangoSearchField, None] = None
    create_field: Union[DjangoCreateUpdateField, None] = None
    update_field: Union[DjangoCreateUpdateField, None] = None
    activate_field: Union[DjangoActivateField, None] = None
    deactivate_field: Union[DjangoDeactivateField, None] = None
    delete_field: Union[DjangoDeleteField, None] = None

    @staticmethod  # TODa: Change to a class method
    def get_where_arg(
        model_as_filter_input_object_type, kw=None, default_required=False
    ):
        if kw is None:
            kw = {}
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

    @staticmethod  # TODa: Change to a class method
    def add_cruddals_model_to_request(info, cruddals_model):
        if info.context is None:

            class Context:
                pass

            info.context = Context()
        info.context.CruddalsModel = cruddals_model

    def wrap_resolver_with_pre_post_resolvers(
        self, kwargs, name_function, default_resolver
    ):
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

    def get_resolve_for_operation_field(
        self, kwargs, name_function: str, default_resolver
    ):
        return self.wrap_resolver_with_pre_post_resolvers(
            kwargs, name_function, default_resolver
        )

    def get_interface_attrs(self, interface, include_meta_attrs=True):
        if interface is not None:
            attrs_internal_cls_meta = {}
            if getattr(interface, "Meta", None) is not None and include_meta_attrs:
                attrs_internal_cls_meta = props(interface.Meta)
            props_function = delete_keys(props(interface), ["Meta"])
            return {**props_function, **attrs_internal_cls_meta}
        return {}

    def get_interface_meta_attrs(self, interface_type):
        if interface_type is not None:
            if getattr(interface_type, "Meta", None) is not None:
                p = props(interface_type.Meta)

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
        def pre_default(*args, **kwargs):
            return (*args, kwargs)

        def post_default(root, info, default_response=None, **kwargs):
            return default_response

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
        )  # TODa: Debo de mirar esto donde lo voy a cuadrar para que sea global

    @staticmethod  # TODa: Change to a class method
    def get_input_arg(model_as_input_object_type, kw=None):
        if kw is None:
            kw = {}
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

    # TODa: I should change to class method
    def build_create(self, **kwargs) -> DjangoCreateUpdateField:
        extra_args = self.get_extra_arguments(kwargs)

        def default_resolver(root, info, **args):
            return default_create_update_resolver(
                self.model, self.model_as_form, self.registry, root, info, **args
            )

        input_arg = self.get_input_arg(self.model_as_create_input_object_type, kwargs)

        name_function = "mutate"
        resolver = self.get_resolve_for_operation_field(
            kwargs, name_function, default_resolver
        )

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

    # TODa: I should change to class method
    def build_read(self, **kwargs) -> DjangoReadField:
        extra_args = self.get_extra_arguments(kwargs)
        where_arg = self.get_where_arg(
            self.model_as_filter_input_object_type, kwargs, True
        )

        name_function = "resolve"

        def default_resolver(root, info, **args):
            return default_read_field_resolver(
                self.model_as_object_type,
                self.model._default_manager,
                root,
                info,
                **args,
            )

        resolver = self.get_resolve_for_operation_field(
            kwargs, name_function, default_resolver
        )

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

    # TODa: I should change to class method
    def build_update(self, **kwargs) -> DjangoCreateUpdateField:
        extra_args = self.get_extra_arguments(kwargs)
        input_arg = self.get_input_arg(self.model_as_update_input_object_type, kwargs)

        name_function = "mutate"

        def default_resolver(root, info, **args):
            return default_update_resolver(
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

    # TODa: I should change to class method
    def build_delete(self, **kwargs) -> DjangoDeleteField:
        extra_args = self.get_extra_arguments(kwargs)
        where_arg = self.get_where_arg(
            self.model_as_filter_input_object_type, kwargs, True
        )

        name_function = "mutate"

        def default_resolver(root, info, **args):
            return default_delete_field_resolver(self.model, root, info, **args)

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

    # TODa: I should change to class method
    def build_deactivate(self, **kwargs) -> DjangoDeactivateField:
        extra_args = self.get_extra_arguments(kwargs)
        where_arg = self.get_where_arg(
            self.model_as_filter_input_object_type, kwargs, True
        )

        name_function = "mutate"
        field_for_activate_deactivate: str = self.get_state_controller_field(kwargs)

        def default_resolver(root, info, **args):
            return default_deactivate_field_resolver(
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

    # TODa: I should change to class method
    def build_activate(self, **kwargs) -> DjangoActivateField:
        extra_args = self.get_extra_arguments(kwargs)
        where_arg = self.get_where_arg(
            self.model_as_filter_input_object_type, kwargs, True
        )

        name_function = "mutate"
        field_for_activate_deactivate: str = self.get_state_controller_field(kwargs)

        def default_resolver(root, info, **args):
            return default_activate_field_resolver(
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

    # TODa: I should change to class method
    def build_list(self, **kwargs) -> DjangoListField:
        extra_args = self.get_extra_arguments(kwargs)

        name_function = "resolve"

        def default_resolver(root, info, **args):
            return default_list_field_resolver(
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

    @staticmethod  # TODa: Change to a class method
    def get_order_by_arg(model_as_order_by_input_object_type, kw=None):
        if kw is None:
            kw = {}
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

    @staticmethod  # TODa: Change to a class method
    def get_pagination_config_arg(kw=None):
        if kw is None:
            kw = {}
        default_values_for_paginated = {
            "type_": PaginationConfigInput,
            "name": "paginated",
            "required": False,
            "description": "",
        }
        attrs_for_pagination_config_arg = kw.get(
            "modify_pagination_config_argument", {}
        )
        attrs_for_pagination_config_arg = (
            default_values_for_paginated | attrs_for_pagination_config_arg
        )
        if default_values_for_paginated.get("hidden", False):
            return {}
        else:
            return {"paginated": graphene.Argument(**default_values_for_paginated)}

    def validate_props_search_field(self, props, name=None):
        self.validate_attrs(props, "override_total_resolve", "Search", name)

    # TODa: I should change to class method
    def build_search(self, **kwargs) -> DjangoSearchField:
        extra_arg_for_search = self.get_extra_arguments(kwargs)
        where_arg = self.get_where_arg(
            self.model_as_filter_input_object_type, kwargs, False
        )
        order_by_arg = self.get_order_by_arg(
            self.model_as_order_by_input_object_type, kw=kwargs
        )
        pagination_config_arg = self.get_pagination_config_arg(kw=kwargs)

        name_function = "resolve"

        def default_resolver(root, info, **args):
            return default_search_field_resolver(
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
            args={
                **where_arg,
                **order_by_arg,
                **pagination_config_arg,
                **extra_arg_for_search,
            },
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

    model: DjangoModel
    prefix: str = ""
    suffix: str = ""

    model_name_in_different_case: NameCaseType
    model_as_form: DjangoModelForm
    registry: RegistryGlobal

    def __init__(
        self,
        model: DjangoModel,
        prefix: str = "",
        suffix: str = "",
        interfaces: Tuple[InterfaceStructure, ...] = (),
        exclude_interfaces: Tuple[str, ...] = (),
        registry: Union[RegistryGlobal, None] = None,
    ) -> None:
        assert model, "model is required for BuilderCruddalsModel"

        attrs_for_child = [
            "model",
            "prefix",
            "suffix",
            "model_as_form",
            "model_name_in_different_case",
            "registry",
            "model_as_object_type",
            "model_as_paginated_object_type",
            "model_as_input_object_type",
            "model_as_filter_input_object_type",
            "model_as_order_by_input_object_type",
            "read_field",
            "list_field",
            "search_field",
            "create_field",
            "update_field",
            "activate_field",
            "deactivate_field",
            "delete_field",
        ]
        [setattr(self, attr, None) for attr in attrs_for_child]

        if not registry:
            self.registry = get_global_registry(f"{prefix}{suffix}")
        else:
            self.registry = registry

        self.model = model
        self.prefix = prefix
        self.suffix = suffix
        self.model_name_in_different_case = get_name_of_model_in_different_case(
            model, prefix, suffix
        )

        assert isinstance(
            interfaces, (tuple,)
        ), f"'interfaces' should be tuple received {type(interfaces)}"
        assert isinstance(
            exclude_interfaces, (tuple,)
        ), f"'exclude_interfaces' should be tuple received {type(exclude_interfaces)}"

        dict_of_interface_attr = self.get_dict_of_interface_attr(
            interfaces, exclude_interfaces
        )

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

    def get_dict_of_interface_attr(
        self,
        interfaces: Tuple[InterfaceStructure, ...],
        exclude_interfaces: Tuple[str, ...],
    ) -> Dict[str, OrderedDict[str, Any]]:
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
        operation_fields_for_queries (Dict[str, Union[graphene.Field, DjangoReadField, DjangoListField, DjangoSearchField]]):
            The query operation fields for the model.
        operation_fields_for_mutations (Union[Dict[str, Union[graphene.Field, DjangoCreateUpdateField, DjangoDeleteField,
            DjangoDeactivateField, DjangoActivateField]], None]): The mutation operation fields for the model.
        meta (BuilderCruddalsModel): An instance of BuilderCruddalsModel containing metadata about the model.

    Methods:
        __init_subclass_with_meta__: Initialize the subclass with meta settings and dynamically create GraphQL schemas.
        _initialize_attributes: Initialize attributes to None.
        _build_cruddals_model: Build the CruddalsModel using BuilderCruddalsModel.
        _build_dict_for_operation_fields: Build dictionaries for query and mutation operation fields.
        _build_schema_query_mutation: Build the schema, Query, and Mutation objects.

    """

    Query: Type[graphene.ObjectType]
    Mutation: Union[Type[graphene.ObjectType], None] = None
    schema: graphene.Schema
    operation_fields_for_queries: Dict[
        str, graphene.Field | DjangoReadField | DjangoListField | DjangoSearchField
    ]
    operation_fields_for_mutations: Union[
        Dict[
            str,
            graphene.Field
            | DjangoCreateUpdateField
            | DjangoDeleteField
            | DjangoDeactivateField
            | DjangoActivateField,
        ],
        None,
    ] = None
    meta: BuilderCruddalsModel

    @classmethod
    def __init_subclass_with_meta__(
        cls,
        model: Union[DjangoModel, None] = None,
        prefix: str = "",
        suffix: str = "",
        interfaces: Tuple[InterfaceStructure, ...] = (),
        exclude_interfaces: Tuple[str, ...] = (),
        functions: Tuple[FunctionType, ...] = (),
        exclude_functions: Tuple[FunctionType, ...] = (),
        registry: Union[RegistryGlobal, None] = None,
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
        cls._build_cruddals_model(
            model, prefix, suffix, interfaces, exclude_interfaces, registry
        )
        cls._build_dict_for_operation_fields(functions, exclude_functions)
        cls._build_schema_query_mutation()
        registry.register_model(model, TypeRegistryForModelEnum.CRUDDALS.value, cls)

        super().__init_subclass_with_meta__(**kwargs)

    @classmethod
    def _initialize_attributes(cls):
        """
        Initialize attributes to None for the child class.
        """
        attrs_for_child = [
            "Query",
            "Mutation",
            "schema",
            "operation_fields_for_queries",
            "operation_fields_for_mutations",
            "meta",
        ]
        [setattr(cls, attr, None) for attr in attrs_for_child]

    @classmethod
    def _build_cruddals_model(
        cls, model, prefix, suffix, interfaces, exclude_interfaces, registry
    ):
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
            model=model,
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
        final_functions = (
            functions
            if functions
            else tuple(
                set(functions_type_query + functions_type_mutation)
                - set(exclude_functions)
            )
        )

        cls.operation_fields_for_queries = {}
        cls.operation_fields_for_mutations = {}

        for function in final_functions:
            key = f"{function}_{cls.meta.model_name_in_different_case['plural_snake_case']}"
            if function == "read":
                key = (
                    f"{function}_{cls.meta.model_name_in_different_case['snake_case']}"
                )
            attr_field: Dict[str, graphene.Field] = {
                key: getattr(cls.meta, f"{function}_field")
            }
            if function in functions_type_query:
                cls.operation_fields_for_queries.update(attr_field)
            elif function in functions_type_mutation:
                cls.operation_fields_for_mutations.update(attr_field)

        if not cls.operation_fields_for_queries:
            cls.operation_fields_for_queries.update(
                {
                    f"read_{cls.meta.model_name_in_different_case['snake_case']}": cls.meta.read_field
                }
            )

    @classmethod
    def _build_schema_query_mutation(cls):
        """
        Build the schema, Query, and Mutation objects.
        """
        cls.schema, cls.Query, cls.Mutation = get_schema_query_mutation(
            (), cls.operation_fields_for_queries, (), cls.operation_fields_for_mutations
        )
