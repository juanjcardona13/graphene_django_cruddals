# -*- coding: utf-8 -*-
from utils.client import Client
from utils.main import SchemaTestCase

model_c_fragment = """
    fragment modelCType on ModelCType {
        id
        charField
        integerField
        booleanField
        dateTimeField
        jsonField
        fileField
        isActive
        oneToOneField { id }
        paginatedManyToManyField { objects { id } }
        paginatedForeignKeyDRelated { objects { id } }
    }
"""

model_d_fragment = """
    fragment modelDType on ModelDType {
        id
        foreignKeyField { id }
        oneToOneCRelated { id }
        paginatedManyToManyCRelated { objects {id} }
        paginatedForeignKeyERelated { objects {id} }
    }
"""

model_e_fragment = """
    fragment modelEType on ModelEType {
        id
        foreignKeyFieldDeep { id }
    }
"""

errors_fragment = """
    fragment errorsType on ErrorsType {
        objectPosition
        errors {
            field
            messages
        }
    }
"""

pagination_fragment = """
    fragment paginationType on PaginationInterface {
        total
        page
        pages
        hasNext
        hasPrev
        indexStartObj
        indexEndObj
    }
"""

all_fragment = (
    model_c_fragment
    + model_d_fragment
    + model_e_fragment
    + errors_fragment
    + pagination_fragment
)

create_model_c_mutation = (
    errors_fragment
    + model_c_fragment
    + """
    mutation createModelCs($input: [CreateModelCInput!]) {
        createModelCs(input: $input) {
            objects { ...modelCType }
            errors { ...errorsType }
        }
    }
"""
)

read_model_c_query = (
    model_c_fragment
    + """
    query readModelC($where: ModelCFilterInput!) {
        readModelC(where: $where) {
            ...modelCType
        }
    }
"""
)

update_model_c_mutation = (
    errors_fragment
    + model_c_fragment
    + """
    mutation updateModelCs($input: [UpdateModelCInput!]) {
        updateModelCs(input: $input) {
            objects { ...modelCType }
            errors { ...errorsType }
        }
    }
"""
)

delete_model_c_mutation = (
    errors_fragment
    + model_c_fragment
    + """
    mutation deleteModelCs($where: ModelCFilterInput!) {
        deleteModelCs(where: $where) {
            success
            objects { ...modelCType }
            errors { ...errorsType }
        }
    }
"""
)

deactivate_model_c_mutation = (
    errors_fragment
    + model_c_fragment
    + """
    mutation deactivateModelCs($where: ModelCFilterInput!) {
        deactivateModelCs(where: $where) {
            objects { ...modelCType }
            errors { ...errorsType }
        }
    }
"""
)

activate_model_c_mutation = (
    errors_fragment
    + model_c_fragment
    + """
    mutation activateModelCs($where: ModelCFilterInput!) {
        activateModelCs(where: $where) {
            objects { ...modelCType }
            errors { ...errorsType }
        }
    }
"""
)

list_model_c_query = (
    model_c_fragment
    + """
    query listModelCs {
        listModelCs {
            ...modelCType
        }
    }
"""
)

search_model_c_query = (
    pagination_fragment
    + """
    query searchModelCs($where: ModelCFilterInput $orderBy: ModelCOrderByInput $paginated: PaginatedInput) {
        searchModelCs(where: $where orderBy: $orderBy paginated: $paginated) {
            ...paginationType
            objects {
                id
            }
        }
    }
"""
)

create_model_d_mutation = (
    all_fragment
    + """
    mutation createModelDs($input: [CreateModelDInput!]) {
        createModelDs(input: $input) {
            objects { ...modelDType }
            errors { ...errorsType }
        }
    }
"""
)

read_model_d_query = (
    all_fragment
    + """
    query readModelD($where: ModelDFilterInput!) {
        readModelD(where: $where) {
            ...modelDType
        }
    }
"""
)

update_model_d_mutation = (
    all_fragment
    + """
    mutation updateModelDs($input: [UpdateModelDInput!]) {
        updateModelDs(input: $input) {
            objects { ...modelDType }
            errors { ...errorsType }
        }
    }
"""
)

delete_model_d_mutation = (
    all_fragment
    + """
    mutation deleteModelDs($where: ModelDFilterInput) {
        deleteModelDs(where: $where) {
            success
            objects { ...modelDType }
            errors { ...errorsType }
        }
    }
"""
)

deactivate_model_d_mutation = (
    all_fragment
    + """
    mutation deactivateModelDs($where: ModelDFilterInput) {
        deactivateModelDs(where: $where) {
            objects { ...modelDType }
            errors { ...errorsType }
        }
    }
"""
)

