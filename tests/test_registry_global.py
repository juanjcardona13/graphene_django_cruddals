import pytest

from graphene_django_cruddals.registry_global import RegistryGlobal


@pytest.fixture
def registry_global():
    return RegistryGlobal()


def test_register_model(registry_global):
    model = "ClassMyModel"
    type_to_registry = "object_type"
    cls = "ClassMyModelObjectType"
    registry_global.register_model(model, type_to_registry, cls)
    assert registry_global.get_registry_for_model(model)[type_to_registry] == cls


def test_get_registry_for_model(registry_global):
    model = "ClassMyModel"
    type_to_registry = "object_type"
    cls = "ClassMyModelObjectType"
    registry_global.register_model(model, type_to_registry, cls)
    assert registry_global.get_registry_for_model(model) == {type_to_registry: cls}


def test_get_all_models_registered(registry_global):
    model1 = "ClassMyModel1"
    type_to_registry1 = "object_type"
    cls1 = "ClassMyModelObjectType1"
    model2 = "ClassMyModel2"
    type_to_registry2 = "paginated_object_type"
    cls2 = "ClassMyModelObjectType2"
    registry_global.register_model(model1, type_to_registry1, cls1)
    registry_global.register_model(model2, type_to_registry2, cls2)
    assert registry_global.get_all_models_registered() == {
        model1: {type_to_registry1: cls1},
        model2: {type_to_registry2: cls2},
    }


def test_get_all_fields_registered(registry_global):
    field1 = "FIELD1"
    type_to_registry1 = "output"
    converted1 = "Field1"
    field2 = "FIELD2"
    type_to_registry2 = "input_for_create_update"
    converted2 = "CreateUpdateInputField2"
    registry_global.register_field(field1, type_to_registry1, converted1)
    registry_global.register_field(field2, type_to_registry2, converted2)
    assert registry_global.get_all_fields_registered() == {
        field1: {type_to_registry1: converted1},
        field2: {type_to_registry2: converted2},
    }


def test_register_field(registry_global):
    field = "FIELD"
    type_to_registry = "output"
    converted = "Field"
    registry_global.register_field(field, type_to_registry, converted)
    assert registry_global.get_registry_for_field(field)[type_to_registry] == converted


def test_get_registry_for_field(registry_global):
    field = "FIELD"
    type_to_registry = "output"
    converted = "Field"
    registry_global.register_field(field, type_to_registry, converted)
    assert registry_global.get_registry_for_field(field) == {
        type_to_registry: converted
    }
