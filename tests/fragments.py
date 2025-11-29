model_c_fragment = """
    fragment modelCType on ModelCType {
        id
        charField
        integerField
        booleanField
        dateTimeField
        jsonField
        fileField
        isActive
        oneToOneField { id }
        paginatedManyToManyField { objects { id } }
        paginatedForeignKeyDRelated { objects { id } }
    }
"""

model_d_fragment = """
    fragment modelDType on ModelDType {
        id
        foreignKeyField { id }
        oneToOneCRelated { id }
        paginatedManyToManyCRelated { objects {id} }
        paginatedForeignKeyERelated { objects {id} }
    }
"""

model_e_fragment = """
    fragment modelEType on ModelEType {
        id
        foreignKeyFieldDeep { id }
    }
"""

model_f_fragment = """
    fragment modelFType on ModelFType {
        id
        name
        foreignKeyField {
            id
        }
    }
"""

model_g_fragment = """
    fragment modelGType on ModelGType {
        id
        name
        paginatedForeignKeyHRelated {
            objects {
                id
            }
        }
    }
"""

model_h_fragment = """
    fragment modelHType on ModelHType {
        id
        name
        foreignKeyField {
            id
        }
    }
"""


errors_fragment = """
    fragment errorsType on ErrorCollectionType {
        objectPosition
        errors {
            field
            messages
        }
    }
"""

pagination_fragment = """
    fragment paginationType on PaginationInterface {
        total
        page
        pages
        hasNext
        hasPrev
        indexStart
        indexEnd
    }
"""


# region CRUDDALS ModelC
create_model_c_mutation = (
    errors_fragment
    + model_c_fragment
    + """
    mutation createModelCs($input: [CreateModelCInput!]!) {
        createModelCs(input: $input) {
            objects { ...modelCType }
            errorsReport { ...errorsType }
        }
    }
"""
)

read_model_c_query = (
    model_c_fragment
    + """
    query readModelC($where: FilterModelCInput!) {
        readModelC(where: $where) {
            ...modelCType
        }
    }
"""
)

update_model_c_mutation = (
    errors_fragment
    + model_c_fragment
    + """
    mutation updateModelCs($input: [UpdateModelCInput!]!) {
        updateModelCs(input: $input) {
            objects { ...modelCType }
            errorsReport { ...errorsType }
        }
    }
"""
)

delete_model_c_mutation = (
    errors_fragment
    + model_c_fragment
    + """
    mutation deleteModelCs($where: FilterModelCInput!) {
        deleteModelCs(where: $where) {
            success
            objects { ...modelCType }
            errorsReport { ...errorsType }
        }
    }
"""
)

deactivate_model_c_mutation = (
    errors_fragment
    + model_c_fragment
    + """
    mutation deactivateModelCs($where: FilterModelCInput!) {
        deactivateModelCs(where: $where) {
            objects { ...modelCType }
            errorsReport { ...errorsType }
        }
    }
"""
)

activate_model_c_mutation = (
    errors_fragment
    + model_c_fragment
    + """
    mutation activateModelCs($where: FilterModelCInput!) {
        activateModelCs(where: $where) {
            objects { ...modelCType }
            errorsReport { ...errorsType }
        }
    }
"""
)

list_model_c_query = (
    model_c_fragment
    + """
    query listModelCs {
        listModelCs {
            ...modelCType
        }
    }
"""
)

search_model_c_query = (
    pagination_fragment
    + """
    query searchModelCs($where: FilterModelCInput $orderBy: OrderByModelCInput $paginationConfig: PaginationConfigInput) {
        searchModelCs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig) {
            ...paginationType
            objects {
                id
            }
        }
    }
"""
)

