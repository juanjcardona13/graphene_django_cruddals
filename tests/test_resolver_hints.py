from django.test import TestCase
from graphene_cruddals import RegistryGlobal

import graphene
from graphene_django_cruddals import (
    DjangoModelCruddals,
    get_computed_field_hints,
    resolver_hints,
)
from tests.models import ModelC


class ResolverHintsDecoratorTestCase(TestCase):
    """Basic tests for the @resolver_hints decorator"""

    def test_resolver_hints_decorator_basic(self):
        """Test that the @resolver_hints decorator adds attributes correctly"""

        @resolver_hints(select_related=["profile"], only=["first_name", "last_name"])
        def resolve_full_name(self, info):
            return f"{self.first_name} {self.last_name}"

        self.assertTrue(hasattr(resolve_full_name, "have_resolver_hints"))
        self.assertEqual(resolve_full_name.select_related, ["profile"])
        self.assertEqual(resolve_full_name.only, ["first_name", "last_name"])
        self.assertEqual(resolve_full_name.prefetch_related, [])

    def test_resolver_hints_decorator_all_params(self):
        """Test that the decorator handles all parameters"""

        @resolver_hints(
            select_related=["author", "category"],
            prefetch_related=["tags", "comments"],
            only=["title", "author__name"],
        )
        def resolve_summary(self, info):
            return "summary"

        self.assertTrue(resolve_summary.have_resolver_hints)
        self.assertEqual(resolve_summary.select_related, ["author", "category"])
        self.assertEqual(resolve_summary.prefetch_related, ["tags", "comments"])
        self.assertEqual(resolve_summary.only, ["title", "author__name"])

    def test_resolver_hints_decorator_empty(self):
        """Test that the decorator works without parameters"""

        @resolver_hints()
        def resolve_something(self, info):
            return "something"

        self.assertTrue(resolve_something.have_resolver_hints)
        self.assertEqual(resolve_something.select_related, [])
        self.assertEqual(resolve_something.prefetch_related, [])
        self.assertEqual(resolve_something.only, [])


class ComputedFieldHintsExtractionTestCase(TestCase):
    """Tests for get_computed_field_hints"""

    def setUp(self):
        """Setup for each test"""
        self.registry = RegistryGlobal()

    def test_get_computed_field_hints_basic(self):
        """Test that get_computed_field_hints extracts hints correctly"""

        class TestType(DjangoModelCruddals):
            display_name = graphene.String()

            @resolver_hints(select_related=["oneToOneField"], only=["name"])
            def resolve_display_name(self, info):
                return self.name

            class Meta:
                model = ModelC
                registry = self.registry

        hints = get_computed_field_hints(self.registry, ModelC)

        self.assertIn("display_name", hints)
        self.assertEqual(hints["display_name"]["select_related"], ["oneToOneField"])
        self.assertEqual(hints["display_name"]["only"], ["name"])
        self.assertEqual(hints["display_name"]["prefetch_related"], [])

    def test_get_computed_field_hints_multiple_fields(self):
        """Test that get_computed_field_hints handles multiple computed fields"""

        class TestType(DjangoModelCruddals):
            display_name = graphene.String()
            upper_name = graphene.String()

            @resolver_hints(only=["name"])
            def resolve_display_name(self, info):
                return self.name

            @resolver_hints(only=["name"])
            def resolve_upper_name(self, info):
                return self.name.upper()

            class Meta:
                model = ModelC
                registry = self.registry

        hints = get_computed_field_hints(self.registry, ModelC)

        self.assertEqual(len(hints), 2)
        self.assertIn("display_name", hints)
        self.assertIn("upper_name", hints)

    def test_get_computed_field_hints_no_hints(self):
        """Test that get_computed_field_hints does not return fields without decorator"""

        class TestType(DjangoModelCruddals):
            with_hint = graphene.String()
            without_hint = graphene.String()

            @resolver_hints(only=["name"])
            def resolve_with_hint(self, info):
                return self.name

            def resolve_without_hint(self, info):
                return "no hint"

            class Meta:
                model = ModelC
                registry = self.registry

        hints = get_computed_field_hints(self.registry, ModelC)

        self.assertEqual(len(hints), 1)
        self.assertIn("with_hint", hints)
        self.assertNotIn("without_hint", hints)

    def test_get_computed_field_hints_excludes_model_fields(self):
        """Test that get_computed_field_hints does not include model fields"""

        class TestType(DjangoModelCruddals):
            computed_field = graphene.String()

            @resolver_hints(only=["name"])
            def resolve_computed_field(self, info):
                return self.name

            class Meta:
                model = ModelC
                registry = self.registry

        hints = get_computed_field_hints(self.registry, ModelC)

        self.assertIn("computed_field", hints)
        self.assertNotIn("name", hints)


class BackwardCompatibilityTestCase(TestCase):
    """Tests to ensure complete backward compatibility"""

    def setUp(self):
        self.registry = RegistryGlobal()

    def test_types_without_computed_fields_still_work(self):
        """Test that Types without computed fields still work"""

        class SimpleType(DjangoModelCruddals):
            class Meta:
                model = ModelC
                registry = self.registry

        hints = get_computed_field_hints(self.registry, ModelC)
        self.assertEqual(len(hints), 0)

    def test_computed_fields_without_hints_work(self):
        """Test that computed fields without @resolver_hints still work"""

        class MixedType(DjangoModelCruddals):
            with_hint = graphene.String()
            without_hint = graphene.String()

            @resolver_hints(only=["name"])
            def resolve_with_hint(self, info):
                return self.name

            def resolve_without_hint(self, info):
                return "no hint"

            class Meta:
                model = ModelC
                registry = self.registry

        hints = get_computed_field_hints(self.registry, ModelC)

        self.assertIn("with_hint", hints)
        self.assertNotIn("without_hint", hints)

    def test_existing_queries_still_work(self):
        """Test that existing queries without @resolver_hints still work"""

        class StandardType(DjangoModelCruddals):
            class Meta:
                model = ModelC
                registry = self.registry

        hints = get_computed_field_hints(self.registry, ModelC)
        self.assertIsInstance(hints, dict)

    def test_error_handling_graceful(self):
        """Test that errors in hints do not break the system"""

        hints = get_computed_field_hints(self.registry, ModelC)

        self.assertIsInstance(hints, dict)
