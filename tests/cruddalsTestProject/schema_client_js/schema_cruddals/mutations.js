import gql from "graphql-tag";
import {PaginatedType, ErrorsType} from "./general_types"

//region ============= SIMPLECRUDDALSMODEL

//region ============= MODELA
export function createModelAs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation createModelAs($input: [CreateModelAInput!]  ${varsStr}) {
            createModelAs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
export function updateModelAs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation updateModelAs($input: [UpdateModelAInput!]  ${varsStr}) {
            updateModelAs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
export function deleteModelAs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation deleteModelAs($where: ModelAFilterInput!  ${varsStr}) {
            deleteModelAs(where: $where ) {
                success
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
export function deactivateModelAs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation deactivateModelAs($where: ModelAFilterInput!  ${varsStr}) {
            deactivateModelAs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
export function activateModelAs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation activateModelAs($where: ModelAFilterInput!  ${varsStr}) {
            activateModelAs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
//endregion

//region ============= MODELB
export function createModelBs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation createModelBs($input: [CreateModelBInput!]  ${varsStr}) {
            createModelBs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
export function updateModelBs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation updateModelBs($input: [UpdateModelBInput!]  ${varsStr}) {
            updateModelBs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
export function deleteModelBs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation deleteModelBs($where: ModelBFilterInput!  ${varsStr}) {
            deleteModelBs(where: $where ) {
                success
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
export function deactivateModelBs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation deactivateModelBs($where: ModelBFilterInput!  ${varsStr}) {
            deactivateModelBs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
export function activateModelBs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation activateModelBs($where: ModelBFilterInput!  ${varsStr}) {
            activateModelBs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
//endregion

//region ============= MODELC
export function createModelCs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation createModelCs($input: [CreateModelCInput!]  ${varsStr}) {
            createModelCs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
export function updateModelCs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation updateModelCs($input: [UpdateModelCInput!]  ${varsStr}) {
            updateModelCs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
export function deleteModelCs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation deleteModelCs($where: ModelCFilterInput!  ${varsStr}) {
            deleteModelCs(where: $where ) {
                success
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
export function deactivateModelCs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation deactivateModelCs($where: ModelCFilterInput!  ${varsStr}) {
            deactivateModelCs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
export function activateModelCs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation activateModelCs($where: ModelCFilterInput!  ${varsStr}) {
            activateModelCs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
//endregion

//region ============= MODELD
export function createModelDs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation createModelDs($input: [CreateModelDInput!]  ${varsStr}) {
            createModelDs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
export function updateModelDs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation updateModelDs($input: [UpdateModelDInput!]  ${varsStr}) {
            updateModelDs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
export function deleteModelDs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation deleteModelDs($where: ModelDFilterInput!  ${varsStr}) {
            deleteModelDs(where: $where ) {
                success
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
export function deactivateModelDs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation deactivateModelDs($where: ModelDFilterInput!  ${varsStr}) {
            deactivateModelDs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
export function activateModelDs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation activateModelDs($where: ModelDFilterInput!  ${varsStr}) {
            activateModelDs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
//endregion

//region ============= MODELE
export function createModelEs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation createModelEs($input: [CreateModelEInput!]  ${varsStr}) {
            createModelEs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
export function updateModelEs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation updateModelEs($input: [UpdateModelEInput!]  ${varsStr}) {
            updateModelEs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
export function deleteModelEs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation deleteModelEs($where: ModelEFilterInput!  ${varsStr}) {
            deleteModelEs(where: $where ) {
                success
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
export function deactivateModelEs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation deactivateModelEs($where: ModelEFilterInput!  ${varsStr}) {
            deactivateModelEs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
export function activateModelEs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation activateModelEs($where: ModelEFilterInput!  ${varsStr}) {
            activateModelEs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errors {
                    ${ErrorsType}
                }
            }
        }
    `;
    return mutation;
};
//endregion

//endregion

//region ============= ADMIN

//endregion

//region ============= AUTH

//endregion

//region ============= CONTENTTYPES

//endregion

//region ============= SESSIONS

//endregion

//region ============= MESSAGES

//endregion

//region ============= STATICFILES

//endregion

//region ============= GRAPHENE_DJANGO

//endregion

