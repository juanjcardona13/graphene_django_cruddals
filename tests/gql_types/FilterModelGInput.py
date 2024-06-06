FilterModelGInput = [
    {
        "name": "extraFieldFilterInputObjectType",
        "description": None,
        "defaultValue": None,
        "type": {"kind": "SCALAR", "name": "String", "ofType": None},
    },
    {
        "name": "id",
        "description": None,
        "defaultValue": None,
        "type": {"kind": "INPUT_OBJECT", "name": "IDFilter", "ofType": None},
    },
    {
        "name": "name",
        "description": None,
        "defaultValue": None,
        "type": {"kind": "INPUT_OBJECT", "name": "StringFilter", "ofType": None},
    },
    {
        "name": "foreignKeyHRelated",
        "description": None,
        "defaultValue": None,
        "type": {"kind": "INPUT_OBJECT", "name": "FilterModelHInput", "ofType": None},
    },
    {
        "name": "oneToOneHRelated",
        "description": None,
        "defaultValue": None,
        "type": {"kind": "INPUT_OBJECT", "name": "FilterModelHInput", "ofType": None},
    },
    {
        "name": "manyToManyHRelated",
        "description": None,
        "defaultValue": None,
        "type": {"kind": "INPUT_OBJECT", "name": "FilterModelHInput", "ofType": None},
    },
    {
        "name": "AND",
        "description": None,
        "defaultValue": None,
        "type": {
            "kind": "LIST",
            "name": None,
            "ofType": {
                "kind": "INPUT_OBJECT",
                "name": "FilterModelGInput",
                "ofType": None,
            },
        },
    },
    {
        "name": "OR",
        "description": None,
        "defaultValue": None,
        "type": {
            "kind": "LIST",
            "name": None,
            "ofType": {
                "kind": "INPUT_OBJECT",
                "name": "FilterModelGInput",
                "ofType": None,
            },
        },
    },
    {
        "name": "NOT",
        "description": None,
        "defaultValue": None,
        "type": {"kind": "INPUT_OBJECT", "name": "FilterModelGInput", "ofType": None},
    },
]
