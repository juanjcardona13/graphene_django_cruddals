from typing import Any, Dict, Literal, Optional, Tuple, Union

from django.apps import apps as django_apps

import graphene
from graphene.utils.subclass_with_meta import SubclassWithMeta
from graphene_django_cruddals.builders.app_to_cruddals import CruddalsApp
from graphene_django_cruddals.utils.utils import get_schema_query_mutation


class CruddalsProject(SubclassWithMeta):
    """
    A base class for defining GraphQL schemas for Django apps in a project using Cruddals.

    This class provides methods to dynamically create GraphQL schemas for each app in the project
    based on provided settings.

    Attributes:
        apps (str or tuple or dict): Names of Django apps for which schemas will be generated.
            Defaults to "__all__", meaning all apps in the project.
        schema: The generated GraphQL schema for the project.
        Query: The combined Query object for the project.
        Mutation: The combined Mutation object for the project.
    """

    apps: Union[Literal["__all__"], Tuple[str, ...]] = "__all__"
    schema: graphene.Schema = None

    Query = None  # TODa: Type
    Mutation = None  # TODa: Type

    @classmethod
    def __init_subclass_with_meta__(
        cls,
        apps: Union[Literal["__all__"], Tuple[str, ...]] = "__all__",
        exclude_apps: Tuple[str, ...] = (),
        interfaces: Tuple[str, ...] = (),
        settings_for_app: Optional[Dict[str, Any]] = None,
        functions: Tuple[str] = (),
        exclude_functions: Tuple[str] = (),
        **kwargs: Any,
    ):
        """
        Initialize the subclass with meta settings and dynamically create GraphQL schemas for apps.

        Args:
            apps (str or tuple): Names of Django apps for which schemas will be generated.
                Defaults to "__all__", meaning all apps in the project.
            exclude_apps (tuple): Names of apps to exclude from schema generation.
            interfaces (tuple): Additional GraphQL interfaces to include in the schemas.
            settings_for_app (dict): Settings specific to each app for schema generation.
            functions (tuple): Functions to include in the schemas can be "create", "read", "update", "delete", "deactivate", "activate", "list", "search" . #TODa: Should name "functions" be changed to "operations" or "fields"?
            exclude_functions (tuple): Functions to exclude from schema generation.
            **kwargs: Additional keyword arguments.
        """
        if settings_for_app is None:
            settings_for_app = {}

        default_exclude_apps = (
            "graphene_django",
            "messages",
            "staticfiles",
            "corsheaders",
            "graphene_django_cruddals",
        )
        exclude_apps = exclude_apps + default_exclude_apps

        interfaces_for_project = interfaces

        apps_name = cls._get_apps_name(apps, exclude_apps)
        cls._validate_apps(apps_name)
        cls._validate_apps(settings_for_app.keys())

        queries = ()
        mutations = ()

        for _app_name in apps_name:
            settings_of_app = settings_for_app.get(_app_name, {})

            final_models, final_exclude_models = cls._get_final_models(
                apps, _app_name, settings_of_app
            )
            final_interfaces, final_exclude_interfaces = cls._get_final_interfaces(
                interfaces_for_project, settings_of_app
            )
            final_functions, final_exclude_functions = cls._get_final_functions(
                functions, exclude_functions, settings_of_app
            )

            final_settings_for_model = settings_of_app.get("settings_for_model", {})

            class_app_schema = cls._create_app_schema(
                _app_name,
                final_models,
                final_exclude_models,
                final_interfaces,
                final_exclude_interfaces,
                final_functions,
                final_exclude_functions,
                final_settings_for_model,
            )

            queries = queries + (class_app_schema.Query,)
            if class_app_schema.Mutation:
                mutations = mutations + (class_app_schema.Mutation,)

        cls.schema, cls.Query, cls.Mutation = get_schema_query_mutation(
            queries, {}, mutations, {}
        )

    @classmethod
    def _get_apps_name(cls, apps, exclude_apps):
        apps_name = ()
        if apps == "__all__":
            apps_name = django_apps.app_configs.keys()
        elif isinstance(apps, tuple):
            apps_name = apps
        else:
            raise ValueError("apps should be '__all__' or tuple")

        apps_name = [item for item in apps_name if item not in exclude_apps]
        return apps_name

    @classmethod
    def _validate_apps(cls, apps_name):
        [django_apps.get_app_config(app_name) for app_name in apps_name]

    @classmethod
    def _get_final_models(cls, apps, _app_name, settings_of_app):
        exclude_models = settings_of_app.get("exclude_models", None)
        if exclude_models is None:
            _models = apps.get(_app_name, None) if isinstance(apps, dict) else None
            return (settings_of_app.get("models", _models), None)
        else:
            return (None, exclude_models)

    @classmethod
    def _get_final_interfaces(cls, interfaces_for_project, settings_of_app):
        interfaces_for_app = settings_of_app.get("interfaces", ())
        return (
            interfaces_for_project + interfaces_for_app,
            settings_of_app.get("exclude_interfaces", ()),
        )

    @classmethod
    def _get_final_functions(cls, functions, exclude_functions, settings_of_app):
        functions_of_app = settings_of_app.get("functions", ())
        exclude_functions_of_app = settings_of_app.get("exclude_functions", ())
        return (
            functions + functions_of_app,
            exclude_functions + exclude_functions_of_app,
        )

    @classmethod
    def _create_app_schema(
        cls,
        _app_name,
        final_models,
        final_exclude_models,
        final_interfaces,
        exclude_interfaces_of_app,
        final_functions,
        final_exclude_functions,
        final_settings_for_model,
    ):
        class AppSchema(CruddalsApp):
            class Meta:
                app_name = _app_name

                models = final_models
                exclude_models = final_exclude_models

                interfaces = final_interfaces
                exclude_interfaces = exclude_interfaces_of_app

                functions = final_functions
                exclude_functions = final_exclude_functions

                settings_for_model = final_settings_for_model

        return AppSchema
