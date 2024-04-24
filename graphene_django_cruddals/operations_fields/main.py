from functools import partial

from graphene.types import Field, List, NonNull
from graphene_django_cruddals.operations_fields.default_resolvers import (
    default_activate_field_resolver,
    default_create_update_resolver,
    default_deactivate_field_resolver,
    default_delete_field_resolver,
    default_list_field_resolver,
    default_read_field_resolver,
    default_search_field_resolver,
)
from graphene_django_cruddals.operations_fields.utils import get_object_type_payload
from graphene_django_cruddals.registry_global import get_global_registry
from graphene_django_cruddals.utils.utils import convert_model_to_model_form


class DjangoCreateUpdateField(Field):
    def __init__(self, _type, name_for_output_type, *args, **kwargs):
        if isinstance(_type, NonNull):
            _type = _type.of_type

        payload_type = get_object_type_payload(
            model_object_type=_type, name_for_output_type=name_for_output_type
        )

        super().__init__(payload_type, *args, **kwargs)

    @property
    def _underlying_type(self):
        _type = self._type
        return _type.objects._underlying_type

    @property
    def model(self):
        return self._underlying_type._meta.model

    @property
    def model_form(self):
        return convert_model_to_model_form(model=self.model)

    def get_manager(self):
        return self.model._default_manager

    def wrap_resolve(self, parent_resolver):
        resolver = super().wrap_resolve(parent_resolver)
        if resolver is not None:
            return resolver
        _type = self.type
        if isinstance(_type, NonNull):
            _type = _type.of_type
        registry = get_global_registry()
        return partial(
            default_create_update_resolver, self.model, self.model_form, registry
        )


class DjangoReadField(Field):
    def __init__(self, _type, *args, **kwargs):
        if isinstance(_type, NonNull):
            _type = _type.of_type
        super().__init__(_type, *args, **kwargs)

    @property
    def _underlying_type(self):
        _type = self._type
        while hasattr(_type, "of_type"):
            _type = _type.of_type
        return _type

    @property
    def model(self):
        return self._underlying_type._meta.model

    def get_manager(self):
        return self.model._default_manager

    def wrap_resolve(self, parent_resolver):
        resolver = super().wrap_resolve(parent_resolver)
        if resolver is not None:
            return resolver
        _type = self.type
        if isinstance(_type, NonNull):
            _type = _type.of_type
        django_object_type = _type
        return partial(
            default_read_field_resolver, django_object_type, self.get_manager()
        )


class DjangoDeleteField(Field):
    def __init__(self, _type, name_for_output_type, *args, **kwargs):
        if isinstance(_type, NonNull):
            _type = _type.of_type

        payload_type = get_object_type_payload(
            model_object_type=_type,
            name_for_output_type=name_for_output_type,
            include_success=True,
        )

        super().__init__(payload_type, *args, **kwargs)

    @property
    def _underlying_type(self):
        _type = self._type
        return _type.objects._underlying_type

    @property
    def model(self):
        return self._underlying_type._meta.model

    def get_manager(self):
        return self.model._default_manager

    def wrap_resolve(self, parent_resolver):
        resolver = super().wrap_resolve(parent_resolver)
        if resolver is not None:
            return resolver
        _type = self.type
        if isinstance(_type, NonNull):
            _type = _type.of_type

        return partial(default_delete_field_resolver, self.model)


class DjangoDeactivateField(Field):
    def __init__(self, _type, name_for_output_type, *args, **kwargs):
        if isinstance(_type, NonNull):
            _type = _type.of_type

        payload_type = get_object_type_payload(
            model_object_type=_type, name_for_output_type=name_for_output_type
        )

        super().__init__(payload_type, *args, **kwargs)

    @property
    def _underlying_type(self):
        _type = self._type
        return _type.objects._underlying_type

    @property
    def model(self):
        return self._underlying_type._meta.model

    def get_manager(self):
        return self.model._default_manager

    def wrap_resolve(self, parent_resolver):
        resolver = super().wrap_resolve(parent_resolver)
        if resolver is not None:
            return resolver
        _type = self.type
        if isinstance(_type, NonNull):
            _type = _type.of_type
        return partial(
            default_deactivate_field_resolver, self.model, "is_active"
        )  # TODO - Debo de mirar esto donde lo voy a cuadrar para que sea global


class DjangoActivateField(Field):
    def __init__(self, _type, name_for_output_type, *args, **kwargs):
        if isinstance(_type, NonNull):
            _type = _type.of_type

        payload_type = get_object_type_payload(
            model_object_type=_type, name_for_output_type=name_for_output_type
        )

        super().__init__(payload_type, *args, **kwargs)

    @property
    def _underlying_type(self):
        _type = self._type
        return _type.objects._underlying_type

    @property
    def model(self):
        return self._underlying_type._meta.model

    def get_manager(self):
        return self.model._default_manager

    def wrap_resolve(self, parent_resolver):
        resolver = super().wrap_resolve(parent_resolver)
        if resolver is not None:
            return resolver
        _type = self.type
        if isinstance(_type, NonNull):
            _type = _type.of_type
        return partial(
            default_activate_field_resolver, self.model, "is_active"
        )  # TODO - Debo de mirar esto donde lo voy a cuadrar para que sea global


class DjangoListField(Field):
    def __init__(self, _type, *args, **kwargs):
        if isinstance(_type, NonNull):
            _type = _type.of_type

        # Django would never return a Set of None  vvvvvvv
        super().__init__(List(NonNull(_type)), *args, **kwargs)

    @property
    def _underlying_type(self):
        _type = self._type
        while hasattr(_type, "of_type"):
            _type = _type.of_type
        return _type

    @property
    def model(self):
        return self._underlying_type._meta.model

    def get_manager(self):
        return self.model._default_manager

    def wrap_resolve(self, parent_resolver):
        resolver = super().wrap_resolve(parent_resolver)
        if resolver is not None and not hasattr(resolver, "func"):
            return resolver
        _type = self.type
        if isinstance(_type, NonNull):
            _type = _type.of_type
        django_object_type = _type.of_type.of_type
        return partial(
            default_list_field_resolver,
            django_object_type,
            resolver,
            self.get_manager(),
        )


class DjangoSearchField(Field):
    def __init__(self, _type, *args, **kwargs):
        if isinstance(_type, NonNull):
            _type = _type.of_type

        # Django would never return a Set of None
        super().__init__(_type, *args, **kwargs)

    @property
    def _underlying_type(self):
        _type = self._type
        return _type.objects._underlying_type

    @property
    def model(self):
        return self._underlying_type._meta.model

    def get_manager(self):
        return self.model._default_manager

    def wrap_resolve(self, parent_resolver):
        resolver = super().wrap_resolve(parent_resolver)
        if resolver is not None and not hasattr(resolver, "func"):
            return resolver
        _type = self.type
        if isinstance(_type, NonNull):
            _type = _type.of_type
        django_object_type = _type.objects._underlying_type
        return partial(
            default_search_field_resolver,
            _type,
            django_object_type,
            resolver,
            self.get_manager(),
        )
