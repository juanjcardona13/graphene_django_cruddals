"""
Tests for _queryset_factory functionality in ModelObjectType.

These tests verify that:
1. _queryset_factory is properly added to ModelObjectType via monkey-patching
2. Nested fields with WHERE/ORDER BY arguments are optimized correctly
3. Recursive calls work for related models
4. The implementation is fully backward compatible
"""
import unittest
import pytest
from django.db import connection, reset_queries
from django.conf import settings

from tests.models import ModelC, ModelD, ModelE
from tests.schema import schema


@pytest.mark.django_db
class QuerysetFactoryTestCase(unittest.TestCase):
    """Tests for _queryset_factory implementation."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Enable DEBUG to track queries
        settings.DEBUG = True

    def setUp(self):
        """Create test data before each test."""
        # Clean up
        ModelC.objects.all().delete()
        ModelD.objects.all().delete()
        ModelE.objects.all().delete()

        # Create test data
        self.model_d1 = ModelD.objects.create(name="ModelD1")
        self.model_d2 = ModelD.objects.create(name="ModelD2")

        self.model_e1 = ModelE.objects.create(name="ModelE1")
        self.model_e2 = ModelE.objects.create(name="ModelE2")

        self.model_c1 = ModelC.objects.create(
            name="AAA",
            one_to_one_field=self.model_d1
        )
        self.model_c2 = ModelC.objects.create(
            name="BBB",
            one_to_one_field=self.model_d2
        )
        self.model_c3 = ModelC.objects.create(
            name="CCC",
            one_to_one_field=None
        )

        self.model_c1.many_to_many_field.add(self.model_e1, self.model_e2)
        self.model_c2.many_to_many_field.add(self.model_e1)

        reset_queries()

    def test_queryset_factory_exists(self):
        """Test that _queryset_factory method exists on ModelObjectType."""
        from graphene_cruddals.types.main import ModelObjectType

        self.assertTrue(hasattr(ModelObjectType, '_queryset_factory'))
        self.assertTrue(hasattr(ModelObjectType, 'get_objects_queryset'))

    def test_queryset_factory_basic_query(self):
        """Test basic query optimization with _queryset_factory."""
        query = """
        query {
          listModelCs(page: 1, itemsPerPage: 3) {
            listDjango {
              id
              name
              oneToOneField {
                id
                name
              }
            }
          }
        }
        """

        reset_queries()
        result = schema.execute(query)

        # Verify no errors
        self.assertIsNone(result.errors, f"Query had errors: {result.errors}")

        # Verify data
        self.assertIsNotNone(result.data)
        self.assertIn('listModelCs', result.data)
        self.assertIn('listDjango', result.data['listModelCs'])

        # Verify optimizations (should be few queries)
        total_queries = len(connection.queries)
        self.assertLessEqual(total_queries, 5,
                            f"Too many queries: {total_queries}. Expected <= 5")

    def test_nested_field_with_where(self):
        """Test nested fields with WHERE clause are optimized."""
        query = """
        query {
          listModelCs(page: 1, itemsPerPage: 3) {
            listDjango {
              id
              name
              paginatedManyToManyField(where: {name: {exact: "ModelE1"}}) {
                listModelE {
                  id
                  name
                }
              }
            }
          }
        }
        """

        reset_queries()
        result = schema.execute(query)

        # Verify no errors
        self.assertIsNone(result.errors, f"Query had errors: {result.errors}")

        # Verify data is filtered correctly
        self.assertIsNotNone(result.data)
        model_cs = result.data['listModelCs']['listDjango']

        # Model C1 should have only ModelE1
        model_c1_data = next(m for m in model_cs if m['name'] == 'AAA')
        self.assertEqual(len(model_c1_data['paginatedManyToManyField']['listModelE']), 1)
        self.assertEqual(
            model_c1_data['paginatedManyToManyField']['listModelE'][0]['name'],
            'ModelE1'
        )

        # Verify query count is reasonable
        total_queries = len(connection.queries)
        self.assertLessEqual(total_queries, 10,
                            f"Too many queries: {total_queries}")

    def test_nested_field_with_order_by(self):
        """Test nested fields with ORDER BY are optimized."""
        query = """
        query {
          listModelCs(page: 1, itemsPerPage: 3) {
            listDjango {
              id
              name
              paginatedManyToManyField(orderBy: [{name: DESC}]) {
                listModelE {
                  id
                  name
                }
              }
            }
          }
        }
        """

        reset_queries()
        result = schema.execute(query)

        # Verify no errors
        self.assertIsNone(result.errors, f"Query had errors: {result.errors}")

        # Verify data is ordered correctly
        self.assertIsNotNone(result.data)
        model_cs = result.data['listModelCs']['listDjango']

        # Model C1 should have ModelE2, ModelE1 (DESC order)
        model_c1_data = next(m for m in model_cs if m['name'] == 'AAA')
        many_to_many = model_c1_data['paginatedManyToManyField']['listModelE']
        if len(many_to_many) == 2:
            self.assertEqual(many_to_many[0]['name'], 'ModelE2')
            self.assertEqual(many_to_many[1]['name'], 'ModelE1')

        # Verify query count
        total_queries = len(connection.queries)
        self.assertLessEqual(total_queries, 10,
                            f"Too many queries: {total_queries}")

    def test_nested_field_with_where_and_order_by(self):
        """Test nested fields with both WHERE and ORDER BY."""
        # Add more test data for better testing
        model_e3 = ModelE.objects.create(name="ModelE3")
        model_e4 = ModelE.objects.create(name="ModelE4")
        self.model_c1.many_to_many_field.add(model_e3, model_e4)

        query = """
        query {
          listModelCs(page: 1, itemsPerPage: 3) {
            listDjango {
              id
              name
              paginatedManyToManyField(
                where: {name: {icontains: "ModelE"}}
                orderBy: [{name: ASC}]
              ) {
                listModelE {
                  id
                  name
                }
              }
            }
          }
        }
        """

        reset_queries()
        result = schema.execute(query)

        # Verify no errors
        self.assertIsNone(result.errors, f"Query had errors: {result.errors}")

        # Verify data
        self.assertIsNotNone(result.data)
        model_cs = result.data['listModelCs']['listDjango']

        # Model C1 should have all ModelEs in ASC order
        model_c1_data = next(m for m in model_cs if m['name'] == 'AAA')
        many_to_many = model_c1_data['paginatedManyToManyField']['listModelE']

        # Verify ordering (ASC)
        if len(many_to_many) >= 2:
            names = [item['name'] for item in many_to_many]
            self.assertEqual(names, sorted(names))

        # Verify query count
        total_queries = len(connection.queries)
        self.assertLessEqual(total_queries, 10,
                            f"Too many queries: {total_queries}")

    def test_search_field_with_nested_where(self):
        """Test search operation with nested WHERE clauses."""
        query = """
        query {
          searchModelCs(page: 1, itemsPerPage: 3) {
            listModelC {
              id
              name
              paginatedManyToManyField(where: {name: {exact: "ModelE1"}}) {
                listModelE {
                  id
                  name
                }
              }
            }
          }
        }
        """

        reset_queries()
        result = schema.execute(query)

        # Verify no errors
        self.assertIsNone(result.errors, f"Query had errors: {result.errors}")

        # Verify data
        self.assertIsNotNone(result.data)
        self.assertIn('searchModelCs', result.data)

        # Verify query count
        total_queries = len(connection.queries)
        self.assertLessEqual(total_queries, 10,
                            f"Too many queries: {total_queries}")

    def test_backward_compatibility(self):
        """Test that existing queries still work (backward compatibility)."""
        # This is the same query from test_n1_optimizations.py
        query = """
        query {
          listModelCs(page: 1, itemsPerPage: 10) {
            listDjango {
              id
              name
              oneToOneField {
                id
                name
              }
              paginatedManyToManyField {
                listModelE {
                  id
                  name
                }
              }
            }
          }
        }
        """

        reset_queries()
        result = schema.execute(query)

        # Verify no errors
        self.assertIsNone(result.errors, f"Query had errors: {result.errors}")

        # Verify data integrity
        self.assertIsNotNone(result.data)
        model_cs = result.data['listModelCs']['listDjango']
        self.assertGreater(len(model_cs), 0)

        # Verify query count is reasonable
        total_queries = len(connection.queries)
        self.assertLessEqual(total_queries, 15,
                            f"Too many queries: {total_queries}")

    def test_read_operation_with_factory(self):
        """Test read operation uses _queryset_factory correctly."""
        query = f"""
        query {{
          readModelC(where: {{id: {self.model_c1.id}}}) {{
            id
            name
            oneToOneField {{
              id
              name
            }}
          }}
        }}
        """

        reset_queries()
        result = schema.execute(query)

        # Verify no errors
        self.assertIsNone(result.errors, f"Query had errors: {result.errors}")

        # Verify data
        self.assertIsNotNone(result.data)
        self.assertEqual(result.data['readModelC']['name'], 'AAA')
        self.assertIsNotNone(result.data['readModelC']['oneToOneField'])
        self.assertEqual(result.data['readModelC']['oneToOneField']['name'], 'ModelD1')

        # Verify optimizations (should be very few queries)
        total_queries = len(connection.queries)
        self.assertLessEqual(total_queries, 3,
                            f"Too many queries for read: {total_queries}")


@pytest.mark.django_db
class QuerysetFactoryRecursionTestCase(unittest.TestCase):
    """Tests for recursive behavior of _queryset_factory."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        settings.DEBUG = True

    def setUp(self):
        """Create test data."""
        ModelC.objects.all().delete()
        ModelD.objects.all().delete()
        ModelE.objects.all().delete()

        # Create linked data for recursion testing
        self.model_d = ModelD.objects.create(name="D1")
        self.model_e1 = ModelE.objects.create(name="E1")
        self.model_e2 = ModelE.objects.create(name="E2")

        self.model_c = ModelC.objects.create(
            name="C1",
            one_to_one_field=self.model_d
        )
        self.model_c.many_to_many_field.add(self.model_e1, self.model_e2)

        reset_queries()

    def test_deep_nesting_with_where(self):
        """Test deeply nested queries with WHERE clauses."""
        query = """
        query {
          searchModelCs(where: {name: {exact: "C1"}}) {
            listModelC {
              id
              name
              oneToOneField {
                id
                name
              }
              paginatedManyToManyField(where: {name: {exact: "E1"}}) {
                listModelE {
                  id
                  name
                }
              }
            }
          }
        }
        """

        reset_queries()
        result = schema.execute(query)

        # Verify no errors
        self.assertIsNone(result.errors, f"Query had errors: {result.errors}")

        # Verify data filtering worked at all levels
        self.assertIsNotNone(result.data)
        model_cs = result.data['searchModelCs']['listModelC']
        self.assertEqual(len(model_cs), 1)
        self.assertEqual(model_cs[0]['name'], 'C1')

        # Verify nested WHERE worked
        many_to_many = model_cs[0]['paginatedManyToManyField']['listModelE']
        self.assertEqual(len(many_to_many), 1)
        self.assertEqual(many_to_many[0]['name'], 'E1')

        # Verify query count
        total_queries = len(connection.queries)
        self.assertLessEqual(total_queries, 10,
                            f"Too many queries: {total_queries}")


if __name__ == '__main__':
    unittest.main()
