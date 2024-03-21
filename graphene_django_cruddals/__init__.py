from .views.cruddals_views import CRUDDALSView
from .main import CruddalsModel, CruddalsApp
from graphene_django_cruddals.utils import *

__version__ = "1.0.0"

__all__ = [
    "__version__",
    # utils
    "is_iterable",
    "camel_to_snake",
    "snake_to_case",
    "transform_string",
    "delete_keys",
    "merge_dict",
    "build_class",
    "add_cruddals_model_to_request",
    "get_name_of_model_in_different_case",
    # views
    "CRUDDALSView",
    # registries
    "get_global_registry",
    # main
    "CruddalsModel",
    "CruddalsApp",
    # TODO: Helpers, interfaces
]
