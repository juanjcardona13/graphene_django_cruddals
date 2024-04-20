from utils.client import Client
from utils.main import SchemaTestCase


class CruddalsModelSchemaErrorsTest(SchemaTestCase):
    def test_errors_in_model_a(self):
        client = Client()

        create_model_a_mutation = """
            mutation CreateModelAs($input: [CreateModelAInput!]) {
                createModelAs(input: $input) {
                    objects {
                        id
                    }
                    errorsReport {
                        objectPosition
                        errors {
                            field
                            messages
                        }
                    }
                }
            }
        """

        variables = {
            "input": [
                {
                    "binaryFieldRequired": b"\x08",
                    "binaryFieldWithDescription": b"\x08",
                    "booleanFieldRequired": True,
                    "booleanFieldWithDescription": True,
                    "charFieldRequired": "0123456789-0123456789-0123456789-0123456789-0123456789-0123456789-0123456789-0123456789-0123456789-0123456789-",
                    "charFieldWithDescription": "0123456789-0123456789-0123456789-0123456789-0123456789-0123456789-0123456789-0123456789-0123456789-0123456789-",
                    "choiceFieldRequired": "A",
                    "choiceFieldWithDescription": "B",
                    "dateFieldRequired": "2007-12-03",
                    "dateFieldWithDescription": "2007-12-03",
                    "dateTimeFieldRequired": "2007-12-03T10:15:30Z",
                    "dateTimeFieldWithDescription": "2007-12-03T10:15:30Z",
                    "timeFieldRequired": "10:15:30Z",
                    "timeFieldWithDescription": "10:15:30Z",
                    "decimalFieldRequired": "1.00",
                    "decimalFieldWithDescription": "1.00",
                    "durationFieldRequired": 121561215,
                    "durationFieldWithDescription": 121561215,
                    "emailFieldRequired": "e@email.com",
                    "emailFieldWithDescription": "e@email.com",
                    "floatFieldRequired": 1.2,
                    "floatFieldWithDescription": 1.2,
                    "integerFieldRequired": 1,
                    "integerFieldWithDescription": 1,
                    "smallIntegerFieldRequired": 1,
                    "smallIntegerFieldWithDescription": 1,
                    "positiveIntegerFieldRequired": 1,
                    "positiveIntegerFieldWithDescription": 1,
                    "slugFieldRequired": "SLUG",
                    "slugFieldWithDescription": "SLUG",
                    "textFieldRequired": "SDF",
                    "textFieldWithDescription": "SDF",
                    "urlFieldRequired": "https://url.com",
                    "urlFieldWithDescription": "https://url.com",
                    "uuidFieldRequired": "8d9a46b6-6e7c-4706-b6b3-5a20130ab038",
                    "uuidFieldWithDescription": "8d9a46b6-6e7c-4706-b6b3-5a20130ab038",
                    "foreignKeyFieldRequired": 1,
                    "foreignKeyFieldWithDescription": 1,
                    "foreignKeyFieldWithoutRelatedName": 1,
                    "oneToOneFieldRequired": 1,
                    "oneToOneFieldWithDescription": 1,
                    "oneToOneFieldWithoutRelatedName": 1,
                    "manyToManyFieldRequired": [1],
                    "manyToManyFieldWithDescription": [1],
                    "manyToManyFieldWithoutRelatedName": [1],
                }
            ]
        }
        expected_response = {
            "data": {
                "createModelAs": {
                    "objects": None,
                    "errorsReport": [
                        {
                            "objectPosition": "0",
                            "errors": [
                                {
                                    "field": "charFieldRequired",
                                    "messages": [
                                        "Ensure this value has at most 100 characters (it has 110)."
                                    ],
                                },
                                {
                                    "field": "charFieldWithDescription",
                                    "messages": [
                                        "Ensure this value has at most 100 characters (it has 110)."
                                    ],
                                },
                                {
                                    "field": "durationFieldWithDefault",
                                    "messages": ["This field is required."],
                                },
                                {
                                    "field": "urlFieldWithDefault",
                                    "messages": ["Enter a valid URL."],
                                },
                                {
                                    "field": "uuidFieldWithDefault",
                                    "messages": ["This field is required."],
                                },
                                {
                                    "field": "foreignKeyFieldRequired",
                                    "messages": [
                                        "Select a valid choice. That choice is not one of the available choices."
                                    ],
                                },
                                {
                                    "field": "foreignKeyFieldWithDescription",
                                    "messages": [
                                        "Select a valid choice. That choice is not one of the available choices."
                                    ],
                                },
                                {
                                    "field": "foreignKeyFieldWithoutRelatedName",
                                    "messages": [
                                        "Select a valid choice. That choice is not one of the available choices."
                                    ],
                                },
                                {
                                    "field": "oneToOneFieldRequired",
                                    "messages": [
                                        "Select a valid choice. That choice is not one of the available choices."
                                    ],
                                },
                                {
                                    "field": "oneToOneFieldWithDescription",
                                    "messages": [
                                        "Select a valid choice. That choice is not one of the available choices."
                                    ],
                                },
                                {
                                    "field": "oneToOneFieldWithoutRelatedName",
                                    "messages": [
                                        "Select a valid choice. That choice is not one of the available choices."
                                    ],
                                },
                                {
                                    "field": "manyToManyFieldRequired",
                                    "messages": [
                                        "Select a valid choice. 1 is not one of the available choices."
                                    ],
                                },
                                {
                                    "field": "manyToManyFieldWithDescription",
                                    "messages": [
                                        "Select a valid choice. 1 is not one of the available choices."
                                    ],
                                },
                                {
                                    "field": "manyToManyFieldWithoutRelatedName",
                                    "messages": [
                                        "Select a valid choice. 1 is not one of the available choices."
                                    ],
                                },
                            ],
                        }
                    ],
                }
            }
        }
        response = client.query(create_model_a_mutation, variables=variables).json()
        self.verify_response(
            response, expected_response, message="CREATE ModelA for test errorsReport"
        )
