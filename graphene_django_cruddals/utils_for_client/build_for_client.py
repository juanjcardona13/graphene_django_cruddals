import json
import os
import textwrap

import graphene
from django.apps import apps as django_apps
from graphql.utilities.build_client_schema import build_client_schema
from graphql.utilities.print_schema import print_introspection_schema, print_schema

from graphene_django_cruddals.utils import transform_string

global_cruddals_strings = {}


current_working_directory = os.getcwd()
PATH_ROOT = current_working_directory + "/schema_client_js"
PATH_CLIENT = current_working_directory + "/schema_client_js/schema_cruddals"

if not os.path.exists(PATH_ROOT):
    os.mkdir(PATH_ROOT)

if not os.path.exists(PATH_CLIENT):
    os.mkdir(PATH_CLIENT)


def get_apps_name():
    def validate_apps(apps_name):
        [django_apps.get_app_config(app_name) for app_name in apps_name]

    apps = "__all__"  # TODO
    apps_name = []
    if apps == "__all__":
        apps_name = django_apps.app_configs.keys()
    elif isinstance(
        apps,
        (
            list,
            tuple,
        ),
    ):
        apps_name = apps
    elif isinstance(apps, dict):
        apps_name = apps.keys()
    validate_apps(apps_name)

    return apps_name


def part_of_import_js(file):
    file.write(
        """import gql from "graphql-tag";\nimport {PaginatedType, ErrorCollectionType} from "./general_types"\n\n"""
    )


def return_args_and_variables(objects_type):
    vars_str = ""
    args_str = ""
    for arg_name, arg_type in objects_type.args.items():
        vars_str += f"${arg_name}: {arg_type.type} "
        args_str += f"{arg_name}: ${arg_name} "
    return vars_str, args_str


def build_schema(schema):
    if schema is not None:
        with open(f"{PATH_CLIENT}/schema.json", "w") as outfile:
            schema_dict = {"data": schema.introspect()}
            json.dump(schema_dict, outfile, indent=2)  # , sort_keys=True
        with open(f"{PATH_CLIENT}/schema.gql", "w") as outfile:
            outfile.write(print_schema(schema.graphql_schema))
        with open(f"{PATH_CLIENT}/schema-introspect.gql", "w") as outfile:
            outfile.write(print_introspection_schema(schema.graphql_schema))


def build_create(app_name, model_name, model_name_plural, mutations):
    name_function_create = f"create{model_name_plural}"
    function_create = mutations.get(name_function_create, None)
    text = ""
    if function_create is not None:
        vars_str, args_str = return_args_and_variables(function_create)

        globals()["global_cruddals_strings"][app_name][model_name].update(
            {
                "create": textwrap.dedent(
                    f"""
                mutation {name_function_create}({vars_str}) {{
                    {name_function_create}({args_str}) {{
                        objects {{
                            id
                        }}
                        errors {{
                            objectPosition
                            errors {{
                                field
                                messages
                            }}
                        }}
                    }}
                }}
            """
                )
            }
        )

        text = f"""
            export function {name_function_create}(fields, extraArgs=[]) {{
                let varsStr = ""
                for (let newArg of extraArgs) {{
                    varsStr += `$${{newArg.variableName}}: ${{newArg.variableType}} `
                }}
                const defaultFields = 'id';
                const selectedFields = fields ? fields : defaultFields;

                const mutation = gql`
                    mutation {name_function_create}({vars_str} ${{varsStr}}) {{
                        {name_function_create}({args_str}) {{
                            objects {{
                                ${{selectedFields}}
                            }}
                            errors {{
                                ${{ErrorCollectionType}}
                            }}
                        }}
                    }}
                `;
                return mutation;
            }};"""
        text = textwrap.dedent(text)
    return text


