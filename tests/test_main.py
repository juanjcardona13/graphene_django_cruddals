import pytest
from graphene_cruddals import get_global_registry

import graphene
from graphene import UUID, Boolean, Date, DateTime, Int, String
from graphene_django_cruddals.converters.converter_filter_input import (
    _is_text_type,
    convert_django_field_to_filter_input,
)
from graphene_django_cruddals.converters.converter_input import (
    convert_django_field_to_input,
)
from graphene_django_cruddals.converters.converter_input_relation_nested import (
    convert_relation_field_to_input,
)
from graphene_django_cruddals.converters.converter_order_by_input import (
    convert_django_field_to_order_by_input,
)
from graphene_django_cruddals.converters.converter_output import (
    convert_django_field_to_output,
)
from graphene_django_cruddals.scalars_type import IP, URL, Email, IPv4, Slug
from tests.fragments import (
    activate_model_c_mutation,
    create_model_c_mutation,
    create_model_d_mutation,
    create_model_e_mutation,
    create_model_f_mutation,
    create_model_g_mutation,
    create_model_h_mutation,
    deactivate_model_c_mutation,
    delete_model_c_mutation,
    list_model_c_query,
    objs_to_create_type_c,
    objs_to_create_type_d,
    objs_to_create_type_f,
    read_model_c_query,
    read_model_g_query,
    read_model_h_query,
    search_model_c_query,
    search_model_d_query,
    search_model_g_query,
    update_model_c_mutation,
)
from tests.gql_fields.activateModelCs import activateModelCs
from tests.gql_fields.createModelCs import createModelCs
from tests.gql_fields.createModelHs import createModelHs
from tests.gql_fields.deactivateModelCs import deactivateModelCs
from tests.gql_fields.deleteModelCs import deleteModelCs
from tests.gql_fields.listModelCs import listModelCs
from tests.gql_fields.readModelC import readModelC
from tests.gql_fields.searchModelCs import searchModelCs
from tests.gql_fields.updateModelCs import updateModelCs
from tests.gql_types.CreateModelAInput import CreateModelAInput
from tests.gql_types.CreateModelGInput import CreateModelGInput
from tests.gql_types.CreateModelHInput import CreateModelHInput
from tests.gql_types.FilterModelAInput import FilterModelAInput
from tests.gql_types.FilterModelGInput import FilterModelGInput
from tests.gql_types.ModelAInput import ModelAInput
from tests.gql_types.ModelAType import ModelAType
from tests.gql_types.ModelGType import ModelGType
from tests.gql_types.OrderByModelAInput import OrderByModelAInput
from tests.gql_types.OrderByModelGInput import OrderByModelGInput
from tests.gql_types.UpdateModelAInput import UpdateModelAInput
from tests.gql_types.UpdateModelGInput import UpdateModelGInput
from tests.gql_types.UpdateModelHInput import UpdateModelHInput
from tests.models import ModelA, ModelC, ModelD, ModelE, ModelG
from tests.utils import Client, SchemaTestCase


class CruddalsModelSchemaTestTypes(SchemaTestCase):
    def test_model_type(self):
        self.run_test_graphql_type("ModelAType", ModelAType)

    def test_model_type_with_extra_field(self):
        self.run_test_graphql_type("ModelGType", ModelGType)

    def test_convert_not_registered_field_to_output_type(self):
        with pytest.raises(ValueError) as e:
            convert_django_field_to_output("field", None, None, None)
        assert (
            str(e.value)
            == "Don't know how to convert the Django field None (<class 'NoneType'>)"
        )

    def test_model_create_update_input_type(self):
        self.run_test_graphql_type("ModelAInput", ModelAInput, input_type=True)

    def test_model_create_input_type(self):
        self.run_test_graphql_type(
            "CreateModelAInput", CreateModelAInput, input_type=True
        )

    def test_model_create_input_type_with_extra_field(self):
        self.run_test_graphql_type(
            "CreateModelGInput", CreateModelGInput, input_type=True
        )

    def test_model_create_input_type_with_field_relation(self):
        self.run_test_graphql_type(
            "CreateModelHInput", CreateModelHInput, input_type=True
        )

    def test_model_update_input_type(self):
        self.run_test_graphql_type(
            "UpdateModelAInput", UpdateModelAInput, input_type=True
        )

    def test_model_update_input_type_with_field_relation(self):
        self.run_test_graphql_type(
            "UpdateModelHInput", UpdateModelHInput, input_type=True
        )

    def test_model_update_input_type_with_extra_field(self):
        self.run_test_graphql_type(
            "UpdateModelGInput", UpdateModelGInput, input_type=True
        )

    def test_convert_not_registered_field_to_input_type(self):
        with pytest.raises(ValueError) as e:
            convert_django_field_to_input("name", None, None, None)
        assert (
            str(e.value)
            == "Don't know how to convert the Django field None (<class 'NoneType'>)"
        )

    def test_model_where_input_type(self):
        self.run_test_graphql_type(
            "FilterModelAInput", FilterModelAInput, input_type=True
        )

    def test_model_where_input_type_with_extra_field(self):
        self.run_test_graphql_type(
            "FilterModelGInput", FilterModelGInput, input_type=True
        )

    def test_convert_not_registered_field_to_filter_input_type(self):
        with pytest.raises(ValueError) as e:
            convert_django_field_to_filter_input("name", None, None, None)
        assert (
            str(e.value)
            == "Don't know how to convert the Django field None (<class 'NoneType'>)"
        )

    def test_is_text_type_with_text_types(self):
        """Test that _is_text_type correctly identifies text types."""
        # Text types should return True
        assert _is_text_type(String) is True
        assert _is_text_type(Email) is True
        assert _is_text_type(Slug) is True
        assert _is_text_type(URL) is True
        assert _is_text_type(UUID) is True
        assert _is_text_type(IP) is True
        assert _is_text_type(IPv4) is True

    def test_is_text_type_with_non_text_types(self):
        """Test that _is_text_type correctly identifies non-text types."""
        # Non-text types should return False
        assert _is_text_type(Int) is False
        assert _is_text_type(Boolean) is False
        assert _is_text_type(Date) is False
        assert _is_text_type(DateTime) is False

    def test_filter_input_text_lookups_for_email_field(self):
        """Test that text lookups (startswith, istartswith, etc.) use String type for EmailField."""
        registry = get_global_registry()
        email_field = ModelA._meta.get_field("email_field_required")
        filter_input = convert_django_field_to_filter_input(
            "email_field_required", email_field, ModelA, registry
        )

        # Get the filter input type
        filter_type = type(filter_input)

        # Check that text lookups use String type
        assert hasattr(filter_type, "startswith")
        assert hasattr(filter_type, "istartswith")
        assert hasattr(filter_type, "contains")
        assert hasattr(filter_type, "icontains")

        # Verify the type is String (not Email) for text lookups
        startswith_field = filter_type._meta.fields.get("startswith")
        assert startswith_field is not None
        assert startswith_field.type == graphene.String

    def test_filter_input_text_lookups_for_slug_field(self):
        """Test that text lookups use String type for SlugField."""
        registry = get_global_registry()
        slug_field = ModelA._meta.get_field("slug_field_required")
        filter_input = convert_django_field_to_filter_input(
            "slug_field_required", slug_field, ModelA, registry
        )

        filter_type = type(filter_input)

        # Check that text lookups use String type
        assert hasattr(filter_type, "startswith")
        startswith_field = filter_type._meta.fields.get("startswith")
        assert startswith_field is not None
        assert startswith_field.type == graphene.String

    def test_filter_input_text_lookups_for_url_field(self):
        """Test that text lookups use String type for URLField."""
        registry = get_global_registry()
        url_field = ModelA._meta.get_field("url_field_required")
        filter_input = convert_django_field_to_filter_input(
            "url_field_required", url_field, ModelA, registry
        )

        filter_type = type(filter_input)

        # Check that text lookups use String type
        assert hasattr(filter_type, "startswith")
        startswith_field = filter_type._meta.fields.get("startswith")
        assert startswith_field is not None
        assert startswith_field.type == graphene.String

    def test_filter_input_non_text_lookups_for_integer_field(self):
        """Test that non-text lookups use the original type for IntegerField."""
        registry = get_global_registry()
        integer_field = ModelA._meta.get_field("integer_field_required")
        filter_input = convert_django_field_to_filter_input(
            "integer_field_required", integer_field, ModelA, registry
        )

        filter_type = type(filter_input)

        # Integer fields should not have text lookups available
        # (Django doesn't expose them for integer fields)
        # But if they did, they should use the original type
        # Check that exact lookup uses Int type
        assert hasattr(filter_type, "exact")
        exact_field = filter_type._meta.fields.get("exact")
        assert exact_field is not None
        assert exact_field.type == graphene.Int

    def test_model_order_by_input_type(self):
        self.run_test_graphql_type(
            "OrderByModelAInput", OrderByModelAInput, input_type=True
        )

    def test_model_order_by_input_type_with_extra_field(self):
        self.run_test_graphql_type(
            "OrderByModelGInput", OrderByModelGInput, input_type=True
        )

    def test_convert_not_registered_field_to_order_by_input_type(self):
        with pytest.raises(ValueError) as e:
            convert_django_field_to_order_by_input("name", None, None, None)
        assert (
            str(e.value)
            == "Don't know how to convert the Django field None (<class 'NoneType'>)"
        )

    def test_convert_not_registered_field_relation(self):
        with pytest.raises(ValueError) as e:
            convert_relation_field_to_input("name", None, None, None, "create")
        assert (
            str(e.value)
            == "Don't know how to convert the Django field None (<class 'NoneType'>), please check if it is a relation Field"
        )


