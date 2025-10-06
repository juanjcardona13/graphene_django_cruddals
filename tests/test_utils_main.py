from unittest.mock import patch

import pytest
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models.functions import Lower
from graphene_cruddals import (
    RegistryGlobal,
    TypeRegistryForFieldEnum,
    TypesMutationEnum,
)

import graphene
from graphene_django_cruddals.utils.main import (
    exists_conversion_for_field,
    get_args,
    get_converted_field,
    get_field_name,
    get_field_values_from_instances,
    get_model_fields_for_input,
    get_model_fields_for_output,
    get_paths,
    nested_get,
    order_by_input_to_args,
    update_dict_with_model_instance,
    where_input_to_Q,
)


@pytest.fixture(scope="module")
def simple_model():
    class SimpleModel(models.Model):
        name = models.CharField(max_length=100)
        age = models.IntegerField()

    return SimpleModel


@pytest.fixture(scope="module")
def one_to_one_related_model(simple_model):
    class OneToOneRelatedModel(models.Model):
        simple1 = models.OneToOneField(
            simple_model,
            on_delete=models.CASCADE,
            related_name="related_one_to_one",
            related_query_name="related_one_to_one_query",
        )
        simple2 = models.OneToOneField(
            simple_model, on_delete=models.CASCADE, related_name="related_one_to_one_2"
        )
        simple3 = models.OneToOneField(
            simple_model,
            on_delete=models.CASCADE,
            related_query_name="related_one_to_one_query_3",
        )
        simple4 = models.OneToOneField(simple_model, on_delete=models.CASCADE)

    return OneToOneRelatedModel


@pytest.fixture(scope="module")
def many_to_one_related_model(simple_model):
    class ManyToOneRelatedModel(models.Model):
        simple1 = models.ForeignKey(
            simple_model,
            on_delete=models.CASCADE,
            related_name="related_many_to_one",
            related_query_name="related_many_to_one_query",
        )
        simple2 = models.ForeignKey(
            simple_model, on_delete=models.CASCADE, related_name="related_many_to_one_2"
        )
        simple3 = models.ForeignKey(
            simple_model,
            on_delete=models.CASCADE,
            related_query_name="related_many_to_one_query_3",
        )
        simple4 = models.ForeignKey(simple_model, on_delete=models.CASCADE)

    return ManyToOneRelatedModel


@pytest.fixture(scope="module")
def many_to_many_related_model(simple_model):
    class ManyToManyRelatedModel(models.Model):
        simple1 = models.ManyToManyField(
            simple_model,
            related_name="related_many_to_many",
            related_query_name="related_many_to_many_query",
        )
        simple2 = models.ManyToManyField(
            simple_model, related_name="related_many_to_many_2"
        )
        simple3 = models.ManyToManyField(
            simple_model, related_query_name="related_many_to_many_query_3"
        )
        simple4 = models.ManyToManyField(simple_model)

    return ManyToManyRelatedModel


# Direct relationships
# ManyToManyField
# ForeignKey
# OneToOneField

# Reverse relationships
# ManyToManyRel
# ManyToOneRel
# OneToOneRel

# Posibles types:
# For queryset
# For input

# Posibles cases:
# With related_query_name
# Without related_query_name
# With related_name
# Without related_name
# With both related_name and related_query_name
# Without both related_name and related_query_name


