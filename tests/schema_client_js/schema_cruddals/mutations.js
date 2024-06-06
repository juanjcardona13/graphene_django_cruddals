import gql from "graphql-tag";
import {PaginatedType, ErrorCollectionType} from "./general_types"

//region ============= TESTS

//region ============= MODELA
export function createModelAs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation createModelAs($input: [CreateModelAInput!]!  ${varsStr}) {
            createModelAs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
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
        mutation updateModelAs($input: [UpdateModelAInput!]!  ${varsStr}) {
            updateModelAs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
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
        mutation deleteModelAs($where: FilterModelAInput!  ${varsStr}) {
            deleteModelAs(where: $where ) {
                success
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
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
        mutation deactivateModelAs($where: FilterModelAInput!  ${varsStr}) {
            deactivateModelAs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
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
        mutation activateModelAs($where: FilterModelAInput!  ${varsStr}) {
            activateModelAs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
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
        mutation createModelBs($input: [CreateModelBInput!]!  ${varsStr}) {
            createModelBs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
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
        mutation updateModelBs($input: [UpdateModelBInput!]!  ${varsStr}) {
            updateModelBs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
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
        mutation deleteModelBs($where: FilterModelBInput!  ${varsStr}) {
            deleteModelBs(where: $where ) {
                success
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
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
        mutation deactivateModelBs($where: FilterModelBInput!  ${varsStr}) {
            deactivateModelBs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
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
        mutation activateModelBs($where: FilterModelBInput!  ${varsStr}) {
            activateModelBs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
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
        mutation createModelCs($input: [CreateModelCInput!]!  ${varsStr}) {
            createModelCs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
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
        mutation updateModelCs($input: [UpdateModelCInput!]!  ${varsStr}) {
            updateModelCs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
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
        mutation deleteModelCs($where: FilterModelCInput!  ${varsStr}) {
            deleteModelCs(where: $where ) {
                success
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
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
        mutation deactivateModelCs($where: FilterModelCInput!  ${varsStr}) {
            deactivateModelCs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
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
        mutation activateModelCs($where: FilterModelCInput!  ${varsStr}) {
            activateModelCs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
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
        mutation createModelDs($input: [CreateModelDInput!]!  ${varsStr}) {
            createModelDs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
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
        mutation updateModelDs($input: [UpdateModelDInput!]!  ${varsStr}) {
            updateModelDs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
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
        mutation deleteModelDs($where: FilterModelDInput!  ${varsStr}) {
            deleteModelDs(where: $where ) {
                success
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
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
        mutation deactivateModelDs($where: FilterModelDInput!  ${varsStr}) {
            deactivateModelDs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
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
        mutation activateModelDs($where: FilterModelDInput!  ${varsStr}) {
            activateModelDs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
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
        mutation createModelEs($input: [CreateModelEInput!]!  ${varsStr}) {
            createModelEs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
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
        mutation updateModelEs($input: [UpdateModelEInput!]!  ${varsStr}) {
            updateModelEs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
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
        mutation deleteModelEs($where: FilterModelEInput!  ${varsStr}) {
            deleteModelEs(where: $where ) {
                success
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
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
        mutation deactivateModelEs($where: FilterModelEInput!  ${varsStr}) {
            deactivateModelEs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
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
        mutation activateModelEs($where: FilterModelEInput!  ${varsStr}) {
            activateModelEs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
                }
            }
        }
    `;
    return mutation;
};
//endregion

//region ============= MODELF
export function createModelFs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation createModelFs($input: [CreateModelFInput!]!  ${varsStr}) {
            createModelFs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
                }
            }
        }
    `;
    return mutation;
};
export function updateModelFs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation updateModelFs($input: [UpdateModelFInput!]!  ${varsStr}) {
            updateModelFs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
                }
            }
        }
    `;
    return mutation;
};
export function deleteModelFs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation deleteModelFs($where: FilterModelFInput!  ${varsStr}) {
            deleteModelFs(where: $where ) {
                success
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
                }
            }
        }
    `;
    return mutation;
};
export function deactivateModelFs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation deactivateModelFs($where: FilterModelFInput!  ${varsStr}) {
            deactivateModelFs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
                }
            }
        }
    `;
    return mutation;
};
export function activateModelFs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation activateModelFs($where: FilterModelFInput!  ${varsStr}) {
            activateModelFs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
                }
            }
        }
    `;
    return mutation;
};
//endregion

//region ============= MODELG
export function createModelGs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation createModelGs($input: [CreateModelGInput!]!  ${varsStr}) {
            createModelGs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
                }
            }
        }
    `;
    return mutation;
};
export function updateModelGs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation updateModelGs($input: [UpdateModelGInput!]!  ${varsStr}) {
            updateModelGs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
                }
            }
        }
    `;
    return mutation;
};
export function deleteModelGs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation deleteModelGs($where: FilterModelGInput!  ${varsStr}) {
            deleteModelGs(where: $where ) {
                success
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
                }
            }
        }
    `;
    return mutation;
};
export function deactivateModelGs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation deactivateModelGs($where: FilterModelGInput!  ${varsStr}) {
            deactivateModelGs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
                }
            }
        }
    `;
    return mutation;
};
export function activateModelGs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation activateModelGs($where: FilterModelGInput!  ${varsStr}) {
            activateModelGs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
                }
            }
        }
    `;
    return mutation;
};
//endregion

//region ============= MODELH
export function createModelHs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation createModelHs($input: [CreateModelHInput!]!  ${varsStr}) {
            createModelHs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
                }
            }
        }
    `;
    return mutation;
};
export function updateModelHs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation updateModelHs($input: [UpdateModelHInput!]!  ${varsStr}) {
            updateModelHs(input: $input ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
                }
            }
        }
    `;
    return mutation;
};
export function deleteModelHs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation deleteModelHs($where: FilterModelHInput!  ${varsStr}) {
            deleteModelHs(where: $where ) {
                success
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
                }
            }
        }
    `;
    return mutation;
};
export function deactivateModelHs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation deactivateModelHs($where: FilterModelHInput!  ${varsStr}) {
            deactivateModelHs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
                }
            }
        }
    `;
    return mutation;
};
export function activateModelHs(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation activateModelHs($where: FilterModelHInput!  ${varsStr}) {
            activateModelHs(where: $where ) {
                objects {
                    ${selectedFields}
                }
                errorsReport {
                    ${ErrorCollectionType}
                }
            }
        }
    `;
    return mutation;
};
//endregion

//endregion
