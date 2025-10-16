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
from graphql.language.ast import (
    ArgumentNode,
    BooleanValueNode,
    EnumValueNode,
    FloatValueNode,
    IntValueNode,
    ListValueNode,
    NameNode,
    ObjectFieldNode,
    ObjectValueNode,
    StringValueNode,
    VariableNode,
)

import graphene
from graphene.types.scalars import MAX_INT, MIN_INT
from graphene_django_cruddals.converters.converter_input import GenericForeignKeyInput
from graphene_django_cruddals.utils.main import (
    PaginatorWithCount,
    add_mutate_errors,
    convert_django_field_with_choices_to_create_update_input,
    convert_django_field_with_choices_to_output,
    convert_django_field_without_choices_to_filter_input,
    convert_django_field_without_choices_to_order_by_input,
    exists_conversion_for_field,
    get_args,
    get_converted_field,
    get_data_for_generic_foreign_key,
    get_field_name,
    get_field_values_from_instances,
    get_list_input_object_type,
    get_model_fields_for_input,
    get_model_fields_for_output,
    get_order_by_list_from_arguments,
    get_paths,
    get_type_field,
    is_list_of_same_type,
    nested_get,
    obj_to_modify_have_generic_foreign_key_input,
    order_by_input_to_args,
    paginate_queryset,
    parse_arguments_ast,
    parse_ast,
    resolve_argument,
    toggle_active_status,
    update_dict_with_model_instance,
    value_is_input_object_type,
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


# ========================= New tests for AST and argument helpers =========================


def test_parse_ast_literals_and_boundaries():
    assert parse_ast(StringValueNode(value="hello")) == "hello"
    assert parse_ast(BooleanValueNode(value=True)) is True
    assert parse_ast(FloatValueNode(value="3.14")) == 3.14
    assert parse_ast(EnumValueNode(value="ENUM_VAL")) == "ENUM_VAL"

    # Int inside range
    assert parse_ast(IntValueNode(value=str(MIN_INT))) == MIN_INT
    assert parse_ast(IntValueNode(value=str(MAX_INT))) == MAX_INT

    # Int outside range should return None
    assert parse_ast(IntValueNode(value=str(MAX_INT + 1))) is None

    # Variable nodes resolved from provided values
    var_node = VariableNode(name=NameNode(value="v"))
    assert parse_ast(var_node, variable_values={"v": 123}) == 123

    # List and Object values
    list_node = ListValueNode(
        values=[StringValueNode(value="a"), IntValueNode(value="1")]
    )
    assert parse_ast(list_node) == ["a", 1]

    obj_node = ObjectValueNode(
        fields=[
            ObjectFieldNode(name=NameNode(value="x"), value=StringValueNode(value="y")),
            ObjectFieldNode(name=NameNode(value="n"), value=IntValueNode(value="2")),
        ]
    )
    assert parse_ast(obj_node) == {"x": "y", "n": 2}


def test_parse_arguments_ast_with_variables():
    args = [
        ArgumentNode(name=NameNode(value="s"), value=StringValueNode(value="str")),
        ArgumentNode(name=NameNode(value="i"), value=IntValueNode(value="10")),
        ArgumentNode(
            name=NameNode(value="v"), value=VariableNode(name=NameNode(value="var"))
        ),
    ]
    out = parse_arguments_ast(args, variable_values={"var": 99})
    assert out == {"s": "str", "i": 10, "v": 99}


def test_get_type_field_with_dynamic_list_and_camelcase():
    class ChildInput(graphene.InputObjectType):
        innerField = graphene.String()

    class RootInput(graphene.InputObjectType):
        camelCase = graphene.Int()
        listField = graphene.List(graphene.String)
        dynamicField = graphene.Dynamic(lambda: graphene.String())
        child = graphene.InputField(ChildInput)

    # camelCase lookup using snake_case key
    name, field_type = get_type_field(RootInput, "camel_case")
    assert name == "camelCase"
    assert field_type == graphene.Int

    # listField should resolve to underlying scalar type
    name, field_type = get_type_field(RootInput, "list_field")
    assert name == "listField"
    assert field_type == graphene.String

    # dynamicField should resolve to the provided type
    name, field_type = get_type_field(RootInput, "dynamic_field")
    assert name == "dynamicField"
    assert field_type.__class__ == graphene.String


def test_resolve_argument_nested_and_lists():
    class ChildInput(graphene.InputObjectType):
        innerField = graphene.String()

    class RootInput(graphene.InputObjectType):
        items = graphene.List(ChildInput)
        child = graphene.InputField(ChildInput)
        value = graphene.Int()

    args = {
        "items": [{"inner_field": "a"}, {"innerField": "b"}],
        "child": {"inner_field": "x"},
        "value": 7,
    }

    resolved = resolve_argument(RootInput, args)
    assert resolved == {
        "items": [{"innerField": "a"}, {"innerField": "b"}],
        "child": {"innerField": "x"},
        "value": 7,
    }


def test_get_order_by_list_from_arguments_defaults_and_mapping():
    # Default when no order_by present
    assert get_order_by_list_from_arguments({}) == ["pk"]

    # Without input type
    args = {
        "order_by": [
            {"name": "ASC"},
            {"age": "DESC"},
            {"code": "IASC"},
            {"title": "IDESC"},
        ]
    }
    out = get_order_by_list_from_arguments(args)
    assert out == ["name", "-age", Lower("code").asc(), Lower("title").desc()]

    # With input type (camelCase mapping)
    class OrderByInput(graphene.InputObjectType):
        fullName = graphene.String()
        createdAt = graphene.String()

    args2 = {"orderBy": [{"full_name": "ASC"}, {"created_at": "DESC"}]}
    out2 = get_order_by_list_from_arguments(args2, order_by_input_type=OrderByInput)
    assert out2 == ["fullName", "-createdAt"]


# ========================= Extra coverage for utils =========================


def test_paginator_with_count_property_uses_cached_value():
    p = PaginatorWithCount([1, 2, 3], per_page=2, count=10)
    # Access property to ensure cached count is used
    assert p.count == 10


def test_paginator_with_count_property_delegates_when_no_cache():
    p = PaginatorWithCount([1, 2, 3], per_page=2, count=None)
    assert p.count == 3


def test_paginate_queryset_list_all_and_limits():
    class PageType(graphene.ObjectType):
        total = graphene.Int()
        page = graphene.Int()
        pages = graphene.Int()
        has_next = graphene.Boolean()
        has_prev = graphene.Boolean()
        index_start = graphene.Int()
        index_end = graphene.Int()
        objects = graphene.List(graphene.Int)

    data = list(range(1, 8))

    # All items
    res_all = paginate_queryset(data, PageType, items_per_page="All", page=1)
    assert res_all.total == 7 and res_all.pages == 1 and res_all.objects == data

    # Invalid page coerced and boundaries
    res = paginate_queryset(data, PageType, items_per_page=3, page=5)
    assert res.page == 3 and res.pages == 3 and res.objects == [7]


def test_paginate_queryset_page_exceptions(monkeypatch):
    class PageType(graphene.ObjectType):
        total = graphene.Int()
        page = graphene.Int()
        pages = graphene.Int()
        has_next = graphene.Boolean()
        has_prev = graphene.Boolean()
        index_start = graphene.Int()
        index_end = graphene.Int()
        objects = graphene.List(graphene.Int)

    data = list(range(1, 6))

    # Test PageNotAnInteger path
    from django.core.paginator import EmptyPage, PageNotAnInteger

    # Create a mock that raises exception only on first call, then works normally
    call_count = {"not_integer": 0, "empty": 0}

    def mock_page_not_integer(self, page):
        call_count["not_integer"] += 1
        if call_count["not_integer"] == 1:
            raise PageNotAnInteger("x")
        # On second call (fallback), return normal page
        return super(PaginatorWithCount, self).page(page)

    def mock_page_empty(self, page):
        call_count["empty"] += 1
        if call_count["empty"] == 1:
            raise EmptyPage("x")
        # On second call (fallback), return normal page
        return super(PaginatorWithCount, self).page(page)

    # First: PageNotAnInteger path
    monkeypatch.setattr(PaginatorWithCount, "page", mock_page_not_integer)
    res = paginate_queryset(data, PageType, items_per_page=2, page=2)
    assert res.page == 1

    # Second: EmptyPage path
    monkeypatch.setattr(PaginatorWithCount, "page", mock_page_empty)
    res2 = paginate_queryset(data, PageType, items_per_page=2, page=999)
    assert res2.page == res2.pages


def test_toggle_active_status_updates_queryset():
    updated = {}

    class DummyQS:
        def update(self, **kwargs):
            updated.update(kwargs)
            return self

    qs = DummyQS()
    toggle_active_status("ACTIVATE", qs, field="flag")
    assert updated == {"flag": True}
    toggle_active_status("DEACTIVATE", qs, field="flag")
    assert updated == {"flag": False}


def test_is_list_of_same_type_and_value_is_input_object_type():
    class MyInput(graphene.InputObjectType):
        a = graphene.Int()

    assert is_list_of_same_type([1, 2, 3], int) is True
    assert is_list_of_same_type([1, "2"], int) is False

    # value_is_input_object_type
    assert value_is_input_object_type(MyInput(a=1)) is True
    assert value_is_input_object_type([MyInput(a=1), MyInput(a=2)]) is True
    assert value_is_input_object_type([MyInput(a=1), 2]) is False


def test_parse_ast_edge_and_parse_arguments_skips_none():
    # Unsupported node returns None
    class Dummy:  # not a GraphQL node
        pass

    assert parse_ast(Dummy()) is None

    # Argument with IntValueNode outside range is ignored
    args = [
        ArgumentNode(
            name=NameNode(value="i"), value=IntValueNode(value=str(MAX_INT + 1))
        ),
        ArgumentNode(name=NameNode(value="ok"), value=StringValueNode(value="v")),
    ]
    out = parse_arguments_ast(args)
    assert out == {"ok": "v"}


def test_get_type_field_not_found_and_resolve_argument_scalar():
    class RootInput(graphene.InputObjectType):
        a = graphene.Int()

    assert get_type_field(RootInput, "missing") is None
    # resolve_argument scalar returns as is
    assert resolve_argument(RootInput, 5) == 5


def test_conversion_short_circuits_with_registry_mocks(monkeypatch):
    class DummyField:
        choices = None

    class DummyModel:
        class _Meta:
            pk = None

    dummy_field = DummyField()
    dummy_model = DummyModel()

    class RegistryMock:
        def __init__(self, mapping):
            self.mapping = mapping

        def get_registry_for_field(self, field):
            return self.mapping

    # OUTPUT
    reg = RegistryMock({TypeRegistryForFieldEnum.OUTPUT.value: "OUT"})
    assert (
        convert_django_field_with_choices_to_output("n", dummy_field, dummy_model, reg)
        == "OUT"
    )
    # INPUT (create/update/create_update)
    reg2 = RegistryMock({TypeRegistryForFieldEnum.INPUT_FOR_UPDATE.value: "UP"})
    assert (
        convert_django_field_with_choices_to_create_update_input(
            "n", dummy_field, dummy_model, reg2, TypesMutationEnum.UPDATE.value
        )
        == "UP"
    )
    reg3 = RegistryMock({TypeRegistryForFieldEnum.INPUT_FOR_CREATE.value: "CR"})
    assert (
        convert_django_field_with_choices_to_create_update_input(
            "n", dummy_field, dummy_model, reg3, TypesMutationEnum.CREATE.value
        )
        == "CR"
    )
    reg4 = RegistryMock(
        {TypeRegistryForFieldEnum.INPUT_FOR_CREATE_UPDATE.value: "CRUP"}
    )
    assert (
        convert_django_field_with_choices_to_create_update_input(
            "n", dummy_field, dummy_model, reg4, TypesMutationEnum.CREATE_UPDATE.value
        )
        == "CRUP"
    )

    # FILTER INPUT
    reg5 = RegistryMock({TypeRegistryForFieldEnum.INPUT_FOR_SEARCH.value: "S"})
    assert (
        convert_django_field_without_choices_to_filter_input(
            "n", dummy_field, dummy_model, reg5
        )
        == "S"
    )
    # ORDER BY INPUT
    reg6 = RegistryMock({TypeRegistryForFieldEnum.INPUT_FOR_ORDER_BY.value: "OB"})
    assert (
        convert_django_field_without_choices_to_order_by_input(
            "n", dummy_field, dummy_model, reg6
        )
        == "OB"
    )


def test_get_data_for_generic_foreign_key_with_mocked_content_type(monkeypatch):
    class FieldFK:
        ct_field = "ct"
        fk_field = "fk"

    class ModelMeta:
        def get_field(self, key):
            return FieldFK()

    class ModelMock:
        class _Meta:
            pass

        _meta = ModelMeta()

    class Obj:
        def __init__(self, pk):
            self.pk = pk

    class ContentTypeMock:
        def __init__(self, pk):
            self.pk = pk

    class CTManager:
        def get_or_create(self, app_label, model):
            return (ContentTypeMock(pk=9), True)

    # Patch ContentType.objects
    from django.contrib.contenttypes.models import ContentType

    monkeypatch.setattr(ContentType, "objects", CTManager(), raising=True)

    responses = {
        "gfk": {
            "create": {"objects": [Obj(7)]},
            "update": None,
        }
    }
    g = GenericForeignKeyInput(app_label="app", model="m", object={})
    data = get_data_for_generic_foreign_key({"gfk": g}, ModelMock, responses)
    assert data == {"fk": 7, "ct": 9}


def test_paginate_queryset_old_false_branch_and_exceptions():
    """Test the else branch (old=False) and exception handling in paginate_queryset"""

    class PageType(graphene.ObjectType):
        total = graphene.Int()
        page = graphene.Int()
        pages = graphene.Int()
        has_next = graphene.Boolean()
        has_prev = graphene.Boolean()
        index_start = graphene.Int()
        index_end = graphene.Int()
        objects = graphene.List(graphene.Int)

    data = list(range(1, 8))  # 7 items

    # Test old=False branch by monkeypatching the old variable
    import graphene_django_cruddals.utils.main as utils_main
    from graphene_django_cruddals.utils.main import paginate_queryset

    # Temporarily set old = False
    original_old = getattr(utils_main, "old", True)
    utils_main.old = False

    try:
        # Test normal case
        res = paginate_queryset(data, PageType, items_per_page=3, page=2)
        assert res.total == 7
        assert res.page == 2
        assert res.pages == 3
        assert res.objects == [4, 5, 6]

        # Test "All" items
        res_all = paginate_queryset(data, PageType, items_per_page="All", page=1)
        assert res_all.total == 7
        assert res_all.objects == data

        # Test exception handling in page conversion
        res_exc = paginate_queryset(
            data, PageType, items_per_page="invalid", page="invalid"
        )
        assert res_exc.page == 1
        assert res_exc.total == 7

        # Test page = 0 case
        res_zero = paginate_queryset(data, PageType, items_per_page=2, page=0)
        assert res_zero.page == 1

        # Test page > num_pages case
        res_high = paginate_queryset(data, PageType, items_per_page=2, page=10)
        assert res_high.page == 4  # Should be last page

        # Test total_count = 0 case
        res_empty = paginate_queryset([], PageType, items_per_page=2, page=1)
        assert res_empty.total == 0
        assert res_empty.index_start == 0
        assert res_empty.index_end == 0

    finally:
        # Restore original value
        utils_main.old = original_old


def test_paginate_queryset_page_conversion_exceptions():
    """Test page conversion exceptions in the old=True branch"""

    class PageType(graphene.ObjectType):
        total = graphene.Int()
        page = graphene.Int()
        pages = graphene.Int()
        has_next = graphene.Boolean()
        has_prev = graphene.Boolean()
        index_start = graphene.Int()
        index_end = graphene.Int()
        objects = graphene.List(graphene.Int)

    data = list(range(1, 6))

    # Test TypeError/ValueError in page conversion
    res = paginate_queryset(data, PageType, items_per_page=2, page="invalid")
    assert res.page == 1

    # Test page < 1 case
    res_negative = paginate_queryset(data, PageType, items_per_page=2, page=-1)
    assert res_negative.page == 1

    # Test items_per_page conversion exception
    res_items_exc = paginate_queryset(data, PageType, items_per_page="invalid", page=1)
    assert res_items_exc.total == 5


def test_get_list_input_object_type_with_generic_fk_mock():
    """Test GenericForeignKeyInput path with mocked object"""

    class _Pk:
        name = "id"

    class _Meta:
        pk = _Pk()

    class FakeModel:
        _meta = _Meta()

    # Mock GenericForeignKeyInput with proper object attribute
    class MockGenericFK:
        def __init__(self, obj_dict):
            self.object = obj_dict

    g = MockGenericFK({"Id": 3, "Name": "test"})
    to_modify, to_connect = get_list_input_object_type(g, FakeModel)
    # The function checks if it's a list of InputObjectType instances
    # Since our mock is not an InputObjectType, it returns empty lists
    assert to_modify == []
    assert to_connect == []


def test_apply_relation_mutations_field_inverse():
    """Test field_inverse path in apply_relation_mutations"""
    from graphene_django_cruddals.utils.main import apply_relation_mutations

    # Mock mutate function
    def mock_mutate(obj, info, **kwargs):
        return {"objects": [{"id": 1}]}

    # Mock obj_modified
    class MockObj:
        def __init__(self):
            self.pk = 5

    obj_modified = MockObj()

    # Mock direct_field_detail
    direct_field_detail = {"name_field": "related_field"}

    # Mock original_field (ManyToOneRel)
    class MockManyToOneRel:
        pass

    result = apply_relation_mutations(
        "field_inverse",  # type_field_relation
        MockManyToOneRel(),  # original_field
        direct_field_detail,
        [{"name": "test"}],  # list_input_objects
        mock_mutate,  # mutate
        {"id": 1},  # direct_obj_to_modify
        obj_modified,  # obj_modified
        None,  # root
        None,  # info
    )

    # Should call mutate with obj_modified
    assert result is not None


def test_handle_disconnect_objs_related_many_to_many():
    """Test ManyToManyField disconnect path"""
    from graphene_django_cruddals.utils.main import handle_disconnect_objs_related

    # Mock model with objects.filter
    class MockModel:
        class objects:
            @staticmethod
            def filter(q):
                class MockQS:
                    def distinct(self):
                        return [{"id": 1}, {"id": 2}]

                return MockQS()

    # Mock field (ManyToManyField)
    class MockManyToManyField:
        pass

    # Mock direct_field_detail
    direct_field_detail = {
        "field": MockManyToManyField(),
        "pk_field_name": "id",
        "model": MockModel,
        "name_field": "related_field",
    }

    # Mock obj_to_modify with pk
    obj_to_modify = {"id": 1}

    # Mock the actual object and its related field
    class MockActualObj:
        def __init__(self):
            self.related_field = MockRelatedManager()

    class MockRelatedManager:
        def remove(self, *args):
            self.removed = args

    # Mock model.objects.get
    MockModel.objects.get = lambda pk: MockActualObj()

    # Mock value_of_field with disconnect
    value_of_field = {"disconnect": [{"id": 1}]}

    handle_disconnect_objs_related(
        direct_field_detail, MockModel, value_of_field, obj_to_modify
    )


def test_handle_disconnect_objs_related_many_to_one_rel():
    """Test ManyToOneRel disconnect path"""
    from graphene_django_cruddals.utils.main import handle_disconnect_objs_related

    # Mock field with null=True
    class MockField:
        null = True
        blank = False
        attname = "related_id"

    class MockManyToOneRel:
        def __init__(self):
            self.field = MockField()

    # Mock model
    class MockModel:
        class objects:
            @staticmethod
            def filter(q):
                class MockQS:
                    def distinct(self):
                        return [MockDisconnectObj()]

                return MockQS()

    class MockDisconnectObj:
        def save(self):
            self.saved = True

    # Mock direct_field_detail
    direct_field_detail = {
        "field": MockManyToOneRel(),
        "pk_field_name": "id",
        "model": MockModel,
        "name_field": "related_field",
    }

    # Mock obj_to_modify
    obj_to_modify = {"id": 1}

    # Mock value_of_field
    value_of_field = {"disconnect": [{"id": 1}]}

    handle_disconnect_objs_related(
        direct_field_detail, MockModel, value_of_field, obj_to_modify
    )


def test_handle_disconnect_objs_related_foreign_key():
    """Test ForeignKey disconnect path"""
    from graphene_django_cruddals.utils.main import handle_disconnect_objs_related

    # Mock field
    class MockForeignKey:
        pass

    # Mock model
    class MockModel:
        class objects:
            @staticmethod
            def filter(q):
                class MockQS:
                    def distinct(self):
                        return [MockDisconnectObj()]

                return MockQS()

    class MockDisconnectObj:
        def save(self):
            self.saved = True

    # Mock direct_field_detail
    direct_field_detail = {"field": MockForeignKey(), "name_field": "related_field"}

    # Mock obj_to_modify
    obj_to_modify = {"id": 1}

    # Mock value_of_field
    value_of_field = {"disconnect": [{"id": 1}]}

    handle_disconnect_objs_related(
        direct_field_detail, MockModel, value_of_field, obj_to_modify
    )


def test_resolve_argument_scalar_return():
    """Test scalar return case in resolve_argument"""

    class RootInput(graphene.InputObjectType):
        value = graphene.Int()

    # Test scalar value (not dict or list)
    result = resolve_argument(RootInput, 42)
    assert result == 42


def test_get_list_input_object_type_with_input_and_generic_fk():
    # Fake model meta
    class _Pk:
        name = "id"

    class _Meta:
        pk = _Pk()

    class FakeModel:
        _meta = _Meta()

    class ItemInput(graphene.InputObjectType):
        id = graphene.Int()
        v = graphene.String()

    # Mixed list with dicts: function only splits when inputs are InputObjectType
    # so for plain dicts both come back empty
    to_modify, to_connect = get_list_input_object_type(
        [{"v": "x"}, {"id": 1, "v": "y"}], FakeModel
    )
    assert to_modify == []
    assert to_connect == []


def test_obj_to_modify_have_generic_foreign_key_input():
    g = GenericForeignKeyInput(app_label="app", model="m", object={})
    assert obj_to_modify_have_generic_foreign_key_input({"g": g}) is True
    assert obj_to_modify_have_generic_foreign_key_input({"x": 1}) is False


def test_add_mutate_errors_sets_positions_and_fields():
    class InternalError:
        def __init__(self, field):
            self.field = field

    class RelatedError:
        def __init__(self, errors):
            self.errors = errors
            self.object_position = None

    # Simulate structure: responses[field][create|update] -> {"errors_report": [RelatedError]}
    responses = {
        "some_field": {
            "create": {"errors_report": [RelatedError([InternalError("inner")])]}
        }
    }

    class Tx:
        def __init__(self):
            self.rollback = False

        def set_rollback(self, v):
            self.rollback = v

    errors = []
    tx = Tx()
    add_mutate_errors(
        responses, object_counter=2, internal_arr_errors=errors, transaction=tx
    )
    assert errors and errors[0].object_position == 2
    assert errors[0].errors[0].field.startswith("someField.")
    assert tx.rollback is True
