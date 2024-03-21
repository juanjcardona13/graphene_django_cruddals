# -*- coding: utf-8 -*-

import re
from collections.abc import Iterable
from typing import Any, Literal, Union

import graphene
from django.forms import ModelForm as DjangoModelForm
from django.utils.encoding import force_str
from django.utils.functional import Promise
from django.db.models import Model as DjangoModel

from graphene.utils.str_converters import to_camel_case

import graphene
from graphene.types.generic import GenericScalar

from graphene_django_cruddals.types import NameCaseType


def is_iterable(obj:Any, exclude_string=True) -> bool:
    if exclude_string:
        return isinstance(obj, Iterable) and not isinstance(obj, str)
    return isinstance(obj, Iterable)


def _camelize_django_str(string:str) -> str:
    if isinstance(string, Promise):
        string = force_str(string)
    return transform_string(string, 'camelCase') if isinstance(string, str) else string


def camelize(data):
    if isinstance(data, dict):
        return {_camelize_django_str(k): camelize(v) for k, v in data.items()}
    if is_iterable(data) and not isinstance(data, (str, Promise)):
        return [camelize(d) for d in data]
    return data


def camel_to_snake(s:Union[str, bytes]) -> str:
    s = str(s)
    s = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", s)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s).lower()


def transform_string(s:Union[str, bytes], type: Literal["PascalCase", "camelCase", "snake_case", "kebab-case", "lowercase"]) -> str:
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


def delete_keys(obj:dict, keys:list[str]) -> dict:
    for key in keys:
        if key in obj:
            del obj[key]
    return obj


def merge_dict(source:dict, destination:dict, overwrite:bool=False, keep_both:bool=False, path:Union[list[str], None]=None) -> dict:
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


def build_class(name:str, bases:tuple=(), attrs:dict={}) -> Any:
    return type(name, bases, attrs)


def get_name_of_model_in_different_case(model:DjangoModel, prefix="", suffix="") -> NameCaseType:
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



#region Maybe I should move this to another file
def convert_model_to_model_form( model:DjangoModel, prefix_for_name="", suffix_for_name="" ) -> DjangoModelForm:
    """
    Convert a Django model to a Django model form
    """
    names_of_model = get_name_of_model_in_different_case( model, prefix=prefix_for_name, suffix=suffix_for_name )
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
#endregion