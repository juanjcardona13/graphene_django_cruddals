## Install Python

  To install or update Python on Ubuntu, follow these steps:

  - Update repositories and install the latest versions of package

    `sudo apt update && sudo apt upgrade -y`

  - Install the necessary dependencies to add the repository

    `sudo apt install software-properties-common -y`

  - Add the deadsnakes PPA to your sources list

    `sudo add-apt-repository ppa:deadsnakes/ppa`

  - Check for pre-installed Python

    `python --version`

  - Install via Package Manager

    ```bash

      sudo apt-get install python3

      # or if you want to install a specific version

      sudo apt-get install python3.8 # change the version number to the version you want to install

    ```

  - Verify installation

    `python3 --version`

  - Install pip

    `sudo apt install python3-pip`

  - Verify pip installation

    `pip3 --version`

  If you have another system such as Windows or Mac or if you want more detailed information about installing Python, you can see how to install it on this site [How To Install Python on Windows, macOS, and Linux](https://kinsta.com/knowledgebase/install-python/)

## Install Django

  To install Django, follow these steps:

  > you need to have Python installed on your system. If you have not installed Python, you can follow the steps in the previous section to install it.

  - Create the folder where you want to install Django

    `mkdir django_projects && cd django_projects`

  - Create a virtual environment

    `python3 -m venv myenv`

  - Activate the virtual environment

    `source myenv/bin/activate`

  - Install Django

    `pip install django`

  - Verify installation

    `django-admin --version`

### Create a Django project

  - Create a Django project

    `django-admin startproject myproject`

  - Change the directory to the project folder

    `cd myproject`

  - Run the server

    `python manage.py runserver`

  - Open your browser and go to `http://localhost:8000/`


### Create a Django app

  - Create a Django app

    `python manage.py startapp myapp`

  - Add the app to the installed apps in the settings.py file of the project

    > This file is located in the `myproject` folder

    ```python

      INSTALLED_APPS = [
        ...
        'myapp.apps.MyappConfig',
      ]

    ```

  - Create a model in the models.py file of the app

    > This file is located in the `myapp` folder

    ```python

      from django.db import models

      class MyModel(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()

    ```

  - Create a migration

    `python manage.py makemigrations`

  - Apply the migration

    `python manage.py migrate`

  - Create a superuser

    `python manage.py createsuperuser`

  - Run the server

    `python manage.py runserver`

  - Open your browser and go to `http://localhost:8000/admin/`


  - Log in with the superuser credentials you created


## Install Graphene Django

  To install Graphene Django, follow these steps:

  - Install Graphene Django with the virtual environment activated and in the project folder

    `pip install graphene-django`

  - Add `graphene_django` to the installed apps in the settings.py file of the project

    ```python

      INSTALLED_APPS = [
          ...
          'django.contrib.staticfiles', # Required for GraphiQL
          'graphene_django',
      ]

    ```

  - Create a schema.py file in the **app folder**

    ```python

      import graphene
      from graphene_django.types import DjangoObjectType
      from .models import MyModel

      class MyModelType(DjangoObjectType):
          class Meta:
              model = MyModel

      class Query(graphene.ObjectType):
          my_model = graphene.Field(MyModelType, id=graphene.Int())

          def resolve_my_model(self, info, **kwargs):
              id = kwargs.get('id')

              if id is not None:
                  return MyModel.objects.get(pk=id)

              return None

    ```

  - Create the root schema in the **project folder**

    ```python

      from myapp.schema import Query as MyAppQuery

      class Query(MyAppQuery, graphene.ObjectType):
          pass

      schema = graphene.Schema(query=Query)

    ```

  - Add the graphene URL to the project's urls.py file

    ```python

      from django.urls import path
      from graphene_django.views import GraphQLView
      from .schema import schema

      urlpatterns = [
          path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
      ]

    ```

  - Run the server

    `python manage.py runserver`

  - Open your browser and go to `http://localhost:8000/graphql/`


  - You can now run queries in the GraphiQL interface



## Install Graphene Django CRUDDALS

  To install Graphene Django CRUDDALS, follow these steps:

  - Install Graphene Django CRUDDALS with the virtual environment activated and in the project folder

    `pip install graphene-django-cruddals`

  - In the schema.py file of the app, replace all content, import the CruddalsModel class, and create a class that 
  inherits from it
    ```python

      from graphene_django_cruddals import CruddalsModel
      from .models import MyModel

      class CruddalsMyModel(CruddalsModel):
          class Meta:
              model = MyModel

    ```

  - In the root schema, import the class created in the previous step and add it to the Query class, and the 
  mutations for your model also was added, so you now can create the Mutation class
    ```python

      from myapp.schema import CruddalsMyModel

      class Query(CruddalsMyModel.Query, graphene.ObjectType):
          pass

      class Mutation(CruddalsMyModel.Mutation, graphene.ObjectType):
          pass
      
      schema = graphene.Schema(query=Query, mutation=Mutation)

    ```

  - Run the server

    `python manage.py runserver`

  - Open your browser and go to `http://localhost:8000/graphql/`


  - You can now run queries and mutations that were created by the Graphene Django CRUDDALS package 🎉 🎊 🥳