class CruddalsModelSchemaTestFields(SchemaTestCase):
    def test_create_operation_field(self):
        self.run_test_graphql_field("createModelCs", "Mutation", createModelCs)

    def test_create_operation_field_with_field_relation(self):
        self.run_test_graphql_field("createModelHs", "Mutation", createModelHs)

    def test_read_operation_field(self):
        self.run_test_graphql_field("readModelC", "Query", readModelC)

    def test_update_operation_field(self):
        self.run_test_graphql_field("updateModelCs", "Mutation", updateModelCs)

    def test_delete_operation_field(self):
        self.run_test_graphql_field("deleteModelCs", "Mutation", deleteModelCs)

    def test_deactivate_operation_field(self):
        self.run_test_graphql_field("deactivateModelCs", "Mutation", deactivateModelCs)

    def test_activate_operation_field(self):
        self.run_test_graphql_field("activateModelCs", "Mutation", activateModelCs)

    def test_list_operation_field(self):
        self.run_test_graphql_field("listModelCs", "Query", listModelCs)

    def test_search_operation_fiel(self):
        self.run_test_graphql_field("searchModelCs", "Query", searchModelCs)


class TestInternalGetObjectsModelG(SchemaTestCase):
    def test_get_objects_model_g(self):
        client = Client()

        variables = {"input": [{"name": "MODEL G NAME"}]}
        expected_response = {
            "data": {
                "createModelGs": {
                    "objects": [
                        {
                            "id": "1",
                            "name": "MODEL G NAME",
                            "paginatedForeignKeyHRelated": {"objects": []},
                        },
                    ],
                    "errorsReport": None,
                }
            }
        }
        response = client.query(create_model_g_mutation, variables=variables).json()
        self.verify_response(response, expected_response, message="CREATE ModelG")

        # region READ ModelG using get_objects
        variables = {"where": {"id": {"exact": "1"}}}
        expected_response = {
            "data": {
                "readModelG": {
                    "id": "2",
                    "name": "MODEL G FROM GET OBJECTS",
                    "paginatedForeignKeyHRelated": {"objects": []},
                }
            }
        }
        response = client.query(read_model_g_query, variables=variables).json()
        self.verify_response(response, expected_response, message="READ ModelG")
        # endregion

        # region SEARCH ModelG using get_objects
        variables = {"where": {"id": {"exact": "1"}}}
        expected_response = {
            "data": {
                "searchModelGs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "2",
                            "name": "MODEL G FROM GET OBJECTS",
                            "paginatedForeignKeyHRelated": {"objects": []},
                        },
                        {
                            "id": "3",
                            "name": "MODEL G FROM GET OBJECTS",
                            "paginatedForeignKeyHRelated": {"objects": []},
                        },
                    ],
                }
            }
        }
        response = client.query(search_model_g_query, variables=variables).json()
        self.verify_response(response, expected_response, message="READ ModelG")
        # endregion


class TestGetObjectsReceivesArguments(SchemaTestCase):
    """Test that get_objects hook receives arguments (where, order_by, etc.) correctly."""

    def test_get_objects_receives_arguments(self):
        # Create test objects
        ModelG.objects.all().delete()
        ModelG.objects.create(name="Test A")
        ModelG.objects.create(name="Test B")
        ModelG.objects.create(name="Test C")

        # Get the ObjectType for ModelG from the schema
        registry = get_global_registry()
        registries_for_model = registry.get_registry_for_model(ModelG)
        object_type = registries_for_model["object_type"]

        # Store original get_objects
        original_get_objects = object_type.get_objects

        # Track arguments passed to get_objects
        captured_args = {}

        def mock_get_objects(queryset, info, **kwargs):
            """Mock get_objects that captures arguments and returns original queryset."""
            captured_args["kwargs"] = kwargs
            captured_args["queryset_count"] = queryset.count()
            # Return the original queryset to not break existing behavior
            return queryset

        # Temporarily replace get_objects
        object_type.get_objects = mock_get_objects

        try:
            client = Client()

            # Test with where and order_by arguments
            variables = {
                "where": {"name": {"icontains": "Test"}},
                "orderBy": {"name": "DESC"},
            }

            query = """
            query searchModelGs($where: FilterModelGInput $orderBy: OrderByModelGInput) {
                searchModelGs(where: $where orderBy: $orderBy) {
                    total
                    objects {
                        id
                        name
                    }
                }
            }
            """

            response = client.query(query, variables=variables).json()

            # Verify the query was successful
            self.assertIn("data", response)
            self.assertIn("searchModelGs", response["data"])

            # Verify that get_objects was called with the correct arguments
            self.assertIn("kwargs", captured_args)
            self.assertIn("where", captured_args["kwargs"])
            # Note: orderBy is normalized to order_by in the arguments
            self.assertIn("order_by", captured_args["kwargs"])

            # Verify where argument structure
            where_arg = captured_args["kwargs"]["where"]
            self.assertIn("name", where_arg)
            self.assertIn("icontains", where_arg["name"])
            self.assertEqual(where_arg["name"]["icontains"], "Test")

            # Verify order_by argument (normalized from orderBy)
            order_by_arg = captured_args["kwargs"]["order_by"]
            self.assertIn("name", order_by_arg)
            # The value might be an Enum, so we check the string representation
            order_by_value = str(order_by_arg["name"])
            self.assertIn("DESC", order_by_value)

        finally:
            # Restore original get_objects
            object_type.get_objects = original_get_objects


