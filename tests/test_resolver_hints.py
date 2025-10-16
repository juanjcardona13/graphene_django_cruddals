# -*- coding: utf-8 -*-
"""
Tests para el decorador @resolver_hints y computed fields optimizados.
"""

import graphene
from django.test import TestCase
from graphene_cruddals import RegistryGlobal

from graphene_django_cruddals import (
    DjangoModelCruddals,
    resolver_hints,
    get_computed_field_hints,
)

# Usar modelos ya existentes de los tests
from tests.models import ModelC


class ResolverHintsDecoratorTestCase(TestCase):
    """Tests básicos para el decorador @resolver_hints"""

    def test_resolver_hints_decorator_basic(self):
        """Test que el decorador @resolver_hints agrega atributos correctamente"""

        @resolver_hints(select_related=['profile'], only=['first_name', 'last_name'])
        def resolve_full_name(self, info):
            return f"{self.first_name} {self.last_name}"

        # Verificar que los atributos fueron agregados
        self.assertTrue(hasattr(resolve_full_name, 'have_resolver_hints'))
        self.assertEqual(resolve_full_name.select_related, ['profile'])
        self.assertEqual(resolve_full_name.only, ['first_name', 'last_name'])
        self.assertEqual(resolve_full_name.prefetch_related, [])

    def test_resolver_hints_decorator_all_params(self):
        """Test que el decorador maneja todos los parámetros"""

        @resolver_hints(
            select_related=['author', 'category'],
            prefetch_related=['tags', 'comments'],
            only=['title', 'author__name']
        )
        def resolve_summary(self, info):
            return "summary"

        self.assertTrue(resolve_summary.have_resolver_hints)
        self.assertEqual(resolve_summary.select_related, ['author', 'category'])
        self.assertEqual(resolve_summary.prefetch_related, ['tags', 'comments'])
        self.assertEqual(resolve_summary.only, ['title', 'author__name'])

    def test_resolver_hints_decorator_empty(self):
        """Test que el decorador funciona sin parámetros"""

        @resolver_hints()
        def resolve_something(self, info):
            return "something"

        self.assertTrue(resolve_something.have_resolver_hints)
        self.assertEqual(resolve_something.select_related, [])
        self.assertEqual(resolve_something.prefetch_related, [])
        self.assertEqual(resolve_something.only, [])


class ComputedFieldHintsExtractionTestCase(TestCase):
    """Tests para get_computed_field_hints"""

    def setUp(self):
        """Setup para cada test"""
        self.registry = RegistryGlobal()

    def test_get_computed_field_hints_basic(self):
        """Test que get_computed_field_hints extrae hints correctamente"""

        class TestType(DjangoModelCruddals):
            display_name = graphene.String()

            @resolver_hints(select_related=['oneToOneField'], only=['name'])
            def resolve_display_name(self, info):
                return self.name

            class Meta:
                model = ModelC
                registry = self.registry

        # Extraer hints
        hints = get_computed_field_hints(self.registry, ModelC)

        # Verificar que se extrajeron correctamente
        self.assertIn('display_name', hints)
        self.assertEqual(hints['display_name']['select_related'], ['oneToOneField'])
        self.assertEqual(hints['display_name']['only'], ['name'])
        self.assertEqual(hints['display_name']['prefetch_related'], [])

    def test_get_computed_field_hints_multiple_fields(self):
        """Test que get_computed_field_hints maneja múltiples computed fields"""

        class TestType(DjangoModelCruddals):
            display_name = graphene.String()
            upper_name = graphene.String()

            @resolver_hints(only=['name'])
            def resolve_display_name(self, info):
                return self.name

            @resolver_hints(only=['name'])
            def resolve_upper_name(self, info):
                return self.name.upper()

            class Meta:
                model = ModelC
                registry = self.registry

        hints = get_computed_field_hints(self.registry, ModelC)

        # Verificar todos los hints
        self.assertEqual(len(hints), 2)
        self.assertIn('display_name', hints)
        self.assertIn('upper_name', hints)

    def test_get_computed_field_hints_no_hints(self):
        """Test que get_computed_field_hints no retorna campos sin decorador"""

        class TestType(DjangoModelCruddals):
            with_hint = graphene.String()
            without_hint = graphene.String()

            @resolver_hints(only=['name'])
            def resolve_with_hint(self, info):
                return self.name

            # Sin decorador
            def resolve_without_hint(self, info):
                return "no hint"

            class Meta:
                model = ModelC
                registry = self.registry

        hints = get_computed_field_hints(self.registry, ModelC)

        # Solo debe retornar el campo con hints
        self.assertEqual(len(hints), 1)
        self.assertIn('with_hint', hints)
        self.assertNotIn('without_hint', hints)

    def test_get_computed_field_hints_excludes_model_fields(self):
        """Test que get_computed_field_hints no incluye model fields"""

        class TestType(DjangoModelCruddals):
            computed_field = graphene.String()

            @resolver_hints(only=['name'])
            def resolve_computed_field(self, info):
                return self.name

            class Meta:
                model = ModelC
                registry = self.registry

        hints = get_computed_field_hints(self.registry, ModelC)

        # Solo debe incluir computed fields, no model fields
        self.assertIn('computed_field', hints)
        # 'name' es un model field, no debe aparecer en hints
        self.assertNotIn('name', hints)



class BackwardCompatibilityTestCase(TestCase):
    """Tests para asegurar retrocompatibilidad completa"""

    def setUp(self):
        self.registry = RegistryGlobal()

    def test_types_without_computed_fields_still_work(self):
        """Test que Types sin computed fields siguen funcionando"""

        class SimpleType(DjangoModelCruddals):
            # Solo model fields, sin computed fields
            class Meta:
                model = ModelC
                registry = self.registry

        # No debe lanzar excepciones
        hints = get_computed_field_hints(self.registry, ModelC)
        self.assertEqual(len(hints), 0)

    def test_computed_fields_without_hints_work(self):
        """Test que computed fields sin @resolver_hints siguen funcionando"""

        class MixedType(DjangoModelCruddals):
            with_hint = graphene.String()
            without_hint = graphene.String()

            @resolver_hints(only=['name'])
            def resolve_with_hint(self, info):
                return self.name

            # Sin decorador
            def resolve_without_hint(self, info):
                return "no hint"

            class Meta:
                model = ModelC
                registry = self.registry

        hints = get_computed_field_hints(self.registry, ModelC)

        # Solo el campo con hint debe aparecer
        self.assertIn('with_hint', hints)
        self.assertNotIn('without_hint', hints)

    def test_existing_queries_still_work(self):
        """Test que queries existentes sin @resolver_hints siguen funcionando"""

        # Este test verifica que el código sin decorador sigue funcionando
        class StandardType(DjangoModelCruddals):
            class Meta:
                model = ModelC
                registry = self.registry

        # No debe haber excepciones al obtener hints para un Type standard
        hints = get_computed_field_hints(self.registry, ModelC)
        self.assertIsInstance(hints, dict)

    def test_error_handling_graceful(self):
        """Test que errores en hints no rompen el sistema"""

        # get_computed_field_hints debe manejar errores gracefully
        hints = get_computed_field_hints(self.registry, ModelC)

        # Incluso sin Type registrado, no debe lanzar excepción
        self.assertIsInstance(hints, dict)
