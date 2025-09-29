import json

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

debug_fragment = """
    fragment debugType on DjangoDebug {
        sql {
            vendor
            alias
            sql
            duration
            rawSql
            params
            startTime
            stopTime
            isSlow
            isSelect
            transId
            transStatus
            isoLevel
            encoding
        }
        exceptions {
            excType
            message
            stack
        }
    }
"""


# region CRUDDALS ModelC
search_model_c_query = (
    debug_fragment
    + pagination_fragment
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
        _debug {
            ...debugType
        }
    }
"""
)
# endregion

# region CRUDDALS ModelD
search_model_d_query = (
    debug_fragment
    + pagination_fragment
    + model_d_fragment
    + """
    query searchModelDs($where: FilterModelDInput $orderBy: OrderByModelDInput $paginationConfig: PaginationConfigInput) {
        searchModelDs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig) {
            ...paginationType
            objects {
                ...modelDType
            }
        }
        _debug {
            ...debugType
        }
    }
"""
)
# endregion

# region CRUDDALS ModelE
search_model_e_query = (
    debug_fragment
    + pagination_fragment
    + model_e_fragment
    + """
    query searchModelEs($where: FilterModelEInput $orderBy: OrderByModelEInput $paginationConfig: PaginationConfigInput) {
        searchModelEs(where: $where orderBy: $orderBy paginationConfig: $paginationConfig) {
            ...paginationType
            objects {
                ...modelEType
            }
        }
        _debug {
            ...debugType
        }
    }
"""
)
# endregion


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

        from django.db import connection, reset_queries
        from django.test.utils import override_settings

        with override_settings(DEBUG=True):
            connection.queries_log.clear()
            reset_queries()

            # print("search_model_c_query", search_model_c_query)
            graphql_response = client.query(search_model_c_query).json()

            graphql_queries = len(connection.queries)
            print(f"GraphQL ejecutó {graphql_queries} consultas SQL")

            # print("graphql_response", graphql_response)
            j = json.dumps(graphql_response, indent=4)
            with open("gql_response.json", "w") as f:
                f.write(j)
            # print("gql response json", j)
            # graphql_queries deberia de ser 10
            self.assertEqual(graphql_queries, 10)
            print("========")

            # connection.queries_log.clear()
            # reset_queries()
            # cache.clear()

            # page = 4
            # items_per_page = 3
            # queryset = (
            #     ModelC.objects
            #     .select_related("one_to_one_field__foreign_key_field")
            #     .prefetch_related(
            #         Prefetch(
            #             "many_to_many_field",
            #             queryset=ModelD.objects.select_related("foreign_key_field")
            #             .prefetch_related(
            #                 Prefetch(
            #                     "foreign_key_E_related",
            #                     queryset=ModelE.objects.select_related("foreign_key_field_deep__foreign_key_field")
            #                 )
            #             )
            #         ),
            #         Prefetch(
            #             "foreign_key_D_related",
            #             queryset=ModelD.objects.only("id")
            #         )
            #     )
            #     .all()
            # )
            # paginator = Paginator(queryset, items_per_page)
            # page_obj = paginator.get_page(page)
            # django_objects = []
            # for obj in page_obj:
            #     one_to_one_data = None
            #     if obj.one_to_one_field:
            #         one_to_one_data = {
            #             "id": str(obj.one_to_one_field.id),
            #             "foreignKeyField": {
            #                 "id": str(obj.one_to_one_field.foreign_key_field.id)
            #             },
            #             "paginatedForeignKeyERelated": {
            #                 "objects": [
            #                     {
            #                         "id": str(e_obj.id),
            #                         "foreignKeyFieldDeep": {
            #                             "id": str(e_obj.foreign_key_field_deep.id),
            #                             "foreignKeyField": {
            #                                 "id": str(
            #                                     e_obj.foreign_key_field_deep.foreign_key_field.id
            #                                 )
            #                             },
            #                         },
            #                     }
            #                     for e_obj in obj.one_to_one_field.foreign_key_E_related.all()
            #                 ]
            #             },
            #         }

            #     many_to_many_data = {
            #         "objects": [
            #             {
            #                 "id": str(m2m_obj.id),
            #                 "foreignKeyField": {
            #                     "id": str(m2m_obj.foreign_key_field.id)
            #                 },
            #                 "paginatedForeignKeyERelated": {
            #                     "objects": [
            #                         {
            #                             "id": str(e_obj.id),
            #                             "foreignKeyFieldDeep": {
            #                                 "id": str(e_obj.foreign_key_field_deep.id),
            #                                 "foreignKeyField": {
            #                                     "id": str(
            #                                         e_obj.foreign_key_field_deep.foreign_key_field.id
            #                                     )
            #                                 },
            #                             },
            #                         }
            #                         for e_obj in m2m_obj.foreign_key_E_related.all()
            #                     ]
            #                 },
            #             }
            #             for m2m_obj in obj.many_to_many_field.all()
            #         ]
            #     }

            #     foreign_key_d_data = {
            #         "objects": [
            #             {"id": str(fk_obj.id)}
            #             for fk_obj in obj.foreign_key_D_related.all()
            #         ]
            #     }

            #     serialized_obj = {
            #         "id": str(obj.id),
            #         "charField": obj.char_field,
            #         "integerField": obj.integer_field,
            #         "booleanField": obj.boolean_field,
            #         "dateTimeField": obj.date_time_field.isoformat() + "+00:00"
            #         if obj.date_time_field
            #         else None,
            #         "jsonField": f'"{obj.json_field}"' if obj.json_field else None,
            #         "fileField": str(obj.file_field) if obj.file_field else "",
            #         "isActive": obj.is_active,
            #         "oneToOneField": one_to_one_data,
            #         "paginatedManyToManyField": many_to_many_data,
            #         "paginatedForeignKeyDRelated": foreign_key_d_data,
            #     }
            #     django_objects.append(serialized_obj)
            # _django_response = {
            #     "searchModelCs": {
            #         "total": paginator.count,
            #         "page": page,
            #         "pages": paginator.num_pages,
            #         "hasNext": page_obj.has_next(),
            #         "hasPrev": page_obj.has_previous(),
            #         "indexStart": page_obj.start_index(),
            #         "indexEnd": page_obj.end_index(),
            #         "objects": django_objects,
            #     }
            # }

            # django_queries = len(connection.queries)  # - graphql_queries
            # print(f"Django ejecutó {django_queries} consultas SQL")

            # graphql_objects = graphql_response["data"]["searchModelCs"]["objects"]
            # print(f"GraphQL devolvió {len(graphql_objects)} objetos")
            # print(f"Django devolvió {len(django_objects)} objetos")

            # # Verificar que los IDs coincidan
            # graphql_ids = [obj["id"] for obj in graphql_objects]
            # django_ids = [obj["id"] for obj in django_objects]
            # print(f"IDs GraphQL: {graphql_ids}")
            # print(f"IDs Django: {django_ids}")
            # print(f"IDs coinciden: {graphql_ids == django_ids}")
        # endregion