class TestModifyArgumentsModelHCruddalsInterface(SchemaTestCase):
    def test_modify_arguments(self):
        client = Client()

        variables = {"input": [{"name": "MODEL H NAME 1"}, {"name": "MODEL H NAME 2"}]}
        expected_response = {
            "data": {
                "createModelHs": {
                    "objects": [
                        {"id": "1", "name": "MODEL H NAME 1", "foreignKeyField": None},
                        {
                            "id": "2",
                            "name": "MODEL H NAME 2",
                            "foreignKeyField": None,
                        },
                    ],
                    "errorsReport": None,
                }
            }
        }
        response = client.query(create_model_h_mutation, variables=variables).json()
        self.verify_response(response, expected_response, message="CREATE ModelH")

        # region READ ModelH modify argument "where"
        variables = {"me": True, "where": {"id": {"exact": "1"}}}
        expected_response = {
            "data": {
                "readModelH": {
                    "id": "2",
                    "name": "MODEL H NAME 2",
                    "foreignKeyField": None,
                }
            }
        }
        response = client.query(read_model_h_query, variables=variables).json()
        self.verify_response(response, expected_response, message="READ ModelH")
        # endregion


class TestReadModelDWithRelatedField(SchemaTestCase):
    def test_read_model_d_with_related_field(self):
        client = Client()

        model_c = ModelC.objects.create(char_field="MODEL C CHAR FIELD")
        model_d = ModelD.objects.create(foreign_key_field=model_c)
        model_e = ModelE.objects.create(foreign_key_field_without_related_name=model_d)

        # region READ ModelD
        variables = {"where": {"id": {"exact": model_d.id}}}
        expected_response = {
            "data": {
                "readModelD": {
                    "id": str(model_d.id),
                    "paginatedModele": {"objects": [{"id": str(model_e.id)}]},
                }
            }
        }
        query = """
        query readModelD($where: FilterModelDInput!) {
            readModelD(where: $where) {
                id
                paginatedModele {
                    objects {
                        id
                    }
                    }
                }
            }
        """
        response = client.query(query, variables=variables).json()
        self.verify_response(response, expected_response, message="READ ModelD")
        # endregion


