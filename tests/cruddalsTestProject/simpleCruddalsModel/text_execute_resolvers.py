# -*- coding: utf-8 -*-
from utils.main import SchemaTestCase

model_c_fragment = """
    fragment modelCType on ModelCType {
        id
        charField
        integerField
        booleanField
        dateTimeField
        jsonField
        fileField
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

errors_fragment = """
    fragment errorsType on ErrorsType {
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
        indexStartObj
        indexEndObj
    }
"""

all_fragment = (
    model_c_fragment
    + model_d_fragment
    + model_e_fragment
    + errors_fragment
    + pagination_fragment
)

create_model_c_mutation = (
    all_fragment
    + """
    mutation createModelCs($input: [CreateModelCInput!]) {
        createModelCs(input: $input) {
            objects { ...modelCType }
            errors { ...errorsType }
        }
    }
"""
)

read_model_c_query = (
    all_fragment
    + """
    query readModelC($where: ModelCFilterInput!) {
        readModelC(where: $where) {
            ...modelCType
        }
    }
"""
)

update_model_c_mutation = (
    all_fragment
    + """
    mutation updateModelCs($input: [UpdateModelCInput!]) {
        updateModelCs(input: $input) {
            objects { ...modelCType }
            errors { ...errorsType }
        }
    }
"""
)

delete_model_c_mutation = (
    all_fragment
    + """
    mutation deleteModelCs($where: ModelCFilterInput) {
        deleteModelCs(where: $where) {
            success
            objects { ...modelCType }
            errors { ...errorsType }
        }
    }
"""
)

deactivate_model_c_mutation = (
    all_fragment
    + """
    mutation deactivateModelCs($where: ModelCFilterInput) {
        deactivateModelCs(where: $where) {
            objects { ...modelCType }
            errors { ...errorsType }
        }
    }
"""
)

activate_model_c_mutation = (
    all_fragment
    + """
    mutation activateModelCs($where: ModelCFilterInput) {
        activateModelCs(where: $where) {
            objects { ...modelCType }
            errors { ...errorsType }
        }
    }
"""
)

list_model_c_query = (
    all_fragment
    + """
    query listModelCs {
        listModelCs {
            ...modelCType
        }
    }
"""
)

search_model_c_query = (
    all_fragment
    + """
    query searchModelCs($where: ModelCFilterInput $orderBy: ModelCOrderByInput $paginated: PaginatedInput) {
        searchModelCs(where: $where orderBy: $orderBy paginated: $paginated) {
            ...paginationType
            objects { ...modelCType }
        }
    }
"""
)

create_model_d_mutation = (
    all_fragment
    + """
    mutation createModelDs($input: [CreateModelDInput!]) {
        createModelDs(input: $input) {
            objects { ...modelDType }
            errors { ...errorsType }
        }
    }
"""
)

read_model_d_query = (
    all_fragment
    + """
    query readModelD($where: ModelDFilterInput!) {
        readModelD(where: $where) {
            ...modelDType
        }
    }
"""
)

update_model_d_mutation = (
    all_fragment
    + """
    mutation updateModelDs($input: [UpdateModelDInput!]) {
        updateModelDs(input: $input) {
            objects { ...modelDType }
            errors { ...errorsType }
        }
    }
"""
)

delete_model_d_mutation = (
    all_fragment
    + """
    mutation deleteModelDs($where: ModelDFilterInput) {
        deleteModelDs(where: $where) {
            success
            objects { ...modelDType }
            errors { ...errorsType }
        }
    }
"""
)

deactivate_model_d_mutation = (
    all_fragment
    + """
    mutation deactivateModelDs($where: ModelDFilterInput) {
        deactivateModelDs(where: $where) {
            objects { ...modelDType }
            errors { ...errorsType }
        }
    }
"""
)

activate_model_d_mutation = (
    all_fragment
    + """
    mutation activateModelDs($where: ModelDFilterInput) {
        activateModelDs(where: $where) {
            objects { ...modelDType }
            errors { ...errorsType }
        }
    }
"""
)

list_model_d_query = (
    all_fragment
    + """
    query listModelDs {
        listModelDs {
            ...modelDType
        }
    }
"""
)

search_model_d_query = (
    all_fragment
    + """
    query searchModelDs($where: ModelDFilterInput $orderBy: ModelDOrderByInput $paginated: PaginatedInput) {
        searchModelDs(where: $where orderBy: $orderBy paginated: $paginated) {
            ...paginationType
            objects { ...modelDType }
        }
    }
"""
)

create_model_e_mutation = (
    all_fragment
    + """
    mutation createModelEs($input: [CreateModelEInput!]) {
        createModelEs(input: $input) {
            objects { ...modelEType }
            errors { ...errorsType }
        }
    }
"""
)

read_model_e_query = (
    all_fragment
    + """
    query readModelE($where: ModelEFilterInput!) {
        readModelE(where: $where) {
            ...modelEType
        }
    }
"""
)

update_model_e_mutation = (
    all_fragment
    + """
    mutation updateModelEs($input: [UpdateModelEInput!]) {
        updateModelEs(input: $input) {
            objects { ...modelEType }
            errors { ...errorsType }
        }
    }
"""
)

delete_model_e_mutation = (
    all_fragment
    + """
    mutation deleteModelEs($where: ModelEFilterInput) {
        deleteModelEs(where: $where) {
            success
            objects { ...modelEType }
            errors { ...errorsType }
        }
    }
"""
)

deactivate_model_e_mutation = (
    all_fragment
    + """
    mutation deactivateModelEs($where: ModelEFilterInput) {
        deactivateModelEs(where: $where) {
            objects { ...modelEType }
            errors { ...errorsType }
        }
    }
"""
)

activate_model_e_mutation = (
    all_fragment
    + """
    mutation activateModelEs($where: ModelEFilterInput) {
        activateModelEs(where: $where) {
            objects { ...modelEType }
            errors { ...errorsType }
        }
    }
"""
)

list_model_e_query = (
    all_fragment
    + """
    query listModelEs {
        listModelEs {
            ...modelEType
        }
    }
"""
)

search_model_e_query = (
    all_fragment
    + """
    query searchModelEs($where: ModelEFilterInput $orderBy: ModelEOrderByInput $paginated: PaginatedInput) {
        searchModelEs(where: $where orderBy: $orderBy paginated: $paginated) {
            ...paginationType
            objects { ...modelEType }
        }
    }
"""
)


class CruddalsModelSchemaTest(SchemaTestCase):
    pass