def build_read(app_name, model_name, queries):
    name_function_read = f"read{model_name}"
    name_model_type = f"{model_name}Type"
    function_read = queries.get(name_function_read, None)
    text = ""
    if function_read is not None:
        vars_str, args_str = return_args_and_variables(function_read)
        globals()["global_cruddals_strings"][app_name][model_name].update(
            {
                "read": textwrap.dedent(
                    f"""
                query {name_function_read}({vars_str}) {{
                    {name_function_read}({args_str}) {{
                        id
                    }}
                }}
            """
                )
            }
        )
        text = f"""
            export function {name_function_read}(fields, extraArgs=[]) {{
                let varsStr = ""
                for (let newArg of extraArgs) {{
                    varsStr += `$${{newArg.variableName}}: ${{newArg.variableType}} `
                }}
                const defaultFields = 'id';
                const selectedFields = fields ? fields : defaultFields;

                const query = gql`
                    query {name_function_read}({vars_str} ${{varsStr}}) {{
                        {name_function_read}({args_str}) {{
                            ${{selectedFields}}
                        }}
                    }}
                `;
                return query;
            }};"""
        text = textwrap.dedent(text)
    return text


def build_update(app_name, model_name, model_name_plural, mutations):
    name_function_update = f"update{model_name_plural}"
    function_update = mutations.get(name_function_update, None)
    text = ""
    if function_update is not None:
        vars_str, args_str = return_args_and_variables(function_update)
        globals()["global_cruddals_strings"][app_name][model_name].update(
            {
                "update": textwrap.dedent(
                    f"""
                mutation {name_function_update}({vars_str}) {{
                    {name_function_update}({args_str}) {{
                        objects {{
                            id
                        }}
                        errors {{
                            objectPosition
                            errors {{
                                field
                                messages
                            }}
                        }}
                    }}
                }}
            """
                )
            }
        )
        text = f"""
            export function {name_function_update}(fields, extraArgs=[]) {{
                let varsStr = ""
                for (let newArg of extraArgs) {{
                    varsStr += `$${{newArg.variableName}}: ${{newArg.variableType}} `
                }}
                const defaultFields = 'id';
                const selectedFields = fields ? fields : defaultFields;
                
                const mutation = gql`
                    mutation {name_function_update}({vars_str} ${{varsStr}}) {{
                        {name_function_update}({args_str}) {{
                            objects {{
                                ${{selectedFields}}
                            }}
                            errors {{
                                ${{ErrorCollectionType}}
                            }}
                        }}
                    }}
                `;
                return mutation;
            }};"""
        text = textwrap.dedent(text)
    return text


def build_delete(app_name, model_name, model_name_plural, mutations):
    name_function_delete = f"delete{model_name_plural}"
    function_delete = mutations.get(name_function_delete, None)
    text = ""
    if function_delete is not None:
        vars_str, args_str = return_args_and_variables(function_delete)
        globals()["global_cruddals_strings"][app_name][model_name].update(
            {
                "delete": textwrap.dedent(
                    f"""
                mutation {name_function_delete}({vars_str}) {{
                    {name_function_delete}({args_str}) {{
                        success
                        objects {{
                            id
                        }}
                        errors {{
                            objectPosition
                            errors {{
                                field
                                messages
                            }}
                        }}
                    }}
                }}
            """
                )
            }
        )
        text = f"""
            export function {name_function_delete}(fields, extraArgs=[]) {{
                let varsStr = ""
                for (let newArg of extraArgs) {{
                    varsStr += `$${{newArg.variableName}}: ${{newArg.variableType}} `
                }}
                const defaultFields = 'id';
                const selectedFields = fields ? fields : defaultFields;
                
                const mutation = gql`
                    mutation {name_function_delete}({vars_str} ${{varsStr}}) {{
                        {name_function_delete}({args_str}) {{
                            success
                            objects {{
                                ${{selectedFields}}
                            }}
                            errors {{
                                ${{ErrorCollectionType}}
                            }}
                        }}
                    }}
                `;
                return mutation;
            }};"""
        text = textwrap.dedent(text)
    return text