objs_to_create_type_c = [
    {
        "charField": "AAA",
        "integerField": 1,
        "booleanField": True,
        "dateTimeField": "2021-01-01T00:00:00Z",
        "jsonField": '{"key": "value"}',
    },
    {
        "charField": "BBB",
        "integerField": 2,
        "booleanField": False,
        "dateTimeField": "2021-02-02T00:00:00Z",
        "jsonField": '{"key": "value"}',
    },
    {
        "charField": "CCC",
        "integerField": 3,
        "booleanField": True,
        "dateTimeField": "2021-03-03T00:00:00Z",
        "jsonField": '{"key": "value"}',
    },
    {
        "charField": "DDD",
        "integerField": 4,
        "booleanField": False,
        "dateTimeField": "2021-04-04T00:00:00Z",
        "jsonField": '{"key": "value"}',
    },
    {
        "charField": "EEE",
        "integerField": 5,
        "booleanField": True,
        "dateTimeField": "2021-05-05T00:00:00Z",
        "jsonField": '{"key": "value"}',
    },
    {
        "charField": "aaa",
        "integerField": 1,
        "booleanField": True,
        "dateTimeField": "2021-01-01T00:00:00Z",
        "jsonField": '{"key": "value"}',
    },
    {
        "charField": "bbb",
        "integerField": 2,
        "booleanField": False,
        "dateTimeField": "2021-02-02T00:00:00Z",
        "jsonField": '{"key": "value"}',
    },
    {
        "charField": "ccc",
        "integerField": 3,
        "booleanField": True,
        "dateTimeField": "2021-03-03T00:00:00Z",
        "jsonField": '{"key": "value"}',
    },
    {
        "charField": "ddd",
        "integerField": 4,
        "booleanField": False,
        "dateTimeField": "2021-04-04T00:00:00Z",
        "jsonField": '{"key": "value"}',
    },
    {
        "charField": "eee",
        "integerField": 5,
        "booleanField": True,
        "dateTimeField": "2021-05-05T00:00:00Z",
        "jsonField": '{"key": "value"}',
    },
]
# endregion

# region CRUDDALS ModelD
create_model_d_mutation = (
    errors_fragment
    + model_d_fragment
    + """
    mutation createModelDs($input: [CreateModelDInput!]!) {
        createModelDs(input: $input) {
            objects { ...modelDType }
            errorsReport { ...errorsType }
        }
    }
"""
)

read_model_d_query = (
    model_d_fragment
    + """
    query readModelD($where: FilterModelDInput!) {
        readModelD(where: $where) {
            ...modelDType
        }
    }
"""
)

update_model_d_mutation = (
    errors_fragment
    + model_d_fragment
    + """
    mutation updateModelDs($input: [UpdateModelDInput!]!) {
        updateModelDs(input: $input) {
            objects { ...modelDType }
            errorsReport { ...errorsType }
        }
    }
"""
)

delete_model_d_mutation = (
    errors_fragment
    + model_d_fragment
    + """
    mutation deleteModelDs($where: FilterModelDInput) {
        deleteModelDs(where: $where) {
            success
            objects { ...modelDType }
            errorsReport { ...errorsType }
        }
    }
"""
)

deactivate_model_d_mutation = (
    errors_fragment
    + model_d_fragment
    + """
    mutation deactivateModelDs($where: FilterModelDInput) {
        deactivateModelDs(where: $where) {
            objects { ...modelDType }
            errorsReport { ...errorsType }
        }
    }
"""
)

activate_model_d_mutation = (
    errors_fragment
    + model_d_fragment
    + """
    mutation activateModelDs($where: FilterModelDInput) {
        activateModelDs(where: $where) {
            objects { ...modelDType }
            errorsReport { ...errorsType }
        }
    }
"""
)

list_model_d_query = (
    model_d_fragment
    + """
    query listModelDs {
        listModelDs {
            ...modelDType
        }
    }
"""
)

search_model_d_query = (
    pagination_fragment
    + """
    query searchModelDs($where: FilterModelDInput $orderBy: OrderByModelDInput $paginationConfig: PaginationConfigInput) {
        searchModelDs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig) {
            ...paginationType
            objects {
                id
            }
        }
    }
"""
)

objs_to_create_type_d = [
    {
        "foreignKeyField": 2,
    },
    {
        "foreignKeyField": 3,
    },
]
# endregion

# region CRUDDALS ModelE
create_model_e_mutation = (
    model_e_fragment
    + errors_fragment
    + """
    mutation createModelEs($input: [CreateModelEInput!]!) {
        createModelEs(input: $input) {
            objects { ...modelEType }
            errorsReport { ...errorsType }
        }
    }
"""
)

read_model_e_query = (
    model_e_fragment
    + """
    query readModelE($where: FilterModelEInput!) {
        readModelE(where: $where) {
            ...modelEType
        }
    }
"""
)

