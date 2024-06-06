from graphene_cruddals import CruddalsRelationField

import graphene
from graphene_django_cruddals.main import (
    DjangoCruddalsApp,
    DjangoCruddalsModel,
    DjangoCruddalsProject,
)

from .models import ModelA, ModelB, ModelC, ModelD, ModelE, ModelF, ModelG, ModelH


class CruddalsModelA(DjangoCruddalsModel):
    class Meta:
        model = ModelA


class CruddalsModelB(DjangoCruddalsModel):
    class Meta:
        model = ModelB


class CruddalsModelC(DjangoCruddalsModel):
    class Meta:
        model = ModelC


class CruddalsModelD(DjangoCruddalsModel):
    class Meta:
        model = ModelD


class CustomResolverModelF:
    class ObjectType:
        def resolve_name(self, info):
            return "CUSTOM RESOLVER FOR NAME"

        def resolve_foreign_key_field(self, info):
            return {"id": 1, "foreign_key_field_deep": None}


class CruddalsModelE(DjangoCruddalsModel):
    class Meta:
        model = ModelE


class CruddalsModelF(DjangoCruddalsModel):
    class Meta:
        model = ModelF
        cruddals_interfaces = (CustomResolverModelF,)


class ExtraFieldsModelG:
    class ObjectType:
        extra_field_object_type = graphene.String()

    class InputObjectType:
        extra_field_input_object_type = graphene.String()

    class CreateInputObjectType:
        extra_field_create_input_object_type = graphene.Int()

    class UpdateInputObjectType:
        extra_field_update_input_object_type = graphene.Boolean()

    class FilterInputObjectType:
        extra_field_filter_input_object_type = graphene.String()

    class OrderByInputObjectType:
        extra_field_order_by_input_object_type = graphene.String()


class CruddalsModelG(DjangoCruddalsModel):
    class Meta:
        model = ModelG
        cruddals_interfaces = (ExtraFieldsModelG,)


class FieldRelationModelH:
    class CreateInputObjectType:
        foreign_key_field = CruddalsRelationField()
        generic_foreign_key = CruddalsRelationField()
        one_to_one_field = CruddalsRelationField()
        many_to_many_field = CruddalsRelationField()

    class UpdateInputObjectType:
        foreign_key_field = CruddalsRelationField()
        generic_foreign_key = CruddalsRelationField()
        one_to_one_field = CruddalsRelationField()
        many_to_many_field = CruddalsRelationField()


class CruddalsModelH(DjangoCruddalsModel):
    class Meta:
        model = ModelH
        cruddals_interfaces = (FieldRelationModelH,)


class Query(
    CruddalsModelA.Query,
    CruddalsModelB.Query,
    CruddalsModelC.Query,
    CruddalsModelD.Query,
    CruddalsModelE.Query,
    CruddalsModelF.Query,
    CruddalsModelG.Query,
    CruddalsModelH.Query,
    graphene.ObjectType,
):
    pass


class Mutation(
    CruddalsModelA.Mutation,
    CruddalsModelB.Mutation,
    CruddalsModelC.Mutation,
    CruddalsModelD.Mutation,
    CruddalsModelE.Mutation,
    CruddalsModelF.Mutation,
    CruddalsModelG.Mutation,
    CruddalsModelH.Mutation,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
    types=[CruddalsModelA.meta.model_as_input_object_type],
)


class SchemaCruddalsApp(DjangoCruddalsApp):
    class Meta:
        app_name = "tests"
        models = (
            "ModelA",
            "ModelB",
            "ModelC",
            "ModelD",
            "ModelE",
            "ModelF",
            "ModelG",
            "ModelH",
        )
        settings_for_model = {
            "ModelF": {"cruddals_interfaces": (CustomResolverModelF,)},
            "ModelG": {"cruddals_interfaces": (ExtraFieldsModelG,)},
            "ModelH": {"cruddals_interfaces": (FieldRelationModelH,)},
        }


app_schema = graphene.Schema(
    query=SchemaCruddalsApp.Query,
    mutation=SchemaCruddalsApp.Mutation,
    types=[
        SchemaCruddalsApp.meta.cruddals_of_models[
            "modelA"
        ].meta.model_as_input_object_type,
    ],
)


class SchemaCruddalsProject(DjangoCruddalsProject):
    class Meta:
        apps = ("tests",)
        settings_for_app = {
            "tests": {
                "models": (
                    "ModelA",
                    "ModelB",
                    "ModelC",
                    "ModelD",
                    "ModelE",
                    "ModelF",
                    "ModelG",
                    "ModelH",
                ),
                "settings_for_model": {
                    "ModelF": {"cruddals_interfaces": (CustomResolverModelF,)},
                    "ModelG": {"cruddals_interfaces": (ExtraFieldsModelG,)},
                    "ModelH": {"cruddals_interfaces": (FieldRelationModelH,)},
                },
            }
        }


project_schema = graphene.Schema(
    query=SchemaCruddalsProject.Query,
    mutation=SchemaCruddalsProject.Mutation,
    types=[
        SchemaCruddalsProject.meta["tests"]
        .meta.cruddals_of_models["modelA"]
        .meta.model_as_input_object_type,
    ],
)
