CreateModelHInput = [
    {
        "name": "name",
        "description": None,
        "defaultValue": None,
        "type": {"kind": "SCALAR", "name": "String", "ofType": None},
    },
    {
        "name": "foreignKeyField",
        "description": None,
        "defaultValue": None,
        "type": {"kind": "INPUT_OBJECT", "name": "ModelGInput", "ofType": None},
    },
    {
        "name": "ctFieldCustom",
        "description": None,
        "defaultValue": None,
        "type": {"kind": "SCALAR", "name": "ID", "ofType": None},
    },
    {
        "name": "fkFieldCustom",
        "description": None,
        "defaultValue": None,
        "type": {"kind": "SCALAR", "name": "PositiveInt", "ofType": None},
    },
    {
        "name": "oneToOneField",
        "description": None,
        "defaultValue": None,
        "type": {"kind": "INPUT_OBJECT", "name": "ModelGInput", "ofType": None},
    },
    {
        "name": "manyToManyField",
        "description": None,
        "defaultValue": None,
        "type": {"kind": "INPUT_OBJECT", "name": "ModelGConnectInput", "ofType": None},
    },
    {
        "name": "genericForeignKey",
        "description": None,
        "defaultValue": None,
        "type": {
            "kind": "INPUT_OBJECT",
            "name": "GenericForeignKeyInput",
            "ofType": None,
        },
    },
]
