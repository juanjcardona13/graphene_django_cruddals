from django.apps import apps as django_apps

from graphene.utils.subclass_with_meta import SubclassWithMeta
from graphene_django_cruddals.builders.model_to_cruddals import CruddalsModel
from graphene_django_cruddals.utils.utils import (
    build_class,
    get_schema_query_mutation,
    validate_list_func_cruddals,
)


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
        interfaces=(),
        exclude_interfaces=(),
        functions=(),
        exclude_functions=(),
        settings_for_model=None,
    ) -> None:
        if settings_for_model is None:
            settings_for_model = {}
        assert app_name, "app_name is required for BuilderCruddalsApp"
        validate_list_func_cruddals(functions, exclude_functions)

        [setattr(self, attr, None) for attr in ["app_name", "app_config", "models"]]
        [setattr(self, attr, ()) for attr in ["queries", "mutations"]]
        self.cruddals_of_models = {}

        self.validate_variables_of_cruddals_app(
            exclude_models,
            models,
            interfaces,
            exclude_interfaces,
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

        for class_model in self.models:
            settings_model = settings_for_model.get(class_model.__name__, {})

            settings_model["interfaces"] = interfaces + settings_model.get(
                "interfaces", ()
            )
            settings_model["exclude_interfaces"] = (
                exclude_interfaces + settings_model.get("exclude_interfaces", ())
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
                name="Meta", attrs={"model": class_model, **settings_model}
            )
            cruddals_model = build_class(
                name=f"{class_model.__name__}Cruddals",
                bases=(CruddalsModel,),
                attrs={"Meta": cruddals_model_meta},
            )

            self.cruddals_of_models.update(
                {
                    f"{cruddals_model.meta.model_name_in_different_case['camel_case']}": cruddals_model
                }
            )
            self.queries = self.queries + (cruddals_model.Query,)
            if cruddals_model.Mutation:
                self.mutations = self.mutations + (cruddals_model.Mutation,)

    @staticmethod  # TODa: Change to a class method
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
        ), f"'interfaces' should be tuple received {type(interfaces_app)}"
        assert isinstance(
            exclude_interfaces_app, (tuple,)
        ), f"'exclude_interfaces' should be tuple received {type(exclude_interfaces_app)}"
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


class CruddalsApp(SubclassWithMeta):
    Query = None
    Mutation = None
    schema = None

    meta = None

    @classmethod
    def __init_subclass_with_meta__(
        cls,
        app_name,
        models=None,
        exclude_models=None,
        prefix="",
        suffix="",
        interfaces=(),
        exclude_interfaces=(),
        functions=(),
        exclude_functions=(),
        settings_for_model=None,
    ):
        if settings_for_model is None:
            settings_for_model = {}
        assert app_name, "app_name is required for CruddalsApp"
        validate_list_func_cruddals(functions, exclude_functions)

        [setattr(cls, attr, None) for attr in ["Query", "Mutation", "schema", "meta"]]

        cruddals_of_app = BuilderCruddalsApp(
            app_name=app_name,
            exclude_models=exclude_models,
            models=models,
            prefix=prefix,
            suffix=suffix,
            interfaces=interfaces,
            exclude_interfaces=exclude_interfaces,
            functions=functions,
            exclude_functions=exclude_functions,
            settings_for_model=settings_for_model,
        )
        cls.meta = cruddals_of_app

        cls.schema, cls.Query, cls.Mutation = get_schema_query_mutation(
            cruddals_of_app.queries, {}, cruddals_of_app.mutations, {}
        )

        super().__init_subclass_with_meta__()
