"""
Tests comprehensivos para optimización N+1 en campos paginados anidados.

Este archivo contiene tests exhaustivos para validar que la optimización
de campos paginados anidados funciona en todos los escenarios posibles.

Cobertura:
1. OneToOne + campos paginados anidados
2. ForeignKey + campos paginados anidados
3. Múltiples niveles de anidación (3+ niveles)
4. Casos edge: nulls, sin relaciones, múltiples objetos
5. Verificación de inclusión de FK fields en .only()
6. Transversalidad: listModelX, searchModelX, campos anidados
"""

from django.db import connection, reset_queries
from django.test import TestCase, override_settings

from tests.models import ModelC, ModelD, ModelE
from tests.utils import Client


class NestedPaginatedFieldsComprehensiveTestCase(TestCase):
    """Tests comprehensivos para campos paginados anidados."""

    @classmethod
    def setUpTestData(cls):
        """Crear data de prueba con diferentes escenarios."""

        # Escenario 1: ModelC con OneToOne a ModelD (con ModelEs)
        model_d1 = ModelD.objects.create()
        model_c1 = ModelC.objects.create(
            char_field="C1", integer_field=1, one_to_one_field=model_d1
        )
        ModelE.objects.create(foreign_key_field_deep=model_d1)
        ModelE.objects.create(foreign_key_field_deep=model_d1)
        ModelE.objects.create(foreign_key_field_deep=model_d1)

        # Escenario 2: ModelC con OneToOne a ModelD (sin ModelEs)
        model_d2 = ModelD.objects.create()
        ModelC.objects.create(
            char_field="C2", integer_field=2, one_to_one_field=model_d2
        )

        # Escenario 3: ModelC SIN OneToOne (null)
        ModelC.objects.create(char_field="C3", integer_field=3, one_to_one_field=None)

        # Escenario 4: ModelC con OneToOne a ModelD (muchos ModelEs)
        model_d4 = ModelD.objects.create()
        ModelC.objects.create(
            char_field="C4", integer_field=4, one_to_one_field=model_d4
        )
        for _i in range(10):
            ModelE.objects.create(foreign_key_field_deep=model_d4)

        # Escenario 5: ModelD huérfano (sin ModelC, con ForeignKey a ModelC)
        model_d5 = ModelD.objects.create(foreign_key_field=model_c1)
        ModelE.objects.create(foreign_key_field_deep=model_d5)
        ModelE.objects.create(foreign_key_field_deep=model_d5)

    def test_onetoone_nested_paginated_no_n1(self):
        """
        Test: OneToOne + campo paginado anidado NO genera N+1.

        Query:
        searchModelCs {
          oneToOneField {              # OneToOne
            paginatedForeignKeyERelated {  # Campo paginado nested
              objects { id }
            }
          }
        }

        Expectativa:
        - 1 COUNT query
        - 1 SELECT ModelC LEFT JOIN ModelD (select_related)
        - 1 SELECT ModelE WHERE ... IN (...) (prefetch)
        - Total: 3 queries
        """
        client = Client()
        query = """
        query {
            searchModelCs {
                total
                objects {
                    id
                    oneToOneField {
                        id
                        paginatedForeignKeyERelated {
                            objects {
                                id
                            }
                        }
                    }
                }
            }
        }
        """

        with override_settings(DEBUG=True):
            reset_queries()
            response = client.query(query).json()
            queries = connection.queries

            # Validar respuesta
            self.assertIsNone(response.get("errors"))
            data = response["data"]["searchModelCs"]
            self.assertGreater(data["total"], 0)

            # Total de queries debe ser exactamente 3
            self.assertEqual(
                len(queries),
                3,
                f"Expected 3 queries (COUNT + SELECT + Prefetch), got {len(queries)}",
            )

            # Verificar que NO hay queries individuales de ModelE
            individual_e_queries = [
                q
                for q in queries
                if "SELECT" in q["sql"].upper()
                and "modele" in q["sql"].lower()
                and "WHERE" in q["sql"].upper()
                and "IN (" not in q["sql"].upper()  # No es Prefetch
                and "LIMIT 21" in q["sql"].upper()  # Query individual
            ]

            self.assertEqual(
                len(individual_e_queries),
                0,
                f"Found {len(individual_e_queries)} N+1 queries. Should be 0.",
            )

            # Verificar que SÍ hay un Prefetch con IN
            prefetch_queries = [
                q
                for q in queries
                if "modele" in q["sql"].lower() and "IN (" in q["sql"].upper()
            ]
            self.assertEqual(
                len(prefetch_queries),
                1,
                "Should have exactly 1 Prefetch query with IN clause",
            )

            # Verificar que el Prefetch incluye el FK field
            prefetch_sql = prefetch_queries[0]["sql"]
            self.assertIn(
                "foreign_key_field_deep_id",
                prefetch_sql.lower(),
                "Prefetch query should include FK field to prevent deferred queries",
            )

    def test_foreignkey_reverse_nested_paginated_no_n1(self):
        """
        Test: Reverse ForeignKey + campo paginado anidado NO genera N+1.

        Query:
        searchModelCs {
          paginatedForeignKeyDRelated {  # Reverse FK (ModelD.foreign_key_field)
            objects {
              paginatedForeignKeyERelated {  # Campo paginado nested
                objects { id }
              }
            }
          }
        }

        Expectativa: Todas las queries deben usar Prefetch con IN.
        """
        client = Client()
        query = """
        query {
            searchModelCs {
                total
                objects {
                    id
                    paginatedForeignKeyDRelated {
                        objects {
                            id
                            paginatedForeignKeyERelated {
                                objects {
                                    id
                                }
                            }
                        }
                    }
                }
            }
        }
        """

        with override_settings(DEBUG=True):
            reset_queries()
            response = client.query(query).json()
            queries = connection.queries

            # Validar respuesta
            self.assertIsNone(response.get("errors"))

            # Verificar que NO hay queries individuales
            individual_queries = [
                q
                for q in queries
                if "LIMIT 21" in q["sql"].upper()
                and "WHERE" in q["sql"].upper()
                and "IN (" not in q["sql"].upper()
            ]

            self.assertEqual(
                len(individual_queries),
                0,
                f"Found {len(individual_queries)} N+1 queries. Should be 0.",
            )

            # Todas las queries de ModelE deben usar IN
            modele_queries = [
                q
                for q in queries
                if "modele" in q["sql"].lower() and "SELECT" in q["sql"].upper()
            ]

            for q in modele_queries:
                self.assertIn(
                    "IN (",
                    q["sql"].upper(),
                    f"ModelE query should use IN clause:\n{q['sql']}",
                )

    def test_multiple_nesting_levels_no_n1(self):
        """
        Test: Múltiples niveles de anidación (3+ niveles) NO genera N+1.

        Query: ModelC → OneToOne ModelD → Paginated ModelE → FK deep

        Expectativa: Cada nivel debe estar optimizado correctamente.
        """
        client = Client()
        query = """
        query {
            searchModelCs {
                objects {
                    id
                    oneToOneField {
                        id
                        paginatedForeignKeyERelated {
                            objects {
                                id
                                foreignKeyFieldDeep {
                                    id
                                }
                            }
                        }
                    }
                }
            }
        }
        """

        with override_settings(DEBUG=True):
            reset_queries()
            response = client.query(query).json()
            queries = connection.queries

            # Validar respuesta
            self.assertIsNone(response.get("errors"))

            # Verificar que NO hay queries individuales
            individual_queries = [
                q
                for q in queries
                if "LIMIT 21" in q["sql"].upper()
                and "WHERE" in q["sql"].upper()
                and "IN (" not in q["sql"].upper()
            ]

            if individual_queries:
                print("Found N+1 queries in multi-level nesting:")
                for i, q in enumerate(individual_queries[:5], 1):
                    print(f"{i}. {q['sql'][:150]}...")

            self.assertEqual(
                len(individual_queries),
                0,
                "Multi-level nesting should not generate N+1 queries",
            )

    def test_null_relations_handled_correctly(self):
        """
        Test: Relaciones NULL no causan errores ni queries extras.

        Escenario: ModelC sin one_to_one_field (null)

        Expectativa:
        - No debe causar errores
        - No debe ejecutar queries adicionales para objetos null
        """
        client = Client()
        query = """
        query {
            searchModelCs(where: { charField: { exact: "C3" } }) {
                objects {
                    id
                    charField
                    oneToOneField {
                        id
                        paginatedForeignKeyERelated {
                            objects {
                                id
                            }
                        }
                    }
                }
            }
        }
        """

        with override_settings(DEBUG=True):
            reset_queries()
            response = client.query(query).json()
            queries = connection.queries

            # Validar respuesta
            self.assertIsNone(response.get("errors"))
            data = response["data"]["searchModelCs"]["objects"]

            # Debe encontrar C3
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["charField"], "C3")

            # oneToOneField debe ser null
            self.assertIsNone(data[0]["oneToOneField"])

            # No debe haber queries de ModelE (porque no hay relación)
            modele_queries = [q for q in queries if "modele" in q["sql"].lower()]

            # Puede haber 0 o 1 query de ModelE (Prefetch puede ejecutarse aunque no haya datos)
            # Lo importante es que NO haya queries individuales
            individual_e_queries = [
                q
                for q in modele_queries
                if "LIMIT 21" in q["sql"].upper() and "IN (" not in q["sql"].upper()
            ]

            self.assertEqual(
                len(individual_e_queries),
                0,
                "NULL relations should not trigger individual queries",
            )

    def test_list_query_uses_optimization(self):
        """
        Test: listModelCs también usa la optimización (transversalidad).

        Verifica que la optimización NO es solo para searchModelCs,
        sino que aplica a TODOS los resolvers que usan _queryset_factory.
        """
        client = Client()
        query = """
        query {
            listModelCs {
                id
                oneToOneField {
                    id
                    paginatedForeignKeyERelated {
                        objects {
                            id
                        }
                    }
                }
            }
        }
        """

        with override_settings(DEBUG=True):
            reset_queries()
            response = client.query(query).json()
            queries = connection.queries

            # Validar respuesta
            self.assertIsNone(response.get("errors"))

            # Verificar que NO hay queries individuales
            individual_e_queries = [
                q
                for q in queries
                if "SELECT" in q["sql"].upper()
                and "modele" in q["sql"].lower()
                and "LIMIT 21" in q["sql"].upper()
                and "IN (" not in q["sql"].upper()
            ]

            self.assertEqual(
                len(individual_e_queries),
                0,
                f"listModelCs should also use optimization. Found {len(individual_e_queries)} N+1 queries.",
            )

    def test_fk_fields_included_in_only(self):
        """
        Test: Campos FK se incluyen automáticamente en .only()

        Verifica que cuando se usa .only(), los campos FK se agregan
        automáticamente para evitar deferred field queries.

        Expectativa: El Prefetch de ModelE debe incluir 'foreign_key_field_deep_id'
        en el SELECT, no solo 'id'.
        """
        client = Client()
        query = """
        query {
            searchModelCs {
                objects {
                    id
                    oneToOneField {
                        id
                        paginatedForeignKeyERelated {
                            objects {
                                id
                                foreignKeyFieldDeep {
                                    id
                                }
                            }
                        }
                    }
                }
            }
        }
        """

        with override_settings(DEBUG=True):
            reset_queries()
            response = client.query(query).json()
            queries = connection.queries

            # Validar respuesta
            self.assertIsNone(response.get("errors"))

            # Buscar el Prefetch de ModelE
            modele_prefetch = [
                q
                for q in queries
                if "modele" in q["sql"].lower() and "IN (" in q["sql"].upper()
            ]

            self.assertGreater(
                len(modele_prefetch),
                0,
                "Should have at least one ModelE Prefetch query",
            )

            # Verificar que el Prefetch incluye el FK field
            prefetch_sql = modele_prefetch[0]["sql"]

            # Debe tener ambos: id Y foreign_key_field_deep_id
            self.assertIn(
                '"tests_modele"."id"', prefetch_sql, "Prefetch should select 'id' field"
            )
            self.assertIn(
                "foreign_key_field_deep_id",
                prefetch_sql.lower(),
                "Prefetch should select FK field to prevent deferred queries",
            )

            # NO debe haber queries adicionales de ModelE para obtener el FK
            individual_e_for_fk = [
                q
                for q in queries
                if "modele" in q["sql"].lower()
                and "WHERE" in q["sql"].upper()
                and q not in modele_prefetch
            ]

            self.assertEqual(
                len(individual_e_for_fk),
                0,
                f"FK fields should be loaded in Prefetch. Found {len(individual_e_for_fk)} deferred field queries.",
            )

    def test_empty_paginated_relation_no_errors(self):
        """
        Test: Relación paginada vacía (sin objetos) no causa errores.

        Escenario: ModelD sin ModelE relacionados

        Expectativa:
        - No debe causar errores
        - Debe devolver lista vacía
        - No debe ejecutar queries individuales
        """
        client = Client()
        query = """
        query {
            searchModelCs(where: { charField: { exact: "C2" } }) {
                objects {
                    id
                    oneToOneField {
                        id
                        paginatedForeignKeyERelated {
                            total
                            objects {
                                id
                            }
                        }
                    }
                }
            }
        }
        """

        with override_settings(DEBUG=True):
            reset_queries()
            response = client.query(query).json()
            queries = connection.queries

            # Validar respuesta
            self.assertIsNone(response.get("errors"))
            data = response["data"]["searchModelCs"]["objects"]

            # Debe encontrar C2
            self.assertEqual(len(data), 1)

            # Debe tener oneToOneField pero sin ModelE
            self.assertIsNotNone(data[0]["oneToOneField"])
            paginated = data[0]["oneToOneField"]["paginatedForeignKeyERelated"]
            self.assertEqual(paginated["total"], 0)
            self.assertEqual(len(paginated["objects"]), 0)

            # No debe haber queries individuales
            individual_queries = [
                q
                for q in queries
                if "LIMIT 21" in q["sql"].upper() and "IN (" not in q["sql"].upper()
            ]

            self.assertEqual(
                len(individual_queries),
                0,
                "Empty paginated relations should not trigger individual queries",
            )

    def test_many_objects_with_nested_pagination(self):
        """
        Test: Múltiples objetos con paginación anidada NO genera N+1.

        Escenario: ModelC4 tiene 10 ModelE relacionados

        Expectativa:
        - Todas las queries deben usar IN
        - NO debe haber 10 queries individuales
        """
        client = Client()
        query = """
        query {
            searchModelCs(where: { charField: { exact: "C4" } }) {
                objects {
                    id
                    oneToOneField {
                        id
                        paginatedForeignKeyERelated {
                            total
                            objects {
                                id
                            }
                        }
                    }
                }
            }
        }
        """

        with override_settings(DEBUG=True):
            reset_queries()
            response = client.query(query).json()
            queries = connection.queries

            # Validar respuesta
            self.assertIsNone(response.get("errors"))
            data = response["data"]["searchModelCs"]["objects"]

            # Debe encontrar C4
            self.assertEqual(len(data), 1)

            # Debe tener 10 ModelE
            paginated = data[0]["oneToOneField"]["paginatedForeignKeyERelated"]
            self.assertEqual(paginated["total"], 10)

            # NO debe haber queries individuales (10 queries serían N+1)
            individual_queries = [
                q
                for q in queries
                if "modele" in q["sql"].lower()
                and "LIMIT 21" in q["sql"].upper()
                and "IN (" not in q["sql"].upper()
            ]

            self.assertEqual(
                len(individual_queries),
                0,
                f"Should use Prefetch, not {len(individual_queries)} individual queries",
            )

    def test_query_count_consistency(self):
        """
        Test: El número de queries es consistente independiente de la cantidad de datos.

        Compara queries con 1 objeto vs 4 objetos.
        El número debe ser el mismo (no crecer linealmente = N+1).
        """
        client = Client()

        # Query 1: Solo un objeto
        query_one = """
        query {
            searchModelCs(where: { charField: { exact: "C1" } }) {
                objects {
                    id
                    oneToOneField {
                        id
                        paginatedForeignKeyERelated {
                            objects { id }
                        }
                    }
                }
            }
        }
        """

        with override_settings(DEBUG=True):
            reset_queries()
            client.query(query_one)
            queries_one_object = len(connection.queries)

        # Query 2: Múltiples objetos
        query_many = """
        query {
            searchModelCs {
                objects {
                    id
                    oneToOneField {
                        id
                        paginatedForeignKeyERelated {
                            objects { id }
                        }
                    }
                }
            }
        }
        """

        with override_settings(DEBUG=True):
            reset_queries()
            client.query(query_many)
            queries_many_objects = len(connection.queries)

        # El número de queries debe ser el mismo o muy cercano
        # (puede variar en ±1 por diferencias en filtros/counts)
        difference = abs(queries_many_objects - queries_one_object)

        self.assertLessEqual(
            difference,
            1,
            f"Query count should be constant. 1 object: {queries_one_object}, "
            f"many objects: {queries_many_objects}. Difference: {difference}",
        )

    def test_read_query_uses_optimization(self):
        """
        Test: readModelC también usa la optimización (transversalidad).

        Aunque readModelC retorna UN solo objeto, si ese objeto tiene
        campos paginados anidados, esos SÍ deben estar optimizados.

        Query: readModelC(where: {id: X}) { oneToOneField { paginatedForeignKeyERelated } }

        Expectativa:
        - 1 SELECT ModelC LEFT JOIN ModelD (select_related)
        - 1 SELECT ModelE WHERE ... IN (...) (prefetch)
        - Total: 2 queries (no hay COUNT porque no es paginado el resultado principal)
        """
        client = Client()

        # Obtener el ID de C1 para usar en readModelC
        model_c1 = ModelC.objects.filter(char_field="C1").first()

        query = f"""
        query {{
            readModelC(where: {{ id: {{exact: {model_c1.id}}} }}) {{
                id
                charField
                oneToOneField {{
                    id
                    paginatedForeignKeyERelated {{
                        total
                        objects {{
                            id
                            foreignKeyFieldDeep {{
                                id
                            }}
                        }}
                    }}
                }}
            }}
        }}
        """

        with override_settings(DEBUG=True):
            reset_queries()
            response = client.query(query).json()
            queries = connection.queries

            # Validar respuesta
            self.assertIsNone(response.get("errors"))
            data = response["data"]["readModelC"]

            # Debe retornar C1
            self.assertEqual(data["charField"], "C1")
            self.assertIsNotNone(data["oneToOneField"])

            # Verificar que NO hay queries individuales de ModelE
            individual_e_queries = [
                q
                for q in queries
                if "SELECT" in q["sql"].upper()
                and "modele" in q["sql"].lower()
                and "LIMIT 21" in q["sql"].upper()
                and "IN (" not in q["sql"].upper()
            ]

            if individual_e_queries:
                print("Found N+1 queries in readModelC:")
                for i, q in enumerate(individual_e_queries[:3], 1):
                    print(f"{i}. {q['sql'][:150]}...")

            self.assertEqual(
                len(individual_e_queries),
                0,
                f"readModelC should use optimization. Found {len(individual_e_queries)} N+1 queries.",
            )

            # Verificar que SÍ hay un Prefetch con IN
            prefetch_queries = [
                q
                for q in queries
                if "modele" in q["sql"].lower() and "IN (" in q["sql"].upper()
            ]

            self.assertGreaterEqual(
                len(prefetch_queries),
                1,
                "Should have at least 1 Prefetch query with IN clause for ModelE",
            )

            # Verificar que el Prefetch incluye FK fields
            if prefetch_queries:
                prefetch_sql = prefetch_queries[0]["sql"]
                self.assertIn(
                    "foreign_key_field_deep_id",
                    prefetch_sql.lower(),
                    "Prefetch should include FK field",
                )

            # Total de queries debe ser razonable (2-3 queries)
            # 1 SELECT principal + 1-2 Prefetch
            self.assertLessEqual(
                len(queries),
                3,
                f"readModelC should have ≤3 queries, got {len(queries)}",
            )