update_model_e_mutation = (
    model_e_fragment
    + errors_fragment
    + """
    mutation updateModelEs($input: [UpdateModelEInput!]!) {
        updateModelEs(input: $input) {
            objects { ...modelEType }
            errorsReport { ...errorsType }
        }
    }
"""
)

delete_model_e_mutation = (
    model_e_fragment
    + errors_fragment
    + """
    mutation deleteModelEs($where: FilterModelEInput) {
        deleteModelEs(where: $where) {
            success
            objects { ...modelEType }
            errorsReport { ...errorsType }
        }
    }
"""
)

deactivate_model_e_mutation = (
    model_e_fragment
    + errors_fragment
    + """
    mutation deactivateModelEs($where: FilterModelEInput) {
        deactivateModelEs(where: $where) {
            objects { ...modelEType }
            errorsReport { ...errorsType }
        }
    }
"""
)

activate_model_e_mutation = (
    model_e_fragment
    + errors_fragment
    + """
    mutation activateModelEs($where: FilterModelEInput) {
        activateModelEs(where: $where) {
            objects { ...modelEType }
            errorsReport { ...errorsType }
        }
    }
"""
)

list_model_e_query = (
    model_e_fragment
    + """
    query listModelEs {
        listModelEs {
            ...modelEType
        }
    }
"""
)

search_model_e_query = (
    pagination_fragment
    + model_e_fragment
    + """
    query searchModelEs($where: FilterModelEInput $orderBy: OrderByModelEInput $paginationConfig: PaginationConfigInput) {
        searchModelEs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig) {
            ...paginationType
            objects { ...modelEType }
        }
    }
"""
)

objs_to_create_type_e = [
    {
        "foreignKeyFieldDeep": 1,
    },
    {
        "foreignKeyFieldDeep": 2,
    },
]

# endregion

# region CRUDDALS ModelF
create_model_f_mutation = (
    model_f_fragment
    + errors_fragment
    + """
    mutation createModelFs($input: [CreateModelFInput!]!) {
        createModelFs(input: $input) {
            objects { ...modelFType }
            errorsReport { ...errorsType }
        }
    }
"""
)

read_model_f_query = (
    model_f_fragment
    + """
    query readModelF($where: FilterModelFInput!) {
        readModelF(where: $where) {
            ...modelFType
        }
    }
"""
)

update_model_f_mutation = (
    model_f_fragment
    + errors_fragment
    + """
    mutation updateModelFs($input: [UpdateModelFInput!]!) {
        updateModelFs(input: $input) {
            objects { ...modelFType }
            errorsReport { ...errorsType }
        }
    }
"""
)

delete_model_f_mutation = (
    model_f_fragment
    + errors_fragment
    + """
    mutation deleteModelFs($where: FilterModelFInput) {
        deleteModelFs(where: $where) {
            success
            objects { ...modelFType }
            errorsReport { ...errorsType }
        }
    }
"""
)

deactivate_model_f_mutation = (
    model_f_fragment
    + errors_fragment
    + """
    mutation deactivateModelFs($where: FilterModelFInput) {
        deactivateModelFs(where: $where) {
            objects { ...modelFType }
            errorsReport { ...errorsType }
        }
    }
"""
)

activate_model_f_mutation = (
    model_f_fragment
    + errors_fragment
    + """
    mutation activateModelFs($where: FilterModelFInput) {
        activateModelFs(where: $where) {
            objects { ...modelFType }
            errorsReport { ...errorsType }
        }
    }
"""
)

list_model_f_query = (
    model_f_fragment
    + """
    query listModelFs {
        listModelFs {
            ...modelFType
        }
    }
"""
)

search_model_f_query = (
    pagination_fragment
    + model_f_fragment
    + """
    query searchModelFs($where: FilterModelFInput $orderBy: OrderByModelFInput $paginationConfig: PaginationConfigInput) {
        searchModelFs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig) {
            ...paginationType
            objects { ...modelFType }
        }
    }
"""
)

objs_to_create_type_f = [
    {
        "name": "Juan",
    },
    {
        "name": "Carlos",
    },
]

# endregion

# region CRUDDALS ModelG
create_model_g_mutation = (
    model_g_fragment
    + errors_fragment
    + """
    mutation createModelGs($input: [CreateModelGInput!]!) {
        createModelGs(input: $input) {
            objects { ...modelGType }
            errorsReport { ...errorsType }
        }
    }
"""
)