def test_get_field_name_for_queryset(
    simple_model,
    one_to_one_related_model,
    many_to_one_related_model,
    many_to_many_related_model,
):
    assert get_field_name(simple_model._meta.get_field("name"), True) == "name"
    assert get_field_name(simple_model._meta.get_field("age"), True) == "age"

    assert (
        get_field_name(one_to_one_related_model._meta.get_field("simple1"), True)
        == "simple1"
    )
    assert (
        get_field_name(one_to_one_related_model._meta.get_field("simple2"), True)
        == "simple2"
    )
    assert (
        get_field_name(one_to_one_related_model._meta.get_field("simple3"), True)
        == "simple3"
    )
    assert (
        get_field_name(one_to_one_related_model._meta.get_field("simple4"), True)
        == "simple4"
    )

    assert (
        get_field_name(many_to_one_related_model._meta.get_field("simple1"), True)
        == "simple1"
    )
    assert (
        get_field_name(many_to_one_related_model._meta.get_field("simple2"), True)
        == "simple2"
    )
    assert (
        get_field_name(many_to_one_related_model._meta.get_field("simple3"), True)
        == "simple3"
    )
    assert (
        get_field_name(many_to_one_related_model._meta.get_field("simple4"), True)
        == "simple4"
    )

    assert (
        get_field_name(many_to_many_related_model._meta.get_field("simple1"), True)
        == "simple1"
    )
    assert (
        get_field_name(many_to_many_related_model._meta.get_field("simple2"), True)
        == "simple2"
    )
    assert (
        get_field_name(many_to_many_related_model._meta.get_field("simple3"), True)
        == "simple3"
    )
    assert (
        get_field_name(many_to_many_related_model._meta.get_field("simple4"), True)
        == "simple4"
    )

    assert (
        get_field_name(
            one_to_one_related_model._meta.get_field("simple1").remote_field, True
        )
        == "related_one_to_one_query"
    )
    assert (
        get_field_name(
            one_to_one_related_model._meta.get_field("simple2").remote_field, True
        )
        == "related_one_to_one_2"
    )
    assert (
        get_field_name(
            one_to_one_related_model._meta.get_field("simple3").remote_field, True
        )
        == "related_one_to_one_query_3"
    )
    assert (
        get_field_name(
            one_to_one_related_model._meta.get_field("simple4").remote_field, True
        )
        == "onetoonerelatedmodel"
    )

    assert (
        get_field_name(
            many_to_one_related_model._meta.get_field("simple1").remote_field, True
        )
        == "related_many_to_one_query"
    )
    assert (
        get_field_name(
            many_to_one_related_model._meta.get_field("simple2").remote_field, True
        )
        == "related_many_to_one_2"
    )
    assert (
        get_field_name(
            many_to_one_related_model._meta.get_field("simple3").remote_field, True
        )
        == "related_many_to_one_query_3"
    )
    assert (
        get_field_name(
            many_to_one_related_model._meta.get_field("simple4").remote_field, True
        )
        == "manytoonerelatedmodel"
    )

    assert (
        get_field_name(
            many_to_many_related_model._meta.get_field("simple1").remote_field, True
        )
        == "related_many_to_many_query"
    )
    assert (
        get_field_name(
            many_to_many_related_model._meta.get_field("simple2").remote_field, True
        )
        == "related_many_to_many_2"
    )
    assert (
        get_field_name(
            many_to_many_related_model._meta.get_field("simple3").remote_field, True
        )
        == "related_many_to_many_query_3"
    )
    assert (
        get_field_name(
            many_to_many_related_model._meta.get_field("simple4").remote_field, True
        )
        == "manytomanyrelatedmodel"
    )


def test_get_field_name_for_input(
    simple_model,
    one_to_one_related_model,
    many_to_one_related_model,
    many_to_many_related_model,
):
    assert get_field_name(simple_model._meta.get_field("name"), False) == "name"
    assert get_field_name(simple_model._meta.get_field("age"), False) == "age"

    assert (
        get_field_name(one_to_one_related_model._meta.get_field("simple1"), False)
        == "simple1"
    )
    assert (
        get_field_name(one_to_one_related_model._meta.get_field("simple2"), False)
        == "simple2"
    )
    assert (
        get_field_name(one_to_one_related_model._meta.get_field("simple3"), False)
        == "simple3"
    )
    assert (
        get_field_name(one_to_one_related_model._meta.get_field("simple4"), False)
        == "simple4"
    )

    assert (
        get_field_name(many_to_one_related_model._meta.get_field("simple1"), False)
        == "simple1"
    )
    assert (
        get_field_name(many_to_one_related_model._meta.get_field("simple2"), False)
        == "simple2"
    )
    assert (
        get_field_name(many_to_one_related_model._meta.get_field("simple3"), False)
        == "simple3"
    )
    assert (
        get_field_name(many_to_one_related_model._meta.get_field("simple4"), False)
        == "simple4"
    )

    assert (
        get_field_name(many_to_many_related_model._meta.get_field("simple1"), False)
        == "simple1"
    )
    assert (
        get_field_name(many_to_many_related_model._meta.get_field("simple2"), False)
        == "simple2"
    )
    assert (
        get_field_name(many_to_many_related_model._meta.get_field("simple3"), False)
        == "simple3"
    )
    assert (
        get_field_name(many_to_many_related_model._meta.get_field("simple4"), False)
        == "simple4"
    )

    assert (
        get_field_name(
            one_to_one_related_model._meta.get_field("simple1").remote_field, False
        )
        == "related_one_to_one"
    )
    assert (
        get_field_name(
            one_to_one_related_model._meta.get_field("simple2").remote_field, False
        )
        == "related_one_to_one_2"
    )
    assert (
        get_field_name(
            one_to_one_related_model._meta.get_field("simple3").remote_field, False
        )
        == "onetoonerelatedmodel"
    )
    assert (
        get_field_name(
            one_to_one_related_model._meta.get_field("simple4").remote_field, False
        )
        == "onetoonerelatedmodel"
    )

    assert (
        get_field_name(
            many_to_one_related_model._meta.get_field("simple1").remote_field, False
        )
        == "related_many_to_one"
    )
    assert (
        get_field_name(
            many_to_one_related_model._meta.get_field("simple2").remote_field, False
        )
        == "related_many_to_one_2"
    )
    assert (
        get_field_name(
            many_to_one_related_model._meta.get_field("simple3").remote_field, False
        )
        == "manytoonerelatedmodel_set"
    )
    assert (
        get_field_name(
            many_to_one_related_model._meta.get_field("simple4").remote_field, False
        )
        == "manytoonerelatedmodel_set"
    )

    assert (
        get_field_name(
            many_to_many_related_model._meta.get_field("simple1").remote_field, False
        )
        == "related_many_to_many"
    )
    assert (
        get_field_name(
            many_to_many_related_model._meta.get_field("simple2").remote_field, False
        )
        == "related_many_to_many_2"
    )
    assert (
        get_field_name(
            many_to_many_related_model._meta.get_field("simple3").remote_field, False
        )
        == "manytomanyrelatedmodel_set"
    )
    assert (
        get_field_name(
            many_to_many_related_model._meta.get_field("simple4").remote_field, False
        )
        == "manytomanyrelatedmodel_set"
    )


