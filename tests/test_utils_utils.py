from graphene_django_cruddals.utils.utils import (
    build_class,
    camel_to_snake,
    camelize,
    delete_keys,
    is_iterable,
    merge_dict,
    transform_string,
)


def test_is_iterable():
    # Test when obj is a list
    assert is_iterable([]) is True

    # Test when obj is a tuple
    assert is_iterable(()) is True

    # Test when obj is a set
    assert is_iterable(set()) is True

    # Test when obj is a string and exclude_string is True
    assert is_iterable("hello", exclude_string=True) is False

    # Test when obj is a string and exclude_string is False
    assert is_iterable("hello", exclude_string=False) is True

    # Test when obj is an integer
    assert is_iterable(5) is False

    # Test when obj is a dictionary
    assert is_iterable({}) is True

    # Test when obj is a custom iterable object
    class CustomIterable:
        def __iter__(self):
            return iter([1, 2, 3])

    assert is_iterable(CustomIterable()) is True

    # Test when obj is None
    assert is_iterable(None) is False

    # Test when obj is a generator
    def generator():
        yield 1
        yield 2
        yield 3

    assert is_iterable(generator()) is True


def test_camelize():
    # Test when data is a dictionary
    data_dict = {"first_name": "John", "last_name": "Doe"}
    expected_result_dict = {"firstName": "John", "lastName": "Doe"}
    assert camelize(data_dict) == expected_result_dict

    # Test when data is a list of dictionaries
    data_list = [
        {"first_name": "John", "last_name": "Doe"},
        {"first_name": "Jane", "last_name": "Smith"},
    ]
    expected_result_list = [
        {"firstName": "John", "lastName": "Doe"},
        {"firstName": "Jane", "lastName": "Smith"},
    ]
    assert camelize(data_list) == expected_result_list

    # Test when data is a nested dictionary
    data_nested_dict = {
        "person": {"first_name": "John", "last_name": "Doe"},
        "address": {"street_name": "Main St", "city": "New York"},
    }
    expected_result_nested_dict = {
        "person": {"firstName": "John", "lastName": "Doe"},
        "address": {"streetName": "Main St", "city": "New York"},
    }
    assert camelize(data_nested_dict) == expected_result_nested_dict

    # Test when data is a nested list of dictionaries
    data_nested_list = [
        {"person": {"first_name": "John", "last_name": "Doe"}},
        {"person": {"first_name": "Jane", "last_name": "Smith"}},
    ]
    expected_result_nested_list = [
        {"person": {"firstName": "John", "lastName": "Doe"}},
        {"person": {"firstName": "Jane", "lastName": "Smith"}},
    ]
    assert camelize(data_nested_list) == expected_result_nested_list

    # Test when data is a string
    data_string = "hello world"
    expected_result_string = "hello world"
    assert camelize(data_string) == expected_result_string

    # Test when data is an integer
    data_integer = 5
    expected_result_integer = 5
    assert camelize(data_integer) == expected_result_integer

    # Test when data is None
    data_none = None
    expected_result_none = None
    assert camelize(data_none) == expected_result_none


def test_camel_to_snake():
    assert camel_to_snake("camelCase") == "camel_case"
    # assert camel_to_snake("PascalCase") == "pascal_case"
    # assert camel_to_snake("kebab-case") == "kebab_case"


def test_transform_string():
    assert transform_string("hello world", "PascalCase") == "HelloWorld"
    # assert transform_string("hello_world", "camelCase") == "helloWorld"
    # assert transform_string("hello-world", "snake_case") == "hello_world"
    # assert transform_string("hello world", "kebab-case") == "hello-world"
    # assert transform_string("HelloWorld", "lowercase") == "helloworld"


def test_delete_keys():
    obj = {"name": "John", "age": 30, "city": "New York"}
    keys = ["age", "city"]
    expected_result = {"name": "John"}
    assert delete_keys(obj, keys) == expected_result


def test_merge_dict():
    source = {"name": "John", "age": 30}
    destination = {"name": "Doe", "city": "New York"}
    expected_result = {"name": ["Doe", "John"], "age": 30, "city": "New York"}
    assert merge_dict(source, destination, keep_both=True) == expected_result


def test_build_class():
    my_class = build_class("MyClass", bases=(object,), attrs={"x": 10})
    my_obj = my_class()
    assert my_obj.x == 10
