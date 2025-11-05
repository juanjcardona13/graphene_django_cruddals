import os
import unittest

from graphql.version import version_info

from graphene_django_cruddals.client.build_functions import (
    PATH_CLIENT,
    build_files_for_client_schema_cruddals,
)
from tests.schema import schema


def normalize_text(text):
    # Add this because in this commit (https://github.com/graphql-python/graphql-core/commit/967d58d20831032ef30555d04103342833b58a15) the word "behaviour" was changed to "behavior"
    # to match the American English spelling, literally the description of the commit is "Use American English"
    return text.replace("behaviour", "behavior")


class TestClientBuildFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        build_files_for_client_schema_cruddals(schema)
        assert os.path.exists(PATH_CLIENT)

    @classmethod
    def tearDownClass(cls):
        os.system(f"rm -rf {PATH_CLIENT}")

    def test_build_general_types_js(self):
        with open(f"{PATH_CLIENT}/general_types.js", encoding="utf-8") as file:
            with open(
                "tests/schema_client_js/schema_cruddals/general_types.js",
                encoding="utf-8",
            ) as expected_file:
                assert file.read().strip() == expected_file.read().strip()

    def test_build_mutations_js(self):
        with open(f"{PATH_CLIENT}/mutations.js", encoding="utf-8") as file:
            with open(
                "tests/schema_client_js/schema_cruddals/mutations.js", encoding="utf-8"
            ) as expected_file:
                assert file.read().strip() == expected_file.read().strip()

    def test_build_queries_js(self):
        with open(f"{PATH_CLIENT}/queries.js", encoding="utf-8") as file:
            with open(
                "tests/schema_client_js/schema_cruddals/queries.js", encoding="utf-8"
            ) as expected_file:
                assert file.read().strip() == expected_file.read().strip()

    def test_build_schema_introspect_gql(self):
        # Select the expected file based on graphql-core version
        # Version 3.2.6 and below: use schema-introspect-3-2-6.gql
        # Version 3.2.7 and above: use schema-introspect-3-2-7.gql
        current_version = (version_info.major, version_info.minor, version_info.micro)
        if current_version <= (3, 2, 6):
            expected_file_path = (
                "tests/schema_client_js/schema_cruddals/schema-introspect-3-2-6.gql"
            )
        else:
            expected_file_path = (
                "tests/schema_client_js/schema_cruddals/schema-introspect-3-2-7.gql"
            )

        with open(f"{PATH_CLIENT}/schema-introspect.gql", encoding="utf-8") as file:
            with open(expected_file_path, encoding="utf-8") as expected_file:
                assert normalize_text(file.read().strip()) == normalize_text(
                    expected_file.read().strip()
                )
                # for line1, line2 in zip(file.read().strip().splitlines(), expected_file.read().strip().splitlines()):
                #     assert line1 == line2, f"Diferencia en la línea:\n{line1}\n{line2}"

    def test_build_test_in_graphiql_gql(self):
        with open(f"{PATH_CLIENT}/test_in_graphiql.gql", encoding="utf-8") as file:
            with open(
                "tests/schema_client_js/schema_cruddals/test_in_graphiql.gql",
                encoding="utf-8",
            ) as expected_file:
                assert file.read().strip() == expected_file.read().strip()

    # def test_build_schema_gql(self):
    #     with open(f"{PATH_CLIENT}/schema.gql", encoding="utf-8") as file:
    #         with open(
    #             "tests/schema_client_js/schema_cruddals/schema.gql", encoding="utf-8"
    #         ) as expected_file:
    #             assert file.read().strip() == expected_file.read().strip()

    # def test_build_schema_json(self):
    #     with open(f"{PATH_CLIENT}/schema.json", encoding="utf-8") as file:
    #         with open(
    #             "tests/schema_client_js/schema_cruddals/schema.json", encoding="utf-8"
    #         ) as expected_file:
    #             assert file.read().strip() == expected_file.read().strip()
