import re
from collections.abc import Iterable
from typing import Any, Dict, Literal, Tuple, Type, Union

from django.db.models import Model as DjangoModel
from django.forms import ModelForm as DjangoModelForm
from django.utils.encoding import force_str
from django.utils.functional import Promise

import graphene
from graphene_django_cruddals.python_types import (
    FunctionType,
    NameCaseType,
    RootFieldsType,
)


def is_iterable(obj: Any, exclude_string=True) -> bool:
    if exclude_string:
        return isinstance(obj, Iterable) and not isinstance(obj, str)
    return isinstance(obj, Iterable)


def _camelize_django_str(string: str) -> str:
    if isinstance(string, Promise):
        string = force_str(string)
    return transform_string(string, "camelCase") if isinstance(string, str) else string


def camelize(data):
    if isinstance(data, dict):
        return {_camelize_django_str(k): camelize(v) for k, v in data.items()}
    if is_iterable(data) and not isinstance(data, (str, Promise)):
        return [camelize(d) for d in data]
    return data


def camel_to_snake(s: Union[str, bytes]) -> str:
    s = str(s)
    s = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", s)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s).lower()


def transform_string(
    s: Union[str, bytes],
    type: Literal["PascalCase", "camelCase", "snake_case", "kebab-case", "lowercase"],
) -> str:
    """Type: PascalCase, camelCase, snake_case, kebab-case, lowercase"""
    s = str(s)
    if " " in s or "_" in s or "-" in s:
        separator = " " if " " in s else "_" if "_" in s else "-"
        if type == "PascalCase":
            return "".join(word.title() for word in s.split(separator))
        elif type == "snake_case":
            return "_".join(word.lower() for word in s.split(separator))
        elif type == "kebab-case":
            return "-".join(word.lower() for word in s.split(separator))
        elif type == "lowercase":
            return "".join(word.lower() for word in s.split(separator))
        elif type == "camelCase":
            return (
                s[0].lower() + "".join(word.title() for word in s.split(separator))[1:]
            )
        else:
            return "".join(word for word in s.split(separator))
    else:
        if type == "PascalCase":
            if s[0] == s.title()[0]:
                return s
            else:
                return s.title()
        elif type == "lowercase":
            return s.lower()
        else:
            return s


def delete_keys(obj: dict, keys: list[str]) -> dict:
    for key in keys:
        if key in obj:
            del obj[key]
    return obj


def merge_dict(
    source: dict,
    destination: dict,
    overwrite: bool = False,
    keep_both: bool = False,
    path: Union[list[str], None] = None,
) -> dict:
    "merges source into destination"
    import copy

    new_destination = copy.deepcopy(destination)

    if path is None:
        path = []
    for key in source:
        if key in new_destination:
            if isinstance(new_destination[key], dict) and isinstance(source[key], dict):
                new_destination[key] = merge_dict(
                    source[key],
                    new_destination[key],
                    overwrite,
                    keep_both,
                    path + [str(key)],
                )
            elif new_destination[key] == source[key]:
                pass
            else:
                if keep_both:
                    if isinstance(
                        new_destination[key],
                        (
                            list,
                            tuple,
                            set,
                        ),
                    ) and isinstance(
                        source[key],
                        (
                            list,
                            tuple,
                            set,
                        ),
                    ):
                        new_destination[key] = new_destination[key] + source[key]
                    else:
                        new_destination[key] = [new_destination[key], source[key]]
                elif overwrite:
                    """Debo de conservar lo que tiene new_destination"""
                    continue
                else:
                    raise Exception("Conflict at %s" % ".".join(path + [str(key)]))
        else:
            new_destination[key] = source[key]
    return new_destination


def build_class(name: str, bases: tuple = (), attrs: dict = None) -> Any:
    if attrs is None:
        attrs = {}
    return type(name, bases, attrs)


