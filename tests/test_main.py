import pytest

from graphene_django_cruddals.converters.converter_filter_input import (
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

model_f_fragment = """
    fragment modelFType on ModelFType {
        id
        name
        foreignKeyField {
            id
        }
    }
"""

model_g_fragment = """
    fragment modelGType on ModelGType {
        id
        name
        paginatedForeignKeyHRelated {
            objects {
                id
            }
        }
    }
"""

model_h_fragment = """
    fragment modelHType on ModelHType {
        id
        name
        foreignKeyField {
            id
        }
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
        indexStart
        indexEnd
    }
"""


# region CRUDDALS ModelC
create_model_c_mutation = (
    errors_fragment
    + model_c_fragment
    + """
    mutation createModelCs($input: [CreateModelCInput!]!) {
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
    mutation updateModelCs($input: [UpdateModelCInput!]!) {
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
    query searchModelCs($where: FilterModelCInput $orderBy: OrderByModelCInput $paginationConfig: PaginationConfigInput) {
        searchModelCs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig) {
            ...paginationType
            objects {
                id
            }
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
# endregion

# region CRUDDALS ModelD
create_model_d_mutation = (
    errors_fragment
    + model_d_fragment
    + """
    mutation createModelDs($input: [CreateModelDInput!]!) {
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
    mutation updateModelDs($input: [UpdateModelDInput!]!) {
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
    query searchModelDs($where: FilterModelDInput $orderBy: OrderByModelDInput $paginationConfig: PaginationConfigInput) {
        searchModelDs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig) {
            ...paginationType
            objects {
                id
            }
        }
    }
"""
)

objs_to_create_type_d = [
    {
        "foreignKeyField": 2,
    },
    {
        "foreignKeyField": 3,
    },
]
# endregion

# region CRUDDALS ModelE
create_model_e_mutation = (
    model_e_fragment
    + errors_fragment
    + """
    mutation createModelEs($input: [CreateModelEInput!]!) {
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
    mutation updateModelEs($input: [UpdateModelEInput!]!) {
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
    query searchModelEs($where: FilterModelEInput $orderBy: OrderByModelEInput $paginationConfig: PaginationConfigInput) {
        searchModelEs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig) {
            ...paginationType
            objects { ...modelEType }
        }
    }
"""
)

objs_to_create_type_e = [
    {
        "foreignKeyFieldDeep": 1,
    },
    {
        "foreignKeyFieldDeep": 2,
    },
]

# endregion

# region CRUDDALS ModelF
create_model_f_mutation = (
    model_f_fragment
    + errors_fragment
    + """
    mutation createModelFs($input: [CreateModelFInput!]!) {
        createModelFs(input: $input) {
            objects { ...modelFType }
            errorsReport { ...errorsType }
        }
    }
"""
)

read_model_f_query = (
    model_f_fragment
    + """
    query readModelF($where: FilterModelFInput!) {
        readModelF(where: $where) {
            ...modelFType
        }
    }
"""
)

update_model_f_mutation = (
    model_f_fragment
    + errors_fragment
    + """
    mutation updateModelFs($input: [UpdateModelFInput!]!) {
        updateModelFs(input: $input) {
            objects { ...modelFType }
            errorsReport { ...errorsType }
        }
    }
"""
)

delete_model_f_mutation = (
    model_f_fragment
    + errors_fragment
    + """
    mutation deleteModelFs($where: FilterModelFInput) {
        deleteModelFs(where: $where) {
            success
            objects { ...modelFType }
            errorsReport { ...errorsType }
        }
    }
"""
)

deactivate_model_f_mutation = (
    model_f_fragment
    + errors_fragment
    + """
    mutation deactivateModelFs($where: FilterModelFInput) {
        deactivateModelFs(where: $where) {
            objects { ...modelFType }
            errorsReport { ...errorsType }
        }
    }
"""
)

activate_model_f_mutation = (
    model_f_fragment
    + errors_fragment
    + """
    mutation activateModelFs($where: FilterModelFInput) {
        activateModelFs(where: $where) {
            objects { ...modelFType }
            errorsReport { ...errorsType }
        }
    }
"""
)

list_model_f_query = (
    model_f_fragment
    + """
    query listModelFs {
        listModelFs {
            ...modelFType
        }
    }
"""
)

search_model_f_query = (
    pagination_fragment
    + model_f_fragment
    + """
    query searchModelFs($where: FilterModelFInput $orderBy: OrderByModelFInput $paginationConfig: PaginationConfigInput) {
        searchModelFs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig) {
            ...paginationType
            objects { ...modelFType }
        }
    }
"""
)

objs_to_create_type_f = [
    {
        "name": "Juan",
    },
    {
        "name": "Carlos",
    },
]

# endregion

# region CRUDDALS ModelG
create_model_g_mutation = (
    model_g_fragment
    + errors_fragment
    + """
    mutation createModelGs($input: [CreateModelGInput!]!) {
        createModelGs(input: $input) {
            objects { ...modelGType }
            errorsReport { ...errorsType }
        }
    }
"""
)

read_model_g_query = (
    model_g_fragment
    + """
    query readModelG($where: FilterModelGInput!) {
        readModelG(where: $where) {
            ...modelGType
        }
    }
"""
)

update_model_g_mutation = (
    model_g_fragment
    + errors_fragment
    + """
    mutation updateModelGs($input: [UpdateModelGInput!]!) {
        updateModelGs(input: $input) {
            objects { ...modelGType }
            errorsReport { ...errorsType }
        }
    }
"""
)

delete_model_g_mutation = (
    model_g_fragment
    + errors_fragment
    + """
    mutation deleteModelGs($where: FilterModelGInput) {
        deleteModelGs(where: $where) {
            success
            objects { ...modelGType }
            errorsReport { ...errorsType }
        }
    }
"""
)

deactivate_model_g_mutation = (
    model_g_fragment
    + errors_fragment
    + """
    mutation deactivateModelGs($where: FilterModelGInput) {
        deactivateModelGs(where: $where) {
            objects { ...modelGType }
            errorsReport { ...errorsType }
        }
    }
"""
)

activate_model_g_mutation = (
    model_g_fragment
    + errors_fragment
    + """
    mutation activateModelGs($where: FilterModelGInput) {
        activateModelGs(where: $where) {
            objects { ...modelGType }
            errorsReport { ...errorsType }
        }
    }
"""
)

list_model_g_query = (
    model_g_fragment
    + """
    query listModelGs {
        listModelGs {
            ...modelGType
        }
    }
"""
)

search_model_g_query = (
    pagination_fragment
    + model_g_fragment
    + """
    query searchModelGs($where: FilterModelGInput $orderBy: OrderByModelGInput $paginationConfig: PaginationConfigInput) {
        searchModelGs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig) {
            ...paginationType
            objects { ...modelGType }
        }
    }
"""
)

objs_to_create_type_g = [
    {
        "name": "Juan",
    },
    {
        "name": "Carlos",
    },
]

# endregion

# region CRUDDALS ModelH
create_model_h_mutation = (
    model_h_fragment
    + errors_fragment
    + """
    mutation createModelHs($input: [CreateModelHInput!]!) {
        createModelHs(input: $input) {
            objects { ...modelHType }
            errorsReport { ...errorsType }
        }
    }
"""
)

read_model_h_query = (
    model_h_fragment
    + """
    query readModelH($where: FilterModelHInput!) {
        readModelH(where: $where) {
            ...modelHType
        }
    }
"""
)

update_model_h_mutation = (
    model_h_fragment
    + errors_fragment
    + """
    mutation updateModelHs($input: [UpdateModelHInput!]!) {
        updateModelHs(input: $input) {
            objects { ...modelHType }
            errorsReport { ...errorsType }
        }
    }
"""
)

delete_model_h_mutation = (
    model_h_fragment
    + errors_fragment
    + """
    mutation deleteModelHs($where: FilterModelHInput) {
        deleteModelHs(where: $where) {
            success
            objects { ...modelHType }
            errorsReport { ...errorsType }
        }
    }
"""
)

deactivate_model_h_mutation = (
    model_h_fragment
    + errors_fragment
    + """
    mutation deactivateModelHs($where: FilterModelHInput) {
        deactivateModelHs(where: $where) {
            objects { ...modelHType }
            errorsReport { ...errorsType }
        }
    }
"""
)

activate_model_h_mutation = (
    model_h_fragment
    + errors_fragment
    + """
    mutation activateModelHs($where: FilterModelHInput) {
        activateModelHs(where: $where) {
            objects { ...modelHType }
            errorsReport { ...errorsType }
        }
    }
"""
)

list_model_h_query = (
    model_h_fragment
    + """
    query listModelHs {
        listModelHs {
            ...modelHType
        }
    }
"""
)

search_model_h_query = (
    pagination_fragment
    + model_h_fragment
    + """
    query searchModelHs($where: FilterModelHInput $orderBy: OrderByModelHInput $paginationConfig: PaginationConfigInput) {
        searchModelHs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig) {
            ...paginationType
            objects { ...modelHType }
        }
    }
"""
)

objs_to_create_type_g = [
    {
        "name": "Juan",
    },
    {
        "name": "Carlos",
    },
]

# endregion


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

        # region READ ModelC
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
