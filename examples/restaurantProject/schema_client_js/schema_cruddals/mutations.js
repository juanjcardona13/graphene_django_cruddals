import gql from "graphql-tag";
import {PaginatedType, ErrorsType} from "./general_types"

//region ============= RESTAURANT

//endregion

//region ============= MENU

//region ============= MENU
export function createMenus(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation createMenus($input: [CreateMenuInput!]  ${varsStr}) {
            createMenus(input: $input ) {
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
export function updateMenus(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation updateMenus($input: [UpdateMenuInput!]  ${varsStr}) {
            updateMenus(input: $input ) {
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
export function deleteMenus(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation deleteMenus($where: MenuFilterInput!  ${varsStr}) {
            deleteMenus(where: $where ) {
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
export function deactivateMenus(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation deactivateMenus($where: MenuFilterInput!  ${varsStr}) {
            deactivateMenus(where: $where ) {
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
export function activateMenus(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const mutation = gql`
        mutation activateMenus($where: MenuFilterInput!  ${varsStr}) {
            activateMenus(where: $where ) {
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

//region ============= CORE

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

//region ============= NESTED_ADMIN

//endregion

