import base64
import json

from django.test import Client as BaseClient
from django.urls import reverse
from graphene_django.utils.testing import GraphQLTestCase
from graphql import get_introspection_query

QUERY_GET_TYPE = """
    fragment ofType on __Type {
        kind
        name
        ofType {
            kind
            name
        }
    }

    fragment type on __Type {
        kind
        name
        ofType {
            ...ofType
        }
    }

    fragment inputValue on __InputValue {
        name
        description
        defaultValue
        type {
            ...type
        }
    }

    fragment field on __Field {
        name
        description
        type {
            ...type
        }
        args {
            ...inputValue
        }
    }

    query ($name: String!) {
        __type(name: $name) {
            name
            fields {
            ...field
            }
            inputFields {
            ...inputValue
            }
        }
    }
"""


def decode_bytes(value):
    if isinstance(value, list):
        return [decode_bytes(v) for v in value]
    if isinstance(value, dict):
        return {k: decode_bytes(v) for k, v in value.items()}
    if isinstance(value, bytes):
        return base64.b64encode(value).decode("utf-8")
    return value


class Client(BaseClient):
    def __init__(self, url="graphql"):
        self.url = reverse(url)
        super().__init__()

    def query(self, query, variables=None):
        data = {"query": query}
        if variables is not None:
            for key, value in variables.items():
                variables[key] = decode_bytes(value)
            data["variables"] = json.dumps(variables)
        response = self.post(path=self.url, data=data)
        return response


class SchemaTestCase(GraphQLTestCase):
    INTROSPECTION_QUERY = get_introspection_query()

    def get_schema(self, client):
        return client.query(self.INTROSPECTION_QUERY).json()

    def get_type(self, name):
        client = Client()
        response = client.query(QUERY_GET_TYPE, variables={"name": name}).json()
        return response["data"]["__type"]

    def get_field_by_name(self, type, name, input_field=False):
        fields_key = "inputFields" if input_field else "fields"
        all_fields = type[fields_key]
        filtered_fields = filter(lambda field: field["name"] == name, all_fields)
        try:
            return next(filtered_fields)
        except StopIteration:
            self.fail(f"Field {name} not found in {type['name']}")

    def run_test_graphql_type(self, type_name, fields_to_test, input_type=False):
        gql_type = self.get_type(type_name)
        if gql_type is None:
            self.fail(f"Type {type_name} not found")
        fields_key = "inputFields" if input_type else "fields"
        self.assertEqual(
            len(fields_to_test),
            len(gql_type[fields_key]),
            f"Fields count didn't match for type {type_name}",
        )
        for ref_field in fields_to_test:
            with self.subTest(field=ref_field):
                field = self.get_field_by_name(
                    gql_type, ref_field["name"], input_field=input_type
                )
                self.assertDictEqual(field, ref_field)

    def run_test_graphql_field(
        self, field_name: str, target_type: str, field_meta: dict
    ):
        gql_type = self.get_type(target_type)
        field = self.get_field_by_name(gql_type, field_name)
        self.assertDictEqual(field, field_meta)

    def assertTypeIsComposeOfFields(self, type_name, field_names, input_type=False):
        fields_key = "inputFields" if input_type else "fields"
        gql_type = self.get_type(type_name)
        self.assertEqual(len(field_names), len(gql_type[fields_key]))
        for field in gql_type[fields_key]:
            self.assertIn(field["name"], field_names)

    def verify_response(self, response, expected_response, message=""):
        if isinstance(expected_response, dict):
            self.assertIsInstance(
                response, dict, msg=f"response is not a dict + {message}"
            )
            self.assertEqual(
                len(expected_response),
                len(response),
                msg=f"len(dict) didn't match + {message}",
            )
            iterator = expected_response.items()
        elif isinstance(expected_response, list):
            self.assertIsInstance(
                response, list, msg=f"response is not a list + {message}"
            )
            self.assertEqual(
                len(expected_response),
                len(response),
                msg=f"len(list) didn't match + {message}",
            )
            iterator = enumerate(expected_response)
        else:
            self.assertEqual(
                expected_response,
                response,
                msg=(
                    "values didn't match :"
                    + str(expected_response)
                    + " == "
                    + str(response)
                    + " + "
                    + message
                ),
            )
            return

        for key, value in iterator:
            if isinstance(value, (dict, list)):
                self.verify_response(response[key], value, message=message)
            else:
                self.assertEqual(
                    value,
                    response[key],
                    msg=(
                        "values didn't match in key:"
                        + str(key)
                        + " :"
                        + str(value)
                        + " == "
                        + str(response[key])
                        + " + "
                        + message
                    ),
                )
