# -*- coding: utf-8 -*-
from tests.utils import SchemaTestCase

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

    