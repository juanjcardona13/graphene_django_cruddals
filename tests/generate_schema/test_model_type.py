# -*- coding: utf-8 -*-
from tests.utils import SchemaTestCase


class DjangoCRUDObjectTypeSchemaTest(SchemaTestCase):
    def test_model_type(self):

        fields_to_test = [
            {
                "name": "id",
                "type": {"kind": "SCALAR", "name": "ID", "ofType": None},
                "args": [],
            },
            {
                "name": "binaryField",
                "type": {"kind": "SCALAR", "name": "Binary", "ofType": None},
                "args": [],
            },
            {
                "name": "booleanField",
                "type": {"kind": "SCALAR", "name": "Boolean", "ofType": None},
                "args": [],
            },
            {
                "name": "booleanFieldNullable",
                "type": {"kind": "SCALAR", "name": "Boolean", "ofType": None},
                "args": [],
            },
            # {
            #     "name": "nullBooleanField",
            #     "type": {"kind": "SCALAR", "name": "Boolean", "ofType": None},
            #     "args": [],
            # },
            {
                "name": "charField",
                "type": {"kind": "SCALAR", "name": "String", "ofType": None},
                "args": [],
            },
            {
                "name": "charFieldUnique",
                "type": {"kind": "SCALAR", "name": "String", "ofType": None},
                "args": [],
            },
            {
                "name": "charFieldNullable",
                "type": {"kind": "SCALAR", "name": "String", "ofType": None},
                "args": [],
            },
            {
                "name": "dateField",
                "type": {"kind": "SCALAR", "name": "Date", "ofType": None},
                "args": [],
            },
            {
                "name": "datetimeField",
                "type": {"kind": "SCALAR", "name": "DateTime", "ofType": None},
                "args": [],
            },
            {
                "name": "timeField",
                "type": {"kind": "SCALAR", "name": "Time", "ofType": None},
                "args": [],
            },
            {
                "name": "decimalField",
                "type": {"kind": "SCALAR", "name": "Float", "ofType": None},
                "args": [],
            },
            {
                "name": "durationField",
                "type": {"kind": "SCALAR", "name": "Float", "ofType": None},
                "args": [],
            },
            {
                "name": "emailField",
                "type": {"kind": "SCALAR", "name": "String", "ofType": None},
                "args": [],
            },
            {
                "name": "floatField",
                "type": {"kind": "SCALAR", "name": "Float", "ofType": None},
                "args": [],
            },
            {
                "name": "integerField",
                "type": {"kind": "SCALAR", "name": "Int", "ofType": None},
                "args": [],
            },
            {
                "name": "integerFieldUnique",
                "type": {"kind": "SCALAR", "name": "Int", "ofType": None},
                "args": [],
            },
            {
                "name": "smallIntegerField",
                "type": {"kind": "SCALAR", "name": "Int", "ofType": None},
                "args": [],
            },
            {
                "name": "smallIntegerFieldUnique",
                "type": {"kind": "SCALAR", "name": "Int", "ofType": None},
                "args": [],
            },
            {
                "name": "positiveIntegerField",
                "type": {"kind": "SCALAR", "name": "Int", "ofType": None},
                "args": [],
            },
            {
                "name": "positiveIntegerFieldUnique",
                "type": {"kind": "SCALAR", "name": "Int", "ofType": None},
                "args": [],
            },
            {
                "name": "slugField",
                "type": {"kind": "SCALAR", "name": "String", "ofType": None},
                "args": [],
            },
            {
                "name": "slugFieldUnique",
                "type": {"kind": "SCALAR", "name": "String", "ofType": None},
                "args": [],
            },
            {
                "name": "textField",
                "type": {"kind": "SCALAR", "name": "String", "ofType": None},
                "args": [],
            },
            {
                "name": "textFieldNullable",
                "type": {"kind": "SCALAR", "name": "String", "ofType": None},
                "args": [],
            },
            {
                "name": "urlField",
                "type": {"kind": "SCALAR", "name": "String", "ofType": None},
                "args": [],
            },
            {
                "name": "urlFieldUnique",
                "type": {"kind": "SCALAR", "name": "String", "ofType": None},
                "args": [],
            },
            {
                "name": "uuidField",
                "type": {"kind": "SCALAR", "name": "UUID", "ofType": None},
                "args": [],
            },
            {
                "name": "uuidFieldUnique",
                "type": {"kind": "SCALAR", "name": "UUID", "ofType": None},
                "args": [],
            },
            # {
            #     "name": "foreignKeyField",
            #     "type": {
            #         "kind": "OBJECT",
            #         "name": "ModelTestGenerateSchemaAType",
            #         "ofType": None,
            #     },
            #     "args": [],
            # },
            # {
            #     "name": "manytomanyField",
            #     "type": {
            #         "kind": "OBJECT",
            #         "name": "ModelTestGenerateSchemaATypeConnection",
            #         "ofType": None,
            #     },
            #     "args": [
            #         {
            #             "name": "where",
            #             "type": {
            #                 "kind": "INPUT_OBJECT",
            #                 "name": "ModelTestGenerateSchemaAWhereInput",
            #                 "ofType": None,
            #             },
            #         },
            #         {
            #             "name": "orderBy",
            #             "type": {
            #                 "kind": "LIST",
            #                 "name": None,
            #                 "ofType": {
            #                     "kind": "INPUT_OBJECT",
            #                     "name": "ModelTestGenerateSchemaAOrderByInput",
            #                 },
            #             },
            #         },
            #         {
            #             "name": "limit",
            #             "type": {"kind": "SCALAR", "name": "Int", "ofType": None},
            #         },
            #         {
            #             "name": "offset",
            #             "type": {"kind": "SCALAR", "name": "Int", "ofType": None},
            #         },
            #     ],
            # },
            # {
            #     "name": "foreignKeyRelated",
            #     "type": {
            #         "kind": "OBJECT",
            #         "name": "ModelTestGenerateSchemaATypeConnection",
            #         "ofType": None,
            #     },
            #     "args": [
            #         {
            #             "name": "where",
            #             "type": {
            #                 "kind": "INPUT_OBJECT",
            #                 "name": "ModelTestGenerateSchemaAWhereInput",
            #                 "ofType": None,
            #             },
            #         },
            #         {
            #             "name": "orderBy",
            #             "type": {
            #                 "kind": "LIST",
            #                 "name": None,
            #                 "ofType": {
            #                     "kind": "INPUT_OBJECT",
            #                     "name": "ModelTestGenerateSchemaAOrderByInput",
            #                 },
            #             },
            #         },
            #         {
            #             "name": "limit",
            #             "type": {"kind": "SCALAR", "name": "Int", "ofType": None},
            #         },
            #         {
            #             "name": "offset",
            #             "type": {"kind": "SCALAR", "name": "Int", "ofType": None},
            #         },
            #     ],
            # },
            # {
            #     "name": "oneToOneRelated",
            #     "type": {
            #         "kind": "OBJECT",
            #         "name": "ModelTestGenerateSchemaAType",
            #         "ofType": None,
            #     },
            #     "args": [],
            # },
            # {
            #     "name": "manyToManyRelated",
            #     "type": {
            #         "kind": "OBJECT",
            #         "name": "ModelTestGenerateSchemaATypeConnection",
            #         "ofType": None,
            #     },
            #     "args": [
            #         {
            #             "name": "where",
            #             "type": {
            #                 "kind": "INPUT_OBJECT",
            #                 "name": "ModelTestGenerateSchemaAWhereInput",
            #                 "ofType": None,
            #             },
            #         },
            #         {
            #             "name": "orderBy",
            #             "type": {
            #                 "kind": "LIST",
            #                 "name": None,
            #                 "ofType": {
            #                     "kind": "INPUT_OBJECT",
            #                     "name": "ModelTestGenerateSchemaAOrderByInput",
            #                 },
            #             },
            #         },
            #         {
            #             "name": "limit",
            #             "type": {"kind": "SCALAR", "name": "Int", "ofType": None},
            #         },
            #         {
            #             "name": "offset",
            #             "type": {"kind": "SCALAR", "name": "Int", "ofType": None},
            #         },
            #     ],
            # },
            # {
            #     "name": "foreignKeyBRelated",
            #     "type": {
            #         "kind": "OBJECT",
            #         "name": "ModelTestGenerateSchemaBTypeConnection",
            #         "ofType": None,
            #     },
            #     "args": [
            #         {
            #             "name": "where",
            #             "type": {
            #                 "kind": "INPUT_OBJECT",
            #                 "name": "ModelTestGenerateSchemaBWhereInput",
            #                 "ofType": None,
            #             },
            #         },
            #         {
            #             "name": "orderBy",
            #             "type": {
            #                 "kind": "LIST",
            #                 "name": None,
            #                 "ofType": {
            #                     "kind": "INPUT_OBJECT",
            #                     "name": "ModelTestGenerateSchemaBOrderByInput",
            #                 },
            #             },
            #         },
            #         {
            #             "name": "limit",
            #             "type": {"kind": "SCALAR", "name": "Int", "ofType": None},
            #         },
            #         {
            #             "name": "offset",
            #             "type": {"kind": "SCALAR", "name": "Int", "ofType": None},
            #         },
            #     ],
            # },
            # {
            #     "name": "oneToOneBRelated",
            #     "type": {
            #         "kind": "OBJECT",
            #         "name": "ModelTestGenerateSchemaBType",
            #         "ofType": None,
            #     },
            #     "args": [],
            # },
            # {
            #     "name": "manyToManyBRelated",
            #     "type": {
            #         "kind": "OBJECT",
            #         "name": "ModelTestGenerateSchemaBTypeConnection",
            #         "ofType": None,
            #     },
            #     "args": [
            #         {
            #             "name": "where",
            #             "type": {
            #                 "kind": "INPUT_OBJECT",
            #                 "name": "ModelTestGenerateSchemaBWhereInput",
            #                 "ofType": None,
            #             },
            #         },
            #         {
            #             "name": "orderBy",
            #             "type": {
            #                 "kind": "LIST",
            #                 "name": None,
            #                 "ofType": {
            #                     "kind": "INPUT_OBJECT",
            #                     "name": "ModelTestGenerateSchemaBOrderByInput",
            #                 },
            #             },
            #         },
            #         {
            #             "name": "limit",
            #             "type": {"kind": "SCALAR", "name": "Int", "ofType": None},
            #         },
            #         {
            #             "name": "offset",
            #             "type": {"kind": "SCALAR", "name": "Int", "ofType": None},
            #         },
            #     ],
            # },
        ]
        self.runtest_fields_of_type("ModelTestGenerateSchemaAType", fields_to_test)

