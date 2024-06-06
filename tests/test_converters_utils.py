from collections import OrderedDict
from unittest.mock import MagicMock, Mock

import pytest
from django.db import models
from django.db.models import NOT_PROVIDED
from django.utils.translation import gettext_lazy as _
from graphql import Undefined
from promise import Promise

import graphene
from graphene_django_cruddals.converters.utils import (
    BlankValueField,
    convert_choice_name,
    get_choices,
    get_django_field_default,
    get_django_field_description,
    get_django_field_is_required,
    get_function_for_type,
    get_unbound_function,
    resolve_for_relation_field,
    to_const,
)


# Tests for get_django_field_description
def test_get_django_field_description_with_help_text():
    field = MagicMock(spec=models.Field)
    field.help_text = "Some helpful text"
    assert get_django_field_description(field) == "Some helpful text"


def test_get_django_field_description_without_help_text():
    field = MagicMock(spec=models.Field)
    field.help_text = ""
    assert get_django_field_description(field) is None


def test_get_django_field_description_no_help_text_attr():
    field = MagicMock(spec=models.Field)
    del field.help_text
    assert get_django_field_description(field) is None


def test_get_django_field_description_help_text_is_none():
    field = MagicMock(spec=models.Field)
    field.help_text = None
    assert get_django_field_description(field) is None


def test_get_django_field_description_help_text_is_number():
    field = MagicMock(spec=models.Field)
    field.help_text = 123
    assert get_django_field_description(field) == "123"


# Tests for get_django_field_is_required
def test_get_django_field_is_required_with_blank_default_not_provided():
    field = MagicMock(spec=models.Field)
    field.blank = False
    field.default = NOT_PROVIDED
    assert get_django_field_is_required(field) is True


def test_get_django_field_is_required_with_blank_default_provided():
    field = MagicMock(spec=models.Field)
    field.blank = False
    field.default = "some_default"
    assert get_django_field_is_required(field) is False


def test_get_django_field_is_required_with_blank():
    field = MagicMock(spec=models.Field)
    field.blank = True
    field.default = NOT_PROVIDED
    assert get_django_field_is_required(field) is False


def test_get_django_field_is_required_with_blank_not_default():
    field = MagicMock(spec=models.Field)
    field.blank = True
    assert get_django_field_is_required(field) is False


def test_get_django_field_is_required_with_null_default_not_provided():
    field = MagicMock(spec=models.Field)
    del field.blank
    field.null = False
    field.default = NOT_PROVIDED
    assert get_django_field_is_required(field) is True


def test_get_django_field_is_required_attribute_error():
    field = MagicMock(spec=models.Field)
    del field.blank
    del field.null
    assert get_django_field_is_required(field) is False


# Tests for get_django_field_default
def test_get_django_field_default_not_provided():
    field = MagicMock(spec=models.Field)
    field.default = NOT_PROVIDED
    assert get_django_field_default(field) is Undefined


def test_get_django_field_default_callable():
    field = MagicMock(spec=models.Field)
    field.default = lambda: "default"
    assert get_django_field_default(field) is Undefined


def test_get_django_field_default_promise():
    field = MagicMock(spec=models.Field)
    field.default = MagicMock(spec=Promise)
    assert get_django_field_default(field) is Undefined


def test_get_django_field_default_choices_meta():
    class YearInSchool(models.TextChoices):
        FRESHMAN = "FR", _("Freshman")
        SOPHOMORE = "SO", _("Sophomore")
        JUNIOR = "JR", _("Junior")
        SENIOR = "SR", _("Senior")
        GRADUATE = "GR", _("Graduate")

    field = MagicMock(spec=models.Field)
    field.default = YearInSchool.FRESHMAN
    assert get_django_field_default(field) == "FR"


def test_get_django_field_default_normal_value():
    field = MagicMock(spec=models.Field)
    field.default = "some_default"
    assert get_django_field_default(field) == "some_default"


# Tests for BlankValueField
@pytest.fixture
def field_instance():
    return BlankValueField(graphene.String)


def test_wrap_resolve_with_non_empty_string(field_instance):
    parent_resolver = MagicMock(return_value="non-empty string")
    wrapped_resolver = field_instance.wrap_resolve(parent_resolver)
    assert wrapped_resolver(None) == "non-empty string"
    parent_resolver.assert_called_once()


def test_wrap_resolve_with_empty_string(field_instance):
    parent_resolver = MagicMock(return_value="")
    wrapped_resolver = field_instance.wrap_resolve(parent_resolver)
    assert wrapped_resolver(None) is None
    parent_resolver.assert_called_once()


def test_wrap_resolve_with_none(field_instance):
    parent_resolver = MagicMock(return_value=None)
    wrapped_resolver = field_instance.wrap_resolve(parent_resolver)
    assert wrapped_resolver(None) is None
    parent_resolver.assert_called_once()


def test_wrap_resolve_with_custom_resolver(field_instance):
    custom_resolver = MagicMock(return_value="custom string")
    field_instance.resolver = custom_resolver
    wrapped_resolver = field_instance.wrap_resolve(None)
    assert wrapped_resolver(None) == "custom string"
    custom_resolver.assert_called_once()


def test_wrap_resolve_no_parent_or_custom_resolver():
    parent_resolver = MagicMock(return_value="parent string")
    field_instance = BlankValueField(graphene.String)
    wrapped_resolver = field_instance.wrap_resolve(parent_resolver)
    assert wrapped_resolver(None) == "parent string"
    parent_resolver.assert_called_once()


# Pruebas unitarias para convert_choice_name
def test_convert_choice_name_valid():
    name = "validName"
    result = convert_choice_name(name)
    assert result == "VALIDNAME"