activate_model_d_mutation = (
    all_fragment
    + """
    mutation activateModelDs($where: ModelDFilterInput) {
        activateModelDs(where: $where) {
            objects { ...modelDType }
            errors { ...errorsType }
        }
    }
"""
)

list_model_d_query = (
    all_fragment
    + """
    query listModelDs {
        listModelDs {
            ...modelDType
        }
    }
"""
)

search_model_d_query = (
    all_fragment
    + """
    query searchModelDs($where: ModelDFilterInput $orderBy: ModelDOrderByInput $paginated: PaginatedInput) {
        searchModelDs(where: $where orderBy: $orderBy paginated: $paginated) {
            ...paginationType
            objects { ...modelDType }
        }
    }
"""
)

create_model_e_mutation = (
    all_fragment
    + """
    mutation createModelEs($input: [CreateModelEInput!]) {
        createModelEs(input: $input) {
            objects { ...modelEType }
            errors { ...errorsType }
        }
    }
"""
)

read_model_e_query = (
    all_fragment
    + """
    query readModelE($where: ModelEFilterInput!) {
        readModelE(where: $where) {
            ...modelEType
        }
    }
"""
)

update_model_e_mutation = (
    all_fragment
    + """
    mutation updateModelEs($input: [UpdateModelEInput!]) {
        updateModelEs(input: $input) {
            objects { ...modelEType }
            errors { ...errorsType }
        }
    }
"""
)

delete_model_e_mutation = (
    all_fragment
    + """
    mutation deleteModelEs($where: ModelEFilterInput) {
        deleteModelEs(where: $where) {
            success
            objects { ...modelEType }
            errors { ...errorsType }
        }
    }
"""
)

deactivate_model_e_mutation = (
    all_fragment
    + """
    mutation deactivateModelEs($where: ModelEFilterInput) {
        deactivateModelEs(where: $where) {
            objects { ...modelEType }
            errors { ...errorsType }
        }
    }
"""
)

activate_model_e_mutation = (
    all_fragment
    + """
    mutation activateModelEs($where: ModelEFilterInput) {
        activateModelEs(where: $where) {
            objects { ...modelEType }
            errors { ...errorsType }
        }
    }
"""
)

list_model_e_query = (
    all_fragment
    + """
    query listModelEs {
        listModelEs {
            ...modelEType
        }
    }
"""
)

search_model_e_query = (
    all_fragment
    + """
    query searchModelEs($where: ModelEFilterInput $orderBy: ModelEOrderByInput $paginated: PaginatedInput) {
        searchModelEs(where: $where orderBy: $orderBy paginated: $paginated) {
            ...paginationType
            objects { ...modelEType }
        }
    }
"""
)

objs_to_create_type_c = [
    {
        "charField": "AAA",
        "integerField": 1,
        "booleanField": True,
        "dateTimeField": "2021-01-01T00:00:00Z",
        "jsonField": '{"key": "value"}',
    },
    {
        "charField": "BBB",
        "integerField": 2,
        "booleanField": False,
        "dateTimeField": "2021-02-02T00:00:00Z",
        "jsonField": '{"key": "value"}',
    },
    {
        "charField": "CCC",
        "integerField": 3,
        "booleanField": True,
        "dateTimeField": "2021-03-03T00:00:00Z",
        "jsonField": '{"key": "value"}',
    },
    {
        "charField": "DDD",
        "integerField": 4,
        "booleanField": False,
        "dateTimeField": "2021-04-04T00:00:00Z",
        "jsonField": '{"key": "value"}',
    },
    {
        "charField": "EEE",
        "integerField": 5,
        "booleanField": True,
        "dateTimeField": "2021-05-05T00:00:00Z",
        "jsonField": '{"key": "value"}',
    },
    {
        "charField": "aaa",
        "integerField": 1,
        "booleanField": True,
        "dateTimeField": "2021-01-01T00:00:00Z",
        "jsonField": '{"key": "value"}',
    },
    {
        "charField": "bbb",
        "integerField": 2,
        "booleanField": False,
        "dateTimeField": "2021-02-02T00:00:00Z",
        "jsonField": '{"key": "value"}',
    },
    {
        "charField": "ccc",
        "integerField": 3,
        "booleanField": True,
        "dateTimeField": "2021-03-03T00:00:00Z",
        "jsonField": '{"key": "value"}',
    },
    {
        "charField": "ddd",
        "integerField": 4,
        "booleanField": False,
        "dateTimeField": "2021-04-04T00:00:00Z",
        "jsonField": '{"key": "value"}',
    },
    {
        "charField": "eee",
        "integerField": 5,
        "booleanField": True,
        "dateTimeField": "2021-05-05T00:00:00Z",
        "jsonField": '{"key": "value"}',
    },
]


