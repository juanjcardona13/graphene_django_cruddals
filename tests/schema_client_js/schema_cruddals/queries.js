import gql from "graphql-tag";
import {PaginatedType, ErrorCollectionType} from "./general_types"

//region ============= TESTS

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
        query searchModelAs($where: FilterModelAInput $orderBy: OrderByModelAInput $paginationConfig: PaginationConfigInput  ${varsStr}) {
            searchModelAs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig ) {
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
        query searchModelBs($where: FilterModelBInput $orderBy: OrderByModelBInput $paginationConfig: PaginationConfigInput  ${varsStr}) {
            searchModelBs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig ) {
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
        query searchModelCs($where: FilterModelCInput $orderBy: OrderByModelCInput $paginationConfig: PaginationConfigInput  ${varsStr}) {
            searchModelCs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig ) {
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
        query searchModelDs($where: FilterModelDInput $orderBy: OrderByModelDInput $paginationConfig: PaginationConfigInput  ${varsStr}) {
            searchModelDs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig ) {
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
        query searchModelEs($where: FilterModelEInput $orderBy: OrderByModelEInput $paginationConfig: PaginationConfigInput  ${varsStr}) {
            searchModelEs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig ) {
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
        query readModelF($where: FilterModelFInput!  ${varsStr}) {
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
        query listModelFs {
            listModelFs {
                ${selectedFields}
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
        query searchModelFs($where: FilterModelFInput $orderBy: OrderByModelFInput $paginationConfig: PaginationConfigInput  ${varsStr}) {
            searchModelFs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig ) {
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

//region ============= MODELG
export function readModelG(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query readModelG($where: FilterModelGInput!  ${varsStr}) {
            readModelG(where: $where ) {
                ${selectedFields}
            }
        }
    `;
    return query;
};
export function listModelGs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query listModelGs {
            listModelGs {
                ${selectedFields}
            }
        }
    `;
    return query;
};
export function searchModelGs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query searchModelGs($where: FilterModelGInput $orderBy: OrderByModelGInput $paginationConfig: PaginationConfigInput  ${varsStr}) {
            searchModelGs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig ) {
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

//region ============= MODELH
export function readModelH(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query readModelH($where: FilterModelHInput!  ${varsStr}) {
            readModelH(where: $where ) {
                ${selectedFields}
            }
        }
    `;
    return query;
};
export function listModelHs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query listModelHs {
            listModelHs {
                ${selectedFields}
            }
        }
    `;
    return query;
};
export function searchModelHs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query searchModelHs($where: FilterModelHInput $orderBy: OrderByModelHInput $paginationConfig: PaginationConfigInput  ${varsStr}) {
            searchModelHs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig ) {
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
