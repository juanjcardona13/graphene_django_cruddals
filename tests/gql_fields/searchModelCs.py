searchModelCs = {
    "name": "searchModelCs",
    "description": None,
    "type": {"kind": "OBJECT", "name": "ModelCPaginatedType", "ofType": None},
    "args": [
        {
            "name": "where",
            "description": None,
            "defaultValue": None,
            "type": {
                "kind": "INPUT_OBJECT",
                "name": "FilterModelCInput",
                "ofType": None,
            },
        },
        {
            "name": "orderBy",
            "description": None,
            "defaultValue": None,
            "type": {
                "kind": "INPUT_OBJECT",
                "name": "OrderByModelCInput",
                "ofType": None,
            },
        },
        {
            "name": "paginationConfig",
            "description": None,
            "defaultValue": None,
            "type": {
                "kind": "INPUT_OBJECT",
                "name": "PaginationConfigInput",
                "ofType": None,
            },
        },
    ],
}
