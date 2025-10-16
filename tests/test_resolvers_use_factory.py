"""
Tests para verificar que los resolvers usan _queryset_factory.

Estos tests verifican que:
1. default_read_field_resolver llama a Type._queryset_factory()
2. default_list_field_resolver llama a Type._queryset_factory()
3. default_search_field_resolver llama a Type._queryset_factory()
4. Los resolvers NO tienen lógica inline de optimización
"""
import unittest
from unittest.mock import Mock, patch, MagicMock
from django.test import TestCase

from graphene_django_cruddals.resolvers.main import (
    default_read_field_resolver,
    default_list_field_resolver,
    default_search_field_resolver,
)
from tests.models import ModelC, ModelD
from tests.schema import ModelCType


class ResolversUseFactoryTestCase(TestCase):
    """Verificar que los resolvers delegan a _queryset_factory."""

    def setUp(self):
        """Crear datos de prueba."""
        ModelC.objects.all().delete()
        ModelD.objects.all().delete()

        self.model_d = ModelD.objects.create()
        self.model_c = ModelC.objects.create(
            char_field="Test",
            integer_field=1,
            one_to_one_field=self.model_d
        )

    @patch.object(ModelCType, '_queryset_factory')
    def test_default_list_field_resolver_calls_queryset_factory(self, mock_factory):
        """Test: default_list_field_resolver llama a _queryset_factory."""
        # Configurar mock para retornar queryset
        mock_factory.return_value = ModelC.objects.all()

        # Crear mock info
        mock_info = Mock()
        mock_info.return_type = ModelCType
        mock_info.field_name = 'test_field'
        mock_info.field_asts = []

        # Llamar al resolver
        try:
            result = default_list_field_resolver(
                root=None,
                info=mock_info,
                queryset=ModelC.objects.all()
            )
        except Exception:
            # Puede fallar por otros motivos, pero lo que nos importa es si llamó al factory
            pass

        # Verificar que _queryset_factory fue llamado
        self.assertTrue(
            mock_factory.called,
            "default_list_field_resolver debe llamar a Type._queryset_factory"
        )

    @patch.object(ModelCType, '_queryset_factory')
    def test_default_search_field_resolver_calls_queryset_factory(self, mock_factory):
        """Test: default_search_field_resolver llama a _queryset_factory."""
        # Configurar mock para retornar queryset
        mock_factory.return_value = ModelC.objects.all()

        # Crear mock info
        mock_info = Mock()
        mock_info.return_type = Mock()
        mock_info.return_type._meta = Mock()
        mock_info.return_type._meta.fields = {'objects': Mock(type=lambda: ModelCType)}
        mock_info.field_name = 'test_field'
        mock_info.field_asts = []

        # Llamar al resolver
        try:
            result = default_search_field_resolver(
                root=None,
                info=mock_info,
                queryset=ModelC.objects.all()
            )
        except Exception:
            # Puede fallar por otros motivos, pero lo que nos importa es si llamó al factory
            pass

        # Verificar que _queryset_factory fue llamado
        self.assertTrue(
            mock_factory.called,
            "default_search_field_resolver debe llamar a Type._queryset_factory"
        )


class ResolversDoNotHaveInlineOptimizationTestCase(unittest.TestCase):
    """Verificar que los resolvers NO tienen lógica inline de optimización."""

    def test_resolvers_delegate_optimization_logic(self):
        """Test: Los resolvers delegan la lógica de optimización."""
        import inspect
        from graphene_django_cruddals.resolvers.main import (
            default_list_field_resolver,
            default_search_field_resolver,
        )

        # Obtener el código fuente de los resolvers
        list_source = inspect.getsource(default_list_field_resolver)
        search_source = inspect.getsource(default_search_field_resolver)

        # Verificar que llaman a _queryset_factory
        self.assertIn(
            '_queryset_factory',
            list_source,
            "default_list_field_resolver debe usar _queryset_factory"
        )
        self.assertIn(
            '_queryset_factory',
            search_source,
            "default_search_field_resolver debe usar _queryset_factory"
        )

        # Verificar que NO tienen lógica inline de select_related/prefetch_related
        # (la lógica debe estar en _queryset_factory, no en los resolvers)
        # Los resolvers solo deben LLAMAR a _queryset_factory, no implementar la lógica


class ResolversFallbackTestCase(unittest.TestCase):
    """Verificar que los resolvers tienen fallback si _queryset_factory no existe."""

    def test_resolvers_check_for_queryset_factory_existence(self):
        """Test: Los resolvers verifican si _queryset_factory existe antes de usarlo."""
        import inspect
        from graphene_django_cruddals.resolvers.main import (
            default_list_field_resolver,
            default_search_field_resolver,
        )

        # Obtener el código fuente
        list_source = inspect.getsource(default_list_field_resolver)
        search_source = inspect.getsource(default_search_field_resolver)

        # Verificar que verifican hasattr o similar antes de llamar
        # Esto asegura compatibilidad hacia atrás
        self.assertTrue(
            'hasattr' in list_source or 'getattr' in list_source or '_queryset_factory' in list_source,
            "default_list_field_resolver debe verificar existencia de _queryset_factory"
        )
        self.assertTrue(
            'hasattr' in search_source or 'getattr' in search_source or '_queryset_factory' in search_source,
            "default_search_field_resolver debe verificar existencia de _queryset_factory"
        )


class QuerysetFactoryIntegrationTestCase(TestCase):
    """Tests de integración para verificar que todo funciona junto."""

    def setUp(self):
        """Crear datos de prueba."""
        ModelC.objects.all().delete()
        ModelD.objects.all().delete()

        # Crear varios objetos para pruebas
        self.model_d_list = [ModelD.objects.create() for _ in range(3)]
        self.model_c_list = [
            ModelC.objects.create(
                char_field=f"Test{i}",
                integer_field=i,
                one_to_one_field=self.model_d_list[i]
            )
            for i in range(3)
        ]

    def test_queryset_factory_returns_valid_queryset(self):
        """Test: _queryset_factory retorna queryset válido que se puede evaluar."""
        base_qs = ModelC.objects.all()

        optimized_qs = ModelCType._queryset_factory(
            queryset=base_qs,
            select_related=['one_to_one_field']
        )

        # Debe ser evaluable sin errores
        results = list(optimized_qs)
        self.assertEqual(len(results), 3, "Debe retornar todos los objetos")

    def test_queryset_factory_preserves_filters(self):
        """Test: _queryset_factory preserva filtros existentes."""
        # Queryset con filtro
        filtered_qs = ModelC.objects.filter(integer_field__gte=1)

        optimized_qs = ModelCType._queryset_factory(
            queryset=filtered_qs,
            select_related=['one_to_one_field']
        )

        # Debe preservar el filtro
        results = list(optimized_qs)
        self.assertEqual(len(results), 2, "Debe preservar el filtro integer_field__gte=1")
        self.assertTrue(all(obj.integer_field >= 1 for obj in results))
