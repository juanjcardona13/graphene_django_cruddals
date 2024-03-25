# -*- coding: utf-8 -*-

from utils.main import SchemaTestCase


class CruddalsModelSchemaTest(SchemaTestCase):
    def test_model_operations_for_query(self):
        fields_to_test = [
            {
                "name": "readModelF",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ModelFType", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelFFilterInput", "ofType": None } }
                }
                ]
            },
            {
                "name": "searchModelFs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ModelFPaginatedType", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "INPUT_OBJECT", "name": "ModelFFilterInput", "ofType": None }
                },
                {
                    "name": "orderBy",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "INPUT_OBJECT", "name": "ModelFOrderByInput", "ofType": None }
                },
                {
                    "name": "paginated",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "INPUT_OBJECT", "name": "PaginatedInput", "ofType": None }
                }
                ]
            },
            {
                "name": "listModelFs",
                "description": None,
                "type": { "kind": "LIST", "name": None, "ofType": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "OBJECT", "name": "ModelFType" } } },
                "args": []
            },
            {
                "name": "readModelE",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ModelEType", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelEFilterInput", "ofType": None } }
                }
                ]
            },
            {
                "name": "searchModelEs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ModelEPaginatedType", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "INPUT_OBJECT", "name": "ModelEFilterInput", "ofType": None }
                },
                {
                    "name": "orderBy",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "INPUT_OBJECT", "name": "ModelEOrderByInput", "ofType": None }
                },
                {
                    "name": "paginated",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "INPUT_OBJECT", "name": "PaginatedInput", "ofType": None }
                }
                ]
            },
            {
                "name": "listModelEs",
                "description": None,
                "type": { "kind": "LIST", "name": None, "ofType": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "OBJECT", "name": "ModelEType" } } },
                "args": []
            },
            {
                "name": "readModelD",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ModelDType", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelDFilterInput", "ofType": None } }
                }
                ]
            },
            {
                "name": "searchModelDs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ModelDPaginatedType", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "INPUT_OBJECT", "name": "ModelDFilterInput", "ofType": None }
                },
                {
                    "name": "orderBy",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "INPUT_OBJECT", "name": "ModelDOrderByInput", "ofType": None }
                },
                {
                    "name": "paginated",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "INPUT_OBJECT", "name": "PaginatedInput", "ofType": None }
                }
                ]
            },
            {
                "name": "listModelDs",
                "description": None,
                "type": { "kind": "LIST", "name": None, "ofType": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "OBJECT", "name": "ModelDType" } } },
                "args": []
            },
            {
                "name": "readModelC",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ModelCType", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelCFilterInput", "ofType": None } }
                }
                ]
            },
            {
                "name": "searchModelCs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ModelCPaginatedType", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "INPUT_OBJECT", "name": "ModelCFilterInput", "ofType": None }
                },
                {
                    "name": "orderBy",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "INPUT_OBJECT", "name": "ModelCOrderByInput", "ofType": None }
                },
                {
                    "name": "paginated",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "INPUT_OBJECT", "name": "PaginatedInput", "ofType": None }
                }
                ]
            },
            {
                "name": "listModelCs",
                "description": None,
                "type": { "kind": "LIST", "name": None, "ofType": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "OBJECT", "name": "ModelCType" } } },
                "args": []
            },
            {
                "name": "readModelB",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ModelBType", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelBFilterInput", "ofType": None } }
                }
                ]
            },
            {
                "name": "searchModelBs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ModelBPaginatedType", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "INPUT_OBJECT", "name": "ModelBFilterInput", "ofType": None }
                },
                {
                    "name": "orderBy",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "INPUT_OBJECT", "name": "ModelBOrderByInput", "ofType": None }
                },
                {
                    "name": "paginated",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "INPUT_OBJECT", "name": "PaginatedInput", "ofType": None }
                }
                ]
            },
            {
                "name": "listModelBs",
                "description": None,
                "type": { "kind": "LIST", "name": None, "ofType": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "OBJECT", "name": "ModelBType" } } },
                "args": []
            },
            {
                "name": "readModelA",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ModelAType", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None } }
                }
                ]
            },
            {
                "name": "searchModelAs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ModelAPaginatedType", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
                },
                {
                    "name": "orderBy",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "INPUT_OBJECT", "name": "ModelAOrderByInput", "ofType": None }
                },
                {
                    "name": "paginated",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "INPUT_OBJECT", "name": "PaginatedInput", "ofType": None }
                }
                ]
            },
            {
                "name": "listModelAs",
                "description": None,
                "type": { "kind": "LIST", "name": None, "ofType": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "OBJECT", "name": "ModelAType" } } },
                "args": []
            }
        ]
        self.run_test_fields_of_type("Query", fields_to_test)
    
    def test_model_operations_for_mutation(self):
        fields_to_test = [
            {
                "name": "createModelFs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "CreateModelFsPayload", "ofType": None },
                "args": [
                {
                    "name": "input",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "LIST", "name": None, "ofType": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "CreateModelFInput" } } }
                }
                ]
            },
            {
                "name": "updateModelFs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "UpdateModelFsPayload", "ofType": None },
                "args": [
                {
                    "name": "input",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "LIST", "name": None, "ofType": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "UpdateModelFInput" } } }
                }
                ]
            },
            {
                "name": "activateModelFs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ActivateModelFsPayload", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelFFilterInput", "ofType": None } }
                }
                ]
            },
            {
                "name": "deactivateModelFs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "DeactivateModelFsPayload", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelFFilterInput", "ofType": None } }
                }
                ]
            },
            {
                "name": "deleteModelFs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "DeleteModelFsPayload", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelFFilterInput", "ofType": None } }
                }
                ]
            },
            {
                "name": "createModelEs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "CreateModelEsPayload", "ofType": None },
                "args": [
                {
                    "name": "input",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "LIST", "name": None, "ofType": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "CreateModelEInput" } } }
                }
                ]
            },
            {
                "name": "updateModelEs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "UpdateModelEsPayload", "ofType": None },
                "args": [
                {
                    "name": "input",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "LIST", "name": None, "ofType": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "UpdateModelEInput" } } }
                }
                ]
            },
            {
                "name": "activateModelEs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ActivateModelEsPayload", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelEFilterInput", "ofType": None } }
                }
                ]
            },
            {
                "name": "deactivateModelEs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "DeactivateModelEsPayload", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelEFilterInput", "ofType": None } }
                }
                ]
            },
            {
                "name": "deleteModelEs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "DeleteModelEsPayload", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelEFilterInput", "ofType": None } }
                }
                ]
            },
            {
                "name": "createModelDs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "CreateModelDsPayload", "ofType": None },
                "args": [
                {
                    "name": "input",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "LIST", "name": None, "ofType": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "CreateModelDInput" } } }
                }
                ]
            },
            {
                "name": "updateModelDs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "UpdateModelDsPayload", "ofType": None },
                "args": [
                {
                    "name": "input",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "LIST", "name": None, "ofType": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "UpdateModelDInput" } } }
                }
                ]
            },
            {
                "name": "activateModelDs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ActivateModelDsPayload", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelDFilterInput", "ofType": None } }
                }
                ]
            },
            {
                "name": "deactivateModelDs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "DeactivateModelDsPayload", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelDFilterInput", "ofType": None } }
                }
                ]
            },
            {
                "name": "deleteModelDs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "DeleteModelDsPayload", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelDFilterInput", "ofType": None } }
                }
                ]
            },
            {
                "name": "createModelCs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "CreateModelCsPayload", "ofType": None },
                "args": [
                {
                    "name": "input",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "LIST", "name": None, "ofType": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "CreateModelCInput" } } }
                }
                ]
            },
            {
                "name": "updateModelCs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "UpdateModelCsPayload", "ofType": None },
                "args": [
                {
                    "name": "input",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "LIST", "name": None, "ofType": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "UpdateModelCInput" } } }
                }
                ]
            },
            {
                "name": "activateModelCs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ActivateModelCsPayload", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelCFilterInput", "ofType": None } }
                }
                ]
            },
            {
                "name": "deactivateModelCs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "DeactivateModelCsPayload", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelCFilterInput", "ofType": None } }
                }
                ]
            },
            {
                "name": "deleteModelCs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "DeleteModelCsPayload", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelCFilterInput", "ofType": None } }
                }
                ]
            },
            {
                "name": "createModelBs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "CreateModelBsPayload", "ofType": None },
                "args": [
                {
                    "name": "input",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "LIST", "name": None, "ofType": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "CreateModelBInput" } } }
                }
                ]
            },
            {
                "name": "updateModelBs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "UpdateModelBsPayload", "ofType": None },
                "args": [
                {
                    "name": "input",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "LIST", "name": None, "ofType": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "UpdateModelBInput" } } }
                }
                ]
            },
            {
                "name": "activateModelBs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ActivateModelBsPayload", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelBFilterInput", "ofType": None } }
                }
                ]
            },
            {
                "name": "deactivateModelBs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "DeactivateModelBsPayload", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelBFilterInput", "ofType": None } }
                }
                ]
            },
            {
                "name": "deleteModelBs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "DeleteModelBsPayload", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelBFilterInput", "ofType": None } }
                }
                ]
            },
            {
                "name": "createModelAs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "CreateModelAsPayload", "ofType": None },
                "args": [
                {
                    "name": "input",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "LIST", "name": None, "ofType": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "CreateModelAInput" } } }
                }
                ]
            },
            {
                "name": "updateModelAs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "UpdateModelAsPayload", "ofType": None },
                "args": [
                {
                    "name": "input",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "LIST", "name": None, "ofType": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "UpdateModelAInput" } } }
                }
                ]
            },
            {
                "name": "activateModelAs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ActivateModelAsPayload", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None } }
                }
                ]
            },
            {
                "name": "deactivateModelAs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "DeactivateModelAsPayload", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None } }
                }
                ]
            },
            {
                "name": "deleteModelAs",
                "description": None,
                "type": { "kind": "OBJECT", "name": "DeleteModelAsPayload", "ofType": None },
                "args": [
                {
                    "name": "where",
                    "description": "",
                    "defaultValue": None,
                    "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None } }
                }
                ]
            }
        ]
        self.run_test_fields_of_type("Mutation", fields_to_test)

    def test_complete_schema(self):
        schema_for_test = {
            "data": {
                "__schema": {
                "queryType": {
                    "name": "Query"
                },
                "mutationType": {
                    "name": "Mutation"
                },
                "subscriptionType": None,
                "types": [
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "ModelAInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "id",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "binaryFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Binary",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "binaryFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Binary",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "binaryFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Binary",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "binaryFieldWithDescription",
                        "description": "binary_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "Binary",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "booleanFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "booleanFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "booleanFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "booleanFieldWithDescription",
                        "description": "boolean_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "charFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "charFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "charFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "charFieldWithDescription",
                        "description": "char_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "choiceFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "SimplecruddalsmodelModelAChoiceFieldRequiredChoices",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "choiceFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "SimplecruddalsmodelModelAChoiceFieldNullableChoices",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "choiceFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "SimplecruddalsmodelModelAChoiceFieldWithDefaultChoices",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "choiceFieldWithDescription",
                        "description": "choice_field_with_description",
                        "type": {
                            "kind": "ENUM",
                            "name": "SimplecruddalsmodelModelAChoiceFieldWithDescriptionChoices",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateFieldWithDescription",
                        "description": "date_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateTimeFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateTimeFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateTimeFieldWithDescription",
                        "description": "date_time_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "timeFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "timeFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "timeFieldWithDescription",
                        "description": "time_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "decimalFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "decimalFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "decimalFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "decimalFieldWithDescription",
                        "description": "decimal_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "durationFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "durationFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "durationFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "durationFieldWithDescription",
                        "description": "duration_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "emailFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "emailFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "emailFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "emailFieldWithDescription",
                        "description": "email_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "floatFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "floatFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "floatFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "floatFieldWithDescription",
                        "description": "float_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "integerFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "integerFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "integerFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "integerFieldWithDescription",
                        "description": "integer_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "smallIntegerFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "smallIntegerFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "smallIntegerFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "smallIntegerFieldWithDescription",
                        "description": "small_integer_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "positiveIntegerFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "positiveIntegerFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "positiveIntegerFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "positiveIntegerFieldWithDescription",
                        "description": "positive_integer_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "slugFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "slugFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "slugFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "slugFieldWithDescription",
                        "description": "slug_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "textFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "textFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "textFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "textFieldWithDescription",
                        "description": "text_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "urlFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "urlFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "urlFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "urlFieldWithDescription",
                        "description": "url_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "uuidFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "uuidFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "uuidFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "uuidFieldWithDescription",
                        "description": "uuid_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyFieldWithDescription",
                        "description": "foreign_key_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyFieldWithoutRelatedName",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "oneToOneFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "oneToOneFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "oneToOneFieldWithDescription",
                        "description": "one_to_one_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "oneToOneFieldWithoutRelatedName",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "contentType",
                        "description": "The content type",
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "objectId",
                        "description": "The object id",
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "manyToManyFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "manyToManyFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "manyToManyFieldWithDescription",
                        "description": "many_to_many_field_with_description",
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "manyToManyFieldWithoutRelatedName",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "SCALAR",
                    "name": "ID",
                    "description": "The `ID` scalar type represents a unique identifier, often used to refetch an object or as key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as `\"4\"`) or integer (such as `4`) input value will be accepted as an ID.",
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "SCALAR",
                    "name": "Binary",
                    "description": "BinaryArray is used to convert a Django BinaryField to the string form",
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "SCALAR",
                    "name": "Boolean",
                    "description": "The `Boolean` scalar type represents `true` or `false`.",
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "SCALAR",
                    "name": "String",
                    "description": "The `String` scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.",
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "ENUM",
                    "name": "SimplecruddalsmodelModelAChoiceFieldRequiredChoices",
                    "description": "An enumeration.",
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": [
                        {
                        "name": "A",
                        "description": "A",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "B",
                        "description": "B",
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "possibleTypes": None
                    },
                    {
                    "kind": "ENUM",
                    "name": "SimplecruddalsmodelModelAChoiceFieldNullableChoices",
                    "description": "An enumeration.",
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": [
                        {
                        "name": "A",
                        "description": "A",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "B",
                        "description": "B",
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "possibleTypes": None
                    },
                    {
                    "kind": "ENUM",
                    "name": "SimplecruddalsmodelModelAChoiceFieldWithDefaultChoices",
                    "description": "An enumeration.",
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": [
                        {
                        "name": "A",
                        "description": "A",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "B",
                        "description": "B",
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "possibleTypes": None
                    },
                    {
                    "kind": "ENUM",
                    "name": "SimplecruddalsmodelModelAChoiceFieldWithDescriptionChoices",
                    "description": "An enumeration.",
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": [
                        {
                        "name": "A",
                        "description": "A",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "B",
                        "description": "B",
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "possibleTypes": None
                    },
                    {
                    "kind": "SCALAR",
                    "name": "Date",
                    "description": "The `Date` scalar type represents a Date\nvalue as specified by\n[iso8601](https://en.wikipedia.org/wiki/ISO_8601).",
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "SCALAR",
                    "name": "DateTime",
                    "description": "The `DateTime` scalar type represents a DateTime\nvalue as specified by\n[iso8601](https://en.wikipedia.org/wiki/ISO_8601).",
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "SCALAR",
                    "name": "Time",
                    "description": "The `Time` scalar type represents a Time value as\nspecified by\n[iso8601](https://en.wikipedia.org/wiki/ISO_8601).",
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "SCALAR",
                    "name": "Decimal",
                    "description": "The `Decimal` scalar type represents a python Decimal.",
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "SCALAR",
                    "name": "Duration",
                    "description": "Duration fields in Django are stored as timedelta in Python,\nand as a duration in the Database. We will represent them as\na total number of seconds in GraphQL.",
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "SCALAR",
                    "name": "Email",
                    "description": "A field whose value conforms to the standard\ninternet email address format as specified in\nHTML Spec: https://html.spec.whatwg.org/multipage/input.html#valid-e-mail-address.",
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "SCALAR",
                    "name": "Float",
                    "description": "The `Float` scalar type represents signed double-precision fractional values as specified by [IEEE 754](https://en.wikipedia.org/wiki/IEEE_floating_point).",
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "SCALAR",
                    "name": "Int",
                    "description": "The `Int` scalar type represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1.",
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "SCALAR",
                    "name": "PositiveInt",
                    "description": "Integers that will have a value of 0 or more.",
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "SCALAR",
                    "name": "Slug",
                    "description": "Slug is a newspaper term. A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They\u2019re generally used in URLs.",
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "SCALAR",
                    "name": "URL",
                    "description": "A field whose value conforms to the standard URL format as specified in RFC3986: https://www.ietf.org/rfc/rfc3986.txt.",
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "SCALAR",
                    "name": "UUID",
                    "description": "Leverages the internal Python implementation of UUID (uuid.UUID) to provide native UUID objects\nin fields, resolvers and input.",
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "Query",
                    "description": None,
                    "fields": [
                        {
                        "name": "readModelF",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelFFilterInput",
                                "ofType": None
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelFType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "searchModelFs",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelFFilterInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "orderBy",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelFOrderByInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "paginated",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PaginatedInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelFPaginatedType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "listModelFs",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelFType",
                                "ofType": None
                            }
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "readModelE",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelEFilterInput",
                                "ofType": None
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelEType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "searchModelEs",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelEFilterInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "orderBy",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelEOrderByInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "paginated",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PaginatedInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelEPaginatedType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "listModelEs",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelEType",
                                "ofType": None
                            }
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "readModelD",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelDFilterInput",
                                "ofType": None
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelDType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "searchModelDs",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelDFilterInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "orderBy",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelDOrderByInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "paginated",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PaginatedInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelDPaginatedType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "listModelDs",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelDType",
                                "ofType": None
                            }
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "readModelC",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelCFilterInput",
                                "ofType": None
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelCType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "searchModelCs",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelCFilterInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "orderBy",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelCOrderByInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "paginated",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PaginatedInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelCPaginatedType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "listModelCs",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelCType",
                                "ofType": None
                            }
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "readModelB",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelBFilterInput",
                                "ofType": None
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelBType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "searchModelBs",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelBFilterInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "orderBy",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelBOrderByInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "paginated",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PaginatedInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelBPaginatedType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "listModelBs",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelBType",
                                "ofType": None
                            }
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "readModelA",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelAType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "searchModelAs",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "orderBy",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAOrderByInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "paginated",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PaginatedInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelAPaginatedType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "listModelAs",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelAType",
                                "ofType": None
                            }
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "ModelFType",
                    "description": None,
                    "fields": [
                        {
                        "name": "id",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "text",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "paginatedFkFRelated",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelEFilterInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "orderBy",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelEOrderByInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "paginated",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PaginatedInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelEPaginatedType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "otoFRelated",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelEType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "paginatedMtmFRelated",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelEFilterInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "orderBy",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelEOrderByInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "paginated",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PaginatedInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelEPaginatedType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "ModelEPaginatedType",
                    "description": None,
                    "fields": [
                        {
                        "name": "total",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "page",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "pages",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "hasNext",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "hasPrev",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "indexStartObj",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "indexEndObj",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelEType",
                                "ofType": None
                            }
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [
                        {
                        "kind": "INTERFACE",
                        "name": "PaginationInterface",
                        "ofType": None
                        }
                    ],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INTERFACE",
                    "name": "PaginationInterface",
                    "description": None,
                    "fields": [
                        {
                        "name": "total",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "page",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "pages",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "hasNext",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "hasPrev",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "indexStartObj",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "indexEndObj",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": [
                        {
                        "kind": "OBJECT",
                        "name": "ModelEPaginatedType",
                        "ofType": None
                        },
                        {
                        "kind": "OBJECT",
                        "name": "ModelFPaginatedType",
                        "ofType": None
                        },
                        {
                        "kind": "OBJECT",
                        "name": "ModelDPaginatedType",
                        "ofType": None
                        },
                        {
                        "kind": "OBJECT",
                        "name": "ModelCPaginatedType",
                        "ofType": None
                        },
                        {
                        "kind": "OBJECT",
                        "name": "ModelAPaginatedType",
                        "ofType": None
                        },
                        {
                        "kind": "OBJECT",
                        "name": "ModelBPaginatedType",
                        "ofType": None
                        }
                    ]
                    },
                    {
                    "kind": "OBJECT",
                    "name": "ModelEType",
                    "description": None,
                    "fields": [
                        {
                        "name": "id",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "fkF",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelFType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "otoF",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelFType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "text",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "paginatedMtmF",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelFFilterInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "orderBy",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelFOrderByInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "paginated",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PaginatedInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelFPaginatedType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "ModelFPaginatedType",
                    "description": None,
                    "fields": [
                        {
                        "name": "total",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "page",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "pages",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "hasNext",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "hasPrev",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "indexStartObj",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "indexEndObj",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelFType",
                                "ofType": None
                            }
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [
                        {
                        "kind": "INTERFACE",
                        "name": "PaginationInterface",
                        "ofType": None
                        }
                    ],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "ModelFFilterInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "id",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "IDFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "text",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "fkFRelated",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelEFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "otoFRelated",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelEFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "mtmFRelated",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelEFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "AND",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelFFilterInput",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "OR",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelFFilterInput",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "NOT",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelFFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "IDFilter",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "exact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iexact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "in",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "contains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "icontains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "startswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "istartswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "endswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iendswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "range",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "isNone",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "regex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iregex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "containedBy",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "StringFilter",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "exact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iexact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "in",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "contains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "icontains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "startswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "istartswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "endswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iendswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "range",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "isNone",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "regex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iregex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "ModelEFilterInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "id",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "IDFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "fkF",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelFFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "otoF",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelFFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "text",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "mtmF",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelFFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "AND",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelEFilterInput",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "OR",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelEFilterInput",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "NOT",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelEFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "ModelFOrderByInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "id",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "text",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "otoFRelated",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelEOrderByInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "ENUM",
                    "name": "OrderEnum",
                    "description": None,
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": [
                        {
                        "name": "ASC",
                        "description": None,
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "DESC",
                        "description": None,
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "possibleTypes": None
                    },
                    {
                    "kind": "ENUM",
                    "name": "OrderStringEnum",
                    "description": None,
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": [
                        {
                        "name": "ASC",
                        "description": None,
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "DESC",
                        "description": None,
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "IASC",
                        "description": None,
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "IDESC",
                        "description": None,
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "ModelEOrderByInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "id",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "fkF",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelFOrderByInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "otoF",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelFOrderByInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "text",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "PaginatedInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "page",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": "1"
                        },
                        {
                        "name": "pageSize",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "IntOrAll",
                            "ofType": None
                        },
                        "defaultValue": "\"All\""
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "SCALAR",
                    "name": "IntOrAll",
                    "description": "The page size can be int or 'All'",
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "ModelDType",
                    "description": None,
                    "fields": [
                        {
                        "name": "id",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "createUpdateOnly",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "createOnly",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "updateOnly",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "whereOnly",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "orderByOnly",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "allInput",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "allExclude",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "ModelDFilterInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "id",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "IDFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "createUpdateOnly",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "createOnly",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "updateOnly",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "whereOnly",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "orderByOnly",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "allInput",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "allExclude",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "AND",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelDFilterInput",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "OR",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelDFilterInput",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "NOT",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelDFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "ModelDPaginatedType",
                    "description": None,
                    "fields": [
                        {
                        "name": "total",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "page",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "pages",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "hasNext",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "hasPrev",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "indexStartObj",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "indexEndObj",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelDType",
                                "ofType": None
                            }
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [
                        {
                        "kind": "INTERFACE",
                        "name": "PaginationInterface",
                        "ofType": None
                        }
                    ],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "ModelDOrderByInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "id",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "createUpdateOnly",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "createOnly",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "updateOnly",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "whereOnly",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "orderByOnly",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "allInput",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "allExclude",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "ModelCType",
                    "description": None,
                    "fields": [
                        {
                        "name": "id",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "createUpdateOnly",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "createOnly",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "updateOnly",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "whereOnly",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "orderByOnly",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "allInput",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "allExclude",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "ModelCFilterInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "id",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "IDFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "createUpdateOnly",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "createOnly",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "updateOnly",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "whereOnly",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "orderByOnly",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "allInput",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "allExclude",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "AND",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelCFilterInput",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "OR",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelCFilterInput",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "NOT",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelCFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "ModelCPaginatedType",
                    "description": None,
                    "fields": [
                        {
                        "name": "total",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "page",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "pages",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "hasNext",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "hasPrev",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "indexStartObj",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "indexEndObj",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelCType",
                                "ofType": None
                            }
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [
                        {
                        "kind": "INTERFACE",
                        "name": "PaginationInterface",
                        "ofType": None
                        }
                    ],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "ModelCOrderByInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "id",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "createUpdateOnly",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "createOnly",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "updateOnly",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "whereOnly",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "orderByOnly",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "allInput",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "allExclude",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "ModelBType",
                    "description": None,
                    "fields": [
                        {
                        "name": "id",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "foreignKeyField",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelAType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "oneToOneField",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelAType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "paginatedManyToManyField",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "orderBy",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAOrderByInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "paginated",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PaginatedInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelAPaginatedType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "ModelAType",
                    "description": None,
                    "fields": [
                        {
                        "name": "id",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "binaryFieldRequired",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Binary",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "binaryFieldNotEditable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Binary",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "binaryFieldNullable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Binary",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "binaryFieldWithDefault",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Binary",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "binaryFieldWithDescription",
                        "description": "binary_field_with_description",
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Binary",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "booleanFieldRequired",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "booleanFieldNotEditable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "booleanFieldNullable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "booleanFieldWithDefault",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "booleanFieldWithDescription",
                        "description": "boolean_field_with_description",
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "charFieldRequired",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "charFieldNotEditable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "charFieldNullable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "charFieldWithDefault",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "charFieldWithDescription",
                        "description": "char_field_with_description",
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "choiceFieldRequired",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "ENUM",
                            "name": "SimplecruddalsmodelModelAChoiceFieldRequiredChoices",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "choiceFieldNotEditable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "ENUM",
                            "name": "SimplecruddalsmodelModelAChoiceFieldNotEditableChoices",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "choiceFieldNullable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "ENUM",
                            "name": "SimplecruddalsmodelModelAChoiceFieldNullableChoices",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "choiceFieldWithDefault",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "ENUM",
                            "name": "SimplecruddalsmodelModelAChoiceFieldWithDefaultChoices",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "choiceFieldWithDescription",
                        "description": "choice_field_with_description",
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "ENUM",
                            "name": "SimplecruddalsmodelModelAChoiceFieldWithDescriptionChoices",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "dateFieldRequired",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "dateFieldNotEditable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "dateFieldNullable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "dateFieldWithDefault",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "dateFieldWithDescription",
                        "description": "date_field_with_description",
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "dateTimeFieldRequired",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "dateTimeFieldNotEditable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "dateTimeFieldNullable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "dateTimeFieldWithDefault",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "dateTimeFieldWithDescription",
                        "description": "date_time_field_with_description",
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "timeFieldRequired",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "timeFieldNotEditable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "timeFieldNullable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "timeFieldWithDefault",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "timeFieldWithDescription",
                        "description": "time_field_with_description",
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "decimalFieldRequired",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "decimalFieldNotEditable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "decimalFieldNullable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "decimalFieldWithDefault",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "decimalFieldWithDescription",
                        "description": "decimal_field_with_description",
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "durationFieldRequired",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "durationFieldNotEditable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "durationFieldNullable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "durationFieldWithDefault",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "durationFieldWithDescription",
                        "description": "duration_field_with_description",
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "emailFieldRequired",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "emailFieldNotEditable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "emailFieldNullable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "emailFieldWithDefault",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "emailFieldWithDescription",
                        "description": "email_field_with_description",
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "floatFieldRequired",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "floatFieldNotEditable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "floatFieldNullable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "floatFieldWithDefault",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "floatFieldWithDescription",
                        "description": "float_field_with_description",
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "integerFieldRequired",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "integerFieldNotEditable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "integerFieldNullable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "integerFieldWithDefault",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "integerFieldWithDescription",
                        "description": "integer_field_with_description",
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "smallIntegerFieldRequired",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "smallIntegerFieldNotEditable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "smallIntegerFieldNullable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "smallIntegerFieldWithDefault",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "smallIntegerFieldWithDescription",
                        "description": "small_integer_field_with_description",
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "positiveIntegerFieldRequired",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "positiveIntegerFieldNotEditable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "positiveIntegerFieldNullable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "positiveIntegerFieldWithDefault",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "positiveIntegerFieldWithDescription",
                        "description": "positive_integer_field_with_description",
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "slugFieldRequired",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "slugFieldNotEditable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "slugFieldNullable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "slugFieldWithDefault",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "slugFieldWithDescription",
                        "description": "slug_field_with_description",
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "textFieldRequired",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "textFieldNotEditable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "textFieldNullable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "textFieldWithDefault",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "textFieldWithDescription",
                        "description": "text_field_with_description",
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "urlFieldRequired",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "urlFieldNotEditable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "urlFieldNullable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "urlFieldWithDefault",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "urlFieldWithDescription",
                        "description": "url_field_with_description",
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "uuidFieldRequired",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "uuidFieldNotEditable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "uuidFieldNullable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "uuidFieldWithDefault",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "uuidFieldWithDescription",
                        "description": "uuid_field_with_description",
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "foreignKeyFieldRequired",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelAType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "foreignKeyFieldNullable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelAType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "foreignKeyFieldWithDescription",
                        "description": "foreign_key_field_with_description",
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelAType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "foreignKeyFieldWithoutRelatedName",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelAType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "oneToOneFieldRequired",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelAType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "oneToOneFieldNullable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelAType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "oneToOneFieldWithDescription",
                        "description": "one_to_one_field_with_description",
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelAType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "oneToOneFieldWithoutRelatedName",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelAType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "objectId",
                        "description": "The object id",
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "paginatedManyToManyFieldRequired",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "orderBy",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAOrderByInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "paginated",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PaginatedInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelAPaginatedType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "paginatedManyToManyFieldNullable",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "orderBy",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAOrderByInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "paginated",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PaginatedInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelAPaginatedType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "paginatedManyToManyFieldWithDescription",
                        "description": "many_to_many_field_with_description",
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "orderBy",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAOrderByInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "paginated",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PaginatedInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelAPaginatedType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "paginatedManyToManyFieldWithoutRelatedName",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "orderBy",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAOrderByInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "paginated",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PaginatedInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelAPaginatedType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "genericForeignKeyField",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "UNION",
                            "name": "ModelAGenericForeignKeyFieldUnionType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "paginatedGenericRelationField",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "orderBy",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAOrderByInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "paginated",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PaginatedInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelAPaginatedType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "paginatedForeignKeyRelated",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "orderBy",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAOrderByInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "paginated",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PaginatedInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelAPaginatedType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "paginatedForeignKeyNullableRelated",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "orderBy",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAOrderByInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "paginated",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PaginatedInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelAPaginatedType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "paginatedForeignKeyWithDescriptionRelated",
                        "description": "foreign_key_field_with_description",
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "orderBy",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAOrderByInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "paginated",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PaginatedInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelAPaginatedType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "oneToOneRelated",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelAType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "oneToOneNullableRelated",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelAType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "oneToOneWithDescriptionRelated",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelAType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "paginatedManyToManyRelated",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "orderBy",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAOrderByInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "paginated",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PaginatedInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelAPaginatedType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "paginatedManyToManyNullableRelated",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "orderBy",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAOrderByInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "paginated",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PaginatedInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelAPaginatedType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "paginatedManyToManyWithDescriptionRelated",
                        "description": "many_to_many_field_with_description",
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "orderBy",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAOrderByInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "paginated",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PaginatedInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelAPaginatedType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "genericRelationRelated",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelAType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "paginatedForeignKeyBRelated",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelBFilterInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "orderBy",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelBOrderByInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "paginated",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PaginatedInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelBPaginatedType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "oneToOneBRelated",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelBType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "paginatedManyToManyBRelated",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelBFilterInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "orderBy",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelBOrderByInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            },
                            {
                            "name": "paginated",
                            "description": "",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PaginatedInput",
                                "ofType": None
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ModelBPaginatedType",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "ENUM",
                    "name": "SimplecruddalsmodelModelAChoiceFieldNotEditableChoices",
                    "description": "An enumeration.",
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": [
                        {
                        "name": "A",
                        "description": "A",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "B",
                        "description": "B",
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "ModelAPaginatedType",
                    "description": None,
                    "fields": [
                        {
                        "name": "total",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "page",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "pages",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "hasNext",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "hasPrev",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "indexStartObj",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "indexEndObj",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelAType",
                                "ofType": None
                            }
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [
                        {
                        "kind": "INTERFACE",
                        "name": "PaginationInterface",
                        "ofType": None
                        }
                    ],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "ModelAFilterInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "id",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "IDFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "booleanFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "BooleanFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "booleanFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "BooleanFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "booleanFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "BooleanFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "booleanFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "BooleanFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "booleanFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "BooleanFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "charFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "charFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "charFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "charFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "charFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "choiceFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "choiceFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "choiceFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "choiceFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "choiceFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "DateFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "DateFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "DateFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "DateFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "DateFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateTimeFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "DateTimeFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateTimeFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "DateTimeFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateTimeFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "DateTimeFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateTimeFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "DateTimeFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateTimeFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "DateTimeFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "timeFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "TimeFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "timeFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "TimeFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "timeFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "TimeFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "timeFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "TimeFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "timeFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "TimeFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "decimalFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "DecimalFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "decimalFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "DecimalFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "decimalFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "DecimalFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "decimalFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "DecimalFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "decimalFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "DecimalFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "durationFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "DurationFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "durationFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "DurationFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "durationFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "DurationFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "durationFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "DurationFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "durationFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "DurationFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "emailFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "EmailFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "emailFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "EmailFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "emailFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "EmailFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "emailFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "EmailFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "emailFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "EmailFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "floatFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "FloatFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "floatFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "FloatFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "floatFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "FloatFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "floatFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "FloatFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "floatFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "FloatFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "integerFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "IntFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "integerFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "IntFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "integerFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "IntFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "integerFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "IntFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "integerFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "IntFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "smallIntegerFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "IntFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "smallIntegerFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "IntFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "smallIntegerFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "IntFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "smallIntegerFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "IntFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "smallIntegerFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "IntFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "positiveIntegerFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "PositiveIntFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "positiveIntegerFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "PositiveIntFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "positiveIntegerFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "PositiveIntFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "positiveIntegerFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "PositiveIntFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "positiveIntegerFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "PositiveIntFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "slugFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "SlugFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "slugFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "SlugFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "slugFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "SlugFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "slugFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "SlugFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "slugFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "SlugFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "textFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "textFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "textFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "textFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "textFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "StringFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "urlFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "URLFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "urlFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "URLFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "urlFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "URLFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "urlFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "URLFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "urlFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "URLFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "uuidFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "UUIDFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "uuidFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "UUIDFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "uuidFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "UUIDFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "uuidFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "UUIDFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "uuidFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "UUIDFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyFieldWithoutRelatedName",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "objectId",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "PositiveIntFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "manyToManyFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "manyToManyFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "manyToManyFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "manyToManyFieldWithoutRelatedName",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "genericRelationField",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyRelated",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyNullableRelated",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyWithDescriptionRelated",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "oneToOneRelated",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "oneToOneNullableRelated",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "oneToOneWithDescriptionRelated",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "manyToManyRelated",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "manyToManyNullableRelated",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "manyToManyWithDescriptionRelated",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyBRelated",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelBFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "oneToOneBRelated",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelBFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "manyToManyBRelated",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelBFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "AND",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAFilterInput",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "OR",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAFilterInput",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "NOT",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "BooleanFilter",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "exact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iexact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "in",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "contains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "icontains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "startswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "istartswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "endswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iendswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "range",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "isNone",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "regex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iregex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "DateFilter",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "exact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iexact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "in",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "contains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "icontains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "startswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "istartswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "endswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iendswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "range",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "isNone",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "regex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iregex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "year",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "month",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "day",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "weekDay",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "isoWeekDay",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "week",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "isoYear",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "quarter",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "containedBy",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "DateTimeFilter",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "exact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iexact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "in",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "contains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "icontains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "startswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "istartswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "endswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iendswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "range",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "isNone",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "regex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iregex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "year",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "month",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "day",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "weekDay",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "isoWeekDay",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "week",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "isoYear",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "quarter",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "containedBy",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "hour",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "minute",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "second",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "date",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "time",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "TimeFilter",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "exact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iexact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "in",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "contains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "icontains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "startswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "istartswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "endswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iendswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "range",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "isNone",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "regex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iregex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "hour",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "minute",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "second",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "DecimalFilter",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "exact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iexact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "in",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "contains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "icontains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "startswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "istartswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "endswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iendswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "range",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "isNone",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "regex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iregex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "containedBy",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "DurationFilter",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "exact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iexact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "in",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "contains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "icontains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "startswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "istartswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "endswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iendswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "range",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "isNone",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "regex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iregex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "EmailFilter",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "exact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iexact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "in",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "contains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "icontains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "startswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "istartswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "endswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iendswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "range",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "isNone",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "regex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iregex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "FloatFilter",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "exact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iexact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "in",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "contains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "icontains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "startswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "istartswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "endswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iendswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "range",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "isNone",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "regex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iregex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "containedBy",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "IntFilter",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "exact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iexact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "in",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "contains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "icontains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "startswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "istartswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "endswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iendswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "range",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "isNone",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "regex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iregex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "containedBy",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "PositiveIntFilter",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "exact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iexact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "in",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "contains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "icontains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "startswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "istartswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "endswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iendswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "range",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "isNone",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "regex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iregex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "containedBy",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "SlugFilter",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "exact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iexact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "in",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "contains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "icontains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "startswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "istartswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "endswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iendswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "range",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "isNone",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "regex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iregex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "URLFilter",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "exact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iexact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "in",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "contains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "icontains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "startswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "istartswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "endswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iendswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "range",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "isNone",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "regex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iregex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "UUIDFilter",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "exact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iexact",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "gte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lt",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "lte",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "in",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "contains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "icontains",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "startswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "istartswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "endswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iendswith",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "range",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "isNone",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "regex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "iregex",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "ModelBFilterInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "id",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "IDFilter",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyField",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "oneToOneField",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "manyToManyField",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "AND",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelBFilterInput",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "OR",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelBFilterInput",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "NOT",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelBFilterInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "ModelAOrderByInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "id",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "booleanFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "booleanFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "booleanFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "booleanFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "booleanFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "charFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "charFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "charFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "charFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "charFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "choiceFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "choiceFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "choiceFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "choiceFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "choiceFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateTimeFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateTimeFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateTimeFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateTimeFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateTimeFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "timeFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "timeFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "timeFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "timeFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "timeFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "decimalFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "decimalFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "decimalFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "decimalFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "decimalFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "durationFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "durationFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "durationFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "durationFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "durationFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "emailFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "emailFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "emailFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "emailFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "emailFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "floatFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "floatFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "floatFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "floatFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "floatFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "integerFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "integerFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "integerFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "integerFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "integerFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "smallIntegerFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "smallIntegerFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "smallIntegerFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "smallIntegerFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "smallIntegerFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "positiveIntegerFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "positiveIntegerFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "positiveIntegerFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "positiveIntegerFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "positiveIntegerFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "slugFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "slugFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "slugFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "slugFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "slugFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "textFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "textFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "textFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "textFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "textFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "urlFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "urlFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "urlFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "urlFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "urlFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderStringEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "uuidFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "uuidFieldNotEditable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "uuidFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "uuidFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "uuidFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAOrderByInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAOrderByInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyFieldWithDescription",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAOrderByInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyFieldWithoutRelatedName",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAOrderByInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "objectId",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "oneToOneRelated",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAOrderByInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "oneToOneNullableRelated",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAOrderByInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "oneToOneWithDescriptionRelated",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAOrderByInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "oneToOneBRelated",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelBOrderByInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "ModelBOrderByInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "id",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "OrderEnum",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyField",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAOrderByInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "oneToOneField",
                        "description": None,
                        "type": {
                            "kind": "INPUT_OBJECT",
                            "name": "ModelAOrderByInput",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "UNION",
                    "name": "ModelAGenericForeignKeyFieldUnionType",
                    "description": None,
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": [
                        {
                        "kind": "OBJECT",
                        "name": "SimplecruddalsmodelType",
                        "ofType": None
                        },
                        {
                        "kind": "OBJECT",
                        "name": "ModelAType",
                        "ofType": None
                        },
                        {
                        "kind": "OBJECT",
                        "name": "ModelBType",
                        "ofType": None
                        },
                        {
                        "kind": "OBJECT",
                        "name": "ModelCType",
                        "ofType": None
                        },
                        {
                        "kind": "OBJECT",
                        "name": "ModelDType",
                        "ofType": None
                        },
                        {
                        "kind": "OBJECT",
                        "name": "ModelEType",
                        "ofType": None
                        },
                        {
                        "kind": "OBJECT",
                        "name": "ModelFType",
                        "ofType": None
                        }
                    ]
                    },
                    {
                    "kind": "OBJECT",
                    "name": "SimplecruddalsmodelType",
                    "description": None,
                    "fields": [
                        {
                        "name": "id",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "name",
                        "description": "The name of the menu",
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "isActive",
                        "description": "The status for enabling or disabling",
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "ModelBPaginatedType",
                    "description": None,
                    "fields": [
                        {
                        "name": "total",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "page",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "pages",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "hasNext",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "hasPrev",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "indexStartObj",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "indexEndObj",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelBType",
                                "ofType": None
                            }
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [
                        {
                        "kind": "INTERFACE",
                        "name": "PaginationInterface",
                        "ofType": None
                        }
                    ],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "Mutation",
                    "description": None,
                    "fields": [
                        {
                        "name": "createModelFs",
                        "description": None,
                        "args": [
                            {
                            "name": "input",
                            "description": "",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "CreateModelFInput",
                                    "ofType": None
                                }
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "CreateModelFsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "updateModelFs",
                        "description": None,
                        "args": [
                            {
                            "name": "input",
                            "description": "",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "UpdateModelFInput",
                                    "ofType": None
                                }
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "UpdateModelFsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "activateModelFs",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelFFilterInput",
                                "ofType": None
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ActivateModelFsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "deactivateModelFs",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelFFilterInput",
                                "ofType": None
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "DeactivateModelFsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "deleteModelFs",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelFFilterInput",
                                "ofType": None
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "DeleteModelFsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "createModelEs",
                        "description": None,
                        "args": [
                            {
                            "name": "input",
                            "description": "",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "CreateModelEInput",
                                    "ofType": None
                                }
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "CreateModelEsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "updateModelEs",
                        "description": None,
                        "args": [
                            {
                            "name": "input",
                            "description": "",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "UpdateModelEInput",
                                    "ofType": None
                                }
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "UpdateModelEsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "activateModelEs",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelEFilterInput",
                                "ofType": None
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ActivateModelEsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "deactivateModelEs",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelEFilterInput",
                                "ofType": None
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "DeactivateModelEsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "deleteModelEs",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelEFilterInput",
                                "ofType": None
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "DeleteModelEsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "createModelDs",
                        "description": None,
                        "args": [
                            {
                            "name": "input",
                            "description": "",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "CreateModelDInput",
                                    "ofType": None
                                }
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "CreateModelDsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "updateModelDs",
                        "description": None,
                        "args": [
                            {
                            "name": "input",
                            "description": "",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "UpdateModelDInput",
                                    "ofType": None
                                }
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "UpdateModelDsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "activateModelDs",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelDFilterInput",
                                "ofType": None
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ActivateModelDsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "deactivateModelDs",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelDFilterInput",
                                "ofType": None
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "DeactivateModelDsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "deleteModelDs",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelDFilterInput",
                                "ofType": None
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "DeleteModelDsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "createModelCs",
                        "description": None,
                        "args": [
                            {
                            "name": "input",
                            "description": "",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "CreateModelCInput",
                                    "ofType": None
                                }
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "CreateModelCsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "updateModelCs",
                        "description": None,
                        "args": [
                            {
                            "name": "input",
                            "description": "",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "UpdateModelCInput",
                                    "ofType": None
                                }
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "UpdateModelCsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "activateModelCs",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelCFilterInput",
                                "ofType": None
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ActivateModelCsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "deactivateModelCs",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelCFilterInput",
                                "ofType": None
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "DeactivateModelCsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "deleteModelCs",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelCFilterInput",
                                "ofType": None
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "DeleteModelCsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "createModelBs",
                        "description": None,
                        "args": [
                            {
                            "name": "input",
                            "description": "",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "CreateModelBInput",
                                    "ofType": None
                                }
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "CreateModelBsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "updateModelBs",
                        "description": None,
                        "args": [
                            {
                            "name": "input",
                            "description": "",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "UpdateModelBInput",
                                    "ofType": None
                                }
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "UpdateModelBsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "activateModelBs",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelBFilterInput",
                                "ofType": None
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ActivateModelBsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "deactivateModelBs",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelBFilterInput",
                                "ofType": None
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "DeactivateModelBsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "deleteModelBs",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelBFilterInput",
                                "ofType": None
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "DeleteModelBsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "createModelAs",
                        "description": None,
                        "args": [
                            {
                            "name": "input",
                            "description": "",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "CreateModelAInput",
                                    "ofType": None
                                }
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "CreateModelAsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "updateModelAs",
                        "description": None,
                        "args": [
                            {
                            "name": "input",
                            "description": "",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "UpdateModelAInput",
                                    "ofType": None
                                }
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "UpdateModelAsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "activateModelAs",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "ActivateModelAsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "deactivateModelAs",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "DeactivateModelAsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "deleteModelAs",
                        "description": None,
                        "args": [
                            {
                            "name": "where",
                            "description": "",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                                }
                            },
                            "defaultValue": None
                            }
                        ],
                        "type": {
                            "kind": "OBJECT",
                            "name": "DeleteModelAsPayload",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "CreateModelFsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelFType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "ErrorsType",
                    "description": None,
                    "fields": [
                        {
                        "name": "objectPosition",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "ErrorType",
                    "description": None,
                    "fields": [
                        {
                        "name": "field",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "messages",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "CreateModelFInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "text",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "UpdateModelFsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelFType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "UpdateModelFInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "id",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "text",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "ActivateModelFsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelFType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "DeactivateModelFsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelFType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "DeleteModelFsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelFType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "success",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "CreateModelEsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelEType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "CreateModelEInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "fkF",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "otoF",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "text",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "mtmF",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            }
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "UpdateModelEsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelEType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "UpdateModelEInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "id",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "fkF",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "otoF",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "text",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "mtmF",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "ActivateModelEsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelEType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "DeactivateModelEsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelEType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "DeleteModelEsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelEType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "success",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "CreateModelDsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelDType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "CreateModelDInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "createUpdateOnly",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "createOnly",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "updateOnly",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "whereOnly",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "orderByOnly",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "allInput",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "allExclude",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "UpdateModelDsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelDType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "UpdateModelDInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "id",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "createUpdateOnly",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "createOnly",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "updateOnly",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "whereOnly",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "orderByOnly",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "allInput",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "allExclude",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "ActivateModelDsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelDType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "DeactivateModelDsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelDType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "DeleteModelDsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelDType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "success",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "CreateModelCsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelCType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "CreateModelCInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "createUpdateOnly",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "createOnly",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "updateOnly",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "whereOnly",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "orderByOnly",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "allInput",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "allExclude",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "UpdateModelCsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelCType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "UpdateModelCInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "id",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "createUpdateOnly",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "createOnly",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "updateOnly",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "whereOnly",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "orderByOnly",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "allInput",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "allExclude",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "ActivateModelCsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelCType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "DeactivateModelCsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelCType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "DeleteModelCsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelCType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "success",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "CreateModelBsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelBType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "CreateModelBInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "foreignKeyField",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "oneToOneField",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "manyToManyField",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            }
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "UpdateModelBsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelBType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "UpdateModelBInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "id",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyField",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "oneToOneField",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "manyToManyField",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "ActivateModelBsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelBType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "DeactivateModelBsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelBType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "DeleteModelBsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelBType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "success",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "CreateModelAsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelAType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "CreateModelAInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "binaryFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Binary",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "binaryFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Binary",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "binaryFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Binary",
                            "ofType": None
                        },
                        "defaultValue": "\"YmluYXJ5X2ZpZWxkX3dpdGhfZGVmYXVsdA==\""
                        },
                        {
                        "name": "binaryFieldWithDescription",
                        "description": "binary_field_with_description",
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Binary",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "booleanFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "booleanFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "booleanFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": "true"
                        },
                        {
                        "name": "booleanFieldWithDescription",
                        "description": "boolean_field_with_description",
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "charFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "charFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "charFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": "\"char_field_with_default\""
                        },
                        {
                        "name": "charFieldWithDescription",
                        "description": "char_field_with_description",
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "choiceFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "ENUM",
                            "name": "SimplecruddalsmodelModelAChoiceFieldRequiredChoices",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "choiceFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "SimplecruddalsmodelModelAChoiceFieldNullableChoices",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "choiceFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "SimplecruddalsmodelModelAChoiceFieldWithDefaultChoices",
                            "ofType": None
                        },
                        "defaultValue": "A"
                        },
                        {
                        "name": "choiceFieldWithDescription",
                        "description": "choice_field_with_description",
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "ENUM",
                            "name": "SimplecruddalsmodelModelAChoiceFieldWithDescriptionChoices",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateFieldWithDescription",
                        "description": "date_field_with_description",
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateTimeFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateTimeFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateTimeFieldWithDescription",
                        "description": "date_time_field_with_description",
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "timeFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "timeFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "timeFieldWithDescription",
                        "description": "time_field_with_description",
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "decimalFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "decimalFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "decimalFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "defaultValue": "\"0\""
                        },
                        {
                        "name": "decimalFieldWithDescription",
                        "description": "decimal_field_with_description",
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "durationFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "durationFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "durationFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "durationFieldWithDescription",
                        "description": "duration_field_with_description",
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "emailFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "emailFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "emailFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "defaultValue": "\"emailField@withDefault.com\""
                        },
                        {
                        "name": "emailFieldWithDescription",
                        "description": "email_field_with_description",
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "floatFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "floatFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "floatFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "defaultValue": "0"
                        },
                        {
                        "name": "floatFieldWithDescription",
                        "description": "float_field_with_description",
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "integerFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "integerFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "integerFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": "0"
                        },
                        {
                        "name": "integerFieldWithDescription",
                        "description": "integer_field_with_description",
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "smallIntegerFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "smallIntegerFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "smallIntegerFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": "0"
                        },
                        {
                        "name": "smallIntegerFieldWithDescription",
                        "description": "small_integer_field_with_description",
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "positiveIntegerFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "positiveIntegerFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "positiveIntegerFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": "0"
                        },
                        {
                        "name": "positiveIntegerFieldWithDescription",
                        "description": "positive_integer_field_with_description",
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "slugFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "slugFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "slugFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "defaultValue": "\"slug_field_with_default\""
                        },
                        {
                        "name": "slugFieldWithDescription",
                        "description": "slug_field_with_description",
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "textFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "textFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "textFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": "\"text_field_with_default\""
                        },
                        {
                        "name": "textFieldWithDescription",
                        "description": "text_field_with_description",
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "urlFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "urlFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "urlFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "defaultValue": "\"https://url_field_with_default.com\""
                        },
                        {
                        "name": "urlFieldWithDescription",
                        "description": "url_field_with_description",
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "uuidFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "uuidFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "uuidFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "uuidFieldWithDescription",
                        "description": "uuid_field_with_description",
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyFieldWithDescription",
                        "description": "foreign_key_field_with_description",
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyFieldWithoutRelatedName",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "oneToOneFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "oneToOneFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "oneToOneFieldWithDescription",
                        "description": "one_to_one_field_with_description",
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "oneToOneFieldWithoutRelatedName",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "contentType",
                        "description": "The content type",
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "objectId",
                        "description": "The object id",
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "manyToManyFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "manyToManyFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "manyToManyFieldWithDescription",
                        "description": "many_to_many_field_with_description",
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "manyToManyFieldWithoutRelatedName",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            }
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "UpdateModelAsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelAType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "INPUT_OBJECT",
                    "name": "UpdateModelAInput",
                    "description": None,
                    "fields": None,
                    "inputFields": [
                        {
                        "name": "id",
                        "description": None,
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "binaryFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Binary",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "binaryFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Binary",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "binaryFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Binary",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "binaryFieldWithDescription",
                        "description": "binary_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "Binary",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "booleanFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "booleanFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "booleanFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "booleanFieldWithDescription",
                        "description": "boolean_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "charFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "charFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "charFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "charFieldWithDescription",
                        "description": "char_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "choiceFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "SimplecruddalsmodelModelAChoiceFieldRequiredChoices",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "choiceFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "SimplecruddalsmodelModelAChoiceFieldNullableChoices",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "choiceFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "ENUM",
                            "name": "SimplecruddalsmodelModelAChoiceFieldWithDefaultChoices",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "choiceFieldWithDescription",
                        "description": "choice_field_with_description",
                        "type": {
                            "kind": "ENUM",
                            "name": "SimplecruddalsmodelModelAChoiceFieldWithDescriptionChoices",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateFieldWithDescription",
                        "description": "date_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "Date",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateTimeFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateTimeFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "dateTimeFieldWithDescription",
                        "description": "date_time_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "DateTime",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "timeFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "timeFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "timeFieldWithDescription",
                        "description": "time_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "Time",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "decimalFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "decimalFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "decimalFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "decimalFieldWithDescription",
                        "description": "decimal_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "Decimal",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "durationFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "durationFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "durationFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "durationFieldWithDescription",
                        "description": "duration_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "Duration",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "emailFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "emailFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "emailFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "emailFieldWithDescription",
                        "description": "email_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "Email",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "floatFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "floatFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "floatFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "floatFieldWithDescription",
                        "description": "float_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "Float",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "integerFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "integerFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "integerFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "integerFieldWithDescription",
                        "description": "integer_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "smallIntegerFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "smallIntegerFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "smallIntegerFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "smallIntegerFieldWithDescription",
                        "description": "small_integer_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "Int",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "positiveIntegerFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "positiveIntegerFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "positiveIntegerFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "positiveIntegerFieldWithDescription",
                        "description": "positive_integer_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "slugFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "slugFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "slugFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "slugFieldWithDescription",
                        "description": "slug_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "Slug",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "textFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "textFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "textFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "textFieldWithDescription",
                        "description": "text_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "urlFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "urlFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "urlFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "urlFieldWithDescription",
                        "description": "url_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "URL",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "uuidFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "uuidFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "uuidFieldWithDefault",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "uuidFieldWithDescription",
                        "description": "uuid_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "UUID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyFieldWithDescription",
                        "description": "foreign_key_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "foreignKeyFieldWithoutRelatedName",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "oneToOneFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "oneToOneFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "oneToOneFieldWithDescription",
                        "description": "one_to_one_field_with_description",
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "oneToOneFieldWithoutRelatedName",
                        "description": None,
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "contentType",
                        "description": "The content type",
                        "type": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "objectId",
                        "description": "The object id",
                        "type": {
                            "kind": "SCALAR",
                            "name": "PositiveInt",
                            "ofType": None
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "manyToManyFieldRequired",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "manyToManyFieldNullable",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "manyToManyFieldWithDescription",
                        "description": "many_to_many_field_with_description",
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        },
                        {
                        "name": "manyToManyFieldWithoutRelatedName",
                        "description": None,
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "ID",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        }
                    ],
                    "interfaces": None,
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "ActivateModelAsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelAType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "DeactivateModelAsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelAType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "DeleteModelAsPayload",
                    "description": None,
                    "fields": [
                        {
                        "name": "objects",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ModelAType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "errors",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "ErrorsType",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "success",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "__Schema",
                    "description": "A GraphQL Schema defines the capabilities of a GraphQL server. It exposes all available types and directives on the server, as well as the entry points for query, mutation, and subscription operations.",
                    "fields": [
                        {
                        "name": "description",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "types",
                        "description": "A list of all types supported by this server.",
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "__Type",
                                "ofType": None
                                }
                            }
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "queryType",
                        "description": "The type that query operations will be rooted at.",
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "__Type",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "mutationType",
                        "description": "If this server supports mutation, the type that mutation operations will be rooted at.",
                        "args": [],
                        "type": {
                            "kind": "OBJECT",
                            "name": "__Type",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "subscriptionType",
                        "description": "If this server support subscription, the type that subscription operations will be rooted at.",
                        "args": [],
                        "type": {
                            "kind": "OBJECT",
                            "name": "__Type",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "directives",
                        "description": "A list of all directives supported by this server.",
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "__Directive",
                                "ofType": None
                                }
                            }
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "__Type",
                    "description": "The fundamental unit of any GraphQL Schema is the type. There are many kinds of types in GraphQL as represented by the `__TypeKind` enum.\n\nDepending on the kind of a type, certain fields describe information about that type. Scalar types provide no information beyond a name, description and optional `specifiedByURL`, while Enum types provide their values. Object and Interface types provide the fields they describe. Abstract types, Union and Interface, provide the Object types possible at runtime. List and NonNull types compose other types.",
                    "fields": [
                        {
                        "name": "kind",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "ENUM",
                            "name": "__TypeKind",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "name",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "description",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "specifiedByURL",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "fields",
                        "description": None,
                        "args": [
                            {
                            "name": "includeDeprecated",
                            "description": None,
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            },
                            "defaultValue": "false"
                            }
                        ],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                                "kind": "OBJECT",
                                "name": "__Field",
                                "ofType": None
                            }
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "interfaces",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                                "kind": "OBJECT",
                                "name": "__Type",
                                "ofType": None
                            }
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "possibleTypes",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                                "kind": "OBJECT",
                                "name": "__Type",
                                "ofType": None
                            }
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "enumValues",
                        "description": None,
                        "args": [
                            {
                            "name": "includeDeprecated",
                            "description": None,
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            },
                            "defaultValue": "false"
                            }
                        ],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                                "kind": "OBJECT",
                                "name": "__EnumValue",
                                "ofType": None
                            }
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "inputFields",
                        "description": None,
                        "args": [
                            {
                            "name": "includeDeprecated",
                            "description": None,
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            },
                            "defaultValue": "false"
                            }
                        ],
                        "type": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                                "kind": "OBJECT",
                                "name": "__InputValue",
                                "ofType": None
                            }
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "ofType",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "OBJECT",
                            "name": "__Type",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "ENUM",
                    "name": "__TypeKind",
                    "description": "An enum describing what kind of type a given `__Type` is.",
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": [
                        {
                        "name": "SCALAR",
                        "description": "Indicates this type is a scalar.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "OBJECT",
                        "description": "Indicates this type is an object. `fields` and `interfaces` are valid fields.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "INTERFACE",
                        "description": "Indicates this type is an interface. `fields`, `interfaces`, and `possibleTypes` are valid fields.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "UNION",
                        "description": "Indicates this type is a union. `possibleTypes` is a valid field.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "ENUM",
                        "description": "Indicates this type is an enum. `enumValues` is a valid field.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "INPUT_OBJECT",
                        "description": "Indicates this type is an input object. `inputFields` is a valid field.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "LIST",
                        "description": "Indicates this type is a list. `ofType` is a valid field.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "NON_NULL",
                        "description": "Indicates this type is a non-None. `ofType` is a valid field.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "__Field",
                    "description": "Object and Interface types are described by a list of Fields, each of which has a name, potentially a list of arguments, and a return type.",
                    "fields": [
                        {
                        "name": "name",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "description",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "args",
                        "description": None,
                        "args": [
                            {
                            "name": "includeDeprecated",
                            "description": None,
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            },
                            "defaultValue": "false"
                            }
                        ],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "__InputValue",
                                "ofType": None
                                }
                            }
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "type",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "__Type",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "isDeprecated",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "deprecationReason",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "__InputValue",
                    "description": "Arguments provided to Fields or Directives and the input fields of an InputObject are represented as Input Values which describe their type and optionally a default value.",
                    "fields": [
                        {
                        "name": "name",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "description",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "type",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "OBJECT",
                            "name": "__Type",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "defaultValue",
                        "description": "A GraphQL-formatted string representing the default value for this input value.",
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "isDeprecated",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "deprecationReason",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "__EnumValue",
                    "description": "One possible value for a given Enum. Enum values are unique values, not a placeholder for a string or numeric value. However an Enum value is returned in a JSON response as a string.",
                    "fields": [
                        {
                        "name": "name",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "description",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "isDeprecated",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "deprecationReason",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "OBJECT",
                    "name": "__Directive",
                    "description": "A Directive provides a way to describe alternate runtime execution and type validation behavior in a GraphQL document.\n\nIn some cases, you need to provide options to alter GraphQL's execution behavior in ways field arguments will not suffice, such as conditionally including or skipping a field. Directives provide this by describing additional information to the executor.",
                    "fields": [
                        {
                        "name": "name",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "description",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "isRepeatable",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "locations",
                        "description": None,
                        "args": [],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "ENUM",
                                "name": "__DirectiveLocation",
                                "ofType": None
                                }
                            }
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "args",
                        "description": None,
                        "args": [
                            {
                            "name": "includeDeprecated",
                            "description": None,
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            },
                            "defaultValue": "false"
                            }
                        ],
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "LIST",
                            "name": None,
                            "ofType": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "__InputValue",
                                "ofType": None
                                }
                            }
                            }
                        },
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "inputFields": None,
                    "interfaces": [],
                    "enumValues": None,
                    "possibleTypes": None
                    },
                    {
                    "kind": "ENUM",
                    "name": "__DirectiveLocation",
                    "description": "A Directive can be adjacent to many parts of the GraphQL language, a __DirectiveLocation describes one such possible adjacencies.",
                    "fields": None,
                    "inputFields": None,
                    "interfaces": None,
                    "enumValues": [
                        {
                        "name": "QUERY",
                        "description": "Location adjacent to a query operation.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "MUTATION",
                        "description": "Location adjacent to a mutation operation.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "SUBSCRIPTION",
                        "description": "Location adjacent to a subscription operation.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "FIELD",
                        "description": "Location adjacent to a field.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "FRAGMENT_DEFINITION",
                        "description": "Location adjacent to a fragment definition.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "FRAGMENT_SPREAD",
                        "description": "Location adjacent to a fragment spread.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "INLINE_FRAGMENT",
                        "description": "Location adjacent to an inline fragment.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "VARIABLE_DEFINITION",
                        "description": "Location adjacent to a variable definition.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "SCHEMA",
                        "description": "Location adjacent to a schema definition.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "SCALAR",
                        "description": "Location adjacent to a scalar definition.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "OBJECT",
                        "description": "Location adjacent to an object type definition.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "FIELD_DEFINITION",
                        "description": "Location adjacent to a field definition.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "ARGUMENT_DEFINITION",
                        "description": "Location adjacent to an argument definition.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "INTERFACE",
                        "description": "Location adjacent to an interface definition.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "UNION",
                        "description": "Location adjacent to a union definition.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "ENUM",
                        "description": "Location adjacent to an enum definition.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "ENUM_VALUE",
                        "description": "Location adjacent to an enum value definition.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "INPUT_OBJECT",
                        "description": "Location adjacent to an input object type definition.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        },
                        {
                        "name": "INPUT_FIELD_DEFINITION",
                        "description": "Location adjacent to an input object field definition.",
                        "isDeprecated": False,
                        "deprecationReason": None
                        }
                    ],
                    "possibleTypes": None
                    }
                ],
                "directives": [
                    {
                    "name": "include",
                    "description": "Directs the executor to include this field or fragment only when the `if` argument is true.",
                    "locations": [
                        "FIELD",
                        "FRAGMENT_SPREAD",
                        "INLINE_FRAGMENT"
                    ],
                    "args": [
                        {
                        "name": "if",
                        "description": "Included when true.",
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        }
                    ]
                    },
                    {
                    "name": "skip",
                    "description": "Directs the executor to skip this field or fragment when the `if` argument is true.",
                    "locations": [
                        "FIELD",
                        "FRAGMENT_SPREAD",
                        "INLINE_FRAGMENT"
                    ],
                    "args": [
                        {
                        "name": "if",
                        "description": "Skipped when true.",
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "Boolean",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        }
                    ]
                    },
                    {
                    "name": "deprecated",
                    "description": "Marks an element of a GraphQL schema as no longer supported.",
                    "locations": [
                        "FIELD_DEFINITION",
                        "ARGUMENT_DEFINITION",
                        "INPUT_FIELD_DEFINITION",
                        "ENUM_VALUE"
                    ],
                    "args": [
                        {
                        "name": "reason",
                        "description": "Explains why this element was deprecated, usually also including a suggestion for how to access supported similar data. Formatted using the Markdown syntax, as specified by [CommonMark](https://commonmark.org/).",
                        "type": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                        },
                        "defaultValue": "\"No longer supported\""
                        }
                    ]
                    },
                    {
                    "name": "specifiedBy",
                    "description": "Exposes a URL that specifies the behaviour of this scalar.",
                    "locations": [
                        "SCALAR"
                    ],
                    "args": [
                        {
                        "name": "url",
                        "description": "The URL that specifies the behaviour of this scalar.",
                        "type": {
                            "kind": "NON_NULL",
                            "name": None,
                            "ofType": {
                            "kind": "SCALAR",
                            "name": "String",
                            "ofType": None
                            }
                        },
                        "defaultValue": None
                        }
                    ]
                    }
                ]
                }
            }
        }
        actual_schema = self.get_schema()
        # self.assertDictEqual(actual_schema, schema_for_test)