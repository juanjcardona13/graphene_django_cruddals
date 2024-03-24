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
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "id",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "binaryFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Binary",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "binaryFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Binary",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "binaryFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Binary",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "binary_field_with_description",
                            "name": "binaryFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Binary",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "booleanFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "booleanFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "booleanFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "boolean_field_with_description",
                            "name": "booleanFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "charFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "charFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "charFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "char_field_with_description",
                            "name": "charFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "choiceFieldRequired",
                            "type": {
                                "kind": "ENUM",
                                "name": "MenuModelAChoiceFieldRequiredChoices",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "choiceFieldNullable",
                            "type": {
                                "kind": "ENUM",
                                "name": "MenuModelAChoiceFieldNullableChoices",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "choiceFieldWithDefault",
                            "type": {
                                "kind": "ENUM",
                                "name": "MenuModelAChoiceFieldWithDefaultChoices",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "choice_field_with_description",
                            "name": "choiceFieldWithDescription",
                            "type": {
                                "kind": "ENUM",
                                "name": "MenuModelAChoiceFieldWithDescriptionChoices",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "date_field_with_description",
                            "name": "dateFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateTimeFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateTimeFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "date_time_field_with_description",
                            "name": "dateTimeFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "timeFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "timeFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "time_field_with_description",
                            "name": "timeFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "decimalFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "decimalFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "decimalFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "decimal_field_with_description",
                            "name": "decimalFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "durationFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "durationFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "durationFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "duration_field_with_description",
                            "name": "durationFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "emailFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "emailFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "emailFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "email_field_with_description",
                            "name": "emailFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "floatFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "floatFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "floatFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "float_field_with_description",
                            "name": "floatFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "integerFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "integerFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "integerFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "integer_field_with_description",
                            "name": "integerFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "smallIntegerFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "smallIntegerFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "smallIntegerFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "small_integer_field_with_description",
                            "name": "smallIntegerFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "positiveIntegerFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "positiveIntegerFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "positiveIntegerFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "positive_integer_field_with_description",
                            "name": "positiveIntegerFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "slugFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "slugFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "slugFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "slug_field_with_description",
                            "name": "slugFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "textFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "textFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "textFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "text_field_with_description",
                            "name": "textFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "urlFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "urlFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "urlFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "url_field_with_description",
                            "name": "urlFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "uuidFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "uuidFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "uuidFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "uuid_field_with_description",
                            "name": "uuidFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "foreign_key_field_with_description",
                            "name": "foreignKeyFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyFieldWithoutRelatedName",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "oneToOneFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "oneToOneFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "one_to_one_field_with_description",
                            "name": "oneToOneFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "oneToOneFieldWithoutRelatedName",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "The content type",
                            "name": "contentType",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "The object id",
                            "name": "objectId",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "manyToManyFieldRequired",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "manyToManyFieldNullable",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "many_to_many_field_with_description",
                            "name": "manyToManyFieldWithDescription",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "manyToManyFieldWithoutRelatedName",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "ModelAInput",
                        "possibleTypes": None
                        },
                        {
                        "description": "The `ID` scalar type represents a unique identifier, often used to refetch an object or as key for a cache. The ID type appears in a JSON response as a String; however, it is not intended to be human-readable. When expected as an input type, any string (such as `\"4\"`) or integer (such as `4`) input value will be accepted as an ID.",
                        "enumValues": None,
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "SCALAR",
                        "name": "ID",
                        "possibleTypes": None
                        },
                        {
                        "description": "BinaryArray is used to convert a Django BinaryField to the string form",
                        "enumValues": None,
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "SCALAR",
                        "name": "Binary",
                        "possibleTypes": None
                        },
                        {
                        "description": "The `Boolean` scalar type represents `true` or `False`.",
                        "enumValues": None,
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "SCALAR",
                        "name": "Boolean",
                        "possibleTypes": None
                        },
                        {
                        "description": "The `String` scalar type represents textual data, represented as UTF-8 character sequences. The String type is most often used by GraphQL to represent free-form human-readable text.",
                        "enumValues": None,
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "SCALAR",
                        "name": "String",
                        "possibleTypes": None
                        },
                        {
                        "description": "An enumeration.",
                        "enumValues": [
                            {
                            "deprecationReason": None,
                            "description": "A",
                            "isDeprecated": False,
                            "name": "A"
                            },
                            {
                            "deprecationReason": None,
                            "description": "B",
                            "isDeprecated": False,
                            "name": "B"
                            }
                        ],
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "ENUM",
                        "name": "MenuModelAChoiceFieldRequiredChoices",
                        "possibleTypes": None
                        },
                        {
                        "description": "An enumeration.",
                        "enumValues": [
                            {
                            "deprecationReason": None,
                            "description": "A",
                            "isDeprecated": False,
                            "name": "A"
                            },
                            {
                            "deprecationReason": None,
                            "description": "B",
                            "isDeprecated": False,
                            "name": "B"
                            }
                        ],
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "ENUM",
                        "name": "MenuModelAChoiceFieldNullableChoices",
                        "possibleTypes": None
                        },
                        {
                        "description": "An enumeration.",
                        "enumValues": [
                            {
                            "deprecationReason": None,
                            "description": "A",
                            "isDeprecated": False,
                            "name": "A"
                            },
                            {
                            "deprecationReason": None,
                            "description": "B",
                            "isDeprecated": False,
                            "name": "B"
                            }
                        ],
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "ENUM",
                        "name": "MenuModelAChoiceFieldWithDefaultChoices",
                        "possibleTypes": None
                        },
                        {
                        "description": "An enumeration.",
                        "enumValues": [
                            {
                            "deprecationReason": None,
                            "description": "A",
                            "isDeprecated": False,
                            "name": "A"
                            },
                            {
                            "deprecationReason": None,
                            "description": "B",
                            "isDeprecated": False,
                            "name": "B"
                            }
                        ],
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "ENUM",
                        "name": "MenuModelAChoiceFieldWithDescriptionChoices",
                        "possibleTypes": None
                        },
                        {
                        "description": "The `Date` scalar type represents a Date\nvalue as specified by\n[iso8601](https://en.wikipedia.org/wiki/ISO_8601).",
                        "enumValues": None,
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "SCALAR",
                        "name": "Date",
                        "possibleTypes": None
                        },
                        {
                        "description": "The `DateTime` scalar type represents a DateTime\nvalue as specified by\n[iso8601](https://en.wikipedia.org/wiki/ISO_8601).",
                        "enumValues": None,
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "SCALAR",
                        "name": "DateTime",
                        "possibleTypes": None
                        },
                        {
                        "description": "The `Time` scalar type represents a Time value as\nspecified by\n[iso8601](https://en.wikipedia.org/wiki/ISO_8601).",
                        "enumValues": None,
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "SCALAR",
                        "name": "Time",
                        "possibleTypes": None
                        },
                        {
                        "description": "The `Decimal` scalar type represents a python Decimal.",
                        "enumValues": None,
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "SCALAR",
                        "name": "Decimal",
                        "possibleTypes": None
                        },
                        {
                        "description": "Duration fields in Django are stored as timedelta in Python,\nand as a duration in the Database. We will represent them as\na total number of seconds in GraphQL.",
                        "enumValues": None,
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "SCALAR",
                        "name": "Duration",
                        "possibleTypes": None
                        },
                        {
                        "description": "A field whose value conforms to the standard\ninternet email address format as specified in\nHTML Spec: https://html.spec.whatwg.org/multipage/input.html#valid-e-mail-address.",
                        "enumValues": None,
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "SCALAR",
                        "name": "Email",
                        "possibleTypes": None
                        },
                        {
                        "description": "The `Float` scalar type represents signed double-precision fractional values as specified by [IEEE 754](https://en.wikipedia.org/wiki/IEEE_floating_point).",
                        "enumValues": None,
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "SCALAR",
                        "name": "Float",
                        "possibleTypes": None
                        },
                        {
                        "description": "The `Int` scalar type represents non-fractional signed whole numeric values. Int can represent values between -(2^31) and 2^31 - 1.",
                        "enumValues": None,
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "SCALAR",
                        "name": "Int",
                        "possibleTypes": None
                        },
                        {
                        "description": "Integers that will have a value of 0 or more.",
                        "enumValues": None,
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "SCALAR",
                        "name": "PositiveInt",
                        "possibleTypes": None
                        },
                        {
                        "description": "Slug is a newspaper term. A slug is a short label for something, containing only letters, numbers, underscores or hyphens. They\u2019re generally used in URLs.",
                        "enumValues": None,
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "SCALAR",
                        "name": "Slug",
                        "possibleTypes": None
                        },
                        {
                        "description": "A field whose value conforms to the standard URL format as specified in RFC3986: https://www.ietf.org/rfc/rfc3986.txt.",
                        "enumValues": None,
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "SCALAR",
                        "name": "URL",
                        "possibleTypes": None
                        },
                        {
                        "description": "Leverages the internal Python implementation of UUID (uuid.UUID) to provide native UUID objects\nin fields, resolvers and input.",
                        "enumValues": None,
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "SCALAR",
                        "name": "UUID",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelFFilterInput",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "readModelF",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelFType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelFFilterInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "orderBy",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelFOrderByInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "paginated",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "PaginatedInput",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "searchModelFs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelFPaginatedType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "listModelFs",
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
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelEFilterInput",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "readModelE",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelEType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelEFilterInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "orderBy",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelEOrderByInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "paginated",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "PaginatedInput",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "searchModelEs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelEPaginatedType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "listModelEs",
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
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelDFilterInput",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "readModelD",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelDType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelDFilterInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "orderBy",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelDOrderByInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "paginated",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "PaginatedInput",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "searchModelDs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelDPaginatedType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "listModelDs",
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
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelCFilterInput",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "readModelC",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelCType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelCFilterInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "orderBy",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelCOrderByInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "paginated",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "PaginatedInput",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "searchModelCs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelCPaginatedType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "listModelCs",
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
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelBFilterInput",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "readModelB",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelBType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelBFilterInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "orderBy",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelBOrderByInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "paginated",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "PaginatedInput",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "searchModelBs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelBPaginatedType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "listModelBs",
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
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAFilterInput",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "readModelA",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelAType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAFilterInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "orderBy",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAOrderByInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "paginated",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "PaginatedInput",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "searchModelAs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelAPaginatedType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "listModelAs",
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
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "Query",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "id",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "text",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelEFilterInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "orderBy",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelEOrderByInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "paginated",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "PaginatedInput",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "paginatedFkFRelated",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelEPaginatedType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "otoFRelated",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelEType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelEFilterInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "orderBy",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelEOrderByInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "paginated",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "PaginatedInput",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "paginatedMtmFRelated",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelEPaginatedType",
                                "ofType": None
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "ModelFType",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "total",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "page",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "pages",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "hasNext",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "hasPrev",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "indexStartObj",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "indexEndObj",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
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
                            }
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
                        "kind": "OBJECT",
                        "name": "ModelEPaginatedType",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "total",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "page",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "pages",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "hasNext",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "hasPrev",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "indexStartObj",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "indexEndObj",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "INTERFACE",
                        "name": "PaginationInterface",
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
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "id",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "fkF",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelFType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "otoF",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelFType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "text",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelFFilterInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "orderBy",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelFOrderByInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "paginated",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "PaginatedInput",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "paginatedMtmF",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelFPaginatedType",
                                "ofType": None
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "ModelEType",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "total",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "page",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "pages",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "hasNext",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "hasPrev",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "indexStartObj",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "indexEndObj",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
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
                            }
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
                        "kind": "OBJECT",
                        "name": "ModelFPaginatedType",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "id",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "IDFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "text",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "fkFRelated",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelEFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "otoFRelated",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelEFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "mtmFRelated",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelEFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "AND",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelFFilterInput",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "OR",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelFFilterInput",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "NOT",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelFFilterInput",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "ModelFFilterInput",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "exact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iexact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "in",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "contains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "icontains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "startswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "istartswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "endswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iendswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "range",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "isNone",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "regex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iregex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "containedBy",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "IDFilter",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "exact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iexact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "in",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "contains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "icontains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "startswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "istartswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "endswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iendswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "range",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "isNone",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "regex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iregex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "StringFilter",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "id",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "IDFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "fkF",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelFFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "otoF",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelFFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "text",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "mtmF",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelFFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "AND",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelEFilterInput",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "OR",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelEFilterInput",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "NOT",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelEFilterInput",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "ModelEFilterInput",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "id",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "text",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "otoFRelated",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelEOrderByInput",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "ModelFOrderByInput",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": [
                            {
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "ASC"
                            },
                            {
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "DESC"
                            }
                        ],
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "ENUM",
                        "name": "OrderEnum",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": [
                            {
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "ASC"
                            },
                            {
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "DESC"
                            },
                            {
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "IASC"
                            },
                            {
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "IDESC"
                            }
                        ],
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "ENUM",
                        "name": "OrderStringEnum",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "id",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "fkF",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelFOrderByInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "otoF",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelFOrderByInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "text",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "ModelEOrderByInput",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": "1",
                            "description": None,
                            "name": "page",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": "\"All\"",
                            "description": None,
                            "name": "pageSize",
                            "type": {
                                "kind": "SCALAR",
                                "name": "IntOrAll",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "PaginatedInput",
                        "possibleTypes": None
                        },
                        {
                        "description": "The page size can be int or 'All'",
                        "enumValues": None,
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "SCALAR",
                        "name": "IntOrAll",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "id",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "createUpdateOnly",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "createOnly",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "updateOnly",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "whereOnly",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "orderByOnly",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "allInput",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "allExclude",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "ModelDType",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "id",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "IDFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "createUpdateOnly",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "createOnly",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "updateOnly",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "whereOnly",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "orderByOnly",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "allInput",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "allExclude",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "AND",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelDFilterInput",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "OR",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelDFilterInput",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "NOT",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelDFilterInput",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "ModelDFilterInput",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "total",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "page",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "pages",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "hasNext",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "hasPrev",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "indexStartObj",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "indexEndObj",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
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
                            }
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
                        "kind": "OBJECT",
                        "name": "ModelDPaginatedType",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "id",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "createUpdateOnly",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "createOnly",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "updateOnly",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "whereOnly",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "orderByOnly",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "allInput",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "allExclude",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "ModelDOrderByInput",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "id",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "createUpdateOnly",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "createOnly",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "updateOnly",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "whereOnly",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "orderByOnly",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "allInput",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "allExclude",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "ModelCType",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "id",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "IDFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "createUpdateOnly",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "createOnly",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "updateOnly",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "whereOnly",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "orderByOnly",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "allInput",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "allExclude",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "AND",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelCFilterInput",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "OR",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelCFilterInput",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "NOT",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelCFilterInput",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "ModelCFilterInput",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "total",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "page",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "pages",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "hasNext",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "hasPrev",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "indexStartObj",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "indexEndObj",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
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
                            }
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
                        "kind": "OBJECT",
                        "name": "ModelCPaginatedType",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "id",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "createUpdateOnly",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "createOnly",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "updateOnly",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "whereOnly",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "orderByOnly",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "allInput",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "allExclude",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "ModelCOrderByInput",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "id",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "foreignKeyField",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelAType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "oneToOneField",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelAType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAFilterInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "orderBy",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAOrderByInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "paginated",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "PaginatedInput",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "paginatedManyToManyField",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelAPaginatedType",
                                "ofType": None
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "ModelBType",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "id",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "binaryFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Binary",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "binaryFieldNotEditable",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Binary",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "binaryFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Binary",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "binaryFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Binary",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "binary_field_with_description",
                            "isDeprecated": False,
                            "name": "binaryFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Binary",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "booleanFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "booleanFieldNotEditable",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "booleanFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "booleanFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "boolean_field_with_description",
                            "isDeprecated": False,
                            "name": "booleanFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "charFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "charFieldNotEditable",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "charFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "charFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "char_field_with_description",
                            "isDeprecated": False,
                            "name": "charFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "choiceFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "ENUM",
                                "name": "MenuModelAChoiceFieldRequiredChoices",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "choiceFieldNotEditable",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "ENUM",
                                "name": "MenuModelAChoiceFieldNotEditableChoices",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "choiceFieldNullable",
                            "type": {
                                "kind": "ENUM",
                                "name": "MenuModelAChoiceFieldNullableChoices",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "choiceFieldWithDefault",
                            "type": {
                                "kind": "ENUM",
                                "name": "MenuModelAChoiceFieldWithDefaultChoices",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "choice_field_with_description",
                            "isDeprecated": False,
                            "name": "choiceFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "ENUM",
                                "name": "MenuModelAChoiceFieldWithDescriptionChoices",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "dateFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "dateFieldNotEditable",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "dateFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "dateFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "date_field_with_description",
                            "isDeprecated": False,
                            "name": "dateFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "dateTimeFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "dateTimeFieldNotEditable",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "dateTimeFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "dateTimeFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "date_time_field_with_description",
                            "isDeprecated": False,
                            "name": "dateTimeFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "timeFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "timeFieldNotEditable",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "timeFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "timeFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "time_field_with_description",
                            "isDeprecated": False,
                            "name": "timeFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "decimalFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "decimalFieldNotEditable",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "decimalFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "decimalFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "decimal_field_with_description",
                            "isDeprecated": False,
                            "name": "decimalFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "durationFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "durationFieldNotEditable",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "durationFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "durationFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "duration_field_with_description",
                            "isDeprecated": False,
                            "name": "durationFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "emailFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "emailFieldNotEditable",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "emailFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "emailFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "email_field_with_description",
                            "isDeprecated": False,
                            "name": "emailFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "floatFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "floatFieldNotEditable",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "floatFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "floatFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "float_field_with_description",
                            "isDeprecated": False,
                            "name": "floatFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "integerFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "integerFieldNotEditable",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "integerFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "integerFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "integer_field_with_description",
                            "isDeprecated": False,
                            "name": "integerFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "smallIntegerFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "smallIntegerFieldNotEditable",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "smallIntegerFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "smallIntegerFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "small_integer_field_with_description",
                            "isDeprecated": False,
                            "name": "smallIntegerFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "positiveIntegerFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "positiveIntegerFieldNotEditable",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "positiveIntegerFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "positiveIntegerFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "positive_integer_field_with_description",
                            "isDeprecated": False,
                            "name": "positiveIntegerFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "slugFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "slugFieldNotEditable",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "slugFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "slugFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "slug_field_with_description",
                            "isDeprecated": False,
                            "name": "slugFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "textFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "textFieldNotEditable",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "textFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "textFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "text_field_with_description",
                            "isDeprecated": False,
                            "name": "textFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "urlFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "urlFieldNotEditable",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "urlFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "urlFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "url_field_with_description",
                            "isDeprecated": False,
                            "name": "urlFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "uuidFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "uuidFieldNotEditable",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "uuidFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "uuidFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "uuid_field_with_description",
                            "isDeprecated": False,
                            "name": "uuidFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "foreignKeyFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelAType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "foreignKeyFieldNullable",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelAType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "foreign_key_field_with_description",
                            "isDeprecated": False,
                            "name": "foreignKeyFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelAType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "foreignKeyFieldWithoutRelatedName",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelAType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "oneToOneFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelAType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "oneToOneFieldNullable",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelAType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "one_to_one_field_with_description",
                            "isDeprecated": False,
                            "name": "oneToOneFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelAType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "oneToOneFieldWithoutRelatedName",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelAType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "The object id",
                            "isDeprecated": False,
                            "name": "objectId",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAFilterInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "orderBy",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAOrderByInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "paginated",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "PaginatedInput",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "paginatedManyToManyFieldRequired",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelAPaginatedType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAFilterInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "orderBy",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAOrderByInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "paginated",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "PaginatedInput",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "paginatedManyToManyFieldNullable",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelAPaginatedType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAFilterInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "orderBy",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAOrderByInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "paginated",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "PaginatedInput",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": "many_to_many_field_with_description",
                            "isDeprecated": False,
                            "name": "paginatedManyToManyFieldWithDescription",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelAPaginatedType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAFilterInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "orderBy",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAOrderByInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "paginated",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "PaginatedInput",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "paginatedManyToManyFieldWithoutRelatedName",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelAPaginatedType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "genericForeignKeyField",
                            "type": {
                                "kind": "UNION",
                                "name": "ModelAGenericForeignKeyFieldUnionType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAFilterInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "orderBy",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAOrderByInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "paginated",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "PaginatedInput",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "paginatedGenericRelationField",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelAPaginatedType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAFilterInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "orderBy",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAOrderByInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "paginated",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "PaginatedInput",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "paginatedForeignKeyRelated",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelAPaginatedType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAFilterInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "orderBy",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAOrderByInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "paginated",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "PaginatedInput",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "paginatedForeignKeyNullableRelated",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelAPaginatedType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAFilterInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "orderBy",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAOrderByInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "paginated",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "PaginatedInput",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": "foreign_key_field_with_description",
                            "isDeprecated": False,
                            "name": "paginatedForeignKeyWithDescriptionRelated",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelAPaginatedType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "oneToOneRelated",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelAType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "oneToOneNullableRelated",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelAType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "oneToOneWithDescriptionRelated",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelAType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAFilterInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "orderBy",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAOrderByInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "paginated",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "PaginatedInput",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "paginatedManyToManyRelated",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelAPaginatedType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAFilterInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "orderBy",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAOrderByInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "paginated",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "PaginatedInput",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "paginatedManyToManyNullableRelated",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelAPaginatedType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAFilterInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "orderBy",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAOrderByInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "paginated",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "PaginatedInput",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": "many_to_many_field_with_description",
                            "isDeprecated": False,
                            "name": "paginatedManyToManyWithDescriptionRelated",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelAPaginatedType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "genericRelationRelated",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelAType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelBFilterInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "orderBy",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelBOrderByInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "paginated",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "PaginatedInput",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "paginatedForeignKeyBRelated",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelBPaginatedType",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "oneToOneBRelated",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelBType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelBFilterInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "orderBy",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelBOrderByInput",
                                    "ofType": None
                                }
                                },
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "paginated",
                                "type": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "PaginatedInput",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "paginatedManyToManyBRelated",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ModelBPaginatedType",
                                "ofType": None
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "ModelAType",
                        "possibleTypes": None
                        },
                        {
                        "description": "An enumeration.",
                        "enumValues": [
                            {
                            "deprecationReason": None,
                            "description": "A",
                            "isDeprecated": False,
                            "name": "A"
                            },
                            {
                            "deprecationReason": None,
                            "description": "B",
                            "isDeprecated": False,
                            "name": "B"
                            }
                        ],
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "ENUM",
                        "name": "MenuModelAChoiceFieldNotEditableChoices",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "total",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "page",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "pages",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "hasNext",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "hasPrev",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "indexStartObj",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "indexEndObj",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
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
                            }
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
                        "kind": "OBJECT",
                        "name": "ModelAPaginatedType",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "id",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "IDFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "booleanFieldRequired",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "BooleanFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "booleanFieldNotEditable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "BooleanFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "booleanFieldNullable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "BooleanFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "booleanFieldWithDefault",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "BooleanFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "booleanFieldWithDescription",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "BooleanFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "charFieldRequired",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "charFieldNotEditable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "charFieldNullable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "charFieldWithDefault",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "charFieldWithDescription",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "choiceFieldRequired",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "choiceFieldNotEditable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "choiceFieldNullable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "choiceFieldWithDefault",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "choiceFieldWithDescription",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateFieldRequired",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "DateFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateFieldNotEditable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "DateFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateFieldNullable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "DateFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateFieldWithDefault",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "DateFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateFieldWithDescription",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "DateFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateTimeFieldRequired",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "DateTimeFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateTimeFieldNotEditable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "DateTimeFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateTimeFieldNullable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "DateTimeFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateTimeFieldWithDefault",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "DateTimeFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateTimeFieldWithDescription",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "DateTimeFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "timeFieldRequired",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "TimeFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "timeFieldNotEditable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "TimeFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "timeFieldNullable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "TimeFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "timeFieldWithDefault",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "TimeFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "timeFieldWithDescription",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "TimeFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "decimalFieldRequired",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "DecimalFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "decimalFieldNotEditable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "DecimalFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "decimalFieldNullable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "DecimalFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "decimalFieldWithDefault",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "DecimalFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "decimalFieldWithDescription",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "DecimalFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "durationFieldRequired",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "DurationFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "durationFieldNotEditable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "DurationFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "durationFieldNullable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "DurationFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "durationFieldWithDefault",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "DurationFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "durationFieldWithDescription",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "DurationFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "emailFieldRequired",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "EmailFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "emailFieldNotEditable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "EmailFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "emailFieldNullable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "EmailFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "emailFieldWithDefault",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "EmailFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "emailFieldWithDescription",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "EmailFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "floatFieldRequired",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "FloatFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "floatFieldNotEditable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "FloatFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "floatFieldNullable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "FloatFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "floatFieldWithDefault",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "FloatFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "floatFieldWithDescription",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "FloatFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "integerFieldRequired",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "IntFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "integerFieldNotEditable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "IntFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "integerFieldNullable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "IntFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "integerFieldWithDefault",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "IntFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "integerFieldWithDescription",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "IntFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "smallIntegerFieldRequired",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "IntFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "smallIntegerFieldNotEditable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "IntFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "smallIntegerFieldNullable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "IntFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "smallIntegerFieldWithDefault",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "IntFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "smallIntegerFieldWithDescription",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "IntFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "positiveIntegerFieldRequired",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PositiveIntFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "positiveIntegerFieldNotEditable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PositiveIntFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "positiveIntegerFieldNullable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PositiveIntFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "positiveIntegerFieldWithDefault",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PositiveIntFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "positiveIntegerFieldWithDescription",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PositiveIntFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "slugFieldRequired",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "SlugFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "slugFieldNotEditable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "SlugFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "slugFieldNullable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "SlugFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "slugFieldWithDefault",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "SlugFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "slugFieldWithDescription",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "SlugFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "textFieldRequired",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "textFieldNotEditable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "textFieldNullable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "textFieldWithDefault",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "textFieldWithDescription",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "StringFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "urlFieldRequired",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "URLFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "urlFieldNotEditable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "URLFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "urlFieldNullable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "URLFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "urlFieldWithDefault",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "URLFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "urlFieldWithDescription",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "URLFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "uuidFieldRequired",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "UUIDFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "uuidFieldNotEditable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "UUIDFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "uuidFieldNullable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "UUIDFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "uuidFieldWithDefault",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "UUIDFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "uuidFieldWithDescription",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "UUIDFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyFieldRequired",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyFieldNullable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyFieldWithDescription",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyFieldWithoutRelatedName",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "objectId",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "PositiveIntFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "manyToManyFieldRequired",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "manyToManyFieldNullable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "manyToManyFieldWithDescription",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "manyToManyFieldWithoutRelatedName",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "genericRelationField",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyRelated",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyNullableRelated",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyWithDescriptionRelated",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "oneToOneRelated",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "oneToOneNullableRelated",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "oneToOneWithDescriptionRelated",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "manyToManyRelated",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "manyToManyNullableRelated",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "manyToManyWithDescriptionRelated",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyBRelated",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelBFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "oneToOneBRelated",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelBFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "manyToManyBRelated",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelBFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "AND",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "OR",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "NOT",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "ModelAFilterInput",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "exact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iexact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "in",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "contains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "icontains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "startswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "istartswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "endswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iendswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "range",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "isNone",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "regex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iregex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "BooleanFilter",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "exact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iexact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "in",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "contains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "icontains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "startswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "istartswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "endswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iendswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "range",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "isNone",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "regex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iregex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "year",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "month",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "day",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "weekDay",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "isoWeekDay",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "week",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "isoYear",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "quarter",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "containedBy",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "DateFilter",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "exact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iexact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "in",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "contains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "icontains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "startswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "istartswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "endswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iendswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "range",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "isNone",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "regex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iregex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "year",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "month",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "day",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "weekDay",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "isoWeekDay",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "week",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "isoYear",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "quarter",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "containedBy",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "hour",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "minute",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "second",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "date",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "time",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "DateTimeFilter",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "exact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iexact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "in",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "contains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "icontains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "startswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "istartswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "endswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iendswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "range",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "isNone",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "regex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iregex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "hour",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "minute",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "second",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "TimeFilter",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "exact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iexact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "in",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "contains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "icontains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "startswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "istartswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "endswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iendswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "range",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "isNone",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "regex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iregex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "containedBy",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "DecimalFilter",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "exact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iexact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "in",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "contains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "icontains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "startswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "istartswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "endswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iendswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "range",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "isNone",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "regex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iregex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "DurationFilter",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "exact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iexact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "in",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "contains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "icontains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "startswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "istartswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "endswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iendswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "range",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "isNone",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "regex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iregex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "EmailFilter",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "exact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iexact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "in",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "contains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "icontains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "startswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "istartswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "endswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iendswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "range",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "isNone",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "regex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iregex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "containedBy",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "FloatFilter",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "exact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iexact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "in",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "contains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "icontains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "startswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "istartswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "endswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iendswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "range",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "isNone",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "regex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iregex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "containedBy",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "IntFilter",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "exact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iexact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "in",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "contains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "icontains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "startswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "istartswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "endswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iendswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "range",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "isNone",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "regex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iregex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "containedBy",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "PositiveIntFilter",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "exact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iexact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "in",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "contains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "icontains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "startswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "istartswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "endswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iendswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "range",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "isNone",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "regex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iregex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "SlugFilter",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "exact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iexact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "in",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "contains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "icontains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "startswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "istartswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "endswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iendswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "range",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "isNone",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "regex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iregex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "URLFilter",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "exact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iexact",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "gte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lt",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "lte",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "in",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "contains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "icontains",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "startswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "istartswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "endswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iendswith",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "range",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "isNone",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "regex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "iregex",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "UUIDFilter",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "id",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "IDFilter",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyField",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "oneToOneField",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "manyToManyField",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAFilterInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "AND",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelBFilterInput",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "OR",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelBFilterInput",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "NOT",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelBFilterInput",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "ModelBFilterInput",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "id",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "booleanFieldRequired",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "booleanFieldNotEditable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "booleanFieldNullable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "booleanFieldWithDefault",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "booleanFieldWithDescription",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "charFieldRequired",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "charFieldNotEditable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "charFieldNullable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "charFieldWithDefault",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "charFieldWithDescription",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "choiceFieldRequired",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "choiceFieldNotEditable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "choiceFieldNullable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "choiceFieldWithDefault",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "choiceFieldWithDescription",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateFieldRequired",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateFieldNotEditable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateFieldNullable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateFieldWithDefault",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateFieldWithDescription",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateTimeFieldRequired",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateTimeFieldNotEditable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateTimeFieldNullable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateTimeFieldWithDefault",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateTimeFieldWithDescription",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "timeFieldRequired",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "timeFieldNotEditable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "timeFieldNullable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "timeFieldWithDefault",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "timeFieldWithDescription",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "decimalFieldRequired",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "decimalFieldNotEditable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "decimalFieldNullable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "decimalFieldWithDefault",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "decimalFieldWithDescription",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "durationFieldRequired",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "durationFieldNotEditable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "durationFieldNullable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "durationFieldWithDefault",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "durationFieldWithDescription",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "emailFieldRequired",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "emailFieldNotEditable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "emailFieldNullable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "emailFieldWithDefault",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "emailFieldWithDescription",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "floatFieldRequired",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "floatFieldNotEditable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "floatFieldNullable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "floatFieldWithDefault",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "floatFieldWithDescription",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "integerFieldRequired",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "integerFieldNotEditable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "integerFieldNullable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "integerFieldWithDefault",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "integerFieldWithDescription",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "smallIntegerFieldRequired",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "smallIntegerFieldNotEditable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "smallIntegerFieldNullable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "smallIntegerFieldWithDefault",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "smallIntegerFieldWithDescription",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "positiveIntegerFieldRequired",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "positiveIntegerFieldNotEditable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "positiveIntegerFieldNullable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "positiveIntegerFieldWithDefault",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "positiveIntegerFieldWithDescription",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "slugFieldRequired",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "slugFieldNotEditable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "slugFieldNullable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "slugFieldWithDefault",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "slugFieldWithDescription",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "textFieldRequired",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "textFieldNotEditable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "textFieldNullable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "textFieldWithDefault",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "textFieldWithDescription",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "urlFieldRequired",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "urlFieldNotEditable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "urlFieldNullable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "urlFieldWithDefault",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "urlFieldWithDescription",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderStringEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "uuidFieldRequired",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "uuidFieldNotEditable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "uuidFieldNullable",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "uuidFieldWithDefault",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "uuidFieldWithDescription",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyFieldRequired",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAOrderByInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyFieldNullable",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAOrderByInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyFieldWithDescription",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAOrderByInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyFieldWithoutRelatedName",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAOrderByInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "objectId",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "oneToOneRelated",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAOrderByInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "oneToOneNullableRelated",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAOrderByInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "oneToOneWithDescriptionRelated",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAOrderByInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "oneToOneBRelated",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelBOrderByInput",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "ModelAOrderByInput",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "id",
                            "type": {
                                "kind": "ENUM",
                                "name": "OrderEnum",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyField",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAOrderByInput",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "oneToOneField",
                            "type": {
                                "kind": "INPUT_OBJECT",
                                "name": "ModelAOrderByInput",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "ModelBOrderByInput",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "UNION",
                        "name": "ModelAGenericForeignKeyFieldUnionType",
                        "possibleTypes": [
                            {
                            "kind": "OBJECT",
                            "name": "MenuType",
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
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "id",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "The name of the menu",
                            "isDeprecated": False,
                            "name": "name",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "The status for enabling or disabling",
                            "isDeprecated": False,
                            "name": "isActive",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "MenuType",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "total",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "page",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "pages",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "hasNext",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "hasPrev",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "indexStartObj",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "indexEndObj",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
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
                            }
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
                        "kind": "OBJECT",
                        "name": "ModelBPaginatedType",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "input",
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
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "createModelFs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "CreateModelFsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "input",
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
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "updateModelFs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "UpdateModelFsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelFFilterInput",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "activateModelFs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ActivateModelFsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelFFilterInput",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "deactivateModelFs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "DeactivateModelFsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelFFilterInput",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "deleteModelFs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "DeleteModelFsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "input",
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
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "createModelEs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "CreateModelEsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "input",
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
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "updateModelEs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "UpdateModelEsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelEFilterInput",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "activateModelEs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ActivateModelEsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelEFilterInput",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "deactivateModelEs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "DeactivateModelEsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelEFilterInput",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "deleteModelEs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "DeleteModelEsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "input",
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
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "createModelDs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "CreateModelDsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "input",
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
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "updateModelDs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "UpdateModelDsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelDFilterInput",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "activateModelDs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ActivateModelDsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelDFilterInput",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "deactivateModelDs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "DeactivateModelDsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelDFilterInput",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "deleteModelDs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "DeleteModelDsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "input",
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
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "createModelCs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "CreateModelCsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "input",
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
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "updateModelCs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "UpdateModelCsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelCFilterInput",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "activateModelCs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ActivateModelCsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelCFilterInput",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "deactivateModelCs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "DeactivateModelCsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelCFilterInput",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "deleteModelCs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "DeleteModelCsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "input",
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
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "createModelBs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "CreateModelBsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "input",
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
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "updateModelBs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "UpdateModelBsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelBFilterInput",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "activateModelBs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ActivateModelBsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelBFilterInput",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "deactivateModelBs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "DeactivateModelBsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelBFilterInput",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "deleteModelBs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "DeleteModelBsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "input",
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
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "createModelAs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "CreateModelAsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "input",
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
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "updateModelAs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "UpdateModelAsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAFilterInput",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "activateModelAs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "ActivateModelAsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAFilterInput",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "deactivateModelAs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "DeactivateModelAsPayload",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "",
                                "name": "where",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "INPUT_OBJECT",
                                    "name": "ModelAFilterInput",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "deleteModelAs",
                            "type": {
                                "kind": "OBJECT",
                                "name": "DeleteModelAsPayload",
                                "ofType": None
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "Mutation",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelFType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "CreateModelFsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objectPosition",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "ErrorsType",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "field",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "messages",
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
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "ErrorType",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "text",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "CreateModelFInput",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelFType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "UpdateModelFsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "id",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "text",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "UpdateModelFInput",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelFType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "ActivateModelFsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelFType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "DeactivateModelFsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelFType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "success",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "DeleteModelFsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelEType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "CreateModelEsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "fkF",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "otoF",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "text",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "mtmF",
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
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "CreateModelEInput",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelEType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "UpdateModelEsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "id",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "fkF",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "otoF",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "text",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "mtmF",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "UpdateModelEInput",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelEType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "ActivateModelEsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelEType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "DeactivateModelEsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelEType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "success",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "DeleteModelEsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelDType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "CreateModelDsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "createUpdateOnly",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "createOnly",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "updateOnly",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "whereOnly",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "orderByOnly",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "allInput",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "allExclude",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "CreateModelDInput",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelDType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "UpdateModelDsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "id",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "createUpdateOnly",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "createOnly",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "updateOnly",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "whereOnly",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "orderByOnly",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "allInput",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "allExclude",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "UpdateModelDInput",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelDType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "ActivateModelDsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelDType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "DeactivateModelDsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelDType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "success",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "DeleteModelDsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelCType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "CreateModelCsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "createUpdateOnly",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "createOnly",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "updateOnly",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "whereOnly",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "orderByOnly",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "allInput",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "allExclude",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "CreateModelCInput",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelCType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "UpdateModelCsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "id",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "createUpdateOnly",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "createOnly",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "updateOnly",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "whereOnly",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "orderByOnly",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "allInput",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "allExclude",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "UpdateModelCInput",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelCType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "ActivateModelCsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelCType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "DeactivateModelCsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelCType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "success",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "DeleteModelCsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelBType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "CreateModelBsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyField",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "oneToOneField",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "manyToManyField",
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
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "CreateModelBInput",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelBType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "UpdateModelBsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "id",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyField",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "oneToOneField",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "manyToManyField",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "UpdateModelBInput",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelBType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "ActivateModelBsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelBType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "DeactivateModelBsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelBType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "success",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "DeleteModelBsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelAType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "CreateModelAsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "binaryFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Binary",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "binaryFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Binary",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": "\"YmluYXJ5X2ZpZWxkX3dpdGhfZGVmYXVsdA==\"",
                            "description": None,
                            "name": "binaryFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Binary",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "binary_field_with_description",
                            "name": "binaryFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Binary",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "booleanFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "booleanFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": "true",
                            "description": None,
                            "name": "booleanFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "boolean_field_with_description",
                            "name": "booleanFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "charFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "charFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": "\"char_field_with_default\"",
                            "description": None,
                            "name": "charFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "char_field_with_description",
                            "name": "charFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "choiceFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "ENUM",
                                "name": "MenuModelAChoiceFieldRequiredChoices",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "choiceFieldNullable",
                            "type": {
                                "kind": "ENUM",
                                "name": "MenuModelAChoiceFieldNullableChoices",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": "A",
                            "description": None,
                            "name": "choiceFieldWithDefault",
                            "type": {
                                "kind": "ENUM",
                                "name": "MenuModelAChoiceFieldWithDefaultChoices",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "choice_field_with_description",
                            "name": "choiceFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "ENUM",
                                "name": "MenuModelAChoiceFieldWithDescriptionChoices",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "date_field_with_description",
                            "name": "dateFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateTimeFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateTimeFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "date_time_field_with_description",
                            "name": "dateTimeFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "timeFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "timeFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "time_field_with_description",
                            "name": "timeFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "decimalFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "decimalFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": "\"0\"",
                            "description": None,
                            "name": "decimalFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "decimal_field_with_description",
                            "name": "decimalFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "durationFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "durationFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "durationFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "duration_field_with_description",
                            "name": "durationFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "emailFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "emailFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": "\"emailField@withDefault.com\"",
                            "description": None,
                            "name": "emailFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "email_field_with_description",
                            "name": "emailFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "floatFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "floatFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": "0",
                            "description": None,
                            "name": "floatFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "float_field_with_description",
                            "name": "floatFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "integerFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "integerFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": "0",
                            "description": None,
                            "name": "integerFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "integer_field_with_description",
                            "name": "integerFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "smallIntegerFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "smallIntegerFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": "0",
                            "description": None,
                            "name": "smallIntegerFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "small_integer_field_with_description",
                            "name": "smallIntegerFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "positiveIntegerFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "positiveIntegerFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": "0",
                            "description": None,
                            "name": "positiveIntegerFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "positive_integer_field_with_description",
                            "name": "positiveIntegerFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "slugFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "slugFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": "\"slug_field_with_default\"",
                            "description": None,
                            "name": "slugFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "slug_field_with_description",
                            "name": "slugFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "textFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "textFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": "\"text_field_with_default\"",
                            "description": None,
                            "name": "textFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "text_field_with_description",
                            "name": "textFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "urlFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "urlFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": "\"https://url_field_with_default.com\"",
                            "description": None,
                            "name": "urlFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "url_field_with_description",
                            "name": "urlFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "uuidFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "uuidFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "uuidFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "uuid_field_with_description",
                            "name": "uuidFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "foreign_key_field_with_description",
                            "name": "foreignKeyFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyFieldWithoutRelatedName",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "oneToOneFieldRequired",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "oneToOneFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "one_to_one_field_with_description",
                            "name": "oneToOneFieldWithDescription",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "oneToOneFieldWithoutRelatedName",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "The content type",
                            "name": "contentType",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "The object id",
                            "name": "objectId",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "manyToManyFieldRequired",
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
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "manyToManyFieldNullable",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "many_to_many_field_with_description",
                            "name": "manyToManyFieldWithDescription",
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
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "manyToManyFieldWithoutRelatedName",
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
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "CreateModelAInput",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelAType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "UpdateModelAsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": None,
                        "inputFields": [
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "id",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "binaryFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Binary",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "binaryFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Binary",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "binaryFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Binary",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "binary_field_with_description",
                            "name": "binaryFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Binary",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "booleanFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "booleanFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "booleanFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "boolean_field_with_description",
                            "name": "booleanFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "charFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "charFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "charFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "char_field_with_description",
                            "name": "charFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "choiceFieldRequired",
                            "type": {
                                "kind": "ENUM",
                                "name": "MenuModelAChoiceFieldRequiredChoices",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "choiceFieldNullable",
                            "type": {
                                "kind": "ENUM",
                                "name": "MenuModelAChoiceFieldNullableChoices",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "choiceFieldWithDefault",
                            "type": {
                                "kind": "ENUM",
                                "name": "MenuModelAChoiceFieldWithDefaultChoices",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "choice_field_with_description",
                            "name": "choiceFieldWithDescription",
                            "type": {
                                "kind": "ENUM",
                                "name": "MenuModelAChoiceFieldWithDescriptionChoices",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "date_field_with_description",
                            "name": "dateFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Date",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateTimeFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "dateTimeFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "date_time_field_with_description",
                            "name": "dateTimeFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "DateTime",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "timeFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "timeFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "time_field_with_description",
                            "name": "timeFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Time",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "decimalFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "decimalFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "decimalFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "decimal_field_with_description",
                            "name": "decimalFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Decimal",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "durationFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "durationFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "durationFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "duration_field_with_description",
                            "name": "durationFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Duration",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "emailFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "emailFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "emailFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "email_field_with_description",
                            "name": "emailFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Email",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "floatFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "floatFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "floatFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "float_field_with_description",
                            "name": "floatFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Float",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "integerFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "integerFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "integerFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "integer_field_with_description",
                            "name": "integerFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "smallIntegerFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "smallIntegerFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "smallIntegerFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "small_integer_field_with_description",
                            "name": "smallIntegerFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Int",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "positiveIntegerFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "positiveIntegerFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "positiveIntegerFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "positive_integer_field_with_description",
                            "name": "positiveIntegerFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "slugFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "slugFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "slugFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "slug_field_with_description",
                            "name": "slugFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Slug",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "textFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "textFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "textFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "text_field_with_description",
                            "name": "textFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "urlFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "urlFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "urlFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "url_field_with_description",
                            "name": "urlFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "URL",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "uuidFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "uuidFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "uuidFieldWithDefault",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "uuid_field_with_description",
                            "name": "uuidFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "UUID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "foreign_key_field_with_description",
                            "name": "foreignKeyFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "foreignKeyFieldWithoutRelatedName",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "oneToOneFieldRequired",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "oneToOneFieldNullable",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "one_to_one_field_with_description",
                            "name": "oneToOneFieldWithDescription",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "oneToOneFieldWithoutRelatedName",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "The content type",
                            "name": "contentType",
                            "type": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "The object id",
                            "name": "objectId",
                            "type": {
                                "kind": "SCALAR",
                                "name": "PositiveInt",
                                "ofType": None
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "manyToManyFieldRequired",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "manyToManyFieldNullable",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": "many_to_many_field_with_description",
                            "name": "manyToManyFieldWithDescription",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "defaultValue": None,
                            "description": None,
                            "name": "manyToManyFieldWithoutRelatedName",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "ID",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "interfaces": None,
                        "kind": "INPUT_OBJECT",
                        "name": "UpdateModelAInput",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelAType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "ActivateModelAsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelAType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "DeactivateModelAsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": None,
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "objects",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ModelAType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "errors",
                            "type": {
                                "kind": "LIST",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "ErrorsType",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "success",
                            "type": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "DeleteModelAsPayload",
                        "possibleTypes": None
                        },
                        {
                        "description": "A GraphQL Schema defines the capabilities of a GraphQL server. It exposes all available types and directives on the server, as well as the entry points for query, mutation, and subscription operations.",
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "description",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "A list of all types supported by this server.",
                            "isDeprecated": False,
                            "name": "types",
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
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "The type that query operations will be rooted at.",
                            "isDeprecated": False,
                            "name": "queryType",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "__Type",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "If this server supports mutation, the type that mutation operations will be rooted at.",
                            "isDeprecated": False,
                            "name": "mutationType",
                            "type": {
                                "kind": "OBJECT",
                                "name": "__Type",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "If this server support subscription, the type that subscription operations will be rooted at.",
                            "isDeprecated": False,
                            "name": "subscriptionType",
                            "type": {
                                "kind": "OBJECT",
                                "name": "__Type",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "A list of all directives supported by this server.",
                            "isDeprecated": False,
                            "name": "directives",
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
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "__Schema",
                        "possibleTypes": None
                        },
                        {
                        "description": "The fundamental unit of any GraphQL Schema is the type. There are many kinds of types in GraphQL as represented by the `__TypeKind` enum.\n\nDepending on the kind of a type, certain fields describe information about that type. Scalar types provide no information beyond a name, description and optional `specifiedByURL`, while Enum types provide their values. Object and Interface types provide the fields they describe. Abstract types, Union and Interface, provide the Object types possible at runtime. List and NonNull types compose other types.",
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "kind",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "ENUM",
                                "name": "__TypeKind",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "name",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "description",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "specifiedByURL",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": "False",
                                "description": None,
                                "name": "includeDeprecated",
                                "type": {
                                    "kind": "SCALAR",
                                    "name": "Boolean",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "fields",
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
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "interfaces",
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
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "possibleTypes",
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
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": "False",
                                "description": None,
                                "name": "includeDeprecated",
                                "type": {
                                    "kind": "SCALAR",
                                    "name": "Boolean",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "enumValues",
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
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": "False",
                                "description": None,
                                "name": "includeDeprecated",
                                "type": {
                                    "kind": "SCALAR",
                                    "name": "Boolean",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "inputFields",
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
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "ofType",
                            "type": {
                                "kind": "OBJECT",
                                "name": "__Type",
                                "ofType": None
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "__Type",
                        "possibleTypes": None
                        },
                        {
                        "description": "An enum describing what kind of type a given `__Type` is.",
                        "enumValues": [
                            {
                            "deprecationReason": None,
                            "description": "Indicates this type is a scalar.",
                            "isDeprecated": False,
                            "name": "SCALAR"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Indicates this type is an object. `fields` and `interfaces` are valid fields.",
                            "isDeprecated": False,
                            "name": "OBJECT"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Indicates this type is an interface. `fields`, `interfaces`, and `possibleTypes` are valid fields.",
                            "isDeprecated": False,
                            "name": "INTERFACE"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Indicates this type is a union. `possibleTypes` is a valid field.",
                            "isDeprecated": False,
                            "name": "UNION"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Indicates this type is an enum. `enumValues` is a valid field.",
                            "isDeprecated": False,
                            "name": "ENUM"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Indicates this type is an input object. `inputFields` is a valid field.",
                            "isDeprecated": False,
                            "name": "INPUT_OBJECT"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Indicates this type is a list. `ofType` is a valid field.",
                            "isDeprecated": False,
                            "name": "LIST"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Indicates this type is a non-None. `ofType` is a valid field.",
                            "isDeprecated": False,
                            "name": "NON_NULL"
                            }
                        ],
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "ENUM",
                        "name": "__TypeKind",
                        "possibleTypes": None
                        },
                        {
                        "description": "Object and Interface types are described by a list of Fields, each of which has a name, potentially a list of arguments, and a return type.",
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "name",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "description",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": "False",
                                "description": None,
                                "name": "includeDeprecated",
                                "type": {
                                    "kind": "SCALAR",
                                    "name": "Boolean",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "args",
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
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "type",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "__Type",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "isDeprecated",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "deprecationReason",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "__Field",
                        "possibleTypes": None
                        },
                        {
                        "description": "Arguments provided to Fields or Directives and the input fields of an InputObject are represented as Input Values which describe their type and optionally a default value.",
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "name",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "description",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "type",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "OBJECT",
                                "name": "__Type",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": "A GraphQL-formatted string representing the default value for this input value.",
                            "isDeprecated": False,
                            "name": "defaultValue",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "isDeprecated",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "deprecationReason",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "__InputValue",
                        "possibleTypes": None
                        },
                        {
                        "description": "One possible value for a given Enum. Enum values are unique values, not a placeholder for a string or numeric value. However an Enum value is returned in a JSON response as a string.",
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "name",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "description",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "isDeprecated",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "deprecationReason",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "__EnumValue",
                        "possibleTypes": None
                        },
                        {
                        "description": "A Directive provides a way to describe alternate runtime execution and type validation behavior in a GraphQL document.\n\nIn some cases, you need to provide options to alter GraphQL's execution behavior in ways field arguments will not suffice, such as conditionally including or skipping a field. Directives provide this by describing additional information to the executor.",
                        "enumValues": None,
                        "fields": [
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "name",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "description",
                            "type": {
                                "kind": "SCALAR",
                                "name": "String",
                                "ofType": None
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "isRepeatable",
                            "type": {
                                "kind": "NON_NULL",
                                "name": None,
                                "ofType": {
                                "kind": "SCALAR",
                                "name": "Boolean",
                                "ofType": None
                                }
                            }
                            },
                            {
                            "args": [],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "locations",
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
                            }
                            },
                            {
                            "args": [
                                {
                                "defaultValue": "False",
                                "description": None,
                                "name": "includeDeprecated",
                                "type": {
                                    "kind": "SCALAR",
                                    "name": "Boolean",
                                    "ofType": None
                                }
                                }
                            ],
                            "deprecationReason": None,
                            "description": None,
                            "isDeprecated": False,
                            "name": "args",
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
                            }
                            }
                        ],
                        "inputFields": None,
                        "interfaces": [],
                        "kind": "OBJECT",
                        "name": "__Directive",
                        "possibleTypes": None
                        },
                        {
                        "description": "A Directive can be adjacent to many parts of the GraphQL language, a __DirectiveLocation describes one such possible adjacencies.",
                        "enumValues": [
                            {
                            "deprecationReason": None,
                            "description": "Location adjacent to a query operation.",
                            "isDeprecated": False,
                            "name": "QUERY"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Location adjacent to a mutation operation.",
                            "isDeprecated": False,
                            "name": "MUTATION"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Location adjacent to a subscription operation.",
                            "isDeprecated": False,
                            "name": "SUBSCRIPTION"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Location adjacent to a field.",
                            "isDeprecated": False,
                            "name": "FIELD"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Location adjacent to a fragment definition.",
                            "isDeprecated": False,
                            "name": "FRAGMENT_DEFINITION"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Location adjacent to a fragment spread.",
                            "isDeprecated": False,
                            "name": "FRAGMENT_SPREAD"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Location adjacent to an inline fragment.",
                            "isDeprecated": False,
                            "name": "INLINE_FRAGMENT"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Location adjacent to a variable definition.",
                            "isDeprecated": False,
                            "name": "VARIABLE_DEFINITION"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Location adjacent to a schema definition.",
                            "isDeprecated": False,
                            "name": "SCHEMA"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Location adjacent to a scalar definition.",
                            "isDeprecated": False,
                            "name": "SCALAR"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Location adjacent to an object type definition.",
                            "isDeprecated": False,
                            "name": "OBJECT"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Location adjacent to a field definition.",
                            "isDeprecated": False,
                            "name": "FIELD_DEFINITION"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Location adjacent to an argument definition.",
                            "isDeprecated": False,
                            "name": "ARGUMENT_DEFINITION"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Location adjacent to an interface definition.",
                            "isDeprecated": False,
                            "name": "INTERFACE"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Location adjacent to a union definition.",
                            "isDeprecated": False,
                            "name": "UNION"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Location adjacent to an enum definition.",
                            "isDeprecated": False,
                            "name": "ENUM"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Location adjacent to an enum value definition.",
                            "isDeprecated": False,
                            "name": "ENUM_VALUE"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Location adjacent to an input object type definition.",
                            "isDeprecated": False,
                            "name": "INPUT_OBJECT"
                            },
                            {
                            "deprecationReason": None,
                            "description": "Location adjacent to an input object field definition.",
                            "isDeprecated": False,
                            "name": "INPUT_FIELD_DEFINITION"
                            }
                        ],
                        "fields": None,
                        "inputFields": None,
                        "interfaces": None,
                        "kind": "ENUM",
                        "name": "__DirectiveLocation",
                        "possibleTypes": None
                        }
                    ],
                    "directives": [
                        {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "Included when true.",
                                "name": "if",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "SCALAR",
                                    "name": "Boolean",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "description": "Directs the executor to include this field or fragment only when the `if` argument is true.",
                            "locations": [
                                "FIELD",
                                "FRAGMENT_SPREAD",
                                "INLINE_FRAGMENT"
                            ],
                            "name": "include"
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "Skipped when true.",
                                "name": "if",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "SCALAR",
                                    "name": "Boolean",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "description": "Directs the executor to skip this field or fragment when the `if` argument is true.",
                            "locations": [
                                "FIELD",
                                "FRAGMENT_SPREAD",
                                "INLINE_FRAGMENT"
                            ],
                            "name": "skip"
                            },
                            {
                            "args": [
                                {
                                "defaultValue": "\"No longer supported\"",
                                "description": "Explains why this element was deprecated, usually also including a suggestion for how to access supported similar data. Formatted using the Markdown syntax, as specified by [CommonMark](https://commonmark.org/).",
                                "name": "reason",
                                "type": {
                                    "kind": "SCALAR",
                                    "name": "String",
                                    "ofType": None
                                }
                                }
                            ],
                            "description": "Marks an element of a GraphQL schema as no longer supported.",
                            "locations": [
                                "FIELD_DEFINITION",
                                "ARGUMENT_DEFINITION",
                                "INPUT_FIELD_DEFINITION",
                                "ENUM_VALUE"
                            ],
                            "name": "deprecated"
                            },
                            {
                            "args": [
                                {
                                "defaultValue": None,
                                "description": "The URL that specifies the behaviour of this scalar.",
                                "name": "url",
                                "type": {
                                    "kind": "NON_NULL",
                                    "name": None,
                                    "ofType": {
                                    "kind": "SCALAR",
                                    "name": "String",
                                    "ofType": None
                                    }
                                }
                                }
                            ],
                            "description": "Exposes a URL that specifies the behaviour of this scalar.",
                            "locations": [
                                "SCALAR"
                            ],
                            "name": "specifiedBy"
                            }
                    ],
                }
            }
        }
        actual_schema = self.get_schema()

        print("==================")
        self.assertDictEqual(actual_schema, schema_for_test)