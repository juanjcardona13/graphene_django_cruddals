import gql from "graphql-tag";
import {PaginatedType, ErrorsType} from "./general_types"

//region ============= RESTAURANT

//region ============= RESTAURANT
//endregion

//region ============= TABLE
//endregion

//endregion

//region ============= MENU

//region ============= MENU
//endregion

//region ============= MENUITEM
//endregion

//region ============= MODELA
export function readModelA(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query readModelA($where: ModelAFilterInput!  ${varsStr}) {
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
        query listModelAs( ${varsStr}) {
            listModelAs() {
                ${PaginatedType}
                objects {
                    ${selectedFields}
                }
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
        query searchModelAs($where: ModelAFilterInput $orderBy: ModelAOrderByInput $paginated: PaginatedInput  ${varsStr}) {
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
        query readModelB($where: ModelBFilterInput!  ${varsStr}) {
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
        query listModelBs( ${varsStr}) {
            listModelBs() {
                ${PaginatedType}
                objects {
                    ${selectedFields}
                }
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
        query searchModelBs($where: ModelBFilterInput $orderBy: ModelBOrderByInput $paginated: PaginatedInput  ${varsStr}) {
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
        query readModelC($where: ModelCFilterInput!  ${varsStr}) {
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
        query listModelCs( ${varsStr}) {
            listModelCs() {
                ${PaginatedType}
                objects {
                    ${selectedFields}
                }
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
        query searchModelCs($where: ModelCFilterInput $orderBy: ModelCOrderByInput $paginated: PaginatedInput  ${varsStr}) {
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
        query readModelD($where: ModelDFilterInput!  ${varsStr}) {
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
        query listModelDs( ${varsStr}) {
            listModelDs() {
                ${PaginatedType}
                objects {
                    ${selectedFields}
                }
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
        query searchModelDs($where: ModelDFilterInput $orderBy: ModelDOrderByInput $paginated: PaginatedInput  ${varsStr}) {
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
        query readModelE($where: ModelEFilterInput!  ${varsStr}) {
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
        query listModelEs( ${varsStr}) {
            listModelEs() {
                ${PaginatedType}
                objects {
                    ${selectedFields}
                }
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
        query searchModelEs($where: ModelEFilterInput $orderBy: ModelEOrderByInput $paginated: PaginatedInput  ${varsStr}) {
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

//region ============= MODELF
export function readModelF(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query readModelF($where: ModelFFilterInput!  ${varsStr}) {
            readModelF(where: $where ) {
                ${selectedFields}
            }
        }
    `;
    return query;
};
export function listModelFs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query listModelFs( ${varsStr}) {
            listModelFs() {
                ${PaginatedType}
                objects {
                    ${selectedFields}
                }
            }
        }
    `;
    return query;
};
export function searchModelFs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query searchModelFs($where: ModelFFilterInput $orderBy: ModelFOrderByInput $paginated: PaginatedInput  ${varsStr}) {
            searchModelFs(where: $where orderBy: $orderBy paginated: $paginated ) {
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

//region ============= CORE

//region ============= EMPLOYEEPROFILE
//endregion

//region ============= SCHEDULE
//endregion

//region ============= TIMESLOT
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

//region ============= NESTED_ADMIN

//endregion