def build_deactivate(app_name, model_name, model_name_plural, mutations):
    name_function_deactivate = f"deactivate{model_name_plural}"
    function_deactivate = mutations.get(name_function_deactivate, None)
    text = ""
    if function_deactivate is not None:
        vars_str, args_str = return_args_and_variables(function_deactivate)
        globals()["global_cruddals_strings"][app_name][model_name].update(
            {
                "deactivate": textwrap.dedent(
                    f"""
                mutation {name_function_deactivate}({vars_str}) {{
                    {name_function_deactivate}({args_str}) {{
                        objects {{
                            id
                        }}
                        errors {{
                            objectPosition
                            errors {{
                                field
                                messages
                            }}
                        }}
                    }}
                }}
            """
                )
            }
        )
        text = f"""
            export function {name_function_deactivate}(fields, extraArgs=[]) {{
                let varsStr = ""
                for (let newArg of extraArgs) {{
                    varsStr += `$${{newArg.variableName}}: ${{newArg.variableType}} `
                }}
                const defaultFields = 'id';
                const selectedFields = fields ? fields : defaultFields;
                
                const mutation = gql`
                    mutation {name_function_deactivate}({vars_str} ${{varsStr}}) {{
                        {name_function_deactivate}({args_str}) {{
                            objects {{
                                ${{selectedFields}}
                            }}
                            errors {{
                                ${{ErrorCollectionType}}
                            }}
                        }}
                    }}
                `;
                return mutation;
            }};"""
        text = textwrap.dedent(text)
    return text


def build_activate(app_name, model_name, model_name_plural, mutations):
    name_function_activate = f"activate{model_name_plural}"
    function_activate = mutations.get(name_function_activate, None)
    text = ""
    if function_activate is not None:
        vars_str, args_str = return_args_and_variables(function_activate)
        globals()["global_cruddals_strings"][app_name][model_name].update(
            {
                "activate": textwrap.dedent(
                    f"""
                mutation {name_function_activate}({vars_str}) {{
                    {name_function_activate}({args_str}) {{
                        objects {{
                            id
                        }}
                        errors {{
                            objectPosition
                            errors {{
                                field
                                messages
                            }}
                        }}
                    }}
                }}
            """
                )
            }
        )
        text = f"""
            export function {name_function_activate}(fields, extraArgs=[]) {{
                let varsStr = ""
                for (let newArg of extraArgs) {{
                    varsStr += `$${{newArg.variableName}}: ${{newArg.variableType}} `
                }}
                const defaultFields = 'id';
                const selectedFields = fields ? fields : defaultFields;
                
                const mutation = gql`
                    mutation {name_function_activate}({vars_str} ${{varsStr}}) {{
                        {name_function_activate}({args_str}) {{
                            objects {{
                                ${{selectedFields}}
                            }}
                            errors {{
                                ${{ErrorCollectionType}}
                            }}
                        }}
                    }}
                `;
                return mutation;
            }};"""
        text = textwrap.dedent(text)
    return text


def build_list(app_name, model_name, model_name_plural, queries):
    name_function_list = f"list{model_name_plural}"
    name_model_type = f"{model_name}Type"
    function_list = queries.get(name_function_list, None)
    text = ""
    if function_list is not None:
        vars_str, args_str = return_args_and_variables(function_list)
        globals()["global_cruddals_strings"][app_name][model_name].update(
            {
                "list": textwrap.dedent(
                    f"""
                query {name_function_list}({vars_str}) {{
                    {name_function_list}({args_str}) {{
                        total
                        page
                        pages
                        hasNext
                        hasPrev
                        indexStartObj
                        indexEndObj
                        objects {{
                            id
                        }}
                    }}
                }}
            """
                )
            }
        )
        text = f"""
            export function {name_function_list}(fields, extraArgs=[]) {{
                let varsStr = ""
                for (let newArg of extraArgs) {{
                    varsStr += `$${{newArg.variableName}}: ${{newArg.variableType}} `
                }}
                const defaultFields = 'id';
                const selectedFields = fields ? fields : defaultFields;
                
                const query = gql`
                    query {name_function_list}({vars_str} ${{varsStr}}) {{
                        {name_function_list}({args_str}) {{
                            ${{PaginatedType}}
                            objects {{
                                ${{selectedFields}}
                            }}
                        }}
                    }}
                `;
                return query;
            }};"""
        text = textwrap.dedent(text)
    return text


