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
    fragment errorsType on ErrorCollectionType {
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


# region CRUDDALS ModelC
create_model_c_mutation = (
    errors_fragment
    + model_c_fragment
    + """
    mutation createModelCs($input: [CreateModelCInput!]) {
        createModelCs(input: $input) {
            objects { ...modelCType }
            errorsReport { ...errorsType }
        }
    }
"""
)

read_model_c_query = (
    model_c_fragment
    + """
    query readModelC($where: FilterModelCInput!) {
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
            errorsReport { ...errorsType }
        }
    }
"""
)

delete_model_c_mutation = (
    errors_fragment
    + model_c_fragment
    + """
    mutation deleteModelCs($where: FilterModelCInput!) {
        deleteModelCs(where: $where) {
            success
            objects { ...modelCType }
            errorsReport { ...errorsType }
        }
    }
"""
)

deactivate_model_c_mutation = (
    errors_fragment
    + model_c_fragment
    + """
    mutation deactivateModelCs($where: FilterModelCInput!) {
        deactivateModelCs(where: $where) {
            objects { ...modelCType }
            errorsReport { ...errorsType }
        }
    }
"""
)

activate_model_c_mutation = (
    errors_fragment
    + model_c_fragment
    + """
    mutation activateModelCs($where: FilterModelCInput!) {
        activateModelCs(where: $where) {
            objects { ...modelCType }
            errorsReport { ...errorsType }
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
    query searchModelCs($where: FilterModelCInput $orderBy: OrderByModelCInput $paginated: PaginationConfigInput) {
        searchModelCs(where: $where orderBy: $orderBy paginated: $paginated) {
            ...paginationType
            objects {
                id
            }
        }
    }
"""
)
# endregion

# region CRUDDALS ModelD
create_model_d_mutation = (
    errors_fragment
    + model_d_fragment
    + """
    mutation createModelDs($input: [CreateModelDInput!]) {
        createModelDs(input: $input) {
            objects { ...modelDType }
            errorsReport { ...errorsType }
        }
    }
"""
)

read_model_d_query = (
    model_d_fragment
    + """
    query readModelD($where: FilterModelDInput!) {
        readModelD(where: $where) {
            ...modelDType
        }
    }
"""
)

update_model_d_mutation = (
    errors_fragment
    + model_d_fragment
    + """
    mutation updateModelDs($input: [UpdateModelDInput!]) {
        updateModelDs(input: $input) {
            objects { ...modelDType }
            errorsReport { ...errorsType }
        }
    }
"""
)

delete_model_d_mutation = (
    errors_fragment
    + model_d_fragment
    + """
    mutation deleteModelDs($where: FilterModelDInput) {
        deleteModelDs(where: $where) {
            success
            objects { ...modelDType }
            errorsReport { ...errorsType }
        }
    }
"""
)

deactivate_model_d_mutation = (
    errors_fragment
    + model_d_fragment
    + """
    mutation deactivateModelDs($where: FilterModelDInput) {
        deactivateModelDs(where: $where) {
            objects { ...modelDType }
            errorsReport { ...errorsType }
        }
    }
"""
)

activate_model_d_mutation = (
    errors_fragment
    + model_d_fragment
    + """
    mutation activateModelDs($where: FilterModelDInput) {
        activateModelDs(where: $where) {
            objects { ...modelDType }
            errorsReport { ...errorsType }
        }
    }
"""
)

list_model_d_query = (
    model_d_fragment
    + """
    query listModelDs {
        listModelDs {
            ...modelDType
        }
    }
"""
)

search_model_d_query = (
    pagination_fragment
    + """
    query searchModelDs($where: FilterModelDInput $orderBy: OrderByModelDInput $paginated: PaginationConfigInput) {
        searchModelDs(where: $where orderBy: $orderBy paginated: $paginated) {
            ...paginationType
            objects {
                id
            }
        }
    }
"""
)
# endregion

# region CRUDDALS ModelE
create_model_e_mutation = (
    model_e_fragment
    + errors_fragment
    + """
    mutation createModelEs($input: [CreateModelEInput!]) {
        createModelEs(input: $input) {
            objects { ...modelEType }
            errorsReport { ...errorsType }
        }
    }
"""
)

read_model_e_query = (
    model_e_fragment
    + """
    query readModelE($where: FilterModelEInput!) {
        readModelE(where: $where) {
            ...modelEType
        }
    }
"""
)

update_model_e_mutation = (
    model_e_fragment
    + errors_fragment
    + """
    mutation updateModelEs($input: [UpdateModelEInput!]) {
        updateModelEs(input: $input) {
            objects { ...modelEType }
            errorsReport { ...errorsType }
        }
    }
"""
)

delete_model_e_mutation = (
    model_e_fragment
    + errors_fragment
    + """
    mutation deleteModelEs($where: FilterModelEInput) {
        deleteModelEs(where: $where) {
            success
            objects { ...modelEType }
            errorsReport { ...errorsType }
        }
    }
"""
)

deactivate_model_e_mutation = (
    model_e_fragment
    + errors_fragment
    + """
    mutation deactivateModelEs($where: FilterModelEInput) {
        deactivateModelEs(where: $where) {
            objects { ...modelEType }
            errorsReport { ...errorsType }
        }
    }
"""
)

activate_model_e_mutation = (
    model_e_fragment
    + errors_fragment
    + """
    mutation activateModelEs($where: FilterModelEInput) {
        activateModelEs(where: $where) {
            objects { ...modelEType }
            errorsReport { ...errorsType }
        }
    }
"""
)

list_model_e_query = (
    model_e_fragment
    + """
    query listModelEs {
        listModelEs {
            ...modelEType
        }
    }
"""
)

search_model_e_query = (
    pagination_fragment
    + model_e_fragment
    + """
    query searchModelEs($where: FilterModelEInput $orderBy: OrderByModelEInput $paginated: PaginationConfigInput) {
        searchModelEs(where: $where orderBy: $orderBy paginated: $paginated) {
            ...paginationType
            objects { ...modelEType }
        }
    }
"""
)
# endregion

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

objs_to_create_type_d = [
    {
        "foreignKeyField": 2,
    },
    {
        "foreignKeyField": 3,
    },
]

objs_to_create_type_e = [
    {
        "foreignKeyFieldDeep": 1,
    },
    {
        "foreignKeyFieldDeep": 2,
    },
]


class CruddalsModelSchemaTest(SchemaTestCase):
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
                    "indexStartObj": 1,
                    "indexEndObj": 9,
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
        variables = {"paginated": {"page": 1, "itemsPerPage": 2}}
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

        variables = {"paginated": {"page": 2, "itemsPerPage": 2}}
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

        variables = {"paginated": {"page": 5, "itemsPerPage": 2}}
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
                    "indexStartObj": 1,
                    "indexEndObj": 1,
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
                    "indexStartObj": 1,
                    "indexEndObj": 2,
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
                    "indexStartObj": 1,
                    "indexEndObj": 2,
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
                    "indexStartObj": 1,
                    "indexEndObj": 2,
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
                    "indexStartObj": 1,
                    "indexEndObj": 2,
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
                    "indexStartObj": 1,
                    "indexEndObj": 2,
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
                    "indexStartObj": 1,
                    "indexEndObj": 2,
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
                    "indexStartObj": 1,
                    "indexEndObj": 2,
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
                    "indexStartObj": 1,
                    "indexEndObj": 2,
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
                    "indexStartObj": 1,
                    "indexEndObj": 3,
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
                    "indexStartObj": 1,
                    "indexEndObj": 9,
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
                    "indexStartObj": 0,
                    "indexEndObj": 0,
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
                    "indexStartObj": 1,
                    "indexEndObj": 1,
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
                    "indexStartObj": 1,
                    "indexEndObj": 2,
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
                    "indexStartObj": 1,
                    "indexEndObj": 2,
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
                    "indexStartObj": 1,
                    "indexEndObj": 2,
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
                    "indexStartObj": 1,
                    "indexEndObj": 4,
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
                    "indexStartObj": 1,
                    "indexEndObj": 6,
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
                    "indexStartObj": 1,
                    "indexEndObj": 3,
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
                    "indexStartObj": 1,
                    "indexEndObj": 5,
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
                    "indexStartObj": 1,
                    "indexEndObj": 4,
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
                    "indexStartObj": 1,
                    "indexEndObj": 2,
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
                    "indexStartObj": 1,
                    "indexEndObj": 2,
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
                    "indexStartObj": 1,
                    "indexEndObj": 2,
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
                    "indexStartObj": 1,
                    "indexEndObj": 2,
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
                    "indexStartObj": 1,
                    "indexEndObj": 2,
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
                    "indexStartObj": 1,
                    "indexEndObj": 2,
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
                    "indexStartObj": 1,
                    "indexEndObj": 6,
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
                    "indexStartObj": 1,
                    "indexEndObj": 9,
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
                    "indexStartObj": 0,
                    "indexEndObj": 0,
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
                    "indexStartObj": 1,
                    "indexEndObj": 2,
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
                    "indexStartObj": 1,
                    "indexEndObj": 2,
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
                    "indexStartObj": 0,
                    "indexEndObj": 0,
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
                    "indexStartObj": 1,
                    "indexEndObj": 2,
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
                    "indexStartObj": 1,
                    "indexEndObj": 2,
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
                    "indexStartObj": 1,
                    "indexEndObj": 5,
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
                    "indexStartObj": 1,
                    "indexEndObj": 1,
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
        # endregion
        # endregion
