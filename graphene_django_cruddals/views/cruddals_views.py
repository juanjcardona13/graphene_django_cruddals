import importlib
import os
import shutil

from django.conf import settings
from django.core.management import call_command
from django.test import override_settings

from graphene_django_cruddals.views.file_upload_graphql_view import FileUploadGraphQLView

CRUDDALS_SCHEMA = None


class CRUDDALSView:
    """
    A class that provides views for CRUD operations in the Cruddals system.

    This class provides two class methods:
    - _execute_test_cruddals: This method executes tests for the Cruddals system. 
        It creates a temporary copy of the URL configuration file, 
        runs tests that match the pattern "cruddals_test.py", and then deletes the temporary file.

    - as_view: This method returns a view for file uploads in the Cruddals system. 
        If the 'generate_cruddals_files_client' argument is True, 
        it also generates files for the client schema.

    Attributes:
    - schema: The schema to use for the view. Defaults to None.
    
    - generate_cruddals_files_client: A boolean that determines whether 
        to generate files for the client schema. Defaults to False.
    """
    @classmethod
    def _execute_test_cruddals(self):
        path_to_urls = settings.ROOT_URLCONF
        ls_path_to_urls = path_to_urls.split(".")
        name_file = ls_path_to_urls[-1]
        modulo = importlib.import_module(path_to_urls)
        ruta_archivo = modulo.__file__
        origen = ruta_archivo
        destino = ruta_archivo.replace(name_file, f"temp_{name_file}")
        shutil.copy(origen, destino)
        ls_path_to_urls[-1] = f"temp_{name_file}"
        new_path_to_urls = ".".join(ls_path_to_urls)

        @override_settings(ROOT_URLCONF=new_path_to_urls)
        def internal_execute_test_cruddals():
            """
            1. Como tengo las apps que cruddalizo, entonces puedo decir que creen archivos con el siguiente nombre cruddals_test.py
            """
            call_command("test", "--pattern=cruddals_test.py")

            print("----------------------------------")
            print("🎉🎉🎉=CRUDDALS IS WORKING=🎉🎉🎉")
            print("----------------------------------")

        internal_execute_test_cruddals()
        if os.path.exists(destino):
            os.remove(destino)

    @classmethod
    def as_view(self, schema=None, generate_cruddals_files_client=False, **kwargs):
        
        if generate_cruddals_files_client:
            from ..utils_for_client.build_for_client import build_files_for_client_schema_cruddals

            build_files_for_client_schema_cruddals(schema)

        return FileUploadGraphQLView.as_view(schema=schema, **kwargs)
