from django.core.paginator import Paginator
from django.db import connection, reset_queries
from django.test.utils import override_settings

from tests.models import ModelC, ModelD, ModelE
from tests.utils import Client, SchemaTestCase

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
        foreignKeyFieldDeep {
            id
            foreignKeyField { id }
            oneToOneCRelated { id }
            paginatedManyToManyCRelated { objects {id} }
            paginatedForeignKeyERelated { objects {id} }
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
        indexStart
        indexEnd
    }
"""


# region CRUDDALS ModelC
get_all_model_c_objects_without_relations_query = (
    pagination_fragment
    + """
    query searchModelCs($where: FilterModelCInput $orderBy: OrderByModelCInput $paginationConfig: PaginationConfigInput) {
        searchModelCs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig) {
            ...paginationType
            objects {
                id
                charField
                integerField
                booleanField
                dateTimeField
                jsonField
                fileField
                isActive
            }
        }
    }
"""
)

get_all_model_c_objects_with_many_to_many_relation_with_order_by = (
    pagination_fragment
    + """
    query searchModelCs($where: FilterModelCInput $orderBy: OrderByModelCInput $paginationConfig: PaginationConfigInput) {
        searchModelCs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig) {
            ...paginationType
            objects {
                id
                charField
                paginatedManyToManyField(orderBy: {foreignKeyField: {id: DESC}}) {
                    objects {
                        id
                        foreignKeyField {
                            id
                        }
                    }
                }
            }
        }
    }
"""
)

get_all_model_c_objects_with_many_to_many_relation_with_where = (
    pagination_fragment
    + """
    query searchModelCs($where: FilterModelCInput $orderBy: OrderByModelCInput $paginationConfig: PaginationConfigInput) {
        searchModelCs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig) {
            ...paginationType
            objects {
                id
                charField
                paginatedManyToManyField(where: {foreignKeyField: {id: {in: [1,2]}}}) {
                    objects {
                        id
                        foreignKeyField {
                            id
                        }
                    }
                }
            }
        }
    }
"""
)

search_model_c_query = (
    pagination_fragment
    + """
    query searchModelCs($where: FilterModelCInput $orderBy: OrderByModelCInput $paginationConfig: PaginationConfigInput) {
        searchModelCs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig) {
            ...paginationType
            objects {
                id
                charField
                integerField
                booleanField
                dateTimeField
                jsonField
                fileField
                isActive
                oneToOneField {
                    id
                    foreignKeyField {
                        id
                    }
                    paginatedForeignKeyERelated {
                        objects {
                            id
                            foreignKeyFieldDeep {
                                id
                                foreignKeyField {
                                    id
                                }
                            }
                        }
                    }
                }
                paginatedManyToManyField {
                    objects {
                        id
                        foreignKeyField {
                            id
                        }
                        paginatedForeignKeyERelated {
                            objects {
                                id
                                foreignKeyFieldDeep {
                                    id
                                    foreignKeyField {
                                        id
                                    }
                                }
                            }
                        }
                    }
                }
                paginatedForeignKeyDRelated { objects { id } }
            }
        }
    }
"""
)
# endregion

# region CRUDDALS ModelD
search_model_d_query = (
    pagination_fragment
    + model_d_fragment
    + """
    query searchModelDs($where: FilterModelDInput $orderBy: OrderByModelDInput $paginationConfig: PaginationConfigInput) {
        searchModelDs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig) {
            ...paginationType
            objects {
                ...modelDType
            }
        }
    }
"""
)
# endregion

# region CRUDDALS ModelE
search_model_e_query = (
    pagination_fragment
    + model_e_fragment
    + """
    query searchModelEs($where: FilterModelEInput $orderBy: OrderByModelEInput $paginationConfig: PaginationConfigInput) {
        searchModelEs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig) {
            ...paginationType
            objects {
                ...modelEType
            }
        }
    }
