import json
import os
import textwrap

from django.apps import apps as django_apps
from graphene_cruddals import transform_string
from graphql.utilities.print_schema import print_introspection_schema, print_schema

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
        with open(f"{PATH_CLIENT}/schema.json", "w", encoding="utf-8") as outfile:
            schema_dict = {"data": schema.introspect()}
            json.dump(schema_dict, outfile, indent=2)  # , sort_keys=True
        with open(f"{PATH_CLIENT}/schema.gql", "w", encoding="utf-8") as outfile:
            outfile.write(print_schema(schema.graphql_schema))
        with open(
            f"{PATH_CLIENT}/schema-introspect.gql", "w", encoding="utf-8"
        ) as outfile:
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
                        errorsReport {{
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
                            errorsReport {{
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
                        errorsReport {{
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
                            errorsReport {{
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
                        errorsReport {{
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
                            errorsReport {{
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
                        errorsReport {{
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
                            errorsReport {{
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
                        errorsReport {{
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
                            errorsReport {{
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
    function_list = queries.get(name_function_list, None)
    text = ""
    if function_list is not None:
        globals()["global_cruddals_strings"][app_name][model_name].update(
            {
                "list": textwrap.dedent(
                    f"""
                query {name_function_list} {{
                    {name_function_list} {{
                        id
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
                    query {name_function_list} {{
                        {name_function_list} {{
                            ${{selectedFields}}
                        }}
                    }}
                `;
                return query;
            }};"""
        text = textwrap.dedent(text)
    return text


def build_search(app_name, model_name, model_name_plural, queries):
    name_function_search = f"search{model_name_plural}"
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
                        indexStart
                        indexEnd
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
            "export const PaginatedType = `\n  total\n  page\n  pages\n  hasNext\n  hasPrev\n  indexStart\n  indexEnd\n`;\n"
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
        internal_text_for_graphiql = ""
        for model_name, strings_cruddals in models.items():
            internal_model_text_for_graphiql = ""
            for string in strings_cruddals.values():
                if string:
                    internal_model_text_for_graphiql += f"{string}"
            if internal_model_text_for_graphiql:
                internal_text_for_graphiql += f"\n#region ============= {model_name.upper()}\n{internal_model_text_for_graphiql}\n#endregion\n"
        if internal_text_for_graphiql:
            text_for_graphiql += f"\n#region ============= {app_name.upper()}\n{internal_text_for_graphiql}\n#endregion\n"
    with open(f"{PATH_CLIENT}/test_in_graphiql.gql", "w+", encoding="utf-8") as file:
        text_for_graphiql = textwrap.dedent(text_for_graphiql)
        file.write(text_for_graphiql)


def build_files_for_client_schema_cruddals(schema, outputPath=None):
    if schema is not None:
        global PATH_ROOT, PATH_CLIENT
        if outputPath:
            PATH_ROOT = outputPath
            PATH_CLIENT = f"{outputPath}/schema_cruddals"
            if not os.path.exists(PATH_ROOT):
                os.mkdir(PATH_ROOT)

            if not os.path.exists(PATH_CLIENT):
                os.mkdir(PATH_CLIENT)

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

            internal_text_queries = ""
            internal_text_mutations = ""

            for model in app.get_models():
                model_name = model.__name__
                model_name_plural = transform_string(
                    model._meta.verbose_name_plural or "", "PascalCase"
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

                if query_read or query_list or query_search:
                    internal_text_queries += f"\n// #region ============= MODEL: {model_name}{query_read}{query_list}{query_search}\n//endregion\n"
                if (
                    mutation_create
                    or mutation_update
                    or mutation_delete
                    or mutation_deactivate
                    or mutation_activate
                ):
                    internal_text_mutations += f"\n// #region ============= MODEL: {model_name}{mutation_create}{mutation_update}{mutation_delete}{mutation_deactivate}{mutation_activate}\n//endregion\n"

            if internal_text_queries:
                text_queries += f"// #region ============= APP: {app_name}\n{internal_text_queries}\n//endregion\n\n"
            if internal_text_mutations:
                text_mutations += f"// #region ============= APP: {app_name}\n{internal_text_mutations}\n//endregion\n\n"

        build_file_general_types()
        build_file_queries(text_queries)
        build_file_mutations(text_mutations)
        build_file_test_in_graphiql()
