import json

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import RequestFactory
from django.test.client import BOUNDARY, MULTIPART_CONTENT, encode_multipart

from graphene_django_cruddals.views.file_upload_graphql_view import (
    FileUploadGraphQLView,
    add_file_to_operations,
    new_list_with_replaced_item,
    new_merged_dict,
    place_files_in_operations,
)
from tests.schema import schema as test_schema


class FFake:
    """Fake File object used to validate placement in operations"""

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"FFake(value={self.value})"

    def __eq__(self, other):
        return isinstance(other, FFake) and self.value == other.value


@pytest.mark.parametrize(
    "operations,files_map,file_name_map,expected",
    (
        # Simple single-file case
        (
            {"query": "q", "variables": {"f": None}},
            {"file1": ["variables.f"]},
            {"file1": FFake("content1")},
            {"query": "q", "variables": {"f": FFake("content1")}},
        ),
        # Batch operations with multiple files and positions
        (
            [
                {"query": "q1", "variables": {"file": None}},
                {"query": "q2", "variables": {"files": [None, None]}},
            ],
            {
                "f1": ["0.variables.file", "1.variables.files.0"],
                "f2": ["1.variables.files.1"],
            },
            {"f1": FFake("v1"), "f2": FFake("v2")},
            [
                {"query": "q1", "variables": {"file": FFake("v1")}},
                {"query": "q2", "variables": {"files": [FFake("v1"), FFake("v2")]}},
            ],
        ),
    ),
)
def test_place_files_in_operations(operations, files_map, file_name_map, expected):
    actual = place_files_in_operations(operations, files_map, file_name_map)
    assert actual == expected


def test_add_file_to_operations_raises_on_non_null_path_target():
    with pytest.raises(ValueError):
        add_file_to_operations("not-null", FFake("x"), [])


def test_new_merged_dict_and_new_list_with_replaced_item_helpers():
    # new_merged_dict
    merged = new_merged_dict({"a": 1}, {"b": 2}, {"a": 3})
    assert merged == {"a": 3, "b": 2}

    # new_list_with_replaced_item
    original = [1, 2, 3]
    updated = new_list_with_replaced_item(original, 1, 99)
    assert updated is original  # function mutates and returns same list reference
    assert updated == [1, 99, 3]


def build_multipart_request(factory, operations_dict, files_map_dict, files_dict):
    data = {
        "operations": json.dumps(operations_dict),
        "map": json.dumps(files_map_dict),
    }
    data.update(files_dict)
    body = encode_multipart(BOUNDARY, data)
    content_type = f"{MULTIPART_CONTENT}; boundary={BOUNDARY}"
    return factory.post("/graphql", data=body, content_type=content_type)


def test_parse_body_handles_multipart_and_places_files():
    factory = RequestFactory()
    view = FileUploadGraphQLView(schema=test_schema)

    query = "mutation($file: Upload!){ dummyUpload(fileIn:$file){ ok } }"
    operations = {"query": query, "variables": {"file": None}}
    t_file = SimpleUploadedFile(name="test.txt", content=b"line1\nline2\n")
    files_map = {"tf": ["variables.file"]}
    request = build_multipart_request(factory, operations, files_map, {"tf": t_file})

    body = view.parse_body(request)

    # Validate shape and that our uploaded file object was placed
    assert isinstance(body, dict)
    placed_file = body["variables"]["file"]
    assert placed_file.name == t_file.name
    assert placed_file.read() == b"line1\nline2\n"
    assert body["query"] == query


def test_parse_body_falls_back_for_non_multipart():
    factory = RequestFactory()
    view = FileUploadGraphQLView(schema=test_schema)

    payload = {"query": "{ ok }", "variables": {"a": 1}}
    request = factory.post(
        "/graphql",
        data=json.dumps(payload),
        content_type="application/json",
    )

    parsed = view.parse_body(request)
    # Expect the same structure parsed from JSON
    assert parsed == payload