@pytest.fixture(scope="module")
def simple_model2():
    class SimpleModel2(models.Model):
        name = models.CharField(max_length=100)
        age = models.IntegerField()
        description = models.TextField(editable=False)
        code = models.AutoField(primary_key=True)

    return SimpleModel2


@pytest.fixture(scope="module")
def complex_model2(simple_model2):
    class ComplexModel2(models.Model):
        simple = models.ForeignKey(simple_model2, on_delete=models.CASCADE)
        simple_m2m = models.ManyToManyField(simple_model2, related_name="m2m_related")
        simple_o2o = models.OneToOneField(simple_model2, on_delete=models.CASCADE)
        small_auto_field = models.SmallAutoField(primary_key=True)

    return ComplexModel2


def test_get_model_fields_for_input_create_update(simple_model2):
    fields = get_model_fields_for_input(
        simple_model2, TypesMutationEnum.CREATE_UPDATE.value
    )
    expected_fields = {
        "code": simple_model2._meta.pk,
        "name": simple_model2._meta.get_field("name"),
        "age": simple_model2._meta.get_field("age"),
    }
    assert fields == expected_fields


def test_get_model_fields_for_input_update(complex_model2):
    fields = get_model_fields_for_input(complex_model2, TypesMutationEnum.UPDATE.value)
    expected_fields = {
        "small_auto_field": complex_model2._meta.pk,
        "simple": complex_model2._meta.get_field("simple"),
        "simple_m2m": complex_model2._meta.get_field("simple_m2m"),
        "simple_o2o": complex_model2._meta.get_field("simple_o2o"),
    }
    assert fields == expected_fields


def test_get_model_fields_for_input_create(complex_model2):
    fields = get_model_fields_for_input(complex_model2, TypesMutationEnum.CREATE.value)
    expected_fields = {
        "simple": complex_model2._meta.get_field("simple"),
        "simple_m2m": complex_model2._meta.get_field("simple_m2m"),
        "simple_o2o": complex_model2._meta.get_field("simple_o2o"),
    }
    assert fields == expected_fields


def test_get_model_fields_for_input_without_type_mutation(simple_model2):
    fields = get_model_fields_for_input(simple_model2)
    expected_fields = {
        "code": simple_model2._meta.pk,
        "name": simple_model2._meta.get_field("name"),
        "age": simple_model2._meta.get_field("age"),
    }
    assert fields == expected_fields


def test_get_model_fields_for_input_with_uneditable_fields(simple_model2):
    fields = get_model_fields_for_input(
        simple_model2, TypesMutationEnum.CREATE_UPDATE.value
    )
    assert "description" not in fields


@pytest.fixture(scope="module")
def simple_model3():
    class SimpleModel3(models.Model):
        name = models.CharField(max_length=100)
        age = models.IntegerField()

    return SimpleModel3


@pytest.fixture(scope="module")
def simple_model3_without_relations():
    class SimpleModel3WithoutRelations(models.Model):
        name = models.CharField(max_length=100)
        age = models.IntegerField()

    return SimpleModel3WithoutRelations


