# -*- coding: utf-8 -*-
from utils.main import SchemaTestCase

class CruddalsModelSchemaTest(SchemaTestCase):
    def test_model_type(self):
        fields_to_test = [
            {
                "name": "id",
                "description": None,
                "type": { "kind": "SCALAR", "name": "ID", "ofType": None },
                "args": []
            },
            {
                "name": "binaryFieldRequired",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Binary", "ofType": None } },
                "args": []
            },
            {
                "name": "binaryFieldNotEditable",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Binary", "ofType": None } },
                "args": []
            },
            {
                "name": "binaryFieldNullable",
                "description": None,
                "type": { "kind": "SCALAR", "name": "Binary", "ofType": None },
                "args": []
            },
            {
                "name": "binaryFieldWithDefault",
                "description": None,
                "type": { "kind": "SCALAR", "name": "Binary", "ofType": None },
                "args": []
            },
            {
                "name": "binaryFieldWithDescription",
                "description": "binary_field_with_description",
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Binary", "ofType": None } },
                "args": []
            },
            {
                "name": "booleanFieldRequired",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Boolean", "ofType": None } },
                "args": []
            },
            {
                "name": "booleanFieldNotEditable",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Boolean", "ofType": None } },
                "args": []
            },
            {
                "name": "booleanFieldNullable",
                "description": None,
                "type": { "kind": "SCALAR", "name": "Boolean", "ofType": None },
                "args": []
            },
            {
                "name": "booleanFieldWithDefault",
                "description": None,
                "type": { "kind": "SCALAR", "name": "Boolean", "ofType": None },
                "args": []
            },
            {
                "name": "booleanFieldWithDescription",
                "description": "boolean_field_with_description",
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Boolean", "ofType": None } },
                "args": []
            },
            {
                "name": "charFieldRequired",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "String", "ofType": None } },
                "args": []
            },
            {
                "name": "charFieldNotEditable",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "String", "ofType": None } },
                "args": []
            },
            {
                "name": "charFieldNullable",
                "description": None,
                "type": { "kind": "SCALAR", "name": "String", "ofType": None },
                "args": []
            },
            {
                "name": "charFieldWithDefault",
                "description": None,
                "type": { "kind": "SCALAR", "name": "String", "ofType": None },
                "args": []
            },
            {
                "name": "charFieldWithDescription",
                "description": "char_field_with_description",
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "String", "ofType": None } },
                "args": []
            },
            {
                "name": "choiceFieldRequired",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "ENUM", "name": "SimplecruddalsmodelModelAChoiceFieldRequiredChoices", "ofType": None } },
                "args": []
            },
            {
                "name": "choiceFieldNotEditable",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "ENUM", "name": "SimplecruddalsmodelModelAChoiceFieldNotEditableChoices", "ofType": None } },
                "args": []
            },
            {
                "name": "choiceFieldNullable",
                "description": None,
                "type": { "kind": "ENUM", "name": "SimplecruddalsmodelModelAChoiceFieldNullableChoices", "ofType": None },
                "args": []
            },
            {
                "name": "choiceFieldWithDefault",
                "description": None,
                "type": { "kind": "ENUM", "name": "SimplecruddalsmodelModelAChoiceFieldWithDefaultChoices", "ofType": None },
                "args": []
            },
            {
                "name": "choiceFieldWithDescription",
                "description": "choice_field_with_description",
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "ENUM", "name": "SimplecruddalsmodelModelAChoiceFieldWithDescriptionChoices", "ofType": None } },
                "args": []
            },
            {
                "name": "dateFieldRequired",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Date", "ofType": None } },
                "args": []
            },
            {
                "name": "dateFieldNotEditable",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Date", "ofType": None } },
                "args": []
            },
            {
                "name": "dateFieldNullable",
                "description": None,
                "type": { "kind": "SCALAR", "name": "Date", "ofType": None },
                "args": []
            },
            {
                "name": "dateFieldWithDefault",
                "description": None,
                "type": { "kind": "SCALAR", "name": "Date", "ofType": None },
                "args": []
            },
            {
                "name": "dateFieldWithDescription",
                "description": "date_field_with_description",
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Date", "ofType": None } },
                "args": []
            },
            {
                "name": "dateTimeFieldRequired",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "DateTime", "ofType": None } },
                "args": []
            },
            {
                "name": "dateTimeFieldNotEditable",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "DateTime", "ofType": None } },
                "args": []
            },
            {
                "name": "dateTimeFieldNullable",
                "description": None,
                "type": { "kind": "SCALAR", "name": "DateTime", "ofType": None },
                "args": []
            },
            {
                "name": "dateTimeFieldWithDefault",
                "description": None,
                "type": { "kind": "SCALAR", "name": "DateTime", "ofType": None },
                "args": []
            },
            {
                "name": "dateTimeFieldWithDescription",
                "description": "date_time_field_with_description",
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "DateTime", "ofType": None } },
                "args": []
            },
            {
                "name": "timeFieldRequired",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Time", "ofType": None } },
                "args": []
            },
            {
                "name": "timeFieldNotEditable",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Time", "ofType": None } },
                "args": []
            },
            {
                "name": "timeFieldNullable",
                "description": None,
                "type": { "kind": "SCALAR", "name": "Time", "ofType": None },
                "args": []
            },
            {
                "name": "timeFieldWithDefault",
                "description": None,
                "type": { "kind": "SCALAR", "name": "Time", "ofType": None },
                "args": []
            },
            {
                "name": "timeFieldWithDescription",
                "description": "time_field_with_description",
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Time", "ofType": None } },
                "args": []
            },
            {
                "name": "decimalFieldRequired",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Decimal", "ofType": None } },
                "args": []
            },
            {
                "name": "decimalFieldNotEditable",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Decimal", "ofType": None } },
                "args": []
            },
            {
                "name": "decimalFieldNullable",
                "description": None,
                "type": { "kind": "SCALAR", "name": "Decimal", "ofType": None },
                "args": []
            },
            {
                "name": "decimalFieldWithDefault",
                "description": None,
                "type": { "kind": "SCALAR", "name": "Decimal", "ofType": None },
                "args": []
            },
            {
                "name": "decimalFieldWithDescription",
                "description": "decimal_field_with_description",
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Decimal", "ofType": None } },
                "args": []
            },
            {
                "name": "durationFieldRequired",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Duration", "ofType": None } },
                "args": []
            },
            {
                "name": "durationFieldNotEditable",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Duration", "ofType": None } },
                "args": []
            },
            {
                "name": "durationFieldNullable",
                "description": None,
                "type": { "kind": "SCALAR", "name": "Duration", "ofType": None },
                "args": []
            },
            {
                "name": "durationFieldWithDefault",
                "description": None,
                "type": { "kind": "SCALAR", "name": "Duration", "ofType": None },
                "args": []
            },
            {
                "name": "durationFieldWithDescription",
                "description": "duration_field_with_description",
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Duration", "ofType": None } },
                "args": []
            },
            {
                "name": "emailFieldRequired",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Email", "ofType": None } },
                "args": []
            },
            {
                "name": "emailFieldNotEditable",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Email", "ofType": None } },
                "args": []
            },
            {
                "name": "emailFieldNullable",
                "description": None,
                "type": { "kind": "SCALAR", "name": "Email", "ofType": None },
                "args": []
            },
            {
                "name": "emailFieldWithDefault",
                "description": None,
                "type": { "kind": "SCALAR", "name": "Email", "ofType": None },
                "args": []
            },
            {
                "name": "emailFieldWithDescription",
                "description": "email_field_with_description",
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Email", "ofType": None } },
                "args": []
            },
            {
                "name": "floatFieldRequired",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Float", "ofType": None } },
                "args": []
            },
            {
                "name": "floatFieldNotEditable",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Float", "ofType": None } },
                "args": []
            },
            {
                "name": "floatFieldNullable",
                "description": None,
                "type": { "kind": "SCALAR", "name": "Float", "ofType": None },
                "args": []
            },
            {
                "name": "floatFieldWithDefault",
                "description": None,
                "type": { "kind": "SCALAR", "name": "Float", "ofType": None },
                "args": []
            },
            {
                "name": "floatFieldWithDescription",
                "description": "float_field_with_description",
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Float", "ofType": None } },
                "args": []
            },
            {
                "name": "integerFieldRequired",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Int", "ofType": None } },
                "args": []
            },
            {
                "name": "integerFieldNotEditable",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Int", "ofType": None } },
                "args": []
            },
            {
                "name": "integerFieldNullable",
                "description": None,
                "type": { "kind": "SCALAR", "name": "Int", "ofType": None },
                "args": []
            },
            {
                "name": "integerFieldWithDefault",
                "description": None,
                "type": { "kind": "SCALAR", "name": "Int", "ofType": None },
                "args": []
            },
            {
                "name": "integerFieldWithDescription",
                "description": "integer_field_with_description",
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Int", "ofType": None } },
                "args": []
            },
            {
                "name": "smallIntegerFieldRequired",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Int", "ofType": None } },
                "args": []
            },
            {
                "name": "smallIntegerFieldNotEditable",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Int", "ofType": None } },
                "args": []
            },
            {
                "name": "smallIntegerFieldNullable",
                "description": None,
                "type": { "kind": "SCALAR", "name": "Int", "ofType": None },
                "args": []
            },
            {
                "name": "smallIntegerFieldWithDefault",
                "description": None,
                "type": { "kind": "SCALAR", "name": "Int", "ofType": None },
                "args": []
            },
            {
                "name": "smallIntegerFieldWithDescription",
                "description": "small_integer_field_with_description",
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Int", "ofType": None } },
                "args": []
            },
            {
                "name": "positiveIntegerFieldRequired",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "PositiveInt", "ofType": None } },
                "args": []
            },
            {
                "name": "positiveIntegerFieldNotEditable",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "PositiveInt", "ofType": None } },
                "args": []
            },
            {
                "name": "positiveIntegerFieldNullable",
                "description": None,
                "type": { "kind": "SCALAR", "name": "PositiveInt", "ofType": None },
                "args": []
            },
            {
                "name": "positiveIntegerFieldWithDefault",
                "description": None,
                "type": { "kind": "SCALAR", "name": "PositiveInt", "ofType": None },
                "args": []
            },
            {
                "name": "positiveIntegerFieldWithDescription",
                "description": "positive_integer_field_with_description",
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "PositiveInt", "ofType": None } },
                "args": []
            },
            {
                "name": "slugFieldRequired",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Slug", "ofType": None } },
                "args": []
            },
            {
                "name": "slugFieldNotEditable",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Slug", "ofType": None } },
                "args": []
            },
            {
                "name": "slugFieldNullable",
                "description": None,
                "type": { "kind": "SCALAR", "name": "Slug", "ofType": None },
                "args": []
            },
            {
                "name": "slugFieldWithDefault",
                "description": None,
                "type": { "kind": "SCALAR", "name": "Slug", "ofType": None },
                "args": []
            },
            {
                "name": "slugFieldWithDescription",
                "description": "slug_field_with_description",
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Slug", "ofType": None } },
                "args": []
            },
            {
                "name": "textFieldRequired",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "String", "ofType": None } },
                "args": []
            },
            {
                "name": "textFieldNotEditable",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "String", "ofType": None } },
                "args": []
            },
            {
                "name": "textFieldNullable",
                "description": None,
                "type": { "kind": "SCALAR", "name": "String", "ofType": None },
                "args": []
            },
            {
                "name": "textFieldWithDefault",
                "description": None,
                "type": { "kind": "SCALAR", "name": "String", "ofType": None },
                "args": []
            },
            {
                "name": "textFieldWithDescription",
                "description": "text_field_with_description",
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "String", "ofType": None } },
                "args": []
            },
            {
                "name": "urlFieldRequired",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "URL", "ofType": None } },
                "args": []
            },
            {
                "name": "urlFieldNotEditable",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "URL", "ofType": None } },
                "args": []
            },
            {
                "name": "urlFieldNullable",
                "description": None,
                "type": { "kind": "SCALAR", "name": "URL", "ofType": None },
                "args": []
            },
            {
                "name": "urlFieldWithDefault",
                "description": None,
                "type": { "kind": "SCALAR", "name": "URL", "ofType": None },
                "args": []
            },
            {
                "name": "urlFieldWithDescription",
                "description": "url_field_with_description",
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "URL", "ofType": None } },
                "args": []
            },
            {
                "name": "uuidFieldRequired",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "UUID", "ofType": None } },
                "args": []
            },
            {
                "name": "uuidFieldNotEditable",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "UUID", "ofType": None } },
                "args": []
            },
            {
                "name": "uuidFieldNullable",
                "description": None,
                "type": { "kind": "SCALAR", "name": "UUID", "ofType": None },
                "args": []
            },
            {
                "name": "uuidFieldWithDefault",
                "description": None,
                "type": { "kind": "SCALAR", "name": "UUID", "ofType": None },
                "args": []
            },
            {
                "name": "uuidFieldWithDescription",
                "description": "uuid_field_with_description",
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "UUID", "ofType": None } },
                "args": []
            },
            {
                "name": "foreignKeyFieldRequired",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "OBJECT", "name": "ModelAType", "ofType": None } },
                "args": []
            },
            {
                "name": "foreignKeyFieldNullable",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ModelAType", "ofType": None },
                "args": []
            },
            {
                "name": "foreignKeyFieldWithDescription",
                "description": "foreign_key_field_with_description",
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "OBJECT", "name": "ModelAType", "ofType": None } },
                "args": []
            },
            {
                "name": "foreignKeyFieldWithoutRelatedName",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "OBJECT", "name": "ModelAType", "ofType": None } },
                "args": []
            },
            {
                "name": "oneToOneFieldRequired",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "OBJECT", "name": "ModelAType", "ofType": None } },
                "args": []
            },
            {
                "name": "oneToOneFieldNullable",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ModelAType", "ofType": None },
                "args": []
            },
            {
                "name": "oneToOneFieldWithDescription",
                "description": "one_to_one_field_with_description",
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "OBJECT", "name": "ModelAType", "ofType": None } },
                "args": []
            },
            {
                "name": "oneToOneFieldWithoutRelatedName",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "OBJECT", "name": "ModelAType", "ofType": None } },
                "args": []
            },
            {
                "name": "objectId",
                "description": "The object id",
                "type": { "kind": "SCALAR", "name": "PositiveInt", "ofType": None },
                "args": []
            },
            {
                "name": "paginatedManyToManyFieldRequired",
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
                    "type": { "kind": "INPUT_OBJECT", "name": "PaginationConfigInput", "ofType": None }
                }
                ]
            },
            {
                "name": "paginatedManyToManyFieldNullable",
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
                    "type": { "kind": "INPUT_OBJECT", "name": "PaginationConfigInput", "ofType": None }
                }
                ]
            },
            {
                "name": "paginatedManyToManyFieldWithDescription",
                "description": "many_to_many_field_with_description",
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
                    "type": { "kind": "INPUT_OBJECT", "name": "PaginationConfigInput", "ofType": None }
                }
                ]
            },
            {
                "name": "paginatedManyToManyFieldWithoutRelatedName",
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
                    "type": { "kind": "INPUT_OBJECT", "name": "PaginationConfigInput", "ofType": None }
                }
                ]
            },
            {
                "name": "genericForeignKeyField",
                "description": None,
                "type": { "kind": "UNION", "name": "ModelAGenericForeignKeyFieldUnionType", "ofType": None },
                "args": []
            },
            {
                "name": "paginatedGenericRelationField",
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
                    "type": { "kind": "INPUT_OBJECT", "name": "PaginationConfigInput", "ofType": None }
                }
                ]
            },
            {
                "name": "paginatedForeignKeyRelated",
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
                    "type": { "kind": "INPUT_OBJECT", "name": "PaginationConfigInput", "ofType": None }
                }
                ]
            },
            {
                "name": "paginatedForeignKeyNullableRelated",
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
                    "type": { "kind": "INPUT_OBJECT", "name": "PaginationConfigInput", "ofType": None }
                }
                ]
            },
            {
                "name": "paginatedForeignKeyWithDescriptionRelated",
                "description": "foreign_key_field_with_description",
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
                    "type": { "kind": "INPUT_OBJECT", "name": "PaginationConfigInput", "ofType": None }
                }
                ]
            },
            {
                "name": "oneToOneRelated",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ModelAType", "ofType": None },
                "args": []
            },
            {
                "name": "oneToOneNullableRelated",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ModelAType", "ofType": None },
                "args": []
            },
            {
                "name": "oneToOneWithDescriptionRelated",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ModelAType", "ofType": None },
                "args": []
            },
            {
                "name": "paginatedManyToManyRelated",
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
                    "type": { "kind": "INPUT_OBJECT", "name": "PaginationConfigInput", "ofType": None }
                }
                ]
            },
            {
                "name": "paginatedManyToManyNullableRelated",
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
                    "type": { "kind": "INPUT_OBJECT", "name": "PaginationConfigInput", "ofType": None }
                }
                ]
            },
            {
                "name": "paginatedManyToManyWithDescriptionRelated",
                "description": "many_to_many_field_with_description",
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
                    "type": { "kind": "INPUT_OBJECT", "name": "PaginationConfigInput", "ofType": None }
                }
                ]
            },
            {
                "name": "genericRelationRelated",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ModelAType", "ofType": None },
                "args": []
            },
            {
                "name": "paginatedForeignKeyBRelated",
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
                    "type": { "kind": "INPUT_OBJECT", "name": "PaginationConfigInput", "ofType": None }
                }
                ]
            },
            {
                "name": "oneToOneBRelated",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ModelBType", "ofType": None },
                "args": []
            },
            {
                "name": "paginatedManyToManyBRelated",
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
                    "type": { "kind": "INPUT_OBJECT", "name": "PaginationConfigInput", "ofType": None }
                }
                ]
            }
        ]
        self.run_test_graphql_type("ModelAType", fields_to_test)

    def test_model_create_input_type(self):
        fields_to_test = [
            {
                "name": "binaryFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Binary", "ofType": None } }
            },
            {
                "name": "binaryFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Binary", "ofType": None }
            },
            {
                "name": "binaryFieldWithDefault",
                "description": None,
                "defaultValue": "\"CA==\"",
                "type": { "kind": "SCALAR", "name": "Binary", "ofType": None }
            },
            {
                "name": "binaryFieldWithDescription",
                "description": "binary_field_with_description",
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Binary", "ofType": None } }
            },
            {
                "name": "booleanFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Boolean", "ofType": None } }
            },
            {
                "name": "booleanFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Boolean", "ofType": None }
            },
            {
                "name": "booleanFieldWithDefault",
                "description": None,
                "defaultValue": "true",
                "type": { "kind": "SCALAR", "name": "Boolean", "ofType": None }
            },
            {
                "name": "booleanFieldWithDescription",
                "description": "boolean_field_with_description",
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Boolean", "ofType": None } }
            },
            {
                "name": "charFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "String", "ofType": None } }
            },
            {
                "name": "charFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "String", "ofType": None }
            },
            {
                "name": "charFieldWithDefault",
                "description": None,
                "defaultValue": "\"char_field_with_default\"",
                "type": { "kind": "SCALAR", "name": "String", "ofType": None }
            },
            {
                "name": "charFieldWithDescription",
                "description": "char_field_with_description",
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "String", "ofType": None } }
            },
            {
                "name": "choiceFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "ENUM", "name": "SimplecruddalsmodelModelAChoiceFieldRequiredChoices", "ofType": None } }
            },
            {
                "name": "choiceFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "SimplecruddalsmodelModelAChoiceFieldNullableChoices", "ofType": None }
            },
            {
                "name": "choiceFieldWithDefault",
                "description": None,
                "defaultValue": "A",
                "type": { "kind": "ENUM", "name": "SimplecruddalsmodelModelAChoiceFieldWithDefaultChoices", "ofType": None }
            },
            {
                "name": "choiceFieldWithDescription",
                "description": "choice_field_with_description",
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "ENUM", "name": "SimplecruddalsmodelModelAChoiceFieldWithDescriptionChoices", "ofType": None } }
            },
            {
                "name": "dateFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Date", "ofType": None } }
            },
            {
                "name": "dateFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Date", "ofType": None }
            },
            {
                "name": "dateFieldWithDescription",
                "description": "date_field_with_description",
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Date", "ofType": None } }
            },
            {
                "name": "dateTimeFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "DateTime", "ofType": None } }
            },
            {
                "name": "dateTimeFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "DateTime", "ofType": None }
            },
            {
                "name": "dateTimeFieldWithDescription",
                "description": "date_time_field_with_description",
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "DateTime", "ofType": None } }
            },
            {
                "name": "timeFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Time", "ofType": None } }
            },
            {
                "name": "timeFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Time", "ofType": None }
            },
            {
                "name": "timeFieldWithDescription",
                "description": "time_field_with_description",
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Time", "ofType": None } }
            },
            {
                "name": "decimalFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Decimal", "ofType": None } }
            },
            {
                "name": "decimalFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Decimal", "ofType": None }
            },
            {
                "name": "decimalFieldWithDefault",
                "description": None,
                "defaultValue": "\"0\"",
                "type": { "kind": "SCALAR", "name": "Decimal", "ofType": None }
            },
            {
                "name": "decimalFieldWithDescription",
                "description": "decimal_field_with_description",
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Decimal", "ofType": None } }
            },
            {
                "name": "durationFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Duration", "ofType": None } }
            },
            {
                "name": "durationFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Duration", "ofType": None }
            },
            {
                "name": "durationFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Duration", "ofType": None }
            },
            {
                "name": "durationFieldWithDescription",
                "description": "duration_field_with_description",
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Duration", "ofType": None } }
            },
            {
                "name": "emailFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Email", "ofType": None } }
            },
            {
                "name": "emailFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Email", "ofType": None }
            },
            {
                "name": "emailFieldWithDefault",
                "description": None,
                "defaultValue": "\"emailField@withDefault.com\"",
                "type": { "kind": "SCALAR", "name": "Email", "ofType": None }
            },
            {
                "name": "emailFieldWithDescription",
                "description": "email_field_with_description",
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Email", "ofType": None } }
            },
            {
                "name": "floatFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Float", "ofType": None } }
            },
            {
                "name": "floatFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Float", "ofType": None }
            },
            {
                "name": "floatFieldWithDefault",
                "description": None,
                "defaultValue": "0",
                "type": { "kind": "SCALAR", "name": "Float", "ofType": None }
            },
            {
                "name": "floatFieldWithDescription",
                "description": "float_field_with_description",
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Float", "ofType": None } }
            },
            {
                "name": "integerFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Int", "ofType": None } }
            },
            {
                "name": "integerFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Int", "ofType": None }
            },
            {
                "name": "integerFieldWithDefault",
                "description": None,
                "defaultValue": "0",
                "type": { "kind": "SCALAR", "name": "Int", "ofType": None }
            },
            {
                "name": "integerFieldWithDescription",
                "description": "integer_field_with_description",
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Int", "ofType": None } }
            },
            {
                "name": "smallIntegerFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Int", "ofType": None } }
            },
            {
                "name": "smallIntegerFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Int", "ofType": None }
            },
            {
                "name": "smallIntegerFieldWithDefault",
                "description": None,
                "defaultValue": "0",
                "type": { "kind": "SCALAR", "name": "Int", "ofType": None }
            },
            {
                "name": "smallIntegerFieldWithDescription",
                "description": "small_integer_field_with_description",
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Int", "ofType": None } }
            },
            {
                "name": "positiveIntegerFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "PositiveInt", "ofType": None } }
            },
            {
                "name": "positiveIntegerFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "PositiveInt", "ofType": None }
            },
            {
                "name": "positiveIntegerFieldWithDefault",
                "description": None,
                "defaultValue": "0",
                "type": { "kind": "SCALAR", "name": "PositiveInt", "ofType": None }
            },
            {
                "name": "positiveIntegerFieldWithDescription",
                "description": "positive_integer_field_with_description",
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "PositiveInt", "ofType": None } }
            },
            {
                "name": "slugFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Slug", "ofType": None } }
            },
            {
                "name": "slugFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Slug", "ofType": None }
            },
            {
                "name": "slugFieldWithDefault",
                "description": None,
                "defaultValue": "\"slug_field_with_default\"",
                "type": { "kind": "SCALAR", "name": "Slug", "ofType": None }
            },
            {
                "name": "slugFieldWithDescription",
                "description": "slug_field_with_description",
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "Slug", "ofType": None } }
            },
            {
                "name": "textFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "String", "ofType": None } }
            },
            {
                "name": "textFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "String", "ofType": None }
            },
            {
                "name": "textFieldWithDefault",
                "description": None,
                "defaultValue": "\"text_field_with_default\"",
                "type": { "kind": "SCALAR", "name": "String", "ofType": None }
            },
            {
                "name": "textFieldWithDescription",
                "description": "text_field_with_description",
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "String", "ofType": None } }
            },
            {
                "name": "urlFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "URL", "ofType": None } }
            },
            {
                "name": "urlFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "URL", "ofType": None }
            },
            {
                "name": "urlFieldWithDefault",
                "description": None,
                "defaultValue": "\"https://url_field_with_default.com\"",
                "type": { "kind": "SCALAR", "name": "URL", "ofType": None }
            },
            {
                "name": "urlFieldWithDescription",
                "description": "url_field_with_description",
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "URL", "ofType": None } }
            },
            {
                "name": "uuidFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "UUID", "ofType": None } }
            },
            {
                "name": "uuidFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "UUID", "ofType": None }
            },
            {
                "name": "uuidFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "UUID", "ofType": None }
            },
            {
                "name": "uuidFieldWithDescription",
                "description": "uuid_field_with_description",
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "UUID", "ofType": None } }
            },
            {
                "name": "foreignKeyFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "ID", "ofType": None } }
            },
            {
                "name": "foreignKeyFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "ID", "ofType": None }
            },
            {
                "name": "foreignKeyFieldWithDescription",
                "description": "foreign_key_field_with_description",
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "ID", "ofType": None } }
            },
            {
                "name": "foreignKeyFieldWithoutRelatedName",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "ID", "ofType": None } }
            },
            {
                "name": "oneToOneFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "ID", "ofType": None } }
            },
            {
                "name": "oneToOneFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "ID", "ofType": None }
            },
            {
                "name": "oneToOneFieldWithDescription",
                "description": "one_to_one_field_with_description",
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "ID", "ofType": None } }
            },
            {
                "name": "oneToOneFieldWithoutRelatedName",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "ID", "ofType": None } }
            },
            {
                "name": "contentType",
                "description": "The content type",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "ID", "ofType": None }
            },
            {
                "name": "objectId",
                "description": "The object id",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "PositiveInt", "ofType": None }
            },
            {
                "name": "manyToManyFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "LIST", "name": None, "ofType": { "kind": "SCALAR", "name": "ID" } } }
            },
            {
                "name": "manyToManyFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "LIST", "name": None, "ofType": { "kind": "SCALAR", "name": "ID", "ofType": None } }
            },
            {
                "name": "manyToManyFieldWithDescription",
                "description": "many_to_many_field_with_description",
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "LIST", "name": None, "ofType": { "kind": "SCALAR", "name": "ID" } } }
            },
            {
                "name": "manyToManyFieldWithoutRelatedName",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "LIST", "name": None, "ofType": { "kind": "SCALAR", "name": "ID" } } }
            }
        ]

        self.run_test_graphql_type("CreateModelAInput", fields_to_test, input_type=True)

    def test_model_update_input_type(self):
        fields_to_test = [
            {
                "name": "id",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "SCALAR", "name": "ID", "ofType": None } }
            },
            {
                "name": "binaryFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Binary", "ofType": None }
            },
            {
                "name": "binaryFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Binary", "ofType": None }
            },
            {
                "name": "binaryFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Binary", "ofType": None }
            },
            {
                "name": "binaryFieldWithDescription",
                "description": "binary_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Binary", "ofType": None }
            },
            {
                "name": "booleanFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Boolean", "ofType": None }
            },
            {
                "name": "booleanFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Boolean", "ofType": None }
            },
            {
                "name": "booleanFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Boolean", "ofType": None }
            },
            {
                "name": "booleanFieldWithDescription",
                "description": "boolean_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Boolean", "ofType": None }
            },
            {
                "name": "charFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "String", "ofType": None }
            },
            {
                "name": "charFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "String", "ofType": None }
            },
            {
                "name": "charFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "String", "ofType": None }
            },
            {
                "name": "charFieldWithDescription",
                "description": "char_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "String", "ofType": None }
            },
            {
                "name": "choiceFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "SimplecruddalsmodelModelAChoiceFieldRequiredChoices", "ofType": None }
            },
            {
                "name": "choiceFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "SimplecruddalsmodelModelAChoiceFieldNullableChoices", "ofType": None }
            },
            {
                "name": "choiceFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "SimplecruddalsmodelModelAChoiceFieldWithDefaultChoices", "ofType": None }
            },
            {
                "name": "choiceFieldWithDescription",
                "description": "choice_field_with_description",
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "SimplecruddalsmodelModelAChoiceFieldWithDescriptionChoices", "ofType": None }
            },
            {
                "name": "dateFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Date", "ofType": None }
            },
            {
                "name": "dateFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Date", "ofType": None }
            },
            {
                "name": "dateFieldWithDescription",
                "description": "date_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Date", "ofType": None }
            },
            {
                "name": "dateTimeFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "DateTime", "ofType": None }
            },
            {
                "name": "dateTimeFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "DateTime", "ofType": None }
            },
            {
                "name": "dateTimeFieldWithDescription",
                "description": "date_time_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "DateTime", "ofType": None }
            },
            {
                "name": "timeFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Time", "ofType": None }
            },
            {
                "name": "timeFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Time", "ofType": None }
            },
            {
                "name": "timeFieldWithDescription",
                "description": "time_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Time", "ofType": None }
            },
            {
                "name": "decimalFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Decimal", "ofType": None }
            },
            {
                "name": "decimalFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Decimal", "ofType": None }
            },
            {
                "name": "decimalFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Decimal", "ofType": None }
            },
            {
                "name": "decimalFieldWithDescription",
                "description": "decimal_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Decimal", "ofType": None }
            },
            {
                "name": "durationFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Duration", "ofType": None }
            },
            {
                "name": "durationFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Duration", "ofType": None }
            },
            {
                "name": "durationFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Duration", "ofType": None }
            },
            {
                "name": "durationFieldWithDescription",
                "description": "duration_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Duration", "ofType": None }
            },
            {
                "name": "emailFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Email", "ofType": None }
            },
            {
                "name": "emailFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Email", "ofType": None }
            },
            {
                "name": "emailFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Email", "ofType": None }
            },
            {
                "name": "emailFieldWithDescription",
                "description": "email_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Email", "ofType": None }
            },
            {
                "name": "floatFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Float", "ofType": None }
            },
            {
                "name": "floatFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Float", "ofType": None }
            },
            {
                "name": "floatFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Float", "ofType": None }
            },
            {
                "name": "floatFieldWithDescription",
                "description": "float_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Float", "ofType": None }
            },
            {
                "name": "integerFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Int", "ofType": None }
            },
            {
                "name": "integerFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Int", "ofType": None }
            },
            {
                "name": "integerFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Int", "ofType": None }
            },
            {
                "name": "integerFieldWithDescription",
                "description": "integer_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Int", "ofType": None }
            },
            {
                "name": "smallIntegerFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Int", "ofType": None }
            },
            {
                "name": "smallIntegerFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Int", "ofType": None }
            },
            {
                "name": "smallIntegerFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Int", "ofType": None }
            },
            {
                "name": "smallIntegerFieldWithDescription",
                "description": "small_integer_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Int", "ofType": None }
            },
            {
                "name": "positiveIntegerFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "PositiveInt", "ofType": None }
            },
            {
                "name": "positiveIntegerFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "PositiveInt", "ofType": None }
            },
            {
                "name": "positiveIntegerFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "PositiveInt", "ofType": None }
            },
            {
                "name": "positiveIntegerFieldWithDescription",
                "description": "positive_integer_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "PositiveInt", "ofType": None }
            },
            {
                "name": "slugFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Slug", "ofType": None }
            },
            {
                "name": "slugFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Slug", "ofType": None }
            },
            {
                "name": "slugFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Slug", "ofType": None }
            },
            {
                "name": "slugFieldWithDescription",
                "description": "slug_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Slug", "ofType": None }
            },
            {
                "name": "textFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "String", "ofType": None }
            },
            {
                "name": "textFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "String", "ofType": None }
            },
            {
                "name": "textFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "String", "ofType": None }
            },
            {
                "name": "textFieldWithDescription",
                "description": "text_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "String", "ofType": None }
            },
            {
                "name": "urlFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "URL", "ofType": None }
            },
            {
                "name": "urlFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "URL", "ofType": None }
            },
            {
                "name": "urlFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "URL", "ofType": None }
            },
            {
                "name": "urlFieldWithDescription",
                "description": "url_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "URL", "ofType": None }
            },
            {
                "name": "uuidFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "UUID", "ofType": None }
            },
            {
                "name": "uuidFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "UUID", "ofType": None }
            },
            {
                "name": "uuidFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "UUID", "ofType": None }
            },
            {
                "name": "uuidFieldWithDescription",
                "description": "uuid_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "UUID", "ofType": None }
            },
            {
                "name": "foreignKeyFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "ID", "ofType": None }
            },
            {
                "name": "foreignKeyFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "ID", "ofType": None }
            },
            {
                "name": "foreignKeyFieldWithDescription",
                "description": "foreign_key_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "ID", "ofType": None }
            },
            {
                "name": "foreignKeyFieldWithoutRelatedName",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "ID", "ofType": None }
            },
            {
                "name": "oneToOneFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "ID", "ofType": None }
            },
            {
                "name": "oneToOneFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "ID", "ofType": None }
            },
            {
                "name": "oneToOneFieldWithDescription",
                "description": "one_to_one_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "ID", "ofType": None }
            },
            {
                "name": "oneToOneFieldWithoutRelatedName",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "ID", "ofType": None }
            },
            {
                "name": "contentType",
                "description": "The content type",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "ID", "ofType": None }
            },
            {
                "name": "objectId",
                "description": "The object id",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "PositiveInt", "ofType": None }
            },
            {
                "name": "manyToManyFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "LIST", "name": None, "ofType": { "kind": "SCALAR", "name": "ID", "ofType": None } }
            },
            {
                "name": "manyToManyFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "LIST", "name": None, "ofType": { "kind": "SCALAR", "name": "ID", "ofType": None } }
            },
            {
                "name": "manyToManyFieldWithDescription",
                "description": "many_to_many_field_with_description",
                "defaultValue": None,
                "type": { "kind": "LIST", "name": None, "ofType": { "kind": "SCALAR", "name": "ID", "ofType": None } }
            },
            {
                "name": "manyToManyFieldWithoutRelatedName",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "LIST", "name": None, "ofType": { "kind": "SCALAR", "name": "ID", "ofType": None } }
            }
        ]

        self.run_test_graphql_type("UpdateModelAInput", fields_to_test, input_type=True)

    def test_model_create_update_input_type(self):
        fields_to_test = [
            {
                "name": "id",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "ID", "ofType": None }
            },
            {
                "name": "binaryFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Binary", "ofType": None }
            },
            {
                "name": "binaryFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Binary", "ofType": None }
            },
            {
                "name": "binaryFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Binary", "ofType": None }
            },
            {
                "name": "binaryFieldWithDescription",
                "description": "binary_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Binary", "ofType": None }
            },
            {
                "name": "booleanFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Boolean", "ofType": None }
            },
            {
                "name": "booleanFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Boolean", "ofType": None }
            },
            {
                "name": "booleanFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Boolean", "ofType": None }
            },
            {
                "name": "booleanFieldWithDescription",
                "description": "boolean_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Boolean", "ofType": None }
            },
            {
                "name": "charFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "String", "ofType": None }
            },
            {
                "name": "charFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "String", "ofType": None }
            },
            {
                "name": "charFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "String", "ofType": None }
            },
            {
                "name": "charFieldWithDescription",
                "description": "char_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "String", "ofType": None }
            },
            {
                "name": "choiceFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "SimplecruddalsmodelModelAChoiceFieldRequiredChoices", "ofType": None }
            },
            {
                "name": "choiceFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "SimplecruddalsmodelModelAChoiceFieldNullableChoices", "ofType": None }
            },
            {
                "name": "choiceFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "SimplecruddalsmodelModelAChoiceFieldWithDefaultChoices", "ofType": None }
            },
            {
                "name": "choiceFieldWithDescription",
                "description": "choice_field_with_description",
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "SimplecruddalsmodelModelAChoiceFieldWithDescriptionChoices", "ofType": None }
            },
            {
                "name": "dateFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Date", "ofType": None }
            },
            {
                "name": "dateFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Date", "ofType": None }
            },
            {
                "name": "dateFieldWithDescription",
                "description": "date_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Date", "ofType": None }
            },
            {
                "name": "dateTimeFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "DateTime", "ofType": None }
            },
            {
                "name": "dateTimeFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "DateTime", "ofType": None }
            },
            {
                "name": "dateTimeFieldWithDescription",
                "description": "date_time_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "DateTime", "ofType": None }
            },
            {
                "name": "timeFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Time", "ofType": None }
            },
            {
                "name": "timeFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Time", "ofType": None }
            },
            {
                "name": "timeFieldWithDescription",
                "description": "time_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Time", "ofType": None }
            },
            {
                "name": "decimalFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Decimal", "ofType": None }
            },
            {
                "name": "decimalFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Decimal", "ofType": None }
            },
            {
                "name": "decimalFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Decimal", "ofType": None }
            },
            {
                "name": "decimalFieldWithDescription",
                "description": "decimal_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Decimal", "ofType": None }
            },
            {
                "name": "durationFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Duration", "ofType": None }
            },
            {
                "name": "durationFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Duration", "ofType": None }
            },
            {
                "name": "durationFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Duration", "ofType": None }
            },
            {
                "name": "durationFieldWithDescription",
                "description": "duration_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Duration", "ofType": None }
            },
            {
                "name": "emailFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Email", "ofType": None }
            },
            {
                "name": "emailFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Email", "ofType": None }
            },
            {
                "name": "emailFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Email", "ofType": None }
            },
            {
                "name": "emailFieldWithDescription",
                "description": "email_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Email", "ofType": None }
            },
            {
                "name": "floatFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Float", "ofType": None }
            },
            {
                "name": "floatFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Float", "ofType": None }
            },
            {
                "name": "floatFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Float", "ofType": None }
            },
            {
                "name": "floatFieldWithDescription",
                "description": "float_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Float", "ofType": None }
            },
            {
                "name": "integerFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Int", "ofType": None }
            },
            {
                "name": "integerFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Int", "ofType": None }
            },
            {
                "name": "integerFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Int", "ofType": None }
            },
            {
                "name": "integerFieldWithDescription",
                "description": "integer_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Int", "ofType": None }
            },
            {
                "name": "smallIntegerFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Int", "ofType": None }
            },
            {
                "name": "smallIntegerFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Int", "ofType": None }
            },
            {
                "name": "smallIntegerFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Int", "ofType": None }
            },
            {
                "name": "smallIntegerFieldWithDescription",
                "description": "small_integer_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Int", "ofType": None }
            },
            {
                "name": "positiveIntegerFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "PositiveInt", "ofType": None }
            },
            {
                "name": "positiveIntegerFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "PositiveInt", "ofType": None }
            },
            {
                "name": "positiveIntegerFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "PositiveInt", "ofType": None }
            },
            {
                "name": "positiveIntegerFieldWithDescription",
                "description": "positive_integer_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "PositiveInt", "ofType": None }
            },
            {
                "name": "slugFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Slug", "ofType": None }
            },
            {
                "name": "slugFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Slug", "ofType": None }
            },
            {
                "name": "slugFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Slug", "ofType": None }
            },
            {
                "name": "slugFieldWithDescription",
                "description": "slug_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "Slug", "ofType": None }
            },
            {
                "name": "textFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "String", "ofType": None }
            },
            {
                "name": "textFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "String", "ofType": None }
            },
            {
                "name": "textFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "String", "ofType": None }
            },
            {
                "name": "textFieldWithDescription",
                "description": "text_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "String", "ofType": None }
            },
            {
                "name": "urlFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "URL", "ofType": None }
            },
            {
                "name": "urlFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "URL", "ofType": None }
            },
            {
                "name": "urlFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "URL", "ofType": None }
            },
            {
                "name": "urlFieldWithDescription",
                "description": "url_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "URL", "ofType": None }
            },
            {
                "name": "uuidFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "UUID", "ofType": None }
            },
            {
                "name": "uuidFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "UUID", "ofType": None }
            },
            {
                "name": "uuidFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "UUID", "ofType": None }
            },
            {
                "name": "uuidFieldWithDescription",
                "description": "uuid_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "UUID", "ofType": None }
            },
            {
                "name": "foreignKeyFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "ID", "ofType": None }
            },
            {
                "name": "foreignKeyFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "ID", "ofType": None }
            },
            {
                "name": "foreignKeyFieldWithDescription",
                "description": "foreign_key_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "ID", "ofType": None }
            },
            {
                "name": "foreignKeyFieldWithoutRelatedName",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "ID", "ofType": None }
            },
            {
                "name": "oneToOneFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "ID", "ofType": None }
            },
            {
                "name": "oneToOneFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "ID", "ofType": None }
            },
            {
                "name": "oneToOneFieldWithDescription",
                "description": "one_to_one_field_with_description",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "ID", "ofType": None }
            },
            {
                "name": "oneToOneFieldWithoutRelatedName",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "ID", "ofType": None }
            },
            {
                "name": "contentType",
                "description": "The content type",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "ID", "ofType": None }
            },
            {
                "name": "objectId",
                "description": "The object id",
                "defaultValue": None,
                "type": { "kind": "SCALAR", "name": "PositiveInt", "ofType": None }
            },
            {
                "name": "manyToManyFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "LIST", "name": None, "ofType": { "kind": "SCALAR", "name": "ID", "ofType": None } }
            },
            {
                "name": "manyToManyFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "LIST", "name": None, "ofType": { "kind": "SCALAR", "name": "ID", "ofType": None } }
            },
            {
                "name": "manyToManyFieldWithDescription",
                "description": "many_to_many_field_with_description",
                "defaultValue": None,
                "type": { "kind": "LIST", "name": None, "ofType": { "kind": "SCALAR", "name": "ID", "ofType": None } }
            },
            {
                "name": "manyToManyFieldWithoutRelatedName",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "LIST", "name": None, "ofType": { "kind": "SCALAR", "name": "ID", "ofType": None } }
            }
        ]


        self.run_test_graphql_type("ModelAInput", fields_to_test, input_type=True)

    def test_model_where_input_type(self):
        fields_to_test = [
            {
                "name": "id",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "IDFilter", "ofType": None }
            },
            {
                "name": "booleanFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "BooleanFilter", "ofType": None }
            },
            {
                "name": "booleanFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "BooleanFilter", "ofType": None }
            },
            {
                "name": "booleanFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "BooleanFilter", "ofType": None }
            },
            {
                "name": "booleanFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "BooleanFilter", "ofType": None }
            },
            {
                "name": "booleanFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "BooleanFilter", "ofType": None }
            },
            {
                "name": "charFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "StringFilter", "ofType": None }
            },
            {
                "name": "charFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "StringFilter", "ofType": None }
            },
            {
                "name": "charFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "StringFilter", "ofType": None }
            },
            {
                "name": "charFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "StringFilter", "ofType": None }
            },
            {
                "name": "charFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "StringFilter", "ofType": None }
            },
            {
                "name": "choiceFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "StringFilter", "ofType": None }
            },
            {
                "name": "choiceFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "StringFilter", "ofType": None }
            },
            {
                "name": "choiceFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "StringFilter", "ofType": None }
            },
            {
                "name": "choiceFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "StringFilter", "ofType": None }
            },
            {
                "name": "choiceFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "StringFilter", "ofType": None }
            },
            {
                "name": "dateFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "DateFilter", "ofType": None }
            },
            {
                "name": "dateFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "DateFilter", "ofType": None }
            },
            {
                "name": "dateFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "DateFilter", "ofType": None }
            },
            {
                "name": "dateFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "DateFilter", "ofType": None }
            },
            {
                "name": "dateFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "DateFilter", "ofType": None }
            },
            {
                "name": "dateTimeFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "DateTimeFilter", "ofType": None }
            },
            {
                "name": "dateTimeFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "DateTimeFilter", "ofType": None }
            },
            {
                "name": "dateTimeFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "DateTimeFilter", "ofType": None }
            },
            {
                "name": "dateTimeFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "DateTimeFilter", "ofType": None }
            },
            {
                "name": "dateTimeFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "DateTimeFilter", "ofType": None }
            },
            {
                "name": "timeFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "TimeFilter", "ofType": None }
            },
            {
                "name": "timeFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "TimeFilter", "ofType": None }
            },
            {
                "name": "timeFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "TimeFilter", "ofType": None }
            },
            {
                "name": "timeFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "TimeFilter", "ofType": None }
            },
            {
                "name": "timeFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "TimeFilter", "ofType": None }
            },
            {
                "name": "decimalFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "DecimalFilter", "ofType": None }
            },
            {
                "name": "decimalFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "DecimalFilter", "ofType": None }
            },
            {
                "name": "decimalFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "DecimalFilter", "ofType": None }
            },
            {
                "name": "decimalFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "DecimalFilter", "ofType": None }
            },
            {
                "name": "decimalFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "DecimalFilter", "ofType": None }
            },
            {
                "name": "durationFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "DurationFilter", "ofType": None }
            },
            {
                "name": "durationFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "DurationFilter", "ofType": None }
            },
            {
                "name": "durationFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "DurationFilter", "ofType": None }
            },
            {
                "name": "durationFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "DurationFilter", "ofType": None }
            },
            {
                "name": "durationFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "DurationFilter", "ofType": None }
            },
            {
                "name": "emailFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "EmailFilter", "ofType": None }
            },
            {
                "name": "emailFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "EmailFilter", "ofType": None }
            },
            {
                "name": "emailFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "EmailFilter", "ofType": None }
            },
            {
                "name": "emailFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "EmailFilter", "ofType": None }
            },
            {
                "name": "emailFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "EmailFilter", "ofType": None }
            },
            {
                "name": "floatFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "FloatFilter", "ofType": None }
            },
            {
                "name": "floatFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "FloatFilter", "ofType": None }
            },
            {
                "name": "floatFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "FloatFilter", "ofType": None }
            },
            {
                "name": "floatFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "FloatFilter", "ofType": None }
            },
            {
                "name": "floatFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "FloatFilter", "ofType": None }
            },
            {
                "name": "integerFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "IntFilter", "ofType": None }
            },
            {
                "name": "integerFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "IntFilter", "ofType": None }
            },
            {
                "name": "integerFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "IntFilter", "ofType": None }
            },
            {
                "name": "integerFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "IntFilter", "ofType": None }
            },
            {
                "name": "integerFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "IntFilter", "ofType": None }
            },
            {
                "name": "smallIntegerFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "IntFilter", "ofType": None }
            },
            {
                "name": "smallIntegerFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "IntFilter", "ofType": None }
            },
            {
                "name": "smallIntegerFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "IntFilter", "ofType": None }
            },
            {
                "name": "smallIntegerFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "IntFilter", "ofType": None }
            },
            {
                "name": "smallIntegerFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "IntFilter", "ofType": None }
            },
            {
                "name": "positiveIntegerFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "PositiveIntFilter", "ofType": None }
            },
            {
                "name": "positiveIntegerFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "PositiveIntFilter", "ofType": None }
            },
            {
                "name": "positiveIntegerFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "PositiveIntFilter", "ofType": None }
            },
            {
                "name": "positiveIntegerFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "PositiveIntFilter", "ofType": None }
            },
            {
                "name": "positiveIntegerFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "PositiveIntFilter", "ofType": None }
            },
            {
                "name": "slugFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "SlugFilter", "ofType": None }
            },
            {
                "name": "slugFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "SlugFilter", "ofType": None }
            },
            {
                "name": "slugFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "SlugFilter", "ofType": None }
            },
            {
                "name": "slugFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "SlugFilter", "ofType": None }
            },
            {
                "name": "slugFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "SlugFilter", "ofType": None }
            },
            {
                "name": "textFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "StringFilter", "ofType": None }
            },
            {
                "name": "textFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "StringFilter", "ofType": None }
            },
            {
                "name": "textFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "StringFilter", "ofType": None }
            },
            {
                "name": "textFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "StringFilter", "ofType": None }
            },
            {
                "name": "textFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "StringFilter", "ofType": None }
            },
            {
                "name": "urlFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "URLFilter", "ofType": None }
            },
            {
                "name": "urlFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "URLFilter", "ofType": None }
            },
            {
                "name": "urlFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "URLFilter", "ofType": None }
            },
            {
                "name": "urlFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "URLFilter", "ofType": None }
            },
            {
                "name": "urlFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "URLFilter", "ofType": None }
            },
            {
                "name": "uuidFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "UUIDFilter", "ofType": None }
            },
            {
                "name": "uuidFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "UUIDFilter", "ofType": None }
            },
            {
                "name": "uuidFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "UUIDFilter", "ofType": None }
            },
            {
                "name": "uuidFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "UUIDFilter", "ofType": None }
            },
            {
                "name": "uuidFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "UUIDFilter", "ofType": None }
            },
            {
                "name": "foreignKeyFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
            },
            {
                "name": "foreignKeyFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
            },
            {
                "name": "foreignKeyFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
            },
            {
                "name": "foreignKeyFieldWithoutRelatedName",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
            },
            {
                "name": "objectId",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "PositiveIntFilter", "ofType": None }
            },
            {
                "name": "manyToManyFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
            },
            {
                "name": "manyToManyFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
            },
            {
                "name": "manyToManyFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
            },
            {
                "name": "manyToManyFieldWithoutRelatedName",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
            },
            {
                "name": "genericRelationField",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
            },
            {
                "name": "foreignKeyRelated",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
            },
            {
                "name": "foreignKeyNullableRelated",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
            },
            {
                "name": "foreignKeyWithDescriptionRelated",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
            },
            {
                "name": "oneToOneRelated",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
            },
            {
                "name": "oneToOneNullableRelated",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
            },
            {
                "name": "oneToOneWithDescriptionRelated",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
            },
            {
                "name": "manyToManyRelated",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
            },
            {
                "name": "manyToManyNullableRelated",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
            },
            {
                "name": "manyToManyWithDescriptionRelated",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
            },
            {
                "name": "foreignKeyBRelated",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelBFilterInput", "ofType": None }
            },
            {
                "name": "oneToOneBRelated",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelBFilterInput", "ofType": None }
            },
            {
                "name": "manyToManyBRelated",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelBFilterInput", "ofType": None }
            },
            {
                "name": "AND",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "LIST", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None } }
            },
            {
                "name": "OR",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "LIST", "name": None, "ofType": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None } }
            },
            {
                "name": "NOT",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
            }
        ]

        self.run_test_graphql_type("ModelAFilterInput", fields_to_test, input_type=True)

    def test_model_order_by_input_type(self):
        fields_to_test = [
            {
                "name": "id",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "booleanFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "booleanFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "booleanFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "booleanFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "booleanFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "charFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "charFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "charFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "charFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "charFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "choiceFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "choiceFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "choiceFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "choiceFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "choiceFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "dateFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "dateFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "dateFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "dateFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "dateFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "dateTimeFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "dateTimeFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "dateTimeFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "dateTimeFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "dateTimeFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "timeFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "timeFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "timeFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "timeFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "timeFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "decimalFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "decimalFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "decimalFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "decimalFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "decimalFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "durationFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "durationFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "durationFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "durationFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "durationFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "emailFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "emailFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "emailFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "emailFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "emailFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "floatFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "floatFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "floatFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "floatFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "floatFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "integerFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "integerFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "integerFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "integerFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "integerFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "smallIntegerFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "smallIntegerFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "smallIntegerFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "smallIntegerFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "smallIntegerFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "positiveIntegerFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "positiveIntegerFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "positiveIntegerFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "positiveIntegerFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "positiveIntegerFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "slugFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "slugFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "slugFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "slugFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "slugFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "textFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "textFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "textFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "textFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "textFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "urlFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "urlFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "urlFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "urlFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "urlFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderStringEnum", "ofType": None }
            },
            {
                "name": "uuidFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "uuidFieldNotEditable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "uuidFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "uuidFieldWithDefault",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "uuidFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "foreignKeyFieldRequired",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAOrderByInput", "ofType": None }
            },
            {
                "name": "foreignKeyFieldNullable",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAOrderByInput", "ofType": None }
            },
            {
                "name": "foreignKeyFieldWithDescription",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAOrderByInput", "ofType": None }
            },
            {
                "name": "foreignKeyFieldWithoutRelatedName",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAOrderByInput", "ofType": None }
            },
            {
                "name": "objectId",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "ENUM", "name": "OrderEnum", "ofType": None }
            },
            {
                "name": "oneToOneRelated",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAOrderByInput", "ofType": None }
            },
            {
                "name": "oneToOneNullableRelated",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAOrderByInput", "ofType": None }
            },
            {
                "name": "oneToOneWithDescriptionRelated",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelAOrderByInput", "ofType": None }
            },
            {
                "name": "oneToOneBRelated",
                "description": None,
                "defaultValue": None,
                "type": { "kind": "INPUT_OBJECT", "name": "ModelBOrderByInput", "ofType": None }
            }
        ]
        self.run_test_graphql_type("ModelAOrderByInput", fields_to_test, input_type=True)

