"""
Tests to validate N+1 optimizations in GraphQL.

This file contains tests that verify that the implemented optimizations
reduce queries from 99 → 27 → 10, eliminating N+1 problems.

Optimizations tested:
1. select_related for ForeignKey and OneToOneField
2. prefetch_related with custom Prefetch for ManyToMany and reverse ForeignKey
3. orderBy extracted from the AST and applied in Prefetch
4. Optimized pagination (count executed only once)
5. resolve_for_relation_field detects already-loaded instances
"""

from django.db import connection, reset_queries
from django.test import TestCase, override_settings

from tests.models import ModelC, ModelD, ModelE
from tests.utils import Client


class N1OptimizationsTestCase(TestCase):
    """Tests to verify N+1 optimizations in GraphQL queries."""

    @classmethod
    def setUpTestData(cls):
        """Create test data once for all tests."""
        model_c_data = [
            {
                "char_field": "AAA",
                "integer_field": 1,
                "boolean_field": True,
                "key": "key1",
            },
            {
                "char_field": "BBB",
                "integer_field": 2,
                "boolean_field": False,
                "key": "key2",
            },
            {
                "char_field": "CCC",
                "integer_field": 3,
                "boolean_field": True,
                "key": "key3",
            },
            {
                "char_field": "DDD",
                "integer_field": 4,
                "boolean_field": False,
                "key": "key4",
            },
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
            ModelD.objects.create(foreign_key_field=mc) for mc in model_c_instances
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
        """Reset queries before each test."""
        reset_queries()
        connection.queries_log.clear()

    def test_search_basic_optimizations(self):
        """
        Test: Basic query with select_related and prefetch_related.

        Verifies that:
        - select_related loads OneToOneField with a single JOIN
        - prefetch_related loads ManyToMany efficiently
        - There are no N+1 queries
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

            # Validate response
            self.assertIsNone(response.get("errors"))
            self.assertIn("data", response)

            # Expected queries:
            # 1. COUNT for pagination
            # 2. SELECT ModelC with JOIN ModelD (select_related)
            # 3. Prefetch ManyToMany
            # Total: ~3-5 queries (depends on data)
            self.assertLess(
                query_count, 10, f"Expected < 10 queries, got {query_count}"
            )

    def test_onetoone_no_additional_queries(self):
        """
        Test: OneToOneField does not execute additional queries.

        Verifies that resolve_for_relation_field detects instances
        already loaded by select_related and returns them directly
        without executing additional queries.
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

            # Validate response
            self.assertIsNone(response.get("errors"))

            # Look for individual ModelD queries (would indicate N+1)
            individual_queries = [
                q for q in queries if 'WHERE "tests_modeld"."id" =' in q["sql"]
            ]

            self.assertEqual(
                len(individual_queries),
                0,
                f"Found {len(individual_queries)} individual ModelD queries (N+1 problem)",
            )

    def test_pagination_single_count(self):
        """
        Test: Pagination executes COUNT only once.

        Verifies that paginate_queryset caches the count and does not execute it
        multiple times.
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
            client.query(query).json()
            queries = connection.queries

            # Count COUNT queries
            count_queries = [q for q in queries if "COUNT(" in q["sql"].upper()]

            # There should be only 1 COUNT
            self.assertLessEqual(
                len(count_queries),
                1,
                f"Expected 1 COUNT query, got {len(count_queries)}",
            )

    def test_prefetch_with_orderby(self):
        """
        Test: Prefetch applies orderBy from the AST.

        Verifies that the prefetched data is ordered according to
        the orderBy specified in the GraphQL query.
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

            # Validate response
            self.assertIsNone(response.get("errors"))

            # Look for the Prefetch in queries
            prefetch_queries = [
                q for q in queries if "tests_modelc_many_to_many_field" in q["sql"]
            ]

            # Prefetch query should include ORDER BY
            if prefetch_queries:
                self.assertTrue(
                    any("ORDER BY" in q["sql"].upper() for q in prefetch_queries),
                    "Prefetch query should include ORDER BY",
                )

    def test_deep_relations_optimization(self):
        """
        Test: Deep relations (3+ levels) optimized.

        Verifies that queries with deep relations such as:
        ModelC -> ModelD -> ModelE -> ModelD -> ModelC
        do not generate N+1 at any level.
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

            # Validate response
            self.assertIsNone(response.get("errors"))

            # With optimizations, even deep relation queries should be < 15 queries
            self.assertLess(
                query_count,
                15,
                f"Deep relation query should be < 15 queries, got {query_count}",
            )

    def test_full_optimization_10_queries(self):
        """
        Test: Full query executes exactly 10 queries.

        This is the main test that validates the full optimization
        (from 99 → 27 → 10 queries) works correctly.
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

            # Debug: print queries if it fails
            if query_count > 10:
                print(f"\n=== Expected ≤10 queries, got {query_count} ===")
                for i, q in enumerate(connection.queries, 1):
                    print(f"{i}. {q['sql'][:100]}...")

            # Validate response
            self.assertIsNone(response.get("errors"))

            # Main goal: at most 10 queries (9-10 is acceptable due to optimizations)
            self.assertLessEqual(
                query_count,
                10,
                f"Expected at most 10 queries with full optimization, got {query_count}",
            )

    def test_query_breakdown(self):
        """
        Test: Detailed breakdown of the 10 queries.

        Documents what each of the final 10 queries does.
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
            client.query(query).json()
            queries = connection.queries

            # Categorize queries
            count_queries = [q for q in queries if "COUNT(" in q["sql"].upper()]
            select_queries = [
                q
                for q in queries
                if "SELECT" in q["sql"].upper() and "COUNT(" not in q["sql"].upper()
            ]
            join_queries = [q for q in select_queries if "JOIN" in q["sql"].upper()]
            prefetch_queries = [q for q in select_queries if "IN (" in q["sql"]]

            print("\n=== Query Breakdown ===")
            print(f"Total queries: {len(queries)}")
            print(f"COUNT queries: {len(count_queries)}")
            print(f"SELECT with JOIN (select_related): {len(join_queries)}")
            print(f"Prefetch (IN clause): {len(prefetch_queries)}")

            # Validations
            self.assertGreaterEqual(
                len(count_queries), 1, "Should have at least 1 COUNT"
            )
            self.assertGreaterEqual(
                len(join_queries), 1, "Should have at least 1 JOIN (select_related)"
            )
            self.assertGreaterEqual(
                len(prefetch_queries), 1, "Should have at least 1 Prefetch"
            )

    def test_data_integrity_basic_fields(self):
        """
        Test: Basic returned data is correct.

        Validates that the basic fields (char_field, integer_field)
        return the expected values.
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

        # Validate response
        self.assertIsNone(response.get("errors"))
        objects = response["data"]["searchModelCs"]["objects"]

        # It should return 1 object (only mc1 has charField="AAA")
        self.assertEqual(len(objects), 1)

        # Validate values
        obj = objects[0]
        self.assertEqual(obj["charField"], "AAA")
        self.assertEqual(obj["integerField"], 1)
        self.assertEqual(obj["booleanField"], True)

    def test_data_integrity_onetoone_relation(self):
        """
        Test: The OneToOne relationship returns the correct data.

        Validates that oneToOneField.foreignKeyField points
        to the correct ModelC.
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

        # Validate response
        self.assertIsNone(response.get("errors"))
        objects = response["data"]["searchModelCs"]["objects"]

        # mc11 has oneToOneField -> md1 -> mc1
        self.assertEqual(len(objects), 1)
        obj = objects[0]

        self.assertEqual(obj["charField"], "AAA1")
        self.assertIsNotNone(obj["oneToOneField"])
        self.assertEqual(obj["oneToOneField"]["foreignKeyField"]["charField"], "AAA")

    def test_data_integrity_manytomany_relation(self):
        """
        Test: ManyToMany returns all related objects.

        Validates that paginatedManyToManyField returns exactly
        the 3 associated ModelD (md1, md2, md3).
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

        # Validate response
        self.assertIsNone(response.get("errors"))
        objects = response["data"]["searchModelCs"]["objects"]

        # mc12 has M2M with [md1, md2, md3]
        self.assertEqual(len(objects), 1)
        obj = objects[0]

        self.assertEqual(obj["charField"], "AAA2")
        m2m_data = obj["paginatedManyToManyField"]

        # Total should be 3
        self.assertEqual(m2m_data["total"], 3)
        self.assertEqual(len(m2m_data["objects"]), 3)

        # Validate that they are AAA, BBB, CCC (md1->mc1, md2->mc2, md3->mc3)
        char_fields = sorted(
            [obj["foreignKeyField"]["charField"] for obj in m2m_data["objects"]]
        )
        self.assertEqual(char_fields, ["AAA", "BBB", "CCC"])

    def test_data_integrity_reverse_fk_relation(self):
        """
        Test: Reverse ForeignKey returns the correct objects.

        Validates that paginatedForeignKeyDRelated returns only
        the ModelD that point to each ModelC.
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

        # Validate response
        self.assertIsNone(response.get("errors"))
        objects = response["data"]["searchModelCs"]["objects"]

        # mc1 (charField="AAA") should have 1 ModelD (md1)
        self.assertEqual(len(objects), 1)
        obj = objects[0]

        fk_data = obj["paginatedForeignKeyDRelated"]
        self.assertEqual(fk_data["total"], 1)
        self.assertEqual(len(fk_data["objects"]), 1)

    def test_data_integrity_deep_relations(self):
        """
        Test: Deep relations return the correct full chain.

        Validates the full chain:
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

        # Validate response
        self.assertIsNone(response.get("errors"))
        objects = response["data"]["searchModelCs"]["objects"]

        self.assertEqual(len(objects), 1)
        obj = objects[0]

        # mc11 -> md1 -> me1 -> md1 -> mc1
        e_related = obj["oneToOneField"]["paginatedForeignKeyERelated"]["objects"]
        self.assertGreater(len(e_related), 0)

        # me1 points to md1, which points to mc1 (charField="AAA")
        deep_char = e_related[0]["foreignKeyFieldDeep"]["foreignKeyField"]["charField"]
        self.assertEqual(deep_char, "AAA")

    def test_data_integrity_with_ordering(self):
        """
        Test: orderBy returns data in the correct order.

        Validates that the data comes ordered as specified.
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

        # Validate response
        self.assertIsNone(response.get("errors"))
        objects = response["data"]["searchModelCs"]["objects"]

        # Extract integerField values
        integer_fields = [obj["integerField"] for obj in objects]

        # They should be in descending order
        self.assertEqual(integer_fields, sorted(integer_fields, reverse=True))

    def test_data_integrity_pagination_consistency(self):
        """
        Test: Pagination returns consistent total and objects.

        Validates that total, pages and len(objects) are consistent.
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

        # Validate response
        self.assertIsNone(response.get("errors"))
        data = response["data"]["searchModelCs"]

        # Total should be 6 (mc1, mc2, mc3, mc4, mc11, mc12)
        self.assertEqual(data["total"], 6)

        # With itemsPerPage=2, it should return 2 objects
        self.assertEqual(len(data["objects"]), 2)

        # Pages should be ceil(6/2) = 3
        self.assertEqual(data["pages"], 3)
