import inspect
import warnings
from typing import Type

import graphene
from django.db.models import Model as DjangoModel
from graphene.relay import Connection, Node
from graphene.types.objecttype import ObjectType, ObjectTypeOptions


ALL_FIELDS = "__all__"


def validate_fields(type_, model, fields, only_fields, exclude_fields):
    # Validate the given fields against the model's fields and custom fields
    all_field_names = set(fields.keys())
    only_fields = only_fields if only_fields is not ALL_FIELDS else ()
    for name in only_fields or ():
        if name in all_field_names:
            continue

        if hasattr(model, name):
            warnings.warn(
                (
                    'Field name "{field_name}" matches an attribute on Django model "{app_label}.{object_name}" '
                    "but it's not a model field so Graphene cannot determine what type it should be. "
                    'Either define the type of the field on DjangoObjectType "{type_}" or remove it from the "fields" list.'
                ).format(
                    field_name=name,
                    app_label=model._meta.app_label,
                    object_name=model._meta.object_name,
                    type_=type_,
                )
            )

        else:
            warnings.warn(
                (
                    'Field name "{field_name}" doesn\'t exist on Django model "{app_label}.{object_name}". '
                    'Consider removing the field from the "fields" list of DjangoObjectType "{type_}" because it has no effect.'
                ).format(
                    field_name=name,
                    app_label=model._meta.app_label,
                    object_name=model._meta.object_name,
                    type_=type_,
                )
            )

    # Validate exclude fields
    for name in exclude_fields or ():
        if name in all_field_names:
            # Field is a custom field
            warnings.warn(
                (
                    'Excluding the custom field "{field_name}" on DjangoObjectType "{type_}" has no effect. '
                    'Either remove the custom field or remove the field from the "exclude" list.'
                ).format(field_name=name, type_=type_)
            )
        else:
            if not hasattr(model, name):
                warnings.warn(
                    (
                        'Django model "{app_label}.{object_name}" does not have a field or attribute named "{field_name}". '
                        'Consider removing the field from the "exclude" list of DjangoObjectType "{type_}" because it has no effect'
                    ).format(
                        field_name=name,
                        app_label=model._meta.app_label,
                        object_name=model._meta.object_name,
                        type_=type_,
                    )
                )


def is_valid_django_model(model):
    return inspect.isclass(model) and issubclass(model, DjangoModel)


class DjangoObjectTypeOptions(ObjectTypeOptions):
    model = None  # type: Type[DjangoModel]
    connection = None  # type: Type[Connection]

    filter_fields = ()
    filterset_class = None


class DjangoObjectType(ObjectType):
    @classmethod
    def __init_subclass_with_meta__(
        cls,
        model=None,
        
        filter_fields=None,
        filterset_class=None,
        connection=None,
        connection_class=None,
        use_connection=None,
        interfaces=(),
        _meta=None,
        **options,
    ):
        # region === validations
        assert is_valid_django_model(model), ( 'You need to pass a valid Django Model in {}.Meta, received "{}".' ).format(cls.__name__, model)
        if filter_fields and filterset_class:
            raise Exception("Can't set both filter_fields and filterset_class")
        # endregion


        if use_connection is None and interfaces:
            use_connection = any(
                issubclass(interface, Node) for interface in interfaces
            )
        if use_connection and not connection:
            if not connection_class:
                connection_class = Connection
            connection = connection_class.create_type(
                "{}Connection".format(options.get("name") or cls.__name__), node=cls
            )
        if connection is not None:
            assert issubclass(connection, Connection), (
                "The connection must be a Connection. Received {}"
            ).format(connection.__name__)

        if not _meta:
            _meta = DjangoObjectTypeOptions(cls)

        _meta.model = model
        _meta.connection = connection
        _meta.filter_fields = filter_fields
        _meta.filterset_class = filterset_class

        super().__init_subclass_with_meta__( _meta=_meta, interfaces=interfaces, **options )

        # Validate fields
        # validate_fields(cls, model, _meta.fields, fields, exclude) #TODO


    def resolve_id(self, info):
        return self.pk

    @classmethod
    def is_type_of(cls, root, info):
        if isinstance(root, cls):
            return True
        if not is_valid_django_model(root.__class__):
            raise Exception(('Received incompatible instance "{}".').format(root))

        if cls._meta.model._meta.proxy:
            model = root._meta.model
        else:
            model = root._meta.model._meta.concrete_model

        return model == cls._meta.model

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset

    @classmethod
    def get_node(cls, info, id):
        queryset = cls.get_queryset(cls._meta.model.objects, info)
        try:
            return queryset.get(pk=id)
        except cls._meta.model.DoesNotExist:
            return None


class ErrorType(ObjectType):
    field = graphene.String(required=True)
    messages = graphene.List(graphene.NonNull(graphene.String), required=True)

    @classmethod
    def from_errors(cls, errors):
        from graphene_django_cruddals.utils import camelize

        data = camelize(errors) if True else errors
        return [cls(field=key, messages=value) for key, value in data.items()]


class ErrorsType(graphene.ObjectType):
    object_position = graphene.String()
    errors = graphene.List(ErrorType)

    @classmethod
    def from_errors(cls, object_position, errors):
        return cls(object_position=object_position, errors=errors)
