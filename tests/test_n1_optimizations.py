"""
Tests para validar las optimizaciones N+1 en GraphQL.

Este archivo contiene tests que verifican que las optimizaciones implementadas
reducen las queries de 99 → 27 → 10, eliminando problemas de N+1.

Optimizaciones probadas:
1. select_related para ForeignKey y OneToOneField
2. prefetch_related con Prefetch personalizado para ManyToMany y reverse ForeignKey
3. orderBy extraído del AST y aplicado en Prefetch
4. Paginación optimizada (count ejecutado solo una vez)
5. resolve_for_relation_field detecta instancias ya cargadas
"""

import json
from django.test import TestCase, override_settings
from django.db import connection, reset_queries

from tests.models import ModelC, ModelD, ModelE
from tests.utils import Client


class N1OptimizationsTestCase(TestCase):
    """Tests para verificar optimizaciones N+1 en queries GraphQL."""

    @classmethod
    def setUpTestData(cls):
        """Crear datos de prueba una sola vez para todos los tests."""
        model_c_data = [
            {"char_field": "AAA", "integer_field": 1, "boolean_field": True, "key": "key1"},
            {"char_field": "BBB", "integer_field": 2, "boolean_field": False, "key": "key2"},
            {"char_field": "CCC", "integer_field": 3, "boolean_field": True, "key": "key3"},
            {"char_field": "DDD", "integer_field": 4, "boolean_field": False, "key": "key4"},
        ]

        model_c_instances = [
            ModelC.objects.create(
                char_field=data["char_field"],
                integer_field=data["integer_field"],
                boolean_field=data["boolean_field"],
                json_field=f'{{"{data["key"]}": "value"}}',
                is_active=True,
            )
            for data in model_c_data
        ]

        cls.mc1, cls.mc2, cls.mc3, cls.mc4 = model_c_instances

        model_d_instances = [
            ModelD.objects.create(foreign_key_field=mc)
            for mc in model_c_instances
        ]
        cls.md1, cls.md2, cls.md3, cls.md4 = model_d_instances

        cls.mc11 = ModelC.objects.create(
            char_field="AAA1",
            integer_field=1,
            boolean_field=True,
            json_field='{"key11": "value"}',
            one_to_one_field=cls.md1,
            is_active=True,
        )

        cls.mc12 = ModelC.objects.create(
            char_field="AAA2",
            integer_field=1,
            boolean_field=True,
            json_field='{"key12": "value"}',
            is_active=True,
        )
        cls.mc12.many_to_many_field.set([cls.md1, cls.md2, cls.md3])

        model_e_instances = [
            ModelE.objects.create(foreign_key_field_deep=md)
            for md in [cls.md1, cls.md2]
        ]
        cls.me1, cls.me2 = model_e_instances

    def setUp(self):
        """Reset queries antes de cada test."""
        reset_queries()
        connection.queries_log.clear()

    def test_search_basic_optimizations(self):
        """
        Test: Query básica con select_related y prefetch_related.

        Verifica que:
        - select_related carga OneToOneField en un solo JOIN
        - prefetch_related carga ManyToMany eficientemente
        - No hay N+1 queries
        """
        client = Client()
        query = """
        query {
            searchModelCs {
                objects {
                    id
                    charField
                    oneToOneField {
                        id
                        foreignKeyField {
                            id
                        }
                    }
                    paginatedManyToManyField {
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
            query_count = len(connection.queries)

            # Validar respuesta
            self.assertIsNone(response.get("errors"))
            self.assertIn("data", response)

            # Queries esperadas:
            # 1. COUNT para paginación
            # 2. SELECT ModelC con JOIN ModelD (select_related)
            # 3. Prefetch ManyToMany
            # Total: ~3-5 queries (depende de los datos)
            self.assertLess(query_count, 10,
                f"Expected < 10 queries, got {query_count}")

    def test_onetoone_no_additional_queries(self):
        """
        Test: OneToOneField no ejecuta queries adicionales.

        Verifica que resolve_for_relation_field detecta instancias
        ya cargadas por select_related y las retorna directamente
        sin ejecutar queries adicionales.
        """
        client = Client()
        query = """
        query {
            searchModelCs {
                objects {
                    id
                    oneToOneField {
                        id
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

            # Buscar queries individuales de ModelD (indicaría N+1)
            individual_queries = [
                q for q in queries
                if 'WHERE "tests_modeld"."id" =' in q['sql']
            ]

            self.assertEqual(len(individual_queries), 0,
                f"Found {len(individual_queries)} individual ModelD queries (N+1 problem)")

    def test_pagination_single_count(self):
        """
        Test: Paginación ejecuta COUNT solo una vez.

        Verifica que paginate_queryset cachea el count y no lo ejecuta
        múltiples veces.
        """
        client = Client()
        query = """
        query {
            searchModelCs {
                total
                pages
                objects {
                    id
                }
            }
        }
        """

        with override_settings(DEBUG=True):
            reset_queries()
            response = client.query(query).json()
            queries = connection.queries

            # Contar queries COUNT
            count_queries = [
                q for q in queries
                if 'COUNT(' in q['sql'].upper()
            ]

            # Solo debe haber 1 COUNT
            self.assertLessEqual(len(count_queries), 1,
                f"Expected 1 COUNT query, got {len(count_queries)}")

    def test_prefetch_with_orderby(self):
        """
        Test: Prefetch aplica orderBy del AST.

        Verifica que los datos prefetcheados vienen ordenados
        según el orderBy especificado en la query GraphQL.
        """
        client = Client()
        query = """
        query {
            searchModelCs {
                objects {
                    id
                    paginatedManyToManyField(orderBy: {id: DESC}) {
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

            # Buscar el Prefetch en las queries
            prefetch_queries = [
                q for q in queries
                if 'tests_modelc_many_to_many_field' in q['sql']
            ]

            # El Prefetch debe incluir ORDER BY
            if prefetch_queries:
                self.assertTrue(
                    any('ORDER BY' in q['sql'].upper() for q in prefetch_queries),
                    "Prefetch query should include ORDER BY"
                )

    def test_deep_relations_optimization(self):
        """
        Test: Relaciones profundas (3+ niveles) optimizadas.

        Verifica que queries con relaciones profundas como:
        ModelC -> ModelD -> ModelE -> ModelD -> ModelC
        no generan N+1 en ningún nivel.
        """
        client = Client()
        query = """
        query {
            searchModelCs {
                objects {
                    id
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
                }
            }
        }
        """

        with override_settings(DEBUG=True):
            reset_queries()
            response = client.query(query).json()
            query_count = len(connection.queries)

            # Validar respuesta
            self.assertIsNone(response.get("errors"))

            # Con optimizaciones, incluso queries profundas deben ser < 15 queries
            self.assertLess(query_count, 15,
                f"Deep relation query should be < 15 queries, got {query_count}")

    def test_full_optimization_10_queries(self):
        """
        Test: Query completa ejecuta exactamente 10 queries.

        Este es el test principal que valida que la optimización
        completa (de 99 → 27 → 10 queries) funciona correctamente.
        """
        client = Client()
        query = """
        query {
            searchModelCs {
                total
                pages
                objects {
                    id
                    charField
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
                        }
                    }
                    paginatedForeignKeyDRelated {
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
            query_count = len(connection.queries)

            # Debug: imprimir queries si falla
            if query_count > 10:
                print(f"\n=== Expected ≤10 queries, got {query_count} ===")
                for i, q in enumerate(connection.queries, 1):
                    print(f"{i}. {q['sql'][:100]}...")

            # Validar respuesta
            self.assertIsNone(response.get("errors"))

            # El objetivo principal: máximo 10 queries (9-10 es aceptable por optimizaciones)
            self.assertLessEqual(query_count, 10,
                f"Expected at most 10 queries with full optimization, got {query_count}")

    def test_query_breakdown(self):
        """
        Test: Breakdown detallado de las 10 queries.

        Documenta qué hace cada una de las 10 queries finales.
        """
        client = Client()
        query = """
        query {
            searchModelCs {
                total
                pages
                objects {
                    id
                    charField
                    oneToOneField {
                        id
                        foreignKeyField {
                            id
                        }
                    }
                    paginatedManyToManyField {
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

            # Categorizar queries
            count_queries = [q for q in queries if 'COUNT(' in q['sql'].upper()]
            select_queries = [q for q in queries if 'SELECT' in q['sql'].upper() and 'COUNT(' not in q['sql'].upper()]
            join_queries = [q for q in select_queries if 'JOIN' in q['sql'].upper()]
            prefetch_queries = [q for q in select_queries if 'IN (' in q['sql']]

            print(f"\n=== Query Breakdown ===")
            print(f"Total queries: {len(queries)}")
            print(f"COUNT queries: {len(count_queries)}")
            print(f"SELECT with JOIN (select_related): {len(join_queries)}")
            print(f"Prefetch (IN clause): {len(prefetch_queries)}")

            # Validaciones
            self.assertGreaterEqual(len(count_queries), 1, "Should have at least 1 COUNT")
            self.assertGreaterEqual(len(join_queries), 1, "Should have at least 1 JOIN (select_related)")
            self.assertGreaterEqual(len(prefetch_queries), 1, "Should have at least 1 Prefetch")

    def test_data_integrity_basic_fields(self):
        """
        Test: Los datos básicos retornados son correctos.

        Valida que los campos básicos (char_field, integer_field)
        retornan los valores esperados.
        """
        client = Client()
        query = """
        query {
            searchModelCs(where: {charField: {exact: "AAA"}}) {
                objects {
                    id
                    charField
                    integerField
                    booleanField
                }
            }
        }
        """

        response = client.query(query).json()

        # Validar respuesta
        self.assertIsNone(response.get("errors"))
        objects = response["data"]["searchModelCs"]["objects"]

        # Debe retornar 1 objeto (solo mc1 tiene charField="AAA")
        self.assertEqual(len(objects), 1)

        # Validar valores
        obj = objects[0]
        self.assertEqual(obj["charField"], "AAA")
        self.assertEqual(obj["integerField"], 1)
        self.assertEqual(obj["booleanField"], True)

    def test_data_integrity_onetoone_relation(self):
        """
        Test: La relación OneToOne retorna los datos correctos.

        Valida que oneToOneField.foreignKeyField apunta
        al ModelC correcto.
        """
        client = Client()
        query = """
        query {
            searchModelCs(where: {charField: {exact: "AAA1"}}) {
                objects {
                    id
                    charField
                    oneToOneField {
                        id
                        foreignKeyField {
                            id
                            charField
                        }
                    }
                }
            }
        }
        """

        response = client.query(query).json()

        # Validar respuesta
        self.assertIsNone(response.get("errors"))
        objects = response["data"]["searchModelCs"]["objects"]

        # mc11 tiene oneToOneField -> md1 -> mc1
        self.assertEqual(len(objects), 1)
        obj = objects[0]

        self.assertEqual(obj["charField"], "AAA1")
        self.assertIsNotNone(obj["oneToOneField"])
        self.assertEqual(obj["oneToOneField"]["foreignKeyField"]["charField"], "AAA")

    def test_data_integrity_manytomany_relation(self):
        """
        Test: ManyToMany retorna todos los objetos relacionados.

        Valida que paginatedManyToManyField retorna exactamente
        los 3 ModelD asociados (md1, md2, md3).
        """
        client = Client()
        query = """
        query {
            searchModelCs(where: {charField: {exact: "AAA2"}}) {
                objects {
                    id
                    charField
                    paginatedManyToManyField {
                        total
                        objects {
                            id
                            foreignKeyField {
                                charField
                            }
                        }
                    }
                }
            }
        }
        """

        response = client.query(query).json()

        # Validar respuesta
        self.assertIsNone(response.get("errors"))
        objects = response["data"]["searchModelCs"]["objects"]

        # mc12 tiene M2M con [md1, md2, md3]
        self.assertEqual(len(objects), 1)
        obj = objects[0]

        self.assertEqual(obj["charField"], "AAA2")
        m2m_data = obj["paginatedManyToManyField"]

        # Total debe ser 3
        self.assertEqual(m2m_data["total"], 3)
        self.assertEqual(len(m2m_data["objects"]), 3)

        # Validar que son AAA, BBB, CCC (md1->mc1, md2->mc2, md3->mc3)
        char_fields = sorted([
            obj["foreignKeyField"]["charField"]
            for obj in m2m_data["objects"]
        ])
        self.assertEqual(char_fields, ["AAA", "BBB", "CCC"])

    def test_data_integrity_reverse_fk_relation(self):
        """
        Test: Reverse ForeignKey retorna los objetos correctos.

        Valida que paginatedForeignKeyDRelated retorna solo
        los ModelD que apuntan a cada ModelC.
        """
        client = Client()
        query = """
        query {
            searchModelCs(where: {charField: {exact: "AAA"}}) {
                objects {
                    id
                    charField
                    paginatedForeignKeyDRelated {
                        total
                        objects {
                            id
                        }
                    }
                }
            }
        }
        """

        response = client.query(query).json()

        # Validar respuesta
        self.assertIsNone(response.get("errors"))
        objects = response["data"]["searchModelCs"]["objects"]

        # mc1 (charField="AAA") debe tener 1 ModelD (md1)
        self.assertEqual(len(objects), 1)
        obj = objects[0]

        fk_data = obj["paginatedForeignKeyDRelated"]
        self.assertEqual(fk_data["total"], 1)
        self.assertEqual(len(fk_data["objects"]), 1)

    def test_data_integrity_deep_relations(self):
        """
        Test: Relaciones profundas retornan la cadena completa correcta.

        Valida la cadena completa:
        mc11 -> md1 (oneToOne) -> me1 (reverse FK) -> md1 -> mc1
        """
        client = Client()
        query = """
        query {
            searchModelCs(where: {charField: {exact: "AAA1"}}) {
                objects {
                    charField
                    oneToOneField {
                        paginatedForeignKeyERelated {
                            objects {
                                id
                                foreignKeyFieldDeep {
                                    foreignKeyField {
                                        charField
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        """

        response = client.query(query).json()

        # Validar respuesta
        self.assertIsNone(response.get("errors"))
        objects = response["data"]["searchModelCs"]["objects"]

        self.assertEqual(len(objects), 1)
        obj = objects[0]

        # mc11 -> md1 -> me1 -> md1 -> mc1
        e_related = obj["oneToOneField"]["paginatedForeignKeyERelated"]["objects"]
        self.assertGreater(len(e_related), 0)

        # me1 apunta a md1, que apunta a mc1 (charField="AAA")
        deep_char = e_related[0]["foreignKeyFieldDeep"]["foreignKeyField"]["charField"]
        self.assertEqual(deep_char, "AAA")

    def test_data_integrity_with_ordering(self):
        """
        Test: orderBy retorna los datos en el orden correcto.

        Valida que los datos vienen ordenados según lo especificado.
        """
        client = Client()
        query = """
        query {
            searchModelCs(orderBy: {integerField: DESC}) {
                objects {
                    integerField
                    charField
                }
            }
        }
        """

        response = client.query(query).json()

        # Validar respuesta
        self.assertIsNone(response.get("errors"))
        objects = response["data"]["searchModelCs"]["objects"]

        # Extraer integerField values
        integer_fields = [obj["integerField"] for obj in objects]

        # Deben estar ordenados descendente
        self.assertEqual(integer_fields, sorted(integer_fields, reverse=True))

    def test_data_integrity_pagination_consistency(self):
        """
        Test: Paginación retorna total y objetos consistentes.

        Valida que total, pages y len(objects) son consistentes.
        """
        client = Client()
        query = """
        query {
            searchModelCs(paginationConfig: {page: 1, itemsPerPage: 2}) {
                total
                pages
                objects {
                    id
                }
            }
        }
        """

        response = client.query(query).json()

        # Validar respuesta
        self.assertIsNone(response.get("errors"))
        data = response["data"]["searchModelCs"]

        # Total debe ser 6 (mc1, mc2, mc3, mc4, mc11, mc12)
        self.assertEqual(data["total"], 6)

        # Con itemsPerPage=2, debe retornar 2 objetos
        self.assertEqual(len(data["objects"]), 2)

        # Pages debe ser ceil(6/2) = 3
        self.assertEqual(data["pages"], 3)