def test_convert_choice_name_invalid():
    name = "invalid name"
    result = convert_choice_name(name)
    assert result == "INVALID_NAME"


def test_convert_choice_name_empty_string():
    name = ""
    result = convert_choice_name(name)
    assert result == "A_"


def test_convert_choice_name_numeric_start():
    name = "123name"
    result = convert_choice_name(name)
    assert result == "A_123NAME"


def test_convert_choice_name_special_characters():
    name = "!@#name"
    result = convert_choice_name(name)
    assert result == "_NAME"


# Pruebas unitarias para to_const
def test_to_const_basic():
    assert to_const("Hello World") == "HELLO_WORLD"


def test_to_const_with_special_characters():
    assert to_const("Hello@World!") == "HELLO_WORLD_"


def test_to_const_with_unicode():
    assert to_const("Héllo Wörld") == "HELLO_WORLD"


def test_to_const_with_numbers():
    assert to_const("Hello123") == "HELLO123"


def test_to_const_empty_string():
    assert to_const("") == ""


# Pruebas unitarias para get_choices
def test_get_choices_with_dict():
    choices = {"A": "Option A", "B": "Option B"}
    result = list(get_choices(choices))
    expected = [("A", "A", "Option A"), ("B", "B", "Option B")]
    assert result == expected


def test_get_choices_with_ordered_dict():
    choices = OrderedDict([("A", "Option A"), ("B", "Option B")])
    result = list(get_choices(choices))
    expected = [("A", "A", "Option A"), ("B", "B", "Option B")]
    assert result == expected


def test_get_choices_with_choices_meta():
    class TestChoices(models.TextChoices):
        A = "A", "Option A"
        B = "B", "Option B"

    result = list(get_choices(TestChoices))
    expected = [("A", "A", "Option A"), ("B", "B", "Option B")]
    assert result == expected


def test_get_choices_with_callable():
    choices_callable = MagicMock(return_value=[("A", "Option A"), ("B", "Option B")])
    result = list(get_choices(choices_callable))
    expected = [("A", "A", "Option A"), ("B", "B", "Option B")]
    assert result == expected


def test_get_choices_with_nested_tuples():
    choices = [("A", "Option A"), ("B", [("C", "Option C"), ("D", "Option D")])]
    result = list(get_choices(choices))
    expected = [("A", "A", "Option A"), ("C", "C", "Option C"), ("D", "D", "Option D")]
    assert result == expected


def test_get_choices_with_repeated_names():
    choices = [("A", "Option A"), ("A", "Option A")]
    result = list(get_choices(choices))
    expected = [("A", "A", "Option A"), ("A_1", "A", "Option A")]
    assert result == expected


def test_get_unbound_function():
    class Test:
        def method(self):
            pass

    test = Test()
    assert get_unbound_function(test.method).__name__ == "method"


def test_get_unbound_function_with_builtin_function():
    assert get_unbound_function(print) == print


def test_get_unbound_function_with_unbound_function():
    def func():
        pass

    assert get_unbound_function(func) == func


def test_get_unbound_function_enters_if():
    mock_func = Mock()
    mock_func.__self__ = False
    mock_func.__func__ = "unbound_func"

    result = get_unbound_function(mock_func)
    assert result == "unbound_func"


def test_get_function_for_type_with_object_type():
    class TestType(graphene.ObjectType):
        def resolve_test(self, info):
            pass

    result = get_function_for_type(TestType, "resolve_test", "test")
    assert result.__name__ == "resolve_test"


def test_get_function_for_type_with_interface():
    class TestInterface(graphene.Interface):
        def resolve_test(self, info):
            pass

    class TestType(graphene.ObjectType):
        class Meta:
            interfaces = (TestInterface,)

    result = get_function_for_type(TestType, "resolve_test", "test")
    assert result.__name__ == "resolve_test"


def test_get_function_for_type_with_no_resolver():
    class TestType(graphene.ObjectType):
        pass

    result = get_function_for_type(TestType, "resolve_test", "test")
    assert result is None


def test_get_function_for_type_with_classmethod():
    class TestType(graphene.ObjectType):
        @classmethod
        def resolve_test(cls, info):
            pass

    result = get_function_for_type(TestType, "resolve_test", "test")
    assert result.__name__ == "resolve_test"


def test_get_function_for_type_with_no_object_type():
    class TestType:
        def resolve_test(self, info):
            pass

    result = get_function_for_type(TestType, "resolve_test", "test")
    assert result is None


def test_get_function_for_type_with_no_resolver_in_interface():
    class TestInterface(graphene.Interface):
        pass

    class TestType(graphene.ObjectType):
        class Meta:
            interfaces = (TestInterface,)

    result = get_function_for_type(TestType, "resolve_test", "test")
    assert result is None


def test_get_function_for_type_with_no_interface():
    class TestType(graphene.ObjectType):
        pass

    result = get_function_for_type(TestType, "resolve_test", "test")
    assert result is None


def test_resolve_for_relation_field_with_instance_does_not_exist():
    field = MagicMock()
    field.name = "field_name"
    field.default = None
    model = MagicMock()
    model.DoesNotExist = Exception
    model.objects.filter.return_value = "filtered_queryset"
    root = MagicMock()
    root.field_name = MagicMock()
    root.field_name.id = "instance_id"
    info = MagicMock()
    _type = MagicMock()
    _type.get_objects.return_value = "objects"

    result = resolve_for_relation_field(field, model, _type, root, info)
    assert result is None
    model.objects.filter.assert_called_once_with(id="instance_id")