def build_search(app_name, model_name, model_name_plural, queries):
    name_function_search = f"search{model_name_plural}"
    name_model_type = f"{model_name}Type"
    function_search = queries.get(name_function_search, None)
    text = ""
    if function_search is not None:
        vars_str, args_str = return_args_and_variables(function_search)
        globals()["global_cruddals_strings"][app_name][model_name].update(
            {
                "search": textwrap.dedent(
                    f"""
                query {name_function_search}({vars_str}) {{
                    {name_function_search}({args_str}) {{
                        total
                        page
                        pages
                        hasNext
                        hasPrev
                        indexStartObj
                        indexEndObj
                        objects {{
                            id
                        }}
                    }}
                }}
            """
                )
            }
        )
        text = f"""
            export function {name_function_search}(fields, extraArgs=[]) {{
                let varsStr = ""
                for (let newArg of extraArgs) {{
                    varsStr += `$${{newArg.variableName}}: ${{newArg.variableType}} `
                }}
                const defaultFields = 'id';
                const selectedFields = fields ? fields : defaultFields;
                
                const query = gql`
                    query {name_function_search}({vars_str} ${{varsStr}}) {{
                        {name_function_search}({args_str}) {{
                            ${{PaginatedType}}
                            objects {{
                                ${{selectedFields}}
                            }}
                        }}
                    }}
                `;
                return query;
            }};"""
        text = textwrap.dedent(text)
    return text


def build_file_general_types():
    with open(f"{PATH_CLIENT}/general_types.js", "w+") as file:
        file.write(
            "export const PaginatedType = `\n  total\n  page\n  pages\n  hasNext\n  hasPrev\n  indexStartObj\n  indexEndObj\n`;\n"
        )
        file.write(
            "export const ErrorCollectionType = `\n  objectPosition\n  errors {\n    field\n    messages\n }\n`;\n"
        )


def build_file_queries(queries):
    with open(f"{PATH_CLIENT}/queries.js", "w+") as file:
        part_of_import_js(file)
        file.write(queries)


def build_file_mutations(mutations):
    with open(f"{PATH_CLIENT}/mutations.js", "w+") as file:
        part_of_import_js(file)
        file.write(mutations)


def build_file_test_in_graphiql():
    text_for_graphiql = ""
    for app_name, models in globals()["global_cruddals_strings"].items():
        text_for_graphiql += f"#region ============= {app_name.upper()}\n"
        for model_name, strings_cruddals in models.items():
            text_for_graphiql += f"\n#region ============= {model_name.upper()}\n"
            for func_name, string in strings_cruddals.items():
                text_for_graphiql += f"{string}"
            text_for_graphiql += f"\n#endregion\n\n"
        text_for_graphiql += f"\n#endregion\n\n"
    with open(f"{PATH_CLIENT}/test_in_graphiql.gql", "w+") as file:
        text_for_graphiql = textwrap.dedent(text_for_graphiql)
        file.write(text_for_graphiql)


def build_files_for_client_schema_cruddals(schema):
    if schema is not None:
        build_schema(schema)

        apps_name = get_apps_name()
        all_models_name = []
        for app_name in apps_name:
            app = django_apps.get_app_config(app_name)
            for model in app.get_models():
                all_models_name.append(model.__name__)

        graphql_schema = schema.graphql_schema

        queries = graphql_schema.query_type.fields
        mutations = []
        if graphql_schema.mutation_type:
            mutations = graphql_schema.mutation_type.fields

        text_queries = ""
        text_mutations = ""

        for app_name in apps_name:
            app = django_apps.get_app_config(app_name)

            globals()["global_cruddals_strings"].update({app_name: {}})

            text_queries += f"//region ============= {app_name.upper()}\n"
            text_mutations += f"//region ============= {app_name.upper()}\n"

            for model in app.get_models():
                model_name = model.__name__
                model_name_plural = transform_string(
                    model._meta.verbose_name_plural, "PascalCase"
                )

                globals()["global_cruddals_strings"][app_name].update({model_name: {}})

                query_read = build_read(app_name, model_name, queries)
                query_list = build_list(
                    app_name, model_name, model_name_plural, queries
                )
                query_search = build_search(
                    app_name, model_name, model_name_plural, queries
                )

                mutation_create = ""
                mutation_update = ""
                mutation_delete = ""
                mutation_deactivate = ""
                mutation_activate = ""

                if mutations:
                    mutation_create = build_create(
                        app_name, model_name, model_name_plural, mutations
                    )
                    mutation_update = build_update(
                        app_name, model_name, model_name_plural, mutations
                    )
                    mutation_delete = build_delete(
                        app_name, model_name, model_name_plural, mutations
                    )
                    mutation_deactivate = build_deactivate(
                        app_name, model_name, model_name_plural, mutations
                    )
                    mutation_activate = build_activate(
                        app_name, model_name, model_name_plural, mutations
                    )

                text_queries += f"\n//region ============= {model_name.upper()}{query_read}{query_list}{query_search}\n//endregion\n"
                if (
                    mutation_create
                    or mutation_update
                    or mutation_delete
                    or mutation_deactivate
                    or mutation_activate
                ):
                    text_mutations += f"\n//region ============= {model_name.upper()}{mutation_create}{mutation_update}{mutation_delete}{mutation_deactivate}{mutation_activate}\n//endregion\n"

            text_queries += f"\n//endregion\n\n"
            text_mutations += f"\n//endregion\n\n"

        build_file_general_types()
        build_file_queries(text_queries)
        build_file_mutations(text_mutations)
        build_file_test_in_graphiql()