"""
)
# endregion


def get_all_model_c_objects_without_relations():
    connection.queries_log.clear()
    reset_queries()
    qs = (
        ModelC.objects.all()
        .only(
            "id",
            "char_field",
            "integer_field",
            "boolean_field",
            "date_time_field",
            "json_field",
            "file_field",
            "is_active",
        )
        .distinct()
        .order_by("id")
    )
    p = Paginator(qs, 12)
    page_obj = p.page(1)
    list(page_obj.object_list)
    django_queries = len(connection.queries)
    return django_queries


def get_all_model_c_objects_with_relation_one_to_one():
    connection.queries_log.clear()
    reset_queries()
    qs = (
        ModelC.objects.all()
        .select_related("one_to_one_field__foreign_key_field")
        .prefetch_related(
            "many_to_many_field__foreign_key_field__foreign_key_E_related",
            "foreign_key_D_related",
        )
        .only(
            "id",
            "char_field",
            "integer_field",
            "boolean_field",
            "date_time_field",
            "json_field",
            "file_field",
            "is_active",
        )
        .distinct()
        .order_by("id")
    )
    p = Paginator(qs, 12)
    page_obj = p.page(1)
    list(page_obj.object_list)
    django_queries = len(connection.queries)
    return django_queries


class CruddalsModelSchemaTestResolvers(SchemaTestCase):
    def test_cruddals_model_c(self):
        client = Client()

        # region CREATE ModelC
        mc1 = ModelC(
            char_field="AAA",
            integer_field=1,
            boolean_field=True,
            date_time_field="2021-01-01T00:00:00+00:00",
            json_field='{"key1": "value"}',
            file_field="",
            one_to_one_field=None,
            is_active=True,
        )
        mc1.save()
        mc2 = ModelC(
            char_field="BBB",
            integer_field=2,
            boolean_field=False,
            date_time_field="2021-02-02T00:00:00+00:00",
            json_field='{"key2": "value"}',
            file_field="",
            one_to_one_field=None,
            is_active=True,
        )
        mc2.save()
        mc3 = ModelC(
            char_field="CCC",
            integer_field=3,
            boolean_field=True,
            date_time_field="2021-03-03T00:00:00+00:00",
            json_field='{"key3": "value"}',
            file_field="",
            one_to_one_field=None,
            is_active=True,
        )
        mc3.save()
        mc4 = ModelC(
            char_field="DDD",
            integer_field=4,
            boolean_field=False,
            date_time_field="2021-04-04T00:00:00+00:00",
            json_field='{"key4": "value"}',
            file_field="",
            one_to_one_field=None,
            is_active=True,
        )
        mc4.save()
        mc5 = ModelC(
            char_field="EEE",
            integer_field=5,
            boolean_field=True,
            date_time_field="2021-05-05T00:00:00+00:00",
            json_field='{"key5": "value"}',
            file_field="",
            one_to_one_field=None,
            is_active=True,
        )
        mc5.save()
        mc6 = ModelC(
            char_field="aaa",
            integer_field=1,
            boolean_field=True,
            date_time_field="2022-01-01T00:00:00+00:00",
            json_field='{"key6": "value"}',
            file_field="",
            one_to_one_field=None,
            is_active=True,
        )
        mc6.save()
        mc7 = ModelC(
            char_field="bbb",
            integer_field=2,
            boolean_field=False,
            date_time_field="2022-02-02T00:00:00+00:00",
            json_field='{"key7": "value"}',
            file_field="",
            one_to_one_field=None,
            is_active=True,
        )
        mc7.save()
        mc8 = ModelC(
            char_field="ccc",
            integer_field=3,
            boolean_field=True,
            date_time_field="2022-03-03T00:00:00+00:00",
            json_field='{"key8": "value"}',
            file_field="",
            one_to_one_field=None,
            is_active=True,
        )
        mc8.save()
        mc9 = ModelC(
            char_field="ddd",
            integer_field=4,
            boolean_field=False,
            date_time_field="2022-04-04T00:00:00+00:00",
            json_field='{"key9": "value"}',
            file_field="",
            one_to_one_field=None,
            is_active=True,
        )
        mc9.save()
        mc10 = ModelC(
            char_field="eee",
            integer_field=5,
            boolean_field=True,
            date_time_field="2022-05-05T00:00:00+00:00",
            json_field='{"key10": "value"}',
            file_field="",
            one_to_one_field=None,
            is_active=True,
        )
        mc10.save()
        # endregion

        # region CREATE ModelD
        md1 = ModelD(foreign_key_field=mc1)
        md1.save()

        # model c with one to one relation to md1
        mc11 = ModelC(
            char_field="AAA1",
            integer_field=1,
            boolean_field=True,
            date_time_field="2021-01-01T00:00:00+00:00",
            json_field='{"key11": "value"}',
            file_field="",
            one_to_one_field=md1,
            is_active=True,
        )
        mc11.save()

        md2 = ModelD(foreign_key_field=mc2)
        md2.save()
        md3 = ModelD(foreign_key_field=mc3)
        md3.save()
        md4 = ModelD(foreign_key_field=mc4)
        md4.save()

        # model c with many to many relation to md1, md2, md3
        mc12 = ModelC(
            char_field="AAA2",
            integer_field=1,
            boolean_field=True,
            date_time_field="2021-01-01T00:00:00+00:00",
            json_field='{"key12": "value"}',
            file_field="",
            one_to_one_field=None,
            is_active=True,
        )
        mc12.save()
        mc12.many_to_many_field.set([md1, md2, md3])
        mc12.save()
        # endregion

        # region CREATE ModelE
        me1 = ModelE(foreign_key_field_deep=md1)
        me1.save()
        me2 = ModelE(foreign_key_field_deep=md2)
        me2.save()
        # endregion

        # region SEARCH ModelC

        with override_settings(DEBUG=True):
            django_queries = get_all_model_c_objects_without_relations()
            connection.queries_log.clear()
            reset_queries()
            client.query(get_all_model_c_objects_without_relations_query).json()
            graphql_queries = len(connection.queries)
            self.assertLessEqual(graphql_queries, django_queries)

            # region SEARCH ModelC with order by DESC in internal field: many to many
            expected_response = {
                "data": {
                    "searchModelCs": {
                        "total": 12,
                        "page": 1,
                        "pages": 1,
                        "hasNext": False,
                        "hasPrev": False,
                        "indexStart": 1,
                        "indexEnd": 12,
                        "objects": [
                            {
                                "id": "1",
                                "charField": "AAA",
                                "paginatedManyToManyField": {"objects": []},
                            },
                            {
                                "id": "2",
                                "charField": "BBB",
                                "paginatedManyToManyField": {"objects": []},
                            },
                            {
                                "id": "3",
                                "charField": "CCC",
                                "paginatedManyToManyField": {"objects": []},
                            },
                            {
                                "id": "4",
                                "charField": "DDD",
                                "paginatedManyToManyField": {"objects": []},
                            },
                            {
                                "id": "5",
                                "charField": "EEE",
                                "paginatedManyToManyField": {"objects": []},
                            },
                            {
                                "id": "6",
                                "charField": "aaa",
                                "paginatedManyToManyField": {"objects": []},
                            },
                            {
                                "id": "7",
                                "charField": "bbb",
                                "paginatedManyToManyField": {"objects": []},
                            },
                            {
                                "id": "8",
                                "charField": "ccc",
                                "paginatedManyToManyField": {"objects": []},
                            },
                            {
                                "id": "9",
                                "charField": "ddd",
                                "paginatedManyToManyField": {"objects": []},
                            },
                            {
                                "id": "10",
                                "charField": "eee",
                                "paginatedManyToManyField": {"objects": []},
                            },
                            {
                                "id": "11",
                                "charField": "AAA1",
                                "paginatedManyToManyField": {"objects": []},
                            },
                            {
                                "id": "12",
                                "charField": "AAA2",
                                "paginatedManyToManyField": {
                                    "objects": [
                                        {"id": "3", "foreignKeyField": {"id": "3"}},
                                        {"id": "2", "foreignKeyField": {"id": "2"}},
                                        {"id": "1", "foreignKeyField": {"id": "1"}},
                                    ]
                                },
                            },
                        ],
                    }
                }
            }
            connection.queries_log.clear()
            reset_queries()
            response = client.query(
                get_all_model_c_objects_with_many_to_many_relation_with_order_by
            ).json()
            graphql_queries = len(connection.queries)
            self.assertLessEqual(graphql_queries, 3)
            self.verify_response(
                response,
                expected_response,
                message="SEARCH with order by DESC in internal field: many to many ModelC",
            )
            # endregion

            # region SEARCH ModelC with where in internal field: many to many
            expected_response = {
                "data": {
                    "searchModelCs": {
                        "total": 12,
                        "page": 1,
                        "pages": 1,
                        "hasNext": False,
                        "hasPrev": False,
                        "indexStart": 1,
                        "indexEnd": 12,
                        "objects": [
                            {
                                "id": "1",
                                "charField": "AAA",
                                "paginatedManyToManyField": {"objects": []},
                            },
                            {
                                "id": "2",
                                "charField": "BBB",
                                "paginatedManyToManyField": {"objects": []},
                            },
                            {
                                "id": "3",
                                "charField": "CCC",
                                "paginatedManyToManyField": {"objects": []},
                            },
                            {
                                "id": "4",
                                "charField": "DDD",
                                "paginatedManyToManyField": {"objects": []},
                            },
                            {
                                "id": "5",
                                "charField": "EEE",
                                "paginatedManyToManyField": {"objects": []},
                            },
                            {
                                "id": "6",
                                "charField": "aaa",
                                "paginatedManyToManyField": {"objects": []},
                            },
                            {
                                "id": "7",
                                "charField": "bbb",
                                "paginatedManyToManyField": {"objects": []},
                            },
                            {
                                "id": "8",
                                "charField": "ccc",
                                "paginatedManyToManyField": {"objects": []},
                            },
                            {
                                "id": "9",
                                "charField": "ddd",
                                "paginatedManyToManyField": {"objects": []},
                            },
                            {
                                "id": "10",
                                "charField": "eee",
                                "paginatedManyToManyField": {"objects": []},
                            },
                            {
                                "id": "11",
                                "charField": "AAA1",
                                "paginatedManyToManyField": {"objects": []},
                            },
                            {
                                "id": "12",
                                "charField": "AAA2",
                                "paginatedManyToManyField": {
                                    "objects": [
                                        {"id": "1", "foreignKeyField": {"id": "1"}},
                                        {"id": "2", "foreignKeyField": {"id": "2"}},
                                    ]
                                },
                            },
                        ],
                    }
                }
            }
            connection.queries_log.clear()
            reset_queries()
            response = client.query(
                get_all_model_c_objects_with_many_to_many_relation_with_where
            ).json()
            graphql_queries = len(connection.queries)
            self.assertLessEqual(graphql_queries, 3)
            self.verify_response(
                response,
                expected_response,
                message="SEARCH with where in internal field: many to many ModelC",
            )
            # endregion
            print("================================================")
        # endregion
