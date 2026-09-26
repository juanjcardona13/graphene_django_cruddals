"""list uses the same get_objects hook as read and search."""

import pytest
from graphene_cruddals import RegistryGlobal

import graphene
from graphene_django_cruddals import DjangoModelCruddals
from tests.models import ModelC


class OnlyAna:
    class ObjectType:
        @classmethod
        def get_objects(cls, queryset, info, **kwargs):
            return queryset.filter(char_field="ANA")


class RequestContext:
    pass


def build_schema(interfaces=()):
    model_registry = RegistryGlobal()

    class ModelCCruddals(DjangoModelCruddals):
        class Meta:
            model = ModelC
            registry = model_registry
            cruddals_interfaces = interfaces

    class Query(ModelCCruddals.Query, graphene.ObjectType):
        pass

    class Mutation(ModelCCruddals.Mutation, graphene.ObjectType):
        pass

    return graphene.Schema(query=Query, mutation=Mutation)


def execute(schema, query, variables=None):
    result = schema.execute(
        query,
        variable_values=variables,
        context_value=RequestContext(),
    )
    assert result.errors is None, [error.message for error in result.errors]
    return result.data


LIST_QUERY = """
    query {
      listModelCs { id charField }
    }
"""


@pytest.mark.django_db
def test_list_applies_get_objects():
    schema = build_schema((OnlyAna,))
    ModelC.objects.create(char_field="ANA")
    ModelC.objects.create(char_field="BRUNO")

    data = execute(schema, LIST_QUERY)

    assert [row["charField"] for row in data["listModelCs"]] == ["ANA"]


@pytest.mark.django_db
def test_list_without_get_objects_returns_every_row():
    schema = build_schema()
    ModelC.objects.create(char_field="ANA")
    ModelC.objects.create(char_field="BRUNO")

    data = execute(schema, LIST_QUERY)

    assert sorted(row["charField"] for row in data["listModelCs"]) == ["ANA", "BRUNO"]


@pytest.mark.django_db
def test_read_and_search_still_apply_get_objects():
    schema = build_schema((OnlyAna,))
    ana = ModelC.objects.create(char_field="ANA")
    bruno = ModelC.objects.create(char_field="BRUNO")

    read_ana = execute(
        schema,
        """
        query($where: FilterModelCInput!) {
          readModelC(where: $where) { charField }
        }
        """,
        {"where": {"id": {"exact": str(ana.pk)}}},
    )
    assert read_ana["readModelC"]["charField"] == "ANA"

    read_bruno = schema.execute(
        """
        query($where: FilterModelCInput!) {
          readModelC(where: $where) { charField }
        }
        """,
        variable_values={"where": {"id": {"exact": str(bruno.pk)}}},
        context_value=RequestContext(),
    )
    assert read_bruno.data["readModelC"] is None
    assert read_bruno.errors

    search = execute(
        schema,
        """
        query {
          searchModelCs { objects { charField } }
        }
        """,
    )
    assert [row["charField"] for row in search["searchModelCs"]["objects"]] == ["ANA"]


@pytest.mark.django_db
def test_delete_does_not_apply_get_objects():
    schema = build_schema((OnlyAna,))
    ModelC.objects.create(char_field="ANA")
    bruno = ModelC.objects.create(char_field="BRUNO")

    data = execute(
        schema,
        """
        mutation($where: FilterModelCInput!) {
          deleteModelCs(where: $where) { success }
        }
        """,
        {"where": {"id": {"exact": str(bruno.pk)}}},
    )

    assert data["deleteModelCs"]["success"] is True
    assert not ModelC.objects.filter(pk=bruno.pk).exists()