def build_files_for_client_schema(schema, name):
    def get_first_scalar_field(field, path=None):
        if path is None:
            path = []

        # Unpack field if it's a List or NonNull type
        if isinstance(field.type, graphene.List) or isinstance(
            field.type, graphene.NonNull
        ):
            field = field.type.of_type

        if isinstance(field.type, graphene.ObjectType):
            if field.type.fields:  # If the field has subfields
                for subfield_name, subfield in field.type.fields.items():
                    result = get_first_scalar_field(subfield, path + [subfield_name])
                    if result is not None:
                        return result
        else:
            # We've found a scalar field, return the full path to it
            return " ".join(path + [field.name])

    if schema is not None:
        CUSTOM_PATH = f"{current_working_directory}/schema_client_js/{name}"
        if not os.path.exists(CUSTOM_PATH):
            os.mkdir(CUSTOM_PATH)

        with open(f"{CUSTOM_PATH}/schema.json", "w") as outfile:
            schema_dict = {"data": schema.introspect()}
            json.dump(schema_dict, outfile, indent=2, sort_keys=True)
        with open(f"{CUSTOM_PATH}/schema.gql", "w") as outfile:
            outfile.write(print_schema(schema.graphql_schema))
        with open(f"{CUSTOM_PATH}/schema-introspect.gql", "w") as outfile:
            outfile.write(print_introspection_schema(schema.graphql_schema))

        schema_introspect = schema.introspect()
        graphql_schema = build_client_schema(schema_introspect)

        queries = graphql_schema._query.fields
        mutations = graphql_schema._mutation.fields

        text_queries = ""
        for name_query, definition_graphql_field in queries.items():
            args_str, vars_args_str = return_args_and_variables(
                definition_graphql_field
            )
            fields = definition_graphql_field.type.fields
            if fields:
                first_field = list(fields.keys())[0]
                fields_str = f"{{ {first_field} }}"
            else:
                fields_str = ""
            text = f"""
                export function {name_query}(fields) {{
                    const defaultFields = '{fields_str}';
                    const selectedFields = fields ? `{{ ${{ fields }} }}` : defaultFields;

                    const query = gql`
                        query {name_query}({args_str}) {{
                            {name_query}({vars_args_str}) ${{selectedFields}}
                        }}
                    `;
                    return query;
                }};\n\n"""
            text_queries += textwrap.dedent(text)
        with open(f"{CUSTOM_PATH}/queries.js", "w+") as file:
            file.write(text_queries)

        text_mutations = ""
        for name_mutation, definition_graphql_field in mutations.items():
            args_str, vars_args_str = return_args_and_variables(
                definition_graphql_field
            )
            fields = definition_graphql_field.type.fields
            if fields:
                first_field = list(fields.keys())[0]
                fields_str = f"{{ {first_field} }}"
            else:
                fields_str = ""
            text = f"""
                export function {name_mutation}(fields) {{
                    const defaultFields = '{fields_str}';
                    const selectedFields = fields ? `{{ ${{ fields }} }}` : defaultFields;

                    const mutation = gql`
                        mutation {name_mutation}({args_str}) {{
                            {name_mutation}({vars_args_str}) ${{selectedFields}}
                        }}
                    `;
                    return mutation;
                }};\n\n"""
            text_mutations += textwrap.dedent(text)
        with open(f"{CUSTOM_PATH}/mutations.js", "w+") as file:
            file.write(text_mutations)
