from graphene_django_cruddals.views.file_upload_graphql_view import (
    FileUploadGraphQLView,
)


class CRUDDALSView:
    """
    A class that provides views for CRUD operations in the Cruddals system.

    This class provides one class methods:
    - as_view: This method returns a view for file uploads in the Cruddals system.
        If the 'generate_cruddals_files_client' argument is True,
        it also generates files for the client schema.

    Attributes:
    - schema: The schema to use for the view. Defaults to None.

    - generate_cruddals_files_client: A boolean that determines whether
        to generate files for the client schema. Defaults to False.
    """

    @classmethod
    def as_view(cls, schema=None, generate_cruddals_files_client=False, **kwargs):
        if generate_cruddals_files_client:
            from ..utils.build_for_client import build_files_for_client_schema_cruddals

            build_files_for_client_schema_cruddals(schema)

        return FileUploadGraphQLView.as_view(schema=schema, **kwargs)