def validate_list_func_cruddals(
    functions: Tuple[FunctionType, ...], exclude_functions: Tuple[FunctionType, ...]
) -> bool:
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
        name_input = "function" if functions else "exclude_function"
        input_list = functions if functions else exclude_functions

    invalid_values = [value for value in input_list if value not in valid_values]

    if invalid_values:
        raise ValueError(
            f"Expected in '{name_input}' a tuple with some of these values {valid_values}, but got these invalid values {invalid_values}"
        )

    return True


def get_schema_query_mutation(
    queries: Tuple[Type[graphene.ObjectType], ...] = (),
    attrs_for_query: Dict[str, graphene.Field] = None,
    mutations: Tuple[Type[graphene.ObjectType], ...] = (),
    attrs_for_mutation: Union[Dict[str, graphene.Field], None] = None,
) -> Tuple[
    graphene.Schema, Type[graphene.ObjectType], Union[Type[graphene.ObjectType], None]
]:
    if attrs_for_query is None:
        attrs_for_query = {}
    if attrs_for_mutation is None:
        attrs_for_mutation = {}
    base = (graphene.ObjectType,)
    query: Type[graphene.ObjectType] = build_class(
        name="Query", bases=(queries + base), attrs=attrs_for_query
    )

    dict_for_schema: RootFieldsType = {"query": query, "mutation": None}

    mutation: Union[Type[graphene.ObjectType], None] = None
    if mutations or attrs_for_mutation:
        attrs_for_mutation = {} if attrs_for_mutation is None else attrs_for_mutation
        mutation = build_class(
            name="Mutation", bases=(mutations + base), attrs=attrs_for_mutation
        )
        dict_for_schema.update({"mutation": mutation})

    schema = graphene.Schema(**dict_for_schema)

    return schema, query, mutation


# region Maybe I should move this to another file
def get_name_of_model_in_different_case(
    model: DjangoModel, prefix="", suffix=""
) -> NameCaseType:
    # snake_case
    # kebab-case
    # camelCase
    # PascalCase

    prefix_lower = prefix.lower()
    prefix_capitalize = prefix.capitalize()

    suffix_lower = suffix.lower()
    suffix_capitalize = suffix.capitalize()

    name_model = model.__name__
    name_model_plural = transform_string(model._meta.verbose_name_plural, "PascalCase")

    snake_case = f"{prefix_lower}{'_' if prefix else ''}{camel_to_snake(name_model)}{'_' if suffix else ''}{suffix_lower}"
    plural_snake_case = f"{prefix}{'_' if prefix else ''}{camel_to_snake(transform_string(name_model_plural, 'PascalCase'))}{'_' if suffix else ''}{suffix}"

    camel_case = f"{prefix_capitalize}{name_model}{suffix_capitalize}"
    plural_camel_case = f"{prefix_lower}{name_model_plural}{suffix_capitalize}"

    pascal_case = f"{prefix_capitalize}{transform_string(name_model, 'PascalCase')}{suffix_capitalize}"
    plural_pascal_case = (
        f"{prefix}{transform_string(name_model_plural, 'PascalCase')}{suffix}"
    )

    return {
        "snake_case": snake_case,
        "plural_snake_case": plural_snake_case,
        "camel_case": camel_case,
        "plural_camel_case": plural_camel_case,
        "pascal_case": pascal_case,
        "plural_pascal_case": plural_pascal_case,
    }


def convert_model_to_model_form(
    model: DjangoModel, prefix_for_name="", suffix_for_name=""
) -> DjangoModelForm:
    """
    Convert a Django model to a Django model form
    """
    names_of_model = get_name_of_model_in_different_case(
        model, prefix=prefix_for_name, suffix=suffix_for_name
    )
    singular_camel_case_name = names_of_model.get("camel_case")

    MetaForm = build_class(
        name="Meta",
        attrs={
            "model": model,
            "fields": "__all__",
            "name": f"{singular_camel_case_name}Form",
        },
    )
    ModelForm = build_class(
        name=f"{singular_camel_case_name}Form",
        bases=(DjangoModelForm,),
        attrs={"Meta": MetaForm},
    )
    return ModelForm


# endregion
