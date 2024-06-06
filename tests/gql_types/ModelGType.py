ModelGType = [
    {
        "name": "extraFieldObjectType",
        "description": None,
        "type": {"kind": "SCALAR", "name": "String", "ofType": None},
        "args": [],
    },
    {
        "name": "id",
        "description": None,
        "type": {"kind": "SCALAR", "name": "ID", "ofType": None},
        "args": [],
    },
    {
        "name": "name",
        "description": None,
        "type": {"kind": "SCALAR", "name": "String", "ofType": None},
        "args": [],
    },
    {
        "name": "paginatedForeignKeyHRelated",
        "description": None,
        "type": {"kind": "OBJECT", "name": "ModelHPaginatedType", "ofType": None},
        "args": [
            {
                "name": "where",
                "description": None,
                "defaultValue": None,
                "type": {
                    "kind": "INPUT_OBJECT",
                    "name": "FilterModelHInput",
                    "ofType": None,
                },
            },
            {
                "name": "orderBy",
                "description": None,
                "defaultValue": None,
                "type": {
                    "kind": "INPUT_OBJECT",
                    "name": "OrderByModelHInput",
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
    },
    {
        "name": "oneToOneHRelated",
        "description": None,
        "type": {"kind": "OBJECT", "name": "ModelHType", "ofType": None},
        "args": [],
    },
    {
        "name": "paginatedManyToManyHRelated",
        "description": None,
        "type": {"kind": "OBJECT", "name": "ModelHPaginatedType", "ofType": None},
        "args": [
            {
                "name": "where",
                "description": None,
                "defaultValue": None,
                "type": {
                    "kind": "INPUT_OBJECT",
                    "name": "FilterModelHInput",
                    "ofType": None,
                },
            },
            {
                "name": "orderBy",
                "description": None,
                "defaultValue": None,
                "type": {
                    "kind": "INPUT_OBJECT",
                    "name": "OrderByModelHInput",
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
    },
]
