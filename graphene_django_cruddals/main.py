from typing import Any, Dict, Literal, NamedTuple, Optional, Tuple, Type, Union

from django.apps import apps as django_apps
from django.db.models import (
    Model as DjangoModel,
)
from django.forms import ModelForm as DjangoModelForm
from graphene_cruddals import (
    RegistryGlobal,
    TypesMutationEnum,
    build_class,
    get_global_registry,
    get_name_of_model_in_different_case,
    get_schema_query_mutation,
    validate_list_func_cruddals,
)
from graphene_cruddals.main import CruddalsBuilderConfig, CruddalsModel
from graphene_cruddals.utils.main import transform_string
from graphene_cruddals.utils.typing.custom_typing import FunctionType

import graphene
from graphene.utils.subclass_with_meta import SubclassWithMeta
from graphene_django_cruddals.resolvers.main import (
    default_activate_field_resolver,
    default_create_update_resolver,
    default_deactivate_field_resolver,
    default_delete_field_resolver,
    default_list_field_resolver,
    default_read_field_resolver,
    default_search_field_resolver,
    default_update_resolver,
)
from graphene_django_cruddals.utils.main import (
    convert_django_field_with_choices_to_create_update_input,
    convert_django_field_with_choices_to_output,
    convert_django_field_without_choices_to_filter_input,
    convert_django_field_without_choices_to_order_by_input,
    get_model_fields_for_input,
    get_model_fields_for_output,
)


