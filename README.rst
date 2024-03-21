
Quickstart
----------

For installing cruddals, just run this command in your shell

.. code:: bash

    pip install graphene_django_cruddals

Settings
~~~~~~~~

.. code:: python

    INSTALLED_APPS = (
        # ...
        'graphene_django_cruddals',
    )

    CRUDDALS = {
        "APPS": "__all__", # Or list of your apps ["appname1", "appname2", ...]
    }

Urls
~~~~

We need to set up a ``GraphQL`` endpoint in our Django app, so we can
serve the queries and mutations.

.. code:: python

    from django.conf.urls import path
    from graphene_django_cruddals.views import CRUDDALSView

    urlpatterns = [
        # ...
        path('graphql/', CRUDDALSView.as_view(graphiql=True)),
    ]

Ready
--------

Then you can simply go to you url GraphQL, and could see all queries and mutations that graphene_django_cruddals make for you