read_model_g_query = (
    model_g_fragment
    + """
    query readModelG($where: FilterModelGInput!) {
        readModelG(where: $where) {
            ...modelGType
        }
    }
"""
)

update_model_g_mutation = (
    model_g_fragment
    + errors_fragment
    + """
    mutation updateModelGs($input: [UpdateModelGInput!]!) {
        updateModelGs(input: $input) {
            objects { ...modelGType }
            errorsReport { ...errorsType }
        }
    }
"""
)

delete_model_g_mutation = (
    model_g_fragment
    + errors_fragment
    + """
    mutation deleteModelGs($where: FilterModelGInput) {
        deleteModelGs(where: $where) {
            success
            objects { ...modelGType }
            errorsReport { ...errorsType }
        }
    }
"""
)

deactivate_model_g_mutation = (
    model_g_fragment
    + errors_fragment
    + """
    mutation deactivateModelGs($where: FilterModelGInput) {
        deactivateModelGs(where: $where) {
            objects { ...modelGType }
            errorsReport { ...errorsType }
        }
    }
"""
)

activate_model_g_mutation = (
    model_g_fragment
    + errors_fragment
    + """
    mutation activateModelGs($where: FilterModelGInput) {
        activateModelGs(where: $where) {
            objects { ...modelGType }
            errorsReport { ...errorsType }
        }
    }
"""
)

list_model_g_query = (
    model_g_fragment
    + """
    query listModelGs {
        listModelGs {
            ...modelGType
        }
    }
"""
)

search_model_g_query = (
    pagination_fragment
    + model_g_fragment
    + """
    query searchModelGs($where: FilterModelGInput $orderBy: OrderByModelGInput $paginationConfig: PaginationConfigInput) {
        searchModelGs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig) {
            ...paginationType
            objects { ...modelGType }
        }
    }
"""
)

objs_to_create_type_g = [
    {
        "name": "Juan",
    },
    {
        "name": "Carlos",
    },
]

# endregion

# region CRUDDALS ModelH
create_model_h_mutation = (
    model_h_fragment
    + errors_fragment
    + """
    mutation createModelHs($input: [CreateModelHInput!]!) {
        createModelHs(input: $input) {
            objects { ...modelHType }
            errorsReport { ...errorsType }
        }
    }
"""
)

read_model_h_query = (
    model_h_fragment
    + """
    query readModelH($where: FilterModelHInput! $me: Boolean) {
        readModelH(where: $where me: $me) {
            ...modelHType
        }
    }
"""
)

update_model_h_mutation = (
    model_h_fragment
    + errors_fragment
    + """
    mutation updateModelHs($input: [UpdateModelHInput!]!) {
        updateModelHs(input: $input) {
            objects { ...modelHType }
            errorsReport { ...errorsType }
        }
    }
"""
)

delete_model_h_mutation = (
    model_h_fragment
    + errors_fragment
    + """
    mutation deleteModelHs($where: FilterModelHInput) {
        deleteModelHs(where: $where) {
            success
            objects { ...modelHType }
            errorsReport { ...errorsType }
        }
    }
"""
)

deactivate_model_h_mutation = (
    model_h_fragment
    + errors_fragment
    + """
    mutation deactivateModelHs($where: FilterModelHInput) {
        deactivateModelHs(where: $where) {
            objects { ...modelHType }
            errorsReport { ...errorsType }
        }
    }
"""
)

activate_model_h_mutation = (
    model_h_fragment
    + errors_fragment
    + """
    mutation activateModelHs($where: FilterModelHInput) {
        activateModelHs(where: $where) {
            objects { ...modelHType }
            errorsReport { ...errorsType }
        }
    }
"""
)

list_model_h_query = (
    model_h_fragment
    + """
    query listModelHs {
        listModelHs {
            ...modelHType
        }
    }
"""
)

search_model_h_query = (
    pagination_fragment
    + model_h_fragment
    + """
    query searchModelHs($where: FilterModelHInput $orderBy: OrderByModelHInput $paginationConfig: PaginationConfigInput) {
        searchModelHs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig) {
            ...paginationType
            objects { ...modelHType }
        }
    }
"""
)

objs_to_create_type_g = [
    {
        "name": "Juan",
    },
    {
        "name": "Carlos",
    },
]

# endregion
