"""
Tests unitarios para _queryset_factory en ModelObjectType.

Estos tests verifican que:
1. _queryset_factory existe en ModelObjectType
2. _queryset_factory aplica select_related correctamente
3. _queryset_factory aplica prefetch_related correctamente
4. _queryset_factory aplica only correctamente
5. _queryset_factory combina múltiples optimizaciones
"""
import unittest
from django.test import TestCase
from unittest.mock import Mock, patch, MagicMock

from tests.models import ModelC, ModelD, ModelE
from tests.schema import ModelCType


class QuerysetFactoryExistsTestCase(unittest.TestCase):
    """Verificar que _queryset_factory existe en ModelObjectType."""

    def test_queryset_factory_exists_in_model_object_type(self):
        """Test: ModelObjectType tiene el método _queryset_factory."""
        self.assertTrue(
            hasattr(ModelCType, '_queryset_factory'),
            "ModelObjectType debe tener _queryset_factory"
        )

    def test_queryset_factory_is_callable(self):
        """Test: _queryset_factory es llamable."""
        self.assertTrue(
            callable(getattr(ModelCType, '_queryset_factory', None)),
            "_queryset_factory debe ser callable"
        )


class QuerysetFactoryFunctionalityTestCase(TestCase):
    """Verificar que _queryset_factory aplica optimizaciones correctamente."""

    def setUp(self):
        """Crear datos de prueba."""
        ModelC.objects.all().delete()
        ModelD.objects.all().delete()
        ModelE.objects.all().delete()

        self.model_d = ModelD.objects.create()
        self.model_c = ModelC.objects.create(
            char_field="Test",
            integer_field=1,
            one_to_one_field=self.model_d
        )

    def test_queryset_factory_applies_select_related(self):
        """Test: _queryset_factory aplica select_related."""
        base_queryset = ModelC.objects.all()

        # Llamar _queryset_factory con select_related
        optimized_qs = ModelCType._queryset_factory(
            queryset=base_queryset,
            select_related=['one_to_one_field']
        )

        # Verificar que select_related fue aplicado
        self.assertIn('one_to_one_field', str(optimized_qs.query))

    def test_queryset_factory_applies_prefetch_related(self):
        """Test: _queryset_factory aplica prefetch_related."""
        base_queryset = ModelC.objects.all()

        # Llamar _queryset_factory con prefetch_related
        optimized_qs = ModelCType._queryset_factory(
            queryset=base_queryset,
            prefetch_related=['many_to_many_field']
        )

        # Verificar que prefetch_related fue configurado
        self.assertIsNotNone(optimized_qs._prefetch_related_lookups)
        self.assertTrue(len(optimized_qs._prefetch_related_lookups) > 0)

    def test_queryset_factory_applies_only(self):
        """Test: _queryset_factory aplica only."""
        base_queryset = ModelC.objects.all()

        # Llamar _queryset_factory con only
        optimized_qs = ModelCType._queryset_factory(
            queryset=base_queryset,
            only=['id', 'char_field']
        )

        # Verificar que only fue aplicado
        query_str = str(optimized_qs.query)
        # El query debe incluir solo los campos especificados
        self.assertIn('char_field', query_str)

    def test_queryset_factory_combines_optimizations(self):
        """Test: _queryset_factory combina múltiples optimizaciones."""
        base_queryset = ModelC.objects.all()

        # Llamar _queryset_factory con todas las optimizaciones
        optimized_qs = ModelCType._queryset_factory(
            queryset=base_queryset,
            select_related=['one_to_one_field'],
            prefetch_related=['many_to_many_field'],
            only=['id', 'char_field']
        )

        # Verificar select_related
        self.assertIn('one_to_one_field', str(optimized_qs.query))

        # Verificar prefetch_related
        self.assertIsNotNone(optimized_qs._prefetch_related_lookups)

        # El queryset debe ser válido y ejecutable
        list(optimized_qs)  # Forzar evaluación
        self.assertTrue(True, "Queryset con múltiples optimizaciones debe ejecutarse sin errores")

    def test_queryset_factory_without_optimizations_returns_queryset(self):
        """Test: _queryset_factory sin optimizaciones retorna queryset válido."""
        base_queryset = ModelC.objects.all()

        # Llamar sin optimizaciones
        result_qs = ModelCType._queryset_factory(queryset=base_queryset)

        # Debe retornar un queryset válido
        self.assertIsNotNone(result_qs)
        list(result_qs)  # Debe ser ejecutable
        self.assertTrue(True, "Queryset sin optimizaciones debe funcionar")


class QuerysetFactoryEdgeCasesTestCase(unittest.TestCase):
    """Verificar edge cases de _queryset_factory."""

    def test_queryset_factory_with_empty_lists(self):
        """Test: _queryset_factory con listas vacías no rompe."""
        from tests.models import ModelC
        base_queryset = ModelC.objects.all()

        # Llamar con listas vacías
        result_qs = ModelCType._queryset_factory(
            queryset=base_queryset,
            select_related=[],
            prefetch_related=[],
            only=[]
        )

        # No debe romper
        self.assertIsNotNone(result_qs)

    def test_queryset_factory_with_none_values(self):
        """Test: _queryset_factory con None no rompe."""
        from tests.models import ModelC
        base_queryset = ModelC.objects.all()

        # Llamar con None
        result_qs = ModelCType._queryset_factory(
            queryset=base_queryset,
            select_related=None,
            prefetch_related=None,
            only=None
        )

        # No debe romper
        self.assertIsNotNone(result_qs)
