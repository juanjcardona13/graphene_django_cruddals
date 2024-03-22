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
export function readMenu(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query readMenu($where: MenuFilterInput!  ${varsStr}) {
            readMenu(where: $where ) {
                ${selectedFields}
            }
        }
    `;
    return query;
};
export function listMenus(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query listMenus( ${varsStr}) {
            listMenus() {
                ${PaginatedType}
                objects {
                    ${selectedFields}
                }
            }
        }
    `;
    return query;
};
export function searchMenus(fields, extraArgs=[]) {
    let varsStr = ""
    for (let newArg of extraArgs) {
        varsStr += `$${newArg.variableName}: ${newArg.variableType} `
    }
    const defaultFields = 'id';
    const selectedFields = fields ? fields : defaultFields;

    const query = gql`
        query searchMenus($where: MenuFilterInput $orderBy: MenuOrderByInput $paginated: PaginatedInput  ${varsStr}) {
            searchMenus(where: $where orderBy: $orderBy paginated: $paginated ) {
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

//region ============= MENUITEM
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

