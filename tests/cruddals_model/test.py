# -*- coding: utf-8 -*-
from tests.utils import SchemaTestCase

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
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "ENUM", "name": "AppTestModelAChoiceFieldRequiredChoices", "ofType": None } },
                "args": []
            },
            {
                "name": "choiceFieldNotEditable",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "ENUM", "name": "AppTestModelAChoiceFieldNotEditableChoices", "ofType": None } },
                "args": []
            },
            {
                "name": "choiceFieldNullable",
                "description": None,
                "type": { "kind": "ENUM", "name": "AppTestModelAChoiceFieldNullableChoices", "ofType": None },
                "args": []
            },
            {
                "name": "choiceFieldWithDefault",
                "description": None,
                "type": { "kind": "ENUM", "name": "AppTestModelAChoiceFieldWithDefaultChoices", "ofType": None },
                "args": []
            },
            {
                "name": "choiceFieldWithDescription",
                "description": "choice_field_with_description",
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "ENUM", "name": "AppTestModelAChoiceFieldWithDescriptionChoices", "ofType": None } },
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
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
                    },
                    {
                        "name": "orderBy",
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelAOrderByInput", "ofType": None }
                    },
                    {
                        "name": "paginated",
                        "type": { "kind": "INPUT_OBJECT", "name": "PaginatedInput", "ofType": None }
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
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
                    },
                    {
                        "name": "orderBy",
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelAOrderByInput", "ofType": None }
                    },
                    {
                        "name": "paginated",
                        "type": { "kind": "INPUT_OBJECT", "name": "PaginatedInput", "ofType": None }
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
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
                    },
                    {
                        "name": "orderBy",
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelAOrderByInput", "ofType": None }
                    },
                    {
                        "name": "paginated",
                        "type": { "kind": "INPUT_OBJECT", "name": "PaginatedInput", "ofType": None }
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
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
                    },
                    {
                        "name": "orderBy",
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelAOrderByInput", "ofType": None }
                    },
                    {
                        "name": "paginated",
                        "type": { "kind": "INPUT_OBJECT", "name": "PaginatedInput", "ofType": None }
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
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
                    },
                    {
                        "name": "orderBy",
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelAOrderByInput", "ofType": None }
                    },
                    {
                        "name": "paginated",
                        "type": { "kind": "INPUT_OBJECT", "name": "PaginatedInput", "ofType": None }
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
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
                    },
                    {
                        "name": "orderBy",
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelAOrderByInput", "ofType": None }
                    },
                    {
                        "name": "paginated",
                        "type": { "kind": "INPUT_OBJECT", "name": "PaginatedInput", "ofType": None }
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
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
                    },
                    {
                        "name": "orderBy",
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelAOrderByInput", "ofType": None }
                    },
                    {
                        "name": "paginated",
                        "type": { "kind": "INPUT_OBJECT", "name": "PaginatedInput", "ofType": None }
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
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
                    },
                    {
                        "name": "orderBy",
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelAOrderByInput", "ofType": None }
                    },
                    {
                        "name": "paginated",
                        "type": { "kind": "INPUT_OBJECT", "name": "PaginatedInput", "ofType": None }
                    }
                ]
            },
            {
                "name": "oneToOneRelated",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "OBJECT", "name": "ModelAType", "ofType": None } },
                "args": []
            },
            {
                "name": "oneToOneNullableRelated",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "OBJECT", "name": "ModelAType", "ofType": None } },
                "args": []
            },
            {
                "name": "oneToOneWithDescriptionRelated",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "OBJECT", "name": "ModelAType", "ofType": None } },
                "args": []
            },
            {
                "name": "paginatedManyToManyRelated",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ModelAPaginatedType", "ofType": None },
                "args": [
                    {
                        "name": "where",
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
                    },
                    {
                        "name": "orderBy",
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelAOrderByInput", "ofType": None }
                    },
                    {
                        "name": "paginated",
                        "type": { "kind": "INPUT_OBJECT", "name": "PaginatedInput", "ofType": None }
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
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
                    },
                    {
                        "name": "orderBy",
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelAOrderByInput", "ofType": None }
                    },
                    {
                        "name": "paginated",
                        "type": { "kind": "INPUT_OBJECT", "name": "PaginatedInput", "ofType": None }
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
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelAFilterInput", "ofType": None }
                    },
                    {
                        "name": "orderBy",
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelAOrderByInput", "ofType": None }
                    },
                    {
                        "name": "paginated",
                        "type": { "kind": "INPUT_OBJECT", "name": "PaginatedInput", "ofType": None }
                    }
                ]
            },
            {
                "name": "genericRelationRelated",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "OBJECT", "name": "ModelAType", "ofType": None } },
                "args": []
            },
            {
                "name": "paginatedForeignKeyBRelated",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ModelBPaginatedType", "ofType": None },
                "args": [
                    {
                        "name": "where",
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelBFilterInput", "ofType": None }
                    },
                    {
                        "name": "orderBy",
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelBOrderByInput", "ofType": None }
                    },
                    {
                        "name": "paginated",
                        "type": { "kind": "INPUT_OBJECT", "name": "PaginatedInput", "ofType": None }
                    }
                ]
            },
            {
                "name": "oneToOneBRelated",
                "description": None,
                "type": { "kind": "NON_NULL", "name": None, "ofType": { "kind": "OBJECT", "name": "ModelBType", "ofType": None } },
                "args": []
            },
            {
                "name": "paginatedManyToManyBRelated",
                "description": None,
                "type": { "kind": "OBJECT", "name": "ModelBPaginatedType", "ofType": None },
                "args": [
                    {
                        "name": "where",
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelBFilterInput", "ofType": None }
                    },
                    {
                        "name": "orderBy",
                        "type": { "kind": "INPUT_OBJECT", "name": "ModelBOrderByInput", "ofType": None }
                    },
                    {
                        "name": "paginated",
                        "type": { "kind": "INPUT_OBJECT", "name": "PaginatedInput", "ofType": None }
                    }
                ]
            }
        ]
        self.run_test_fields_of_type("ModelAType", fields_to_test)