import gql from "graphql-tag";
import {PaginatedType, ErrorCollectionType} from "./general_types"

//region ============= SIMPLECRUDDALSMODEL

//region ============= MODELA
export function readModelA(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query readModelA($where: FilterModelAInput!  ${varsStr}) {
            readModelA(where: $where ) {
                ${selectedFields}
            }
        }
    `;
    return query;
};
export function listModelAs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query listModelAs {
            listModelAs {
                ${selectedFields}
            }
        }
    `;
    return query;
};
export function searchModelAs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query searchModelAs($where: FilterModelAInput $orderBy: OrderByModelAInput $paginated: PaginationConfigInput  ${varsStr}) {
            searchModelAs(where: $where orderBy: $orderBy paginated: $paginated ) {
                ${PaginatedType}
                objects {
                    ${selectedFields}
                }
            }
        }
    `;
    return query;
};
//endregion

//region ============= MODELB
export function readModelB(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query readModelB($where: FilterModelBInput!  ${varsStr}) {
            readModelB(where: $where ) {
                ${selectedFields}
            }
        }
    `;
    return query;
};
export function listModelBs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query listModelBs {
            listModelBs {
                ${selectedFields}
            }
        }
    `;
    return query;
};
export function searchModelBs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query searchModelBs($where: FilterModelBInput $orderBy: OrderByModelBInput $paginated: PaginationConfigInput  ${varsStr}) {
            searchModelBs(where: $where orderBy: $orderBy paginated: $paginated ) {
                ${PaginatedType}
                objects {
                    ${selectedFields}
                }
            }
        }
    `;
    return query;
};
//endregion

//region ============= MODELC
export function readModelC(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query readModelC($where: FilterModelCInput!  ${varsStr}) {
            readModelC(where: $where ) {
                ${selectedFields}
            }
        }
    `;
    return query;
};
export function listModelCs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query listModelCs {
            listModelCs {
                ${selectedFields}
            }
        }
    `;
    return query;
};
export function searchModelCs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query searchModelCs($where: FilterModelCInput $orderBy: OrderByModelCInput $paginated: PaginationConfigInput  ${varsStr}) {
            searchModelCs(where: $where orderBy: $orderBy paginated: $paginated ) {
                ${PaginatedType}
                objects {
                    ${selectedFields}
                }
            }
        }
    `;
    return query;
};
//endregion

//region ============= MODELD
export function readModelD(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query readModelD($where: FilterModelDInput!  ${varsStr}) {
            readModelD(where: $where ) {
                ${selectedFields}
            }
        }
    `;
    return query;
};
export function listModelDs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query listModelDs {
            listModelDs {
                ${selectedFields}
            }
        }
    `;
    return query;
};
export function searchModelDs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query searchModelDs($where: FilterModelDInput $orderBy: OrderByModelDInput $paginated: PaginationConfigInput  ${varsStr}) {
            searchModelDs(where: $where orderBy: $orderBy paginated: $paginated ) {
                ${PaginatedType}
                objects {
                    ${selectedFields}
                }
            }
        }
    `;
    return query;
};
//endregion

//region ============= MODELE
export function readModelE(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query readModelE($where: FilterModelEInput!  ${varsStr}) {
            readModelE(where: $where ) {
                ${selectedFields}
            }
        }
    `;
    return query;
};
export function listModelEs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query listModelEs {
            listModelEs {
                ${selectedFields}
            }
        }
    `;
    return query;
};
export function searchModelEs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query searchModelEs($where: FilterModelEInput $orderBy: OrderByModelEInput $paginated: PaginationConfigInput  ${varsStr}) {
            searchModelEs(where: $where orderBy: $orderBy paginated: $paginated ) {
                ${PaginatedType}
                objects {
                    ${selectedFields}
                }
            }
        }
    `;
    return query;
};
//endregion

//endregion

//region ============= ADMIN

//region ============= LOGENTRY
//endregion

//endregion

//region ============= AUTH

//region ============= PERMISSION
//endregion

//region ============= GROUP
//endregion

//region ============= USER
//endregion

//endregion

//region ============= CONTENTTYPES

//region ============= CONTENTTYPE
//endregion

//endregion

//region ============= SESSIONS

//region ============= SESSION
//endregion

//endregion

//region ============= MESSAGES

//endregion

//region ============= STATICFILES

//endregion

//region ============= GRAPHENE_DJANGO

//endregion
