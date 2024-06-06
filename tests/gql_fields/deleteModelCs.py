deleteModelCs = {
    "name": "deleteModelCs",
    "description": None,
    "type": {"kind": "OBJECT", "name": "DeleteModelCsPayload", "ofType": None},
    "args": [
        {
            "name": "where",
            "description": None,
            "defaultValue": None,
            "type": {
                "kind": "NON_NULL",
                "name": None,
                "ofType": {
                    "kind": "INPUT_OBJECT",
                    "name": "FilterModelCInput",
                    "ofType": None,
                },
            },
        }
    ],
}
