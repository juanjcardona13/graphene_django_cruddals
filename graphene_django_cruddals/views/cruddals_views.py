from graphene_django_cruddals.views.file_upload_graphql_view import (
    FileUploadGraphQLView,
)


class CRUDDALSView:
    """
    A class that provides views for CRUD operations in the Cruddals system.

    This class provides one class methods:
    - as_view: This method returns a view for file uploads in the Cruddals system.

    Attributes:
    - schema: The schema to use for the view. Defaults to None.
    """

    @classmethod
    def as_view(cls, schema=None, **kwargs):
        return FileUploadGraphQLView.as_view(schema=schema, **kwargs)
