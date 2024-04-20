from graphene_django_cruddals.utils import (
    build_class,
    camel_to_snake,
    delete_keys,
    is_iterable,
    merge_dict,
    transform_string,
)


def test_is_iterable():
    # Test when obj is a list
    assert is_iterable([]) == True

    # Test when obj is a tuple
    assert is_iterable(()) == True

    # Test when obj is a set
    assert is_iterable(set()) == True

    # Test when obj is a string and exclude_string is True
    assert is_iterable("hello", exclude_string=True) == False

    # Test when obj is a string and exclude_string is False
    assert is_iterable("hello", exclude_string=False) == True

    # Test when obj is an integer
    assert is_iterable(5) == False

    # Test when obj is a dictionary
    assert is_iterable({}) == True

    # Test when obj is a custom iterable object
    class CustomIterable:
        def __iter__(self):
            return iter([1, 2, 3])

    assert is_iterable(CustomIterable()) == True

    # Test when obj is None
    assert is_iterable(None) == False

    # Test when obj is a generator
    def generator():
        yield 1
        yield 2
        yield 3

    assert is_iterable(generator()) == True


# def test_camelize():
#     data = {
#         "first_name": "John",
#         "last_name": "Doe",
#         "address": {
#             "street_name": "123 Main St",
#             "city": "New York",
#             "state": "NY",
#         },
#     }
#     expected_result = {
#         "firstName": "John",
#         "lastName": "Doe",
#         "address": {
#             "streetName": "123 Main St",
#             "city": "New York",
#             "state": "NY",
#         },
#     }
#     assert camelize(data) == expected_result


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
