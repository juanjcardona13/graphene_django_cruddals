import os

from graphene_django_cruddals.client.build_functions import (
    PATH_CLIENT,
    build_files_for_client_schema_cruddals,
)
from tests.schema import schema


def test_build_files_for_client_schema_cruddals():
    build_files_for_client_schema_cruddals(schema)

    assert os.path.exists(PATH_CLIENT)

    with open(f"{PATH_CLIENT}/general_types.js", encoding="utf-8") as file:
        with open(
            "tests/schema_client_js/schema_cruddals/general_types.js", encoding="utf-8"
        ) as expected_file:
            assert file.read().strip() == expected_file.read().strip()

    with open(f"{PATH_CLIENT}/mutations.js", encoding="utf-8") as file:
        with open(
            "tests/schema_client_js/schema_cruddals/mutations.js", encoding="utf-8"
        ) as expected_file:
            assert file.read().strip() == expected_file.read().strip()

    with open(f"{PATH_CLIENT}/queries.js", encoding="utf-8") as file:
        with open(
            "tests/schema_client_js/schema_cruddals/queries.js", encoding="utf-8"
        ) as expected_file:
            assert file.read().strip() == expected_file.read().strip()

    with open(f"{PATH_CLIENT}/schema-introspect.gql", encoding="utf-8") as file:
        with open(
            "tests/schema_client_js/schema_cruddals/schema-introspect.gql",
            encoding="utf-8",
        ) as expected_file:
            assert file.read().strip() == expected_file.read().strip()

    # with open(f"{PATH_CLIENT}/schema.gql", encoding="utf-8") as file:
    #     with open(
    #         "tests/schema_client_js/schema_cruddals/schema.gql", encoding="utf-8"
    #     ) as expected_file:
    #         assert file.read().strip() == expected_file.read().strip()

    # with open(f"{PATH_CLIENT}/schema.json", encoding="utf-8") as file:
    #     with open(
    #         "tests/schema_client_js/schema_cruddals/schema.json", encoding="utf-8"
    #     ) as expected_file:
    #         assert file.read().strip() == expected_file.read().strip()

    with open(f"{PATH_CLIENT}/test_in_graphiql.gql", encoding="utf-8") as file:
        with open(
            "tests/schema_client_js/schema_cruddals/test_in_graphiql.gql",
            encoding="utf-8",
        ) as expected_file:
            assert file.read().strip() == expected_file.read().strip()

    os.system(f"rm -rf {PATH_CLIENT}")
