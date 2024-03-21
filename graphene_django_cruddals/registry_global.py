from enum import Enum
from typing import Any, Dict, Union

from django.db.models import Model as DjangoModel
from django.db.models.fields import Field as DjangoField

from graphene_django_cruddals.types import TypeRegistryForField, TypeRegistryForModel


class TypeRegistryForModelEnum(Enum):
    OBJECT_TYPE = "object_type"
    PAGINATED_OBJECT_TYPE = "paginated_object_type"
    INPUT_OBJECT_TYPE = "input_object_type"
    INPUT_OBJECT_TYPE_FOR_CREATE = "input_object_type_for_create"
    INPUT_OBJECT_TYPE_FOR_UPDATE = "input_object_type_for_update"
    INPUT_OBJECT_TYPE_FOR_SEARCH = "input_object_type_for_search"
    INPUT_OBJECT_TYPE_FOR_ORDER_BY = "input_object_type_for_order_by"
    INPUT_OBJECT_TYPE_FOR_CONNECT = (
        "input_object_type_for_connect"
    )
    INPUT_OBJECT_TYPE_FOR_CONNECT_DISCONNECT = (
        "input_object_type_for_connect_disconnect"
    )
    CRUDDALS = "cruddals"


class TypeRegistryForFieldEnum(Enum):
    OUTPUT = "output"
    INPUT_FOR_CREATE_UPDATE = "input_for_create_update"
    INPUT_FOR_CREATE = "input_for_create"
    INPUT_FOR_UPDATE = "input_for_update"
    INPUT_FOR_SEARCH = "input_for_search"
    INPUT_FOR_ORDER_BY = "input_for_order_by"


class RegistryGlobal:
    """
    Registry all necessary for convert your ORM Django to valid API GraphQL
    Example Complete:

    model_registry = {
        "ClassMyModel": {
            "object_type": ClassMyModelObjectType,
            "paginated_object_type": ClassMyModelObjectType,
            "input_object_type": ClassMyModelInputObjectType,
            "input_object_type_for_create": ClassMyModelCreateInputObjectType,
            "input_object_type_for_update": ClassMyModelUpdateInputObjectType,
            "input_object_type_for_search": ClassMyModelFilterInputObjectType,
            "input_object_type_for_order_by": ClassMyModelOrderInputObjectType,
            "input_object_type_for_connect": ClassMyModelConnectInputObjectType,
            "input_object_type_for_connect_disconnect": ClassMyModelConnectDisconnectInputObjectType,
            "cruddals": ClassMyModelCRUDDALS,
        }
    }

    field_registry = {
        "FIELD": {
            "output": Field,
            "input_for_create_update": CreateUpdateInputField,
            "input_for_create": CreateInputField,
            "input_for_update": UpdateInputField,
            "input_for_search": FilterInputField,
            "input_for_order_by": OrderByInputField,
        }
    }
    """

    def __init__(self):
        self._model_registry: Dict[Any, Dict[TypeRegistryForModel, Any]] = {}
        self._field_registry: Dict[Any, Dict[TypeRegistryForField, Any]] = {}

    def register_model( self, model: DjangoModel, type_to_registry: TypeRegistryForModel, cls ):
        self._model_registry.setdefault(model, {})[type_to_registry] = cls

    def get_registry_for_model(self, model: DjangoModel):
        return self._model_registry.get(model)

    def get_all_models_registered(self):
        return self._model_registry

    def get_all_fields_registered(self):
        return self._field_registry

    def register_field( self, field: DjangoField, type_to_registry: TypeRegistryForField, converted ):
        self._field_registry.setdefault(field, {})[type_to_registry] = converted

    def get_registry_for_field(self, field: DjangoField):
        return self._field_registry.get(field)


registry = None


def get_global_registry(name_registry:Union[str,None]=None) -> RegistryGlobal :
    if name_registry:
        custom_registry = globals().get(name_registry)
        if not custom_registry:
            globals()[name_registry] = RegistryGlobal()
        return globals()[name_registry]
    else:
        global registry
        if not registry:
            registry = RegistryGlobal()
        return registry


def reset_global_registry():
    global registry
    registry = None