class CruddalsModelSchemaTestResolvers(SchemaTestCase):
    def test_cruddals_model_c(self):
        client = Client()

        # region CREATE ModelC
        variables = {"input": objs_to_create_type_c}
        expected_response = {
            "data": {
                "createModelCs": {
                    "objects": [
                        {
                            "id": "1",
                            "charField": "AAA",
                            "integerField": 1,
                            "booleanField": True,
                            "dateTimeField": "2021-01-01T00:00:00+00:00",
                            "jsonField": '{"key": "value"}',
                            "fileField": "",
                            "isActive": True,
                            "oneToOneField": None,
                            "paginatedManyToManyField": {"objects": []},
                            "paginatedForeignKeyDRelated": {"objects": []},
                        },
                        {
                            "id": "2",
                            "charField": "BBB",
                            "integerField": 2,
                            "booleanField": False,
                            "dateTimeField": "2021-02-02T00:00:00+00:00",
                            "jsonField": '{"key": "value"}',
                            "fileField": "",
                            "isActive": True,
                            "oneToOneField": None,
                            "paginatedManyToManyField": {"objects": []},
                            "paginatedForeignKeyDRelated": {"objects": []},
                        },
                        {
                            "id": "3",
                            "charField": "CCC",
                            "integerField": 3,
                            "booleanField": True,
                            "dateTimeField": "2021-03-03T00:00:00+00:00",
                            "jsonField": '{"key": "value"}',
                            "fileField": "",
                            "isActive": True,
                            "oneToOneField": None,
                            "paginatedManyToManyField": {"objects": []},
                            "paginatedForeignKeyDRelated": {"objects": []},
                        },
                        {
                            "id": "4",
                            "charField": "DDD",
                            "integerField": 4,
                            "booleanField": False,
                            "dateTimeField": "2021-04-04T00:00:00+00:00",
                            "jsonField": '{"key": "value"}',
                            "fileField": "",
                            "isActive": True,
                            "oneToOneField": None,
                            "paginatedManyToManyField": {"objects": []},
                            "paginatedForeignKeyDRelated": {"objects": []},
                        },
                        {
                            "id": "5",
                            "charField": "EEE",
                            "integerField": 5,
                            "booleanField": True,
                            "dateTimeField": "2021-05-05T00:00:00+00:00",
                            "jsonField": '{"key": "value"}',
                            "fileField": "",
                            "isActive": True,
                            "oneToOneField": None,
                            "paginatedManyToManyField": {"objects": []},
                            "paginatedForeignKeyDRelated": {"objects": []},
                        },
                        {
                            "id": "6",
                            "charField": "aaa",
                            "integerField": 1,
                            "booleanField": True,
                            "dateTimeField": "2021-01-01T00:00:00+00:00",
                            "jsonField": '{"key": "value"}',
                            "fileField": "",
                            "isActive": True,
                            "oneToOneField": None,
                            "paginatedManyToManyField": {"objects": []},
                            "paginatedForeignKeyDRelated": {"objects": []},
                        },
                        {
                            "id": "7",
                            "charField": "bbb",
                            "integerField": 2,
                            "booleanField": False,
                            "dateTimeField": "2021-02-02T00:00:00+00:00",
                            "jsonField": '{"key": "value"}',
                            "fileField": "",
                            "isActive": True,
                            "oneToOneField": None,
                            "paginatedManyToManyField": {"objects": []},
                            "paginatedForeignKeyDRelated": {"objects": []},
                        },
                        {
                            "id": "8",
                            "charField": "ccc",
                            "integerField": 3,
                            "booleanField": True,
                            "dateTimeField": "2021-03-03T00:00:00+00:00",
                            "jsonField": '{"key": "value"}',
                            "fileField": "",
                            "isActive": True,
                            "oneToOneField": None,
                            "paginatedManyToManyField": {"objects": []},
                            "paginatedForeignKeyDRelated": {"objects": []},
                        },
                        {
                            "id": "9",
                            "charField": "ddd",
                            "integerField": 4,
                            "booleanField": False,
                            "dateTimeField": "2021-04-04T00:00:00+00:00",
                            "jsonField": '{"key": "value"}',
                            "fileField": "",
                            "isActive": True,
                            "oneToOneField": None,
                            "paginatedManyToManyField": {"objects": []},
                            "paginatedForeignKeyDRelated": {"objects": []},
                        },
                        {
                            "id": "10",
                            "charField": "eee",
                            "integerField": 5,
                            "booleanField": True,
                            "dateTimeField": "2021-05-05T00:00:00+00:00",
                            "jsonField": '{"key": "value"}',
                            "fileField": "",
                            "isActive": True,
                            "oneToOneField": None,
                            "paginatedManyToManyField": {"objects": []},
                            "paginatedForeignKeyDRelated": {"objects": []},
                        },
                    ],
                    "errorsReport": None,
                }
            }
        }
        response = client.query(create_model_c_mutation, variables=variables).json()
        self.verify_response(response, expected_response, message="CREATE ModelC")
        # endregion

        # region READ ModelC
        variables = {"where": {"id": {"exact": "1"}}}
        expected_response = {
            "data": {
                "readModelC": {
                    "id": "1",
                    "charField": "AAA",
                    "integerField": 1,
                    "booleanField": True,
                    "dateTimeField": "2021-01-01T00:00:00+00:00",
                    "jsonField": '{"key": "value"}',
                    "fileField": "",
                    "isActive": True,
                    "oneToOneField": None,
                    "paginatedManyToManyField": {"objects": []},
                    "paginatedForeignKeyDRelated": {"objects": []},
                }
            }
        }
        response = client.query(read_model_c_query, variables=variables).json()
        self.verify_response(response, expected_response, message="READ ModelC")
        # endregion

        # region UPDATE ModelC
        variables = {"input": [{"id": "1", "charField": "UPDATED"}]}
        expected_response = {
            "data": {
                "updateModelCs": {
                    "objects": [
                        {
                            "id": "1",
                            "charField": "UPDATED",
                            "integerField": 1,
                            "booleanField": True,
                            "dateTimeField": "2021-01-01T00:00:00+00:00",
                            "jsonField": '{"key": "value"}',
                            "fileField": "",
                            "isActive": True,
                            "oneToOneField": None,
                            "paginatedManyToManyField": {"objects": []},
                            "paginatedForeignKeyDRelated": {"objects": []},
                        }
                    ],
                    "errorsReport": None,
                }
            }
        }
        response = client.query(update_model_c_mutation, variables=variables).json()
        self.verify_response(response, expected_response, message="UPDATE ModelC")
        # endregion

        # region DEACTIVATE ModelC
        variables = {"where": {"id": {"exact": "1"}}}
        expected_response = {
            "data": {
                "deactivateModelCs": {
                    "objects": [
                        {
                            "id": "1",
                            "charField": "UPDATED",
                            "integerField": 1,
                            "booleanField": True,
                            "dateTimeField": "2021-01-01T00:00:00+00:00",
                            "jsonField": '{"key": "value"}',
                            "fileField": "",
                            "isActive": False,
                            "oneToOneField": None,
                            "paginatedManyToManyField": {"objects": []},
                            "paginatedForeignKeyDRelated": {"objects": []},
                        }
                    ],
                    "errorsReport": None,
                }
            }
        }
        response = client.query(deactivate_model_c_mutation, variables=variables).json()
        self.verify_response(response, expected_response, message="DEACTIVATE ModelC")
        # endregion

        # region ACTIVATE ModelC
        variables = {"where": {"id": {"exact": "1"}}}
        expected_response = {
            "data": {
                "activateModelCs": {
                    "objects": [
                        {
                            "id": "1",
                            "charField": "UPDATED",
                            "integerField": 1,
                            "booleanField": True,
                            "dateTimeField": "2021-01-01T00:00:00+00:00",
                            "jsonField": '{"key": "value"}',
                            "fileField": "",
                            "isActive": True,
                            "oneToOneField": None,
                            "paginatedManyToManyField": {"objects": []},
                            "paginatedForeignKeyDRelated": {"objects": []},
                        }
                    ],
                    "errorsReport": None,
                }
            }
        }
        response = client.query(activate_model_c_mutation, variables=variables).json()
        self.verify_response(response, expected_response, message="ACTIVATE ModelC")
        # endregion

        # region DELETE ModelC
        variables = {"where": {"id": {"exact": "1"}}}
        expected_response = {
            "data": {
                "deleteModelCs": {
                    "success": True,
                    "objects": None,
                    "errorsReport": None,
                }
            }
        }
        response = client.query(delete_model_c_mutation, variables=variables).json()
        self.verify_response(response, expected_response, message="DELETE ModelC")
        # endregion

        # region LIST ModelC
        expected_response = {
            "data": {
                "listModelCs": [
                    {
                        "id": "2",
                        "charField": "BBB",
                        "integerField": 2,
                        "booleanField": False,
                        "dateTimeField": "2021-02-02T00:00:00+00:00",
                        "jsonField": '{"key": "value"}',
                        "fileField": "",
                        "isActive": True,
                        "oneToOneField": None,
                        "paginatedManyToManyField": {"objects": []},
                        "paginatedForeignKeyDRelated": {"objects": []},
                    },
                    {
                        "id": "3",
                        "charField": "CCC",
                        "integerField": 3,
                        "booleanField": True,
                        "dateTimeField": "2021-03-03T00:00:00+00:00",
                        "jsonField": '{"key": "value"}',
                        "fileField": "",
                        "isActive": True,
                        "oneToOneField": None,
                        "paginatedManyToManyField": {"objects": []},
                        "paginatedForeignKeyDRelated": {"objects": []},
                    },
                    {
                        "id": "4",
                        "charField": "DDD",
                        "integerField": 4,
                        "booleanField": False,
                        "dateTimeField": "2021-04-04T00:00:00+00:00",
                        "jsonField": '{"key": "value"}',
                        "fileField": "",
                        "isActive": True,
                        "oneToOneField": None,
                        "paginatedManyToManyField": {"objects": []},
                        "paginatedForeignKeyDRelated": {"objects": []},
                    },
                    {
                        "id": "5",
                        "charField": "EEE",
                        "integerField": 5,
                        "booleanField": True,
                        "dateTimeField": "2021-05-05T00:00:00+00:00",
                        "jsonField": '{"key": "value"}',
                        "fileField": "",
                        "isActive": True,
                        "oneToOneField": None,
                        "paginatedManyToManyField": {"objects": []},
                        "paginatedForeignKeyDRelated": {"objects": []},
                    },
                    {
                        "id": "6",
                        "charField": "aaa",
                        "integerField": 1,
                        "booleanField": True,
                        "dateTimeField": "2021-01-01T00:00:00+00:00",
                        "jsonField": '{"key": "value"}',
                        "fileField": "",
                        "isActive": True,
                        "oneToOneField": None,
                        "paginatedManyToManyField": {"objects": []},
                        "paginatedForeignKeyDRelated": {"objects": []},
                    },
                    {
                        "id": "7",
                        "charField": "bbb",
                        "integerField": 2,
                        "booleanField": False,
                        "dateTimeField": "2021-02-02T00:00:00+00:00",
                        "jsonField": '{"key": "value"}',
                        "fileField": "",
                        "isActive": True,
                        "oneToOneField": None,
                        "paginatedManyToManyField": {"objects": []},
                        "paginatedForeignKeyDRelated": {"objects": []},
                    },
                    {
                        "id": "8",
                        "charField": "ccc",
                        "integerField": 3,
                        "booleanField": True,
                        "dateTimeField": "2021-03-03T00:00:00+00:00",
                        "jsonField": '{"key": "value"}',
                        "fileField": "",
                        "isActive": True,
                        "oneToOneField": None,
                        "paginatedManyToManyField": {"objects": []},
                        "paginatedForeignKeyDRelated": {"objects": []},
                    },
                    {
                        "id": "9",
                        "charField": "ddd",
                        "integerField": 4,
                        "booleanField": False,
                        "dateTimeField": "2021-04-04T00:00:00+00:00",
                        "jsonField": '{"key": "value"}',
                        "fileField": "",
                        "isActive": True,
                        "oneToOneField": None,
                        "paginatedManyToManyField": {"objects": []},
                        "paginatedForeignKeyDRelated": {"objects": []},
                    },
                    {
                        "id": "10",
                        "charField": "eee",
                        "integerField": 5,
                        "booleanField": True,
                        "dateTimeField": "2021-05-05T00:00:00+00:00",
                        "jsonField": '{"key": "value"}',
                        "fileField": "",
                        "isActive": True,
                        "oneToOneField": None,
                        "paginatedManyToManyField": {"objects": []},
                        "paginatedForeignKeyDRelated": {"objects": []},
                    },
                ]
            }
        }
        response = client.query(list_model_c_query).json()
        self.verify_response(response, expected_response, message="LIST ModelC")
        # endregion

        # region SEARCH ModelC
        # region Test search with no filters
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 9,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 9,
                    "objects": [
                        {"id": "2"},
                        {"id": "3"},
                        {"id": "4"},
                        {"id": "5"},
                        {"id": "6"},
                        {"id": "7"},
                        {"id": "8"},
                        {"id": "9"},
                        {"id": "10"},
                    ],
                }
            }
        }
        response = client.query(search_model_c_query).json()
        self.verify_response(
            response, expected_response, message="SEARCH with no filters ModelC"
        )
        # endregion

        # region Test search with pagination
        variables = {"paginationConfig": {"page": 1, "itemsPerPage": 2}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 9,
                    "page": 1,
                    "pages": 5,
                    "hasNext": True,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "2",
                        },
                        {
                            "id": "3",
                        },
                    ],
                }
            }
        }
        response = client.query(search_model_c_query, variables=variables).json()
        self.verify_response(
            response, expected_response, message="SEARCH with pagination 1 ModelC"
        )

        variables = {"paginationConfig": {"page": 2, "itemsPerPage": 2}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 9,
                    "page": 2,
                    "pages": 5,
                    "hasNext": True,
                    "hasPrev": True,
                    "indexStart": 3,
                    "indexEnd": 4,
                    "objects": [
                        {
                            "id": "4",
                        },
                        {
                            "id": "5",
                        },
                    ],
                }
            }
        }
        response = client.query(search_model_c_query, variables=variables).json()
        self.verify_response(
            response, expected_response, message="SEARCH with pagination 2 ModelC"
        )

        variables = {"paginationConfig": {"page": 5, "itemsPerPage": 2}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 9,
                    "page": 5,
                    "pages": 5,
                    "hasNext": False,
                    "hasPrev": True,
                    "indexStart": 9,
                    "indexEnd": 9,
                    "objects": [
                        {
                            "id": "10",
                        }
                    ],
                }
            }
        }
        response = client.query(search_model_c_query, variables=variables).json()
        self.verify_response(
            response, expected_response, message="SEARCH with pagination 3 ModelC"
        )
        # endregion

        # region Test search with order by
        variables = {"orderBy": {"charField": "DESC"}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 9,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 9,
                    "objects": [
                        {
                            "id": "10",
                            "charField": "eee",
                        },
                        {
                            "id": "9",
                            "charField": "ddd",
                        },
                        {
                            "id": "8",
                            "charField": "ccc",
                        },
                        {
                            "id": "7",
                            "charField": "bbb",
                        },
                        {
                            "id": "6",
                            "charField": "aaa",
                        },
                        {
                            "id": "5",
                            "charField": "EEE",
                        },
                        {
                            "id": "4",
                            "charField": "DDD",
                        },
                        {
                            "id": "3",
                            "charField": "CCC",
                        },
                        {
                            "id": "2",
                            "charField": "BBB",
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id charField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with order by DESC ModelC"
        )

        variables = {"orderBy": {"charField": "IDESC"}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 9,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 9,
                    "objects": [
                        {
                            "id": "5",
                            "charField": "EEE",
                        },
                        {
                            "id": "10",
                            "charField": "eee",
                        },
                        {
                            "id": "4",
                            "charField": "DDD",
                        },
                        {
                            "id": "9",
                            "charField": "ddd",
                        },
                        {
                            "id": "3",
                            "charField": "CCC",
                        },
                        {
                            "id": "8",
                            "charField": "ccc",
                        },
                        {
                            "id": "2",
                            "charField": "BBB",
                        },
                        {
                            "id": "7",
                            "charField": "bbb",
                        },
                        {
                            "id": "6",
                            "charField": "aaa",
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id charField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with order by IDESC ModelC"
        )
        # endregion

        # region Test search with filters

        # region CharField
        # - charField.exact
        variables = {"where": {"charField": {"exact": "BBB"}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 1,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 1,
                    "objects": [
                        {
                            "id": "2",
                            "charField": "BBB",
                        }
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id charField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters exact ModelC"
        )

        # - charField.iexact
        variables = {"where": {"charField": {"iexact": "BBB"}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "2",
                            "charField": "BBB",
                        },
                        {
                            "id": "7",
                            "charField": "bbb",
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id charField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters iexact ModelC"
        )

        # - charField.lte
        # - charField.lt
        # - charField.gte
        # - charField.gt

        # - charField.in
        variables = {"where": {"charField": {"in": ["CCC", "EEE"]}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "3",
                            "charField": "CCC",
                        },
                        {
                            "id": "5",
                            "charField": "EEE",
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id charField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters in ModelC"
        )

        # ===> - charField.contains SQLite doesn’t support case-sensitive LIKE statements; contains acts like icontains for SQLite
        variables = {"where": {"charField": {"contains": "B"}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "2",
                            "charField": "BBB",
                        },
                        {
                            "id": "7",
                            "charField": "bbb",
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id charField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters contains ModelC"
        )

        # - charField.icontains
        variables = {"where": {"charField": {"icontains": "b"}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "2",
                            "charField": "BBB",
                        },
                        {
                            "id": "7",
                            "charField": "bbb",
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id charField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters icontains ModelC"
        )

        # - charField.startswith SQLite doesn’t support case-sensitive LIKE statements; startswith acts like istartswith for SQLite.
        variables = {"where": {"charField": {"startswith": "C"}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "3",
                            "charField": "CCC",
                        },
                        {
                            "id": "8",
                            "charField": "ccc",
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id charField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters startswith ModelC"
        )

        # - charField.istartswith
        variables = {"where": {"charField": {"istartswith": "c"}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "3",
                            "charField": "CCC",
                        },
                        {
                            "id": "8",
                            "charField": "ccc",
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id charField"), variables=variables
        ).json()
        self.verify_response(
            response,
            expected_response,
            message="SEARCH with filters istartswith ModelC",
        )

        # - charField.endswith SQLite doesn’t support case-sensitive LIKE statements; endswith acts like iendswith for SQLite.
        variables = {"where": {"charField": {"endswith": "E"}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "5",
                            "charField": "EEE",
                        },
                        {
                            "id": "10",
                            "charField": "eee",
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id charField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters endswith ModelC"
        )

        # - charField.iendswith
        variables = {"where": {"charField": {"iendswith": "E"}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "5",
                            "charField": "EEE",
                        },
                        {
                            "id": "10",
                            "charField": "eee",
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id charField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters iendswith ModelC"
        )

        # - charField.range
        variables = {"where": {"charField": {"range": ["CCC", "EEE"]}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 3,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 3,
                    "objects": [
                        {
                            "id": "3",
                            "charField": "CCC",
                        },
                        {
                            "id": "4",
                            "charField": "DDD",
                        },
                        {
                            "id": "5",
                            "charField": "EEE",
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id charField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters range ModelC"
        )

        # - charField.isnull
        variables = {"where": {"charField": {"isnull": False}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 9,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 9,
                    "objects": [
                        {"id": "2"},
                        {"id": "3"},
                        {"id": "4"},
                        {"id": "5"},
                        {"id": "6"},
                        {"id": "7"},
                        {"id": "8"},
                        {"id": "9"},
                        {"id": "10"},
                    ],
                }
            }
        }
        response = client.query(search_model_c_query, variables=variables).json()
        self.verify_response(
            response,
            expected_response,
            message="SEARCH with filters charfield isnull False ModelC",
        )

        variables = {"where": {"charField": {"isnull": True}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 0,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 0,
                    "indexEnd": 0,
                    "objects": [],
                }
            }
        }
        response = client.query(search_model_c_query, variables=variables).json()
        self.verify_response(
            response,
            expected_response,
            message="SEARCH with filters isnull True ModelC",
        )

        # - charField.regex
        variables = {"where": {"charField": {"regex": "^C"}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 1,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 1,
                    "objects": [
                        {
                            "id": "3",
                            "charField": "CCC",
                        }
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id charField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters regex ModelC"
        )

        # - charField.iregex
        variables = {"where": {"charField": {"iregex": "^c"}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "3",
                            "charField": "CCC",
                        },
                        {
                            "id": "8",
                            "charField": "ccc",
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id charField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters iregex ModelC"
        )

        # endregion

        # region IntegerField
        # - integerField.exact
        variables = {"where": {"integerField": {"exact": 2}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "2",
                            "integerField": 2,
                        },
                        {
                            "id": "7",
                            "integerField": 2,
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id integerField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters exact ModelC"
        )

        # - integerField.iexact
        variables = {"where": {"integerField": {"iexact": 2}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "2",
                            "integerField": 2,
                        },
                        {
                            "id": "7",
                            "integerField": 2,
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id integerField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters iexact ModelC"
        )

        # - integerField.gt
        variables = {"where": {"integerField": {"gt": 3}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 4,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 4,
                    "objects": [
                        {
                            "id": "4",
                            "integerField": 4,
                        },
                        {
                            "id": "5",
                            "integerField": 5,
                        },
                        {
                            "id": "9",
                            "integerField": 4,
                        },
                        {
                            "id": "10",
                            "integerField": 5,
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id integerField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters gt ModelC"
        )

        # - integerField.gte
        variables = {"where": {"integerField": {"gte": 3}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 6,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 6,
                    "objects": [
                        {
                            "id": "3",
                            "integerField": 3,
                        },
                        {
                            "id": "4",
                            "integerField": 4,
                        },
                        {
                            "id": "5",
                            "integerField": 5,
                        },
                        {
                            "id": "8",
                            "integerField": 3,
                        },
                        {
                            "id": "9",
                            "integerField": 4,
                        },
                        {
                            "id": "10",
                            "integerField": 5,
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id integerField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters gte ModelC"
        )

        # - integerField.lt
        variables = {"where": {"integerField": {"lt": 3}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 3,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 3,
                    "objects": [
                        {
                            "id": "2",
                            "integerField": 2,
                        },
                        {
                            "id": "6",
                            "integerField": 1,
                        },
                        {
                            "id": "7",
                            "integerField": 2,
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id integerField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters lt ModelC"
        )

        # - integerField.lte
        variables = {"where": {"integerField": {"lte": 3}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 5,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 5,
                    "objects": [
                        {
                            "id": "2",
                            "integerField": 2,
                        },
                        {
                            "id": "3",
                            "integerField": 3,
                        },
                        {
                            "id": "6",
                            "integerField": 1,
                        },
                        {
                            "id": "7",
                            "integerField": 2,
                        },
                        {
                            "id": "8",
                            "integerField": 3,
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id integerField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters lte ModelC"
        )

        # - integerField.in
        variables = {"where": {"integerField": {"in": [3, 5]}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 4,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 4,
                    "objects": [
                        {
                            "id": "3",
                            "integerField": 3,
                        },
                        {
                            "id": "5",
                            "integerField": 5,
                        },
                        {
                            "id": "8",
                            "integerField": 3,
                        },
                        {
                            "id": "10",
                            "integerField": 5,
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id integerField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters in ModelC"
        )

        # - integerField.contains
        variables = {"where": {"integerField": {"contains": 2}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "2",
                            "integerField": 2,
                        },
                        {
                            "id": "7",
                            "integerField": 2,
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id integerField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters contains ModelC"
        )

        # - integerField.icontains
        variables = {"where": {"integerField": {"icontains": 2}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "2",
                            "integerField": 2,
                        },
                        {
                            "id": "7",
                            "integerField": 2,
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id integerField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters icontains ModelC"
        )

        # - integerField.startswith
        variables = {"where": {"integerField": {"startswith": 2}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "2",
                            "integerField": 2,
                        },
                        {
                            "id": "7",
                            "integerField": 2,
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id integerField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters startswith ModelC"
        )

        # - integerField.istartswith
        variables = {"where": {"integerField": {"istartswith": 2}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "2",
                            "integerField": 2,
                        },
                        {
                            "id": "7",
                            "integerField": 2,
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id integerField"), variables=variables
        ).json()
        self.verify_response(
            response,
            expected_response,
            message="SEARCH with filters istartswith ModelC",
        )

        # - integerField.endswith
        variables = {"where": {"integerField": {"endswith": 2}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "2",
                            "integerField": 2,
                        },
                        {
                            "id": "7",
                            "integerField": 2,
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id integerField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters endswith ModelC"
        )

        # - integerField.iendswith
        variables = {"where": {"integerField": {"iendswith": 2}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "2",
                            "integerField": 2,
                        },
                        {
                            "id": "7",
                            "integerField": 2,
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id integerField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters iendswith ModelC"
        )

        # - integerField.range
        variables = {"where": {"integerField": {"range": [3, 5]}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 6,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 6,
                    "objects": [
                        {
                            "id": "3",
                            "integerField": 3,
                        },
                        {
                            "id": "4",
                            "integerField": 4,
                        },
                        {
                            "id": "5",
                            "integerField": 5,
                        },
                        {
                            "id": "8",
                            "integerField": 3,
                        },
                        {
                            "id": "9",
                            "integerField": 4,
                        },
                        {
                            "id": "10",
                            "integerField": 5,
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id integerField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters range ModelC"
        )

        # - integerField.isnull
        variables = {"where": {"integerField": {"isnull": False}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 9,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 9,
                    "objects": [
                        {"id": "2"},
                        {"id": "3"},
                        {"id": "4"},
                        {"id": "5"},
                        {"id": "6"},
                        {"id": "7"},
                        {"id": "8"},
                        {"id": "9"},
                        {"id": "10"},
                    ],
                }
            }
        }
        response = client.query(search_model_c_query, variables=variables).json()
        self.verify_response(
            response,
            expected_response,
            message="SEARCH with filters integer isnull False ModelC",
        )

        variables = {"where": {"integerField": {"isnull": True}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 0,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 0,
                    "indexEnd": 0,
                    "objects": [],
                }
            }
        }
        response = client.query(search_model_c_query, variables=variables).json()
        self.verify_response(
            response,
            expected_response,
            message="SEARCH with filters isnull True ModelC",
        )

        # - integerField.regex
        variables = {"where": {"integerField": {"regex": "^3"}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "3",
                            "integerField": 3,
                        },
                        {
                            "id": "8",
                            "integerField": 3,
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id integerField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters regex ModelC"
        )

        # - integerField.iregex
        variables = {"where": {"integerField": {"iregex": "^3"}}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "3",
                            "integerField": 3,
                        },
                        {
                            "id": "8",
                            "integerField": 3,
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id integerField"), variables=variables
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with filters iregex ModelC"
        )
        # endregion
        # endregion

        # region Test search with more than one filter
        variables = {
            "where": {"charField": {"icontains": "b"}, "integerField": {"exact": 3}}
        }
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 0,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 0,
                    "indexEnd": 0,
                    "objects": [],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id charField integerField"),
            variables=variables,
        ).json()
        self.verify_response(
            response,
            expected_response,
            message="SEARCH with more than one filter ModelC",
        )

        variables = {
            "where": {"charField": {"icontains": "b"}, "integerField": {"exact": 2}}
        }
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "2",
                            "charField": "BBB",
                            "integerField": 2,
                        },
                        {
                            "id": "7",
                            "charField": "bbb",
                            "integerField": 2,
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id charField integerField"),
            variables=variables,
        ).json()
        self.verify_response(
            response,
            expected_response,
            message="SEARCH with more than one filter ModelC",
        )

        # endregion

        # region Test search with operator AND
        variables = {
            "where": {
                "charField": {"icontains": "c"},
                "AND": {"integerField": {"lte": 3}},
            }
        }
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "3",
                            "charField": "CCC",
                            "integerField": 3,
                        },
                        {
                            "id": "8",
                            "charField": "ccc",
                            "integerField": 3,
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id charField integerField"),
            variables=variables,
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with operator AND ModelC"
        )
        # endregion

        # region Test search with operator OR
        variables = {
            "where": {
                "charField": {"icontains": "c"},
                "OR": {"integerField": {"lt": 3}},
            }
        }
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 5,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 5,
                    "objects": [
                        {
                            "id": "2",
                            "charField": "BBB",
                            "integerField": 2,
                        },
                        {
                            "id": "3",
                            "charField": "CCC",
                            "integerField": 3,
                        },
                        {
                            "id": "6",
                            "charField": "aaa",
                            "integerField": 1,
                        },
                        {
                            "id": "7",
                            "charField": "bbb",
                            "integerField": 2,
                        },
                        {
                            "id": "8",
                            "charField": "ccc",
                            "integerField": 3,
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_c_query.replace("id", "id charField integerField"),
            variables=variables,
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with operator OR ModelC"
        )

        # endregion
        # endregion

        # region CREATE ModelD
        variables = {"input": objs_to_create_type_d}
        expected_response = {
            "data": {
                "createModelDs": {
                    "objects": [
                        {
                            "id": "1",
                            "foreignKeyField": {
                                "id": "2",
                            },
                            "oneToOneCRelated": None,
                            "paginatedManyToManyCRelated": {"objects": []},
                            "paginatedForeignKeyERelated": {"objects": []},
                        },
                        {
                            "id": "2",
                            "foreignKeyField": {
                                "id": "3",
                            },
                            "oneToOneCRelated": None,
                            "paginatedManyToManyCRelated": {"objects": []},
                            "paginatedForeignKeyERelated": {"objects": []},
                        },
                    ],
                    "errorsReport": None,
                }
            }
        }
        response = client.query(create_model_d_mutation, variables=variables).json()
        self.verify_response(response, expected_response, message="CREATE ModelD")
        # endregion

        # region SEARCH ModelD
        # region Test search with relation fields
        variables = {"where": {"foreignKeyField": {"charField": {"exact": "BBB"}}}}
        expected_response = {
            "data": {
                "searchModelDs": {
                    "total": 1,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 1,
                    "objects": [
                        {
                            "id": "1",
                            "foreignKeyField": {
                                "id": "2",
                                "charField": "BBB",
                            },
                        }
                    ],
                }
            }
        }
        response = client.query(
            search_model_d_query.replace("id", "id foreignKeyField{id charField}"),
            variables=variables,
        ).json()
        self.verify_response(
            response, expected_response, message="SEARCH with relation fields ModelD"
        )

        # region Test search with operator AND and relations
        variables = {
            "where": {
                "foreignKeyField": {"charField": {"icontains": "b"}},
                "AND": [{"foreignKeyField": {"integerField": {"exact": 2}}}],
            }
        }
        expected_response = {
            "data": {
                "searchModelDs": {
                    "total": 1,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 1,
                    "objects": [
                        {
                            "id": "1",
                            "foreignKeyField": {
                                "id": "2",
                                "charField": "BBB",
                                "integerField": 2,
                            },
                        }
                    ],
                }
            }
        }
        response = client.query(
            search_model_d_query.replace(
                "id", "id foreignKeyField{id charField integerField}"
            ),
            variables=variables,
        ).json()
        self.verify_response(
            response,
            expected_response,
            message="SEARCH with operator AND and relations ModelD",
        )
        # endregion

        # region Test search with internal operator AND in relations
        # This tests using AND operator INSIDE a relation field (foreignKeyField)
        # It searches for ModelD where foreignKeyField satisfies BOTH conditions
        variables = {
            "where": {
                "foreignKeyField": {
                    "AND": [
                        {"charField": {"icontains": "b"}},
                        {"integerField": {"exact": 2}},
                    ],
                },
            },
        }
        expected_response = {
            "data": {
                "searchModelDs": {
                    "total": 1,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 1,
                    "objects": [
                        {
                            "id": "1",
                            "foreignKeyField": {
                                "id": "2",
                                "charField": "BBB",
                                "integerField": 2,
                            },
                        }
                    ],
                }
            }
        }
        response = client.query(
            search_model_d_query.replace(
                "id", "id foreignKeyField{id charField integerField}"
            ),
            variables=variables,
        ).json()
        self.verify_response(
            response,
            expected_response,
            message="SEARCH with internal AND operator in relations ModelD",
        )
        # endregion

        # region Test with multiple AND conditions on different relation fields
        variables = {
            "where": {
                "foreignKeyField": {"charField": {"icontains": "c"}},
                "AND": [
                    {"foreignKeyField": {"integerField": {"gte": 2}}},
                    {"foreignKeyField": {"integerField": {"lte": 3}}},
                ],
            }
        }
        expected_response = {
            "data": {
                "searchModelDs": {
                    "total": 1,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 1,
                    "objects": [
                        {
                            "id": "2",
                            "foreignKeyField": {
                                "id": "3",
                                "charField": "CCC",
                                "integerField": 3,
                            },
                        }
                    ],
                }
            }
        }
        response = client.query(
            search_model_d_query.replace(
                "id", "id foreignKeyField{id charField integerField}"
            ),
            variables=variables,
        ).json()
        self.verify_response(
            response,
            expected_response,
            message="SEARCH with multiple AND conditions and relations ModelD",
        )
        # endregion

        # region Test search with operator OR and relations
        variables = {
            "where": {
                "foreignKeyField": {"charField": {"exact": "BBB"}},
                "OR": {"foreignKeyField": {"integerField": {"exact": 3}}},
            }
        }
        expected_response = {
            "data": {
                "searchModelDs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "1",
                            "foreignKeyField": {
                                "id": "2",
                                "charField": "BBB",
                                "integerField": 2,
                            },
                        },
                        {
                            "id": "2",
                            "foreignKeyField": {
                                "id": "3",
                                "charField": "CCC",
                                "integerField": 3,
                            },
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_d_query.replace(
                "id", "id foreignKeyField{id charField integerField}"
            ),
            variables=variables,
        ).json()
        self.verify_response(
            response,
            expected_response,
            message="SEARCH with operator OR and relations ModelD",
        )

        # endregion

        # region Test with multiple OR conditions on different relation fields
        variables = {
            "where": {
                "foreignKeyField": {"charField": {"icontains": "zzz"}},
                "OR": [
                    {"foreignKeyField": {"integerField": {"exact": 2}}},
                    {"foreignKeyField": {"integerField": {"exact": 3}}},
                ],
            }
        }
        expected_response = {
            "data": {
                "searchModelDs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "1",
                            "foreignKeyField": {
                                "id": "2",
                                "charField": "BBB",
                                "integerField": 2,
                            },
                        },
                        {
                            "id": "2",
                            "foreignKeyField": {
                                "id": "3",
                                "charField": "CCC",
                                "integerField": 3,
                            },
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_d_query.replace(
                "id", "id foreignKeyField{id charField integerField}"
            ),
            variables=variables,
        ).json()
        self.verify_response(
            response,
            expected_response,
            message="SEARCH with multiple OR conditions and relations ModelD",
        )
        # endregion

        # region Test search with combined AND/OR operators and relations
        variables = {
            "where": {
                "foreignKeyField": {"charField": {"icontains": "b"}},
                "AND": {"foreignKeyField": {"integerField": {"gte": 2}}},
                "OR": {"foreignKeyField": {"integerField": {"exact": 3}}},
            }
        }
        expected_response = {
            "data": {
                "searchModelDs": {
                    "total": 2,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStart": 1,
                    "indexEnd": 2,
                    "objects": [
                        {
                            "id": "1",
                            "foreignKeyField": {
                                "id": "2",
                                "charField": "BBB",
                                "integerField": 2,
                            },
                        },
                        {
                            "id": "2",
                            "foreignKeyField": {
                                "id": "3",
                                "charField": "CCC",
                                "integerField": 3,
                            },
                        },
                    ],
                }
            }
        }
        response = client.query(
            search_model_d_query.replace(
                "id", "id foreignKeyField{id charField integerField}"
            ),
            variables=variables,
        ).json()
        self.verify_response(
            response,
            expected_response,
            message="SEARCH with combined AND/OR operators and relations ModelD",
        )
        # endregion

        # endregion
        # endregion

    def test_custom_resolver(self):
        client = Client()

        variables = {"input": objs_to_create_type_f}
        expected_response = {
            "data": {
                "createModelFs": {
                    "objects": [
                        {
                            "id": "1",
                            "name": "CUSTOM RESOLVER FOR NAME",
                            "foreignKeyField": {
                                "id": "1",
                            },
                        },
                        {
                            "id": "2",
                            "name": "CUSTOM RESOLVER FOR NAME",
                            "foreignKeyField": {
                                "id": "1",
                            },
                        },
                    ],
                    "errorsReport": None,
                }
            }
        }
        response = client.query(create_model_f_mutation, variables=variables).json()
        self.verify_response(response, expected_response, message="CREATE ModelF")

    def test_custom_resolver_foreign_key(self):
        client = Client()

        variables_c = {
            "input": [
                {
                    "charField": "AAA",
                    "integerField": 1,
                    "booleanField": True,
                    "dateTimeField": "2021-01-01T00:00:00Z",
                    "jsonField": '{"key": "value"}',
                }
            ]
        }
        client.query(create_model_c_mutation, variables=variables_c).json()

        variables_d = {
            "input": [
                {
                    "foreignKeyField": "1",
                }
            ]
        }
        client.query(create_model_d_mutation, variables=variables_d).json()

        variables_e = {
            "input": [
                {
                    "foreignKeyFieldDeep": "1",
                }
            ]
        }
        client.query(create_model_e_mutation, variables=variables_e).json()

        variables_f = {
            "input": [
                {
                    "name": "Mayra",
                    "foreignKeyField": "1",
                }
            ]
        }
        expected_response = {
            "data": {
                "createModelFs": {
                    "objects": [
                        {
                            "id": "1",
                            "name": "CUSTOM RESOLVER FOR NAME",
                            "foreignKeyField": {
                                "id": "1",
                            },
                        },
                    ],
                    "errorsReport": None,
                }
            }
        }
        response = client.query(create_model_f_mutation, variables=variables_f).json()
        self.verify_response(response, expected_response, message="CREATE ModelF")


class CruddalsAppSchemaTests(SchemaTestCase):
    def test_schema(self):
        app_client = Client("app_graphql")
        default_client = Client()

        app_schema = self.get_schema(app_client)
        expected_schema = self.get_schema(default_client)

        self.assertEqual(app_schema, expected_schema)


class CruddalsProjectSchemaGlobalTests(SchemaTestCase):
    def test_schema(self):
        project_client = Client("project_graphql")
        default_client = Client()

        project_schema = self.get_schema(project_client)
        expected_schema = self.get_schema(default_client)

        self.assertEqual(project_schema, expected_schema)