@pytest.fixture(scope="module")
def complex_model3(simple_model3):
    class ComplexModel3(models.Model):
        simple = models.ForeignKey(simple_model3, on_delete=models.CASCADE)
        simple_m2m = models.ManyToManyField(simple_model3, related_name="m2m_related")
        simple_o2o = models.OneToOneField(simple_model3, on_delete=models.CASCADE)
        simple_without_inverse = models.ForeignKey(
            simple_model3, on_delete=models.CASCADE, related_name="+"
        )
        generic_relation = GenericRelation(simple_model3)

    return ComplexModel3


def test_get_model_fields_for_output_without_for_object_type(
    simple_model3_without_relations,
):
    fields = get_model_fields_for_output(simple_model3_without_relations, False)
    expected_fields = {
        "id": simple_model3_without_relations._meta.pk,
        "name": simple_model3_without_relations._meta.get_field("name"),
        "age": simple_model3_without_relations._meta.get_field("age"),
    }
    assert fields == expected_fields


def test_get_model_fields_for_output_with_for_object_type(
    simple_model3_without_relations,
):
    fields = get_model_fields_for_output(simple_model3_without_relations, True)
    expected_fields = {
        "id": simple_model3_without_relations._meta.pk,
        "name": simple_model3_without_relations._meta.get_field("name"),
        "age": simple_model3_without_relations._meta.get_field("age"),
    }
    assert fields == expected_fields


def test_get_model_fields_for_output_with_many_to_many(complex_model3):
    fields = get_model_fields_for_output(complex_model3, False)
    expected_fields = {
        "id": complex_model3._meta.pk,
        "simple": complex_model3._meta.get_field("simple"),
        "simple_m2m": complex_model3._meta.get_field("simple_m2m"),
        "simple_o2o": complex_model3._meta.get_field("simple_o2o"),
        "simple_without_inverse": complex_model3._meta.get_field(
            "simple_without_inverse"
        ),
        "generic_relation": complex_model3._meta.get_field("generic_relation"),
    }
    assert fields == expected_fields


def test_get_model_fields_for_output_with_paginated_fields(complex_model3):
    fields = get_model_fields_for_output(complex_model3, True)
    expected_fields = {
        "id": complex_model3._meta.pk,
        "simple": complex_model3._meta.get_field("simple"),
        "simple_o2o": complex_model3._meta.get_field("simple_o2o"),
        "simple_without_inverse": complex_model3._meta.get_field(
            "simple_without_inverse"
        ),
        "paginated_simple_m2m": complex_model3._meta.get_field("simple_m2m"),
        "paginated_generic_relation": complex_model3._meta.get_field(
            "generic_relation"
        ),
    }
    assert fields == expected_fields


def test_nested_get():
    d = {"a": {"b": {"c": "d"}}}
    assert nested_get(d, ["a", "b", "c"]) == "d"
    assert nested_get(d, ["a", "b"]) == {"c": "d"}
    assert nested_get(d, ["a"]) == {"b": {"c": "d"}}
    assert nested_get(d, ["a", "x"]) is None
    assert nested_get({}, ["a", "b", "c"]) is None


def test_get_paths():
    d = {"a": {"b": {"c": "d"}}}
    paths = list(get_paths(d))
    expected_paths = [[], ["a"], ["a", "b"], ["a", "b", "c"]]
    assert paths == expected_paths


def test_get_args():
    where = {"a": {"b": {"c__equals": "d"}}, "e": {"f__equals": "g"}, "h": "i"}
    args = get_args(where)
    expected_args = {"a__b__c__exact": "d", "e__f__exact": "g", "h": "i"}
    assert args == expected_args


def test_where_input_to_Q():
    where = {
        "a": {"b__equals": "c"},
        "OR": [{"d__equals": "e"}, {"f__equals": "g"}],
        "AND": [{"h__equals": "i"}, {"j__equals": "k"}],
        "NOT": {"l__equals": "m"},
    }
    q = where_input_to_Q(where)
    e = "(AND: (OR: ('a__b__exact', 'c'), (AND: ('d__exact', 'e')), (AND: ('f__exact', 'g'))), (AND: ('h__exact', 'i')), (AND: ('j__exact', 'k')), (NOT (AND: (AND: ('l__exact', 'm')))))"
    assert str(q) == e


def test_order_by_input_to_args():
    order_by = [{"a": "ASC"}, {"b": "DESC"}, {"c": "IASC"}, {"d": "IDESC"}]
    args = order_by_input_to_args(order_by)
    expected_args = ["a", "-b", Lower("c").asc(), Lower("d").desc()]
    assert args == expected_args