def convert_model_to_model_form(
    model: DjangoModel, prefix_for_name="", suffix_for_name=""
) -> DjangoModelForm:
    """
    Convert a Django model to a Django model form
    """
    names_of_model = get_name_of_model_in_different_case(
        model.__name__, prefix=prefix_for_name, suffix=suffix_for_name
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


class DjangoCruddalsModel(CruddalsModel):
    @classmethod
    def __init_subclass_with_meta__(
        cls,
        config: Optional[CruddalsBuilderConfig] = None,
        functions: Optional[Tuple[FunctionType, ...]] = None,
        exclude_functions: Optional[Tuple[FunctionType, ...]] = None,
        model: Union[DjangoModel, None] = None,
        prefix: str = "",
        suffix: str = "",
        cruddals_interfaces: Tuple[Type[Any], ...] = (),
        exclude_cruddals_interfaces: Tuple[str, ...] = (),
        registry: Union[RegistryGlobal, None] = None,
        field_for_activate_deactivate: str = "is_active",
        **kwargs,
    ):
        assert model, "model is required for CruddalsModel"

        model_form_class = convert_model_to_model_form(
            model=model,
            prefix_for_name=prefix,
            suffix_for_name=suffix,
        )

        if not registry:
            registry = get_global_registry()

        if not config:
            config = CruddalsBuilderConfig(
                model=model,
                pascal_case_name=model.__name__,
                get_fields_for_output=cls.get_fields_for_output,
                output_field_converter_function=convert_django_field_with_choices_to_output,
                get_fields_for_input=cls.get_fields_for_input,
                input_field_converter_function=cls.input_field_converter_function,
                get_fields_for_create_input=cls.get_fields_for_create_input,
                create_input_field_converter_function=cls.create_input_field_converter_function,
                get_fields_for_update_input=cls.get_fields_for_update_input,
                update_input_field_converter_function=cls.update_input_field_converter_function,
                get_fields_for_filter=cls.get_fields_for_filter,
                filter_field_converter_function=convert_django_field_without_choices_to_filter_input,
                get_fields_for_order_by=cls.get_fields_for_order_by,
                order_by_field_converter_function=convert_django_field_without_choices_to_order_by_input,
                create_resolver=lambda root,
                info,
                **kwargs: default_create_update_resolver(
                    model, model_form_class, registry, root, info, **kwargs
                ),
                read_resolver=lambda root, info, **kwargs: default_read_field_resolver(
                    model, registry, model._default_manager, root, info, **kwargs
                ),
                update_resolver=lambda root, info, **kwargs: default_update_resolver(
                    model, model_form_class, registry, root, info, **kwargs
                ),
                delete_resolver=lambda root,
                info,
                **kwargs: default_delete_field_resolver(model, root, info, **kwargs),
                deactivate_resolver=lambda root,
                info,
                **kwargs: default_deactivate_field_resolver(
                    model, field_for_activate_deactivate, root, info, **kwargs
                ),
                activate_resolver=lambda root,
                info,
                **kwargs: default_activate_field_resolver(
                    model, field_for_activate_deactivate, root, info, **kwargs
                ),
                list_resolver=lambda root, info, **kwargs: default_list_field_resolver(
                    None, model._default_manager, root, info, **kwargs
                ),
                search_resolver=lambda root,
                info,
                **kwargs: default_search_field_resolver(
                    model,
                    registry,
                    None,
                    model._default_manager,
                    root,
                    info,
                    **kwargs,
                ),
                field_for_activate_deactivate=field_for_activate_deactivate,
                plural_pascal_case_name=transform_string(
                    model._meta.verbose_name_plural or "", "PascalCase"
                ),
                prefix=prefix,
                suffix=suffix,
                cruddals_interfaces=cruddals_interfaces,
                exclude_cruddals_interfaces=exclude_cruddals_interfaces,
                registry=registry,
            )

        super().__init_subclass_with_meta__(
            config=config,
            functions=functions,
            exclude_functions=exclude_functions,
            **kwargs,
        )

    @staticmethod
    def get_fields_for_output(model: DjangoModel):
        return get_model_fields_for_output(model, True)

    @staticmethod
    def get_fields_for_input(model: DjangoModel):
        return get_model_fields_for_input(model, TypesMutationEnum.CREATE_UPDATE.value)

    @staticmethod
    def input_field_converter_function(name, field, model: DjangoModel, registry):
        return convert_django_field_with_choices_to_create_update_input(
            name, field, model, registry, TypesMutationEnum.CREATE_UPDATE.value
        )

    @staticmethod
    def get_fields_for_create_input(model: DjangoModel):
        return get_model_fields_for_input(model, TypesMutationEnum.CREATE.value)

    @staticmethod
    def create_input_field_converter_function(name, field, model, registry):
        return convert_django_field_with_choices_to_create_update_input(
            name, field, model, registry, TypesMutationEnum.CREATE.value
        )

    @staticmethod
    def get_fields_for_update_input(model: DjangoModel):
        return get_model_fields_for_input(model, TypesMutationEnum.UPDATE.value)

    @staticmethod
    def update_input_field_converter_function(name, field, model, registry):
        return convert_django_field_with_choices_to_create_update_input(
            name, field, model, registry, TypesMutationEnum.UPDATE.value
        )

    @staticmethod
    def get_fields_for_filter(model: DjangoModel):
        return get_model_fields_for_output(model)

    @staticmethod
    def get_fields_for_order_by(model: DjangoModel):
        return get_model_fields_for_output(model)


class BuilderCruddalsApp:
    app_name = None
    app_config = None
    models = None
    cruddals_of_models = {}

    queries = ()
    mutations = ()

    def __init__(
        self,
        app_name,
        exclude_models=None,
        models=None,
        prefix="",
        suffix="",
        cruddals_interfaces=(),
        exclude_cruddals_interfaces=(),
        functions=(),
        exclude_functions=(),
        settings_for_model=None,
    ) -> None:
        assert app_name, "app_name is required for BuilderCruddalsApp"
        validate_list_func_cruddals(functions, exclude_functions)

        [setattr(self, attr, None) for attr in ["app_name", "app_config", "models"]]
        [setattr(self, attr, ()) for attr in ["queries", "mutations"]]

        if settings_for_model is None:
            settings_for_model = {}

        self.cruddals_of_models = {}

        self.validate_variables_of_cruddals_app(
            exclude_models,
            models,
            cruddals_interfaces,
            exclude_cruddals_interfaces,
            functions,
            exclude_functions,
            settings_for_model,
            app_name,
        )

        self.app_name = app_name
        self.app_config = django_apps.get_app_config(app_name)
        self.models = tuple(self.app_config.get_models())

        if exclude_models is not None:
            models_to_exclude = set()
            for exclude_model in exclude_models:
                model_to_exclude = self.app_config.get_model(model_name=exclude_model)
                models_to_exclude.add(model_to_exclude)
            self.models = tuple(set(self.models) - models_to_exclude)
        elif models is not None:
            models_to_include = []
            for include_model in models:
                model_to_include = self.app_config.get_model(model_name=include_model)
                models_to_include.append(model_to_include)
            self.models = models_to_include

        for Model in self.models:
            settings_model = settings_for_model.get(Model.__name__, {})

            settings_model["cruddals_interfaces"] = (
                cruddals_interfaces + settings_model.get("cruddals_interfaces", ())
            )
            settings_model["exclude_cruddals_interfaces"] = (
                exclude_cruddals_interfaces
                + settings_model.get("exclude_cruddals_interfaces", ())
            )

            settings_model["functions"] = functions + settings_model.get(
                "functions", ()
            )
            settings_model["exclude_functions"] = (
                exclude_functions + settings_model.get("exclude_functions", ())
            )

            settings_model["prefix"] = settings_model.get("prefix", prefix)
            settings_model["suffix"] = settings_model.get("suffix", suffix)

            cruddals_model_meta = build_class(
                name="Meta", attrs={"model": Model, **settings_model}
            )
            cruddals_model = build_class(
                name=f"{Model.__name__}Cruddals",
                bases=(DjangoCruddalsModel,),
                attrs={"Meta": cruddals_model_meta},
            )

            self.cruddals_of_models.update(
                {
                    f"{cruddals_model.meta.model_name_in_different_case['camel_case']}": cruddals_model  # TODO: Change this name for the model in pascal case
                }
            )
            self.queries = self.queries + (cruddals_model.Query,)
            if cruddals_model.Mutation:
                self.mutations = self.mutations + (cruddals_model.Mutation,)

    @staticmethod
    def validate_variables_of_cruddals_app(
        exclude_models,
        include_models,
        interfaces_app,
        exclude_interfaces_app,
        functions_app,
        exclude_functions_app,
        settings_for_model,
        app_name,
    ):
        assert not (
            exclude_models and include_models
        ), f"Cannot set both 'exclude_models' and 'models' options on {app_name}."
        assert isinstance(
            interfaces_app, (tuple,)
        ), f"'cruddals_interfaces' should be tuple received {type(interfaces_app)}"
        assert isinstance(
            exclude_interfaces_app, (tuple,)
        ), f"'exclude_cruddals_interfaces' should be tuple received {type(exclude_interfaces_app)}"
        assert isinstance(
            functions_app, (tuple,)
        ), f"'functions' should be tuple received {type(functions_app)}"
        assert isinstance(
            exclude_functions_app, (tuple,)
        ), f"'exclude_functions' should be tuple received {type(exclude_functions_app)}"
        assert isinstance(
            settings_for_model, dict
        ), f"'settings_for_model' should be dict, received {type(settings_for_model)}"

        if exclude_models is not None:
            assert isinstance(
                exclude_models, (tuple,)
            ), f"'exclude_models' should be tuple received {type(exclude_models)}"
        if include_models is not None:
            assert isinstance(
                include_models, (tuple,)
            ), f"'models' should be tuple received {type(include_models)}"


class DjangoCruddalsApp(SubclassWithMeta):
    Query = None
    Mutation = None
    schema = None

    meta = None

    @classmethod
    def __init_subclass_with_meta__(
        cls,
        app_name=None,
        models=None,
        exclude_models=None,
        prefix="",
        suffix="",
        cruddals_interfaces=(),
        exclude_cruddals_interfaces=(),
        functions=(),
        exclude_functions=(),
        settings_for_model=None,
        **kwargs,
    ):
        assert app_name, "app_name is required for DjangoCruddalsApp"
        validate_list_func_cruddals(functions, exclude_functions)

        [setattr(cls, attr, None) for attr in ["Query", "Mutation", "schema", "meta"]]

        if settings_for_model is None:
            settings_for_model = {}

        cruddals_of_app = BuilderCruddalsApp(
            app_name=app_name,
            exclude_models=exclude_models,
            models=models,
            prefix=prefix,
            suffix=suffix,
            cruddals_interfaces=cruddals_interfaces,
            exclude_cruddals_interfaces=exclude_cruddals_interfaces,
            functions=functions,
            exclude_functions=exclude_functions,
            settings_for_model=settings_for_model,
        )
        cls.meta = cruddals_of_app

        cls.schema, cls.Query, cls.Mutation = get_schema_query_mutation(
            cruddals_of_app.queries, {}, cruddals_of_app.mutations, {}
        )

        super().__init_subclass_with_meta__(**kwargs)


class AppSettings(NamedTuple):
    exclude_models: Union[tuple, None] = None
    models: Union[tuple, None] = None
    cruddals_interfaces: tuple = ()
    exclude_cruddals_interfaces: tuple = ()
    functions: tuple = ()
    exclude_functions: tuple = ()
    settings_for_model: dict = {}


class DjangoCruddalsProject(SubclassWithMeta):
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
    schema: graphene.Schema

    Query: Type[graphene.ObjectType]
    Mutation: Type[graphene.Mutation]

    meta = None

    @classmethod
    def __init_subclass_with_meta__(
        cls,
        apps: Union[Literal["__all__"], Tuple[str, ...]] = "__all__",
        exclude_apps: Tuple[str, ...] = (),
        cruddals_interfaces: Tuple[str, ...] = (),
        settings_for_app: Optional[Dict[str, Any]] = None,
        functions: Tuple[str, ...] = (),
        exclude_functions: Tuple[str, ...] = (),
        **kwargs: Any,
    ):
        """
        Initialize the subclass with meta settings and dynamically create GraphQL schemas for apps.

        Args:
            apps (str or tuple): Names of Django apps for which schemas will be generated.
                Defaults to "__all__", meaning all apps in the project.
            exclude_apps (tuple): Names of apps to exclude from schema generation.
            cruddals_interfaces (tuple): Additional GraphQL cruddals_interfaces to include in the schemas.
            settings_for_app (dict): Settings specific to each app for schema generation.
            functions (tuple): Functions to include in the schemas can be "create", "read", "update", "delete", "deactivate", "activate", "list", "search" .
            exclude_functions (tuple): Functions to exclude from schema generation.
            **kwargs: Additional keyword arguments.
        """
        cls.apps = apps
        if settings_for_app is None:
            settings_for_app = {}

        default_exclude_apps = (
            "graphene_django",
            "messages",
            "staticfiles",
            "corsheaders",
            "new_cruddals_django",
        )
        exclude_apps = exclude_apps + default_exclude_apps

        interfaces_for_project = cruddals_interfaces

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

            AppSchema = cls._create_app_schema(
                _app_name,
                final_models,
                final_exclude_models,
                final_interfaces,
                final_exclude_interfaces,
                final_functions,
                final_exclude_functions,
                final_settings_for_model,
            )

            queries = queries + (AppSchema.Query,)
            if AppSchema.Mutation:
                mutations = mutations + (AppSchema.Mutation,)

        cls.schema, cls.Query, cls.Mutation = get_schema_query_mutation(
            queries, {}, mutations, {}
        )  # type: ignore

        super().__init_subclass_with_meta__(**kwargs)

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
        interfaces_for_app = settings_of_app.get("cruddals_interfaces", ())
        return (
            interfaces_for_project + interfaces_for_app,
            settings_of_app.get("exclude_cruddals_interfaces", ()),
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
        MetaAppCruddals = build_class(
            name="Meta",
            attrs={
                "app_name": _app_name,
                "models": final_models,
                "exclude_models": final_exclude_models,
                "cruddals_interfaces": final_interfaces,
                "exclude_cruddals_interfaces": exclude_interfaces_of_app,
                "functions": final_functions,
                "exclude_functions": final_exclude_functions,
                "settings_for_model": final_settings_for_model,
            },
        )
        AppCruddals = build_class(
            name=f"{_app_name}AppCruddals",
            bases=(DjangoCruddalsApp,),
            attrs={"Meta": MetaAppCruddals},
        )

        if cls.meta is None:
            cls.meta = {_app_name: AppCruddals}
        else:
            cls.meta.update({_app_name: AppCruddals})
        return AppCruddals
