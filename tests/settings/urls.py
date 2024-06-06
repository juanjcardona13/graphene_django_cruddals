from django.urls import path
from graphene_django.views import GraphQLView

from tests.schema import app_schema, project_schema, schema

urlpatterns = [
    path("graphql/batch", GraphQLView.as_view(batch=True)),
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema), name="graphql"),
    path(
        "app_graphql",
        GraphQLView.as_view(graphiql=True, schema=app_schema),
        name="app_graphql",
    ),
    path(
        "project_graphql",
        GraphQLView.as_view(graphiql=True, schema=project_schema),
        name="project_graphql",
    ),
]
