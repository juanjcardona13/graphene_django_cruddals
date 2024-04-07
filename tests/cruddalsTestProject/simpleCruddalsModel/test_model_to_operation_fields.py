# -*- coding: utf-8 -*-

from utils.main import SchemaTestCase


class CruddalsModelSchemaTest(SchemaTestCase):
    
    def test_create_operation_field(self):
        create_field = {
          "name": "createModelCs",
          "description": None,
          "type": {
            "kind": "OBJECT",
            "name": "CreateModelCsPayload",
            "ofType": None
          },
          "args": [
            {
              "name": "input",
              "description": "",
              "defaultValue": None,
              "type": {
                "kind": "LIST",
                "name": None,
                "ofType": {
                  "kind": "NON_NULL",
                  "name": None,
                  "ofType": {
                    "kind": "INPUT_OBJECT",
                    "name": "CreateModelCInput"
                  }
                }
              }
            }
          ]
        }
        self.run_test_graphql_field("createModelCs", "Mutation", create_field)

    def test_read_operation_field(self):
        read_field = {
          "name": "readModelC",
          "description": None,
          "type": {
            "kind": "OBJECT",
            "name": "ModelCType",
            "ofType": None
          },
          "args": [
            {
              "name": "where",
              "description": "",
              "defaultValue": None,
              "type": {
                "kind": "NON_NULL",
                "name": None,
                "ofType": {
                  "kind": "INPUT_OBJECT",
                  "name": "FilterModelCInput",
                  "ofType": None
                }
              }
            }
          ]
        }
        self.run_test_graphql_field("readModelC", "Query", read_field)

    def test_update_operation_field(self):
        update_field = {
          "name": "updateModelCs",
          "description": None,
          "type": {
            "kind": "OBJECT",
            "name": "UpdateModelCsPayload",
            "ofType": None
          },
          "args": [
            {
              "name": "input",
              "description": "",
              "defaultValue": None,
              "type": {
                "kind": "LIST",
                "name": None,
                "ofType": {
                  "kind": "NON_NULL",
                  "name": None,
                  "ofType": {
                    "kind": "INPUT_OBJECT",
                    "name": "UpdateModelCInput"
                  }
                }
              }
            }
          ]
        }
        self.run_test_graphql_field("updateModelCs", "Mutation", update_field)
    
    def test_delete_operation_field(self):
        delete_field = {
          "name": "deleteModelCs",
          "description": None,
          "type": {
            "kind": "OBJECT",
            "name": "DeleteModelCsPayload",
            "ofType": None
          },
          "args": [
            {
              "name": "where",
              "description": "",
              "defaultValue": None,
              "type": {
                "kind": "NON_NULL",
                "name": None,
                "ofType": {
                  "kind": "INPUT_OBJECT",
                  "name": "FilterModelCInput",
                  "ofType": None
                }
              }
            }
          ]
        }
        self.run_test_graphql_field("deleteModelCs", "Mutation", delete_field)
    
    def test_deactivate_operation_field(self):
        deactivate_field = {
          "name": "deactivateModelCs",
          "description": None,
          "type": {
            "kind": "OBJECT",
            "name": "DeactivateModelCsPayload",
            "ofType": None
          },
          "args": [
            {
              "name": "where",
              "description": "",
              "defaultValue": None,
              "type": {
                "kind": "NON_NULL",
                "name": None,
                "ofType": {
                  "kind": "INPUT_OBJECT",
                  "name": "FilterModelCInput",
                  "ofType": None
                }
              }
            }
          ]
        }
        self.run_test_graphql_field("deactivateModelCs", "Mutation", deactivate_field)

    def test_activate_operation_field(self):
        activate_field = {
          "name": "activateModelCs",
          "description": None,
          "type": {
            "kind": "OBJECT",
            "name": "ActivateModelCsPayload",
            "ofType": None
          },
          "args": [
            {
              "name": "where",
              "description": "",
              "defaultValue": None,
              "type": {
                "kind": "NON_NULL",
                "name": None,
                "ofType": {
                  "kind": "INPUT_OBJECT",
                  "name": "FilterModelCInput",
                  "ofType": None
                }
              }
            }
          ]
        }
        self.run_test_graphql_field("activateModelCs", "Mutation", activate_field)
    
    def test_list_operation_field(self):
        list_field = {
          "name": "listModelCs",
          "description": None,
          "type": {
            "kind": "LIST",
            "name": None,
            "ofType": {
              "kind": "NON_NULL",
              "name": None,
              "ofType": {
                "kind": "OBJECT",
                "name": "ModelCType"
              }
            }
          },
          "args": []
        }
        self.run_test_graphql_field("listModelCs", "Query", list_field)
    
    def test_search_operation_fiel(self):
        search_field = {
          "name": "searchModelCs",
          "description": None,
          "type": {
            "kind": "OBJECT",
            "name": "ModelCPaginatedType",
            "ofType": None
          },
          "args": [
            {
              "name": "where",
              "description": "",
              "defaultValue": None,
              "type": {
                "kind": "INPUT_OBJECT",
                "name": "FilterModelCInput",
                "ofType": None
              }
            },
            {
              "name": "orderBy",
              "description": "",
              "defaultValue": None,
              "type": {
                "kind": "INPUT_OBJECT",
                "name": "OrderByModelCInput",
                "ofType": None
              }
            },
            {
              "name": "paginated",
              "description": "",
              "defaultValue": None,
              "type": {
                "kind": "INPUT_OBJECT",
                "name": "PaginationConfigInput",
                "ofType": None
              }
            }
          ]
        }
        self.run_test_graphql_field("searchModelCs", "Query", search_field)