class CruddalsModelSchemaTest(SchemaTestCase):
    def test_cruddals_model_c(self):
        client = Client()
        
        #region CREATE
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
                    "errors": None,
                }
            }
        }
        response = client.query(create_model_c_mutation, variables=variables).json()
        self.verify_response(response, expected_response)
        #endregion

        #region READ
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
        self.verify_response(response, expected_response)
        #endregion

        #region UPDATE
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
                    "errors": None,
                }
            }
        }
        response = client.query(update_model_c_mutation, variables=variables).json()
        self.verify_response(response, expected_response)
        #endregion

        #region DEACTIVATE
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
                    "errors": None,
                }
            }
        }
        response = client.query(deactivate_model_c_mutation, variables=variables).json()
        self.verify_response(response, expected_response)
        #endregion

        #region ACTIVATE
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
                    "errors": None,
                }
            }
        }
        response = client.query(activate_model_c_mutation, variables=variables).json()
        self.verify_response(response, expected_response)
        #endregion

        #region DELETE
        variables = {"where": {"id": {"exact": "1"}}}
        expected_response = {
            "data": {
                "deleteModelCs": {
                    "success": True,
                    "objects": None,
                    "errors": None,
                }
            }
        }
        response = client.query(delete_model_c_mutation, variables=variables).json()
        self.verify_response(response, expected_response)
        #endregion

        #region LIST
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
        self.verify_response(response, expected_response)
        #endregion

        #region SEARCH
        #region Test search with no filters
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 9,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStartObj": 1,
                    "indexEndObj": 9,
                    "objects": [
                        { "id": "2" },
                        { "id": "3" },
                        { "id": "4" },
                        { "id": "5" },
                        { "id": "6" },
                        { "id": "7" },
                        { "id": "8" },
                        { "id": "9" },
                        { "id": "10" },
                    ]
                }
            }
        }
        response = client.query(search_model_c_query).json()
        self.verify_response(response, expected_response)
        #endregion

        #region Test search with pagination
        variables = {"paginated": {"page": 1, "pageSize": 2}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 9,
                    "page": 1,
                    "pages": 5,
                    "hasNext": True,
                    "hasPrev": False,
                    "indexStartObj": 1,
                    "indexEndObj": 2,
                    "objects": [
                        { "id": "2", },
                        { "id": "3", },
                    ]
                }
            }
        }
        response = client.query(search_model_c_query, variables=variables).json()
        self.verify_response(response, expected_response)

        variables = {"paginated": {"page": 2, "pageSize": 2}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 9,
                    "page": 2,
                    "pages": 5,
                    "hasNext": True,
                    "hasPrev": True,
                    "indexStartObj": 3,
                    "indexEndObj": 4,
                    "objects": [
                        { "id": "4", },
                        { "id": "5", },
                    ]
                }
            }
        }
        response = client.query(search_model_c_query, variables=variables).json()
        self.verify_response(response, expected_response)

        variables = {"paginated": {"page": 5, "pageSize": 2}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 9,
                    "page": 5,
                    "pages": 5,
                    "hasNext": False,
                    "hasPrev": True,
                    "indexStartObj": 9,
                    "indexEndObj": 9,
                    "objects": [
                        { "id": "10", }
                    ]
                }
            }
        }
        response = client.query(search_model_c_query, variables=variables).json()
        self.verify_response(response, expected_response)
        #endregion
        
        #region Test search with order by
        variables = {"orderBy": {"charField": "DESC"}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 9,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStartObj": 1,
                    "indexEndObj": 9,
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
                    ]
                }
            }
        }
        response = client.query(search_model_c_query.replace("id", "id charField"), variables=variables).json()
        self.verify_response(response, expected_response)

        variables = {"orderBy": {"charField": "IDESC"}}
        expected_response = {
            "data": {
                "searchModelCs": {
                    "total": 9,
                    "page": 1,
                    "pages": 1,
                    "hasNext": False,
                    "hasPrev": False,
                    "indexStartObj": 1,
                    "indexEndObj": 9,
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
                    ]
                }
            }
        }
        response = client.query(search_model_c_query.replace("id", "id charField"), variables=variables).json()
        self.verify_response(response, expected_response)

        
        #endregion