@pytest.fixture
def registry():
    return RegistryGlobal()


def test_exists_conversion_for_field(registry: RegistryGlobal):
    # Create a Django field
    field = models.CharField(max_length=100)

    # Register a conversion for the field
    registry.register_field(
        field, TypeRegistryForFieldEnum.OUTPUT.value, graphene.String()
    )

    # Check if the conversion exists
    assert (
        exists_conversion_for_field(
            field, registry, TypeRegistryForFieldEnum.OUTPUT.value
        )
        is True
    )

    # Check if the conversion does not exist for a different type
    assert (
        exists_conversion_for_field(
            field, registry, TypeRegistryForFieldEnum.INPUT_FOR_SEARCH.value
        )
        is False
    )


def test_exists_conversion_for_field_with_no_conversion(registry: RegistryGlobal):
    field = models.CharField(max_length=100)

    assert (
        exists_conversion_for_field(
            field, registry, TypeRegistryForFieldEnum.OUTPUT.value
        )
        is False
    )
    assert (
        exists_conversion_for_field(
            field, registry, TypeRegistryForFieldEnum.INPUT_FOR_SEARCH.value
        )
        is False
    )


def test_get_converted_field(registry: RegistryGlobal):
    field = models.CharField(max_length=100)
    converted_field = graphene.String()

    registry.register_field(
        field, TypeRegistryForFieldEnum.OUTPUT.value, converted_field
    )

    assert (
        get_converted_field(field, registry, TypeRegistryForFieldEnum.OUTPUT.value)
        == converted_field
    )


class SimpleModel4(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()


class ObjToUpdate:
    def __init__(self, id):
        self.id = id


@pytest.fixture
def simple_model_instance():
    return SimpleModel4(id=1, name="John", age=30)


def test_update_dict_with_instance(simple_model_instance):
    obj_to_update = {"id": 1}
    with patch.object(SimpleModel4, "objects") as mock_manager:
        mock_manager.get.return_value = simple_model_instance
        result = update_dict_with_model_instance(obj_to_update, instance=SimpleModel4)
        assert result == {"id": 1, "name": "John", "age": 30}


def test_update_dict_with_model(simple_model_instance):
    obj_to_update = {"id": 1}
    with patch.object(SimpleModel4, "objects") as mock_manager:
        mock_manager.get.return_value = simple_model_instance
        result = update_dict_with_model_instance(obj_to_update, model=SimpleModel4)
        assert result == {"id": 1, "name": "John", "age": 30}


def test_update_dict_without_instance_or_model():
    obj_to_update = {"id": 1}
    with pytest.raises(
        ValueError,
        match="Either 'instance' or 'model' parameters must be provided to update the dictionary with the model instance.",
    ):
        update_dict_with_model_instance(obj_to_update)


def test_update_dict_with_instance_object(simple_model_instance):
    obj_to_update = ObjToUpdate(id=1)
    with patch.object(SimpleModel4, "objects") as mock_manager:
        mock_manager.get.return_value = simple_model_instance
        result = update_dict_with_model_instance(obj_to_update, instance=SimpleModel4)
        assert result.id == 1
        assert result.name == "John"
        assert result.age == 30


# Definición de modelos de prueba
class SimpleModel5:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class AnotherModel:
    def __init__(self, title):
        self.title = title


# Pruebas unitarias
def test_get_field_values_valid_field():
    instances = [SimpleModel5("Alice", 30), SimpleModel5("Bob", 25)]
    result = get_field_values_from_instances(instances, "name")
    assert result == ["Alice", "Bob"]


def test_get_field_values_non_existent_field():
    instances = [SimpleModel5("Alice", 30), SimpleModel5("Bob", 25)]
    with pytest.raises(
        ValueError, match="The field 'title' does not exist in the model SimpleModel5"
    ):
        get_field_values_from_instances(instances, "title")


def test_get_field_values_mixed_models():
    instances = [SimpleModel5("Alice", 30), AnotherModel("Some Title")]
    with pytest.raises(
        ValueError, match="The field 'name' does not exist in the model AnotherModel"
    ):
        get_field_values_from_instances(instances, "name")


def test_get_field_values_empty_instance_list():
    instances = []
    result = get_field_values_from_instances(instances, "name")
    assert result == []


def test_get_field_values_partial_missing_field():
    instances = [
        SimpleModel5("Alice", 30),
        SimpleModel5("Bob", 25),
        AnotherModel("Some Title"),
    ]
    with pytest.raises(
        ValueError, match="The field 'age' does not exist in the model AnotherModel"
    ):
        get_field_values_from_instances(instances, "age")
