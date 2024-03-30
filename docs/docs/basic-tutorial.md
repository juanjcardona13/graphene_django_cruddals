## Install Python

To install or update Python on Ubuntu, follow these steps:

1. Update repositories and install the latest versions of package

   `sudo apt update && sudo apt upgrade -y`

2. Install the necessary dependencies to add the repository

   `sudo apt install software-properties-common -y`

3. Add the deadsnakes PPA to your sources list

   `sudo add-apt-repository ppa:deadsnakes/ppa`

4. Check for pre-installed Python

   `python --version`

5. Install via Package Manager

   ```bash
   sudo apt-get install python3

   # or if you want to install a specific version

   sudo apt-get install python3.8 # change the version number to the version you want to install
   ```

6. Verify installation

   `python3 --version`

7. Install pip

   `sudo apt install python3-pip`

8. Verify pip installation

   `pip3 --version`

If you have another system such as Windows or Mac or if you want more detailed information about installing Python, you can see how to install it on this site [How To Install Python on Windows, macOS, and Linux](https://kinsta.com/knowledgebase/install-python/)

## Install Django

To install Django, follow these steps:

> you need to have Python installed on your system. If you have not installed Python, you can follow the steps in the previous section to install it.

1. Create the folder where you want to install Django

   `mkdir django_projects && cd django_projects`

2. Create a virtual environment

   `python3 -m venv myenv`

3. Activate the virtual environment

   `source myenv/bin/activate`

4. Install Django

   `pip install django`

5. Verify installation

   `django-admin --version`

### Create a Django project

1. Create a Django project

   `django-admin startproject myproject`

2. Change the directory to the project folder

   `cd myproject`

3. Run the server

   `python manage.py runserver`

4. Open your browser and go to `http://localhost:8000/`

### Create a Django app

1. Create a Django app

   `python manage.py startapp myapp`

2. Add the app to the installed apps in the settings.py file of the project

   > This file is located in the `myproject` folder

   ```python
    INSTALLED_APPS = [
        ...
        'myapp.apps.MyappConfig',
    ]
   ```

3. Create a model in the models.py file of the app

   > This file is located in the `myapp` folder

   ```python
     from django.db import models

     class MyModel(models.Model):
         name = models.CharField(max_length=100)
         description = models.TextField()
   ```

4. Create a migration

   `python manage.py makemigrations`

5. Apply the migration

   `python manage.py migrate`

6. Create a superuser

   `python manage.py createsuperuser`

7. Run the server

   `python manage.py runserver`

8. Open your browser and go to `http://localhost:8000/admin/`

9. Log in with the superuser credentials you created

## Install Graphene Django

To install Graphene Django, follow these steps:

1. Install Graphene Django with the virtual environment activated and in the project folder

   `pip install graphene-django`

2. Add `graphene_django` to the installed apps in the settings.py file of the project

   ```python
    INSTALLED_APPS = [
        ...
        'django.contrib.staticfiles', # Required for GraphiQL
        'graphene_django',
    ]
   ```

3. Create a schema.py file in the **app folder**

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

4. Create the root schema in the **project folder**

```python
  from myapp.schema import Query as MyAppQuery

  class Query(MyAppQuery, graphene.ObjectType):
      pass

  schema = graphene.Schema(query=Query)
```

5. Add the graphene URL to the project's urls.py file

   ```python
     from django.urls import path
     from graphene_django.views import GraphQLView
     from .schema import schema

     urlpatterns = [
         path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
     ]
   ```

6. Run the server

   `python manage.py runserver`

7. Open your browser and go to `http://localhost:8000/graphql/`

8. You can now run queries in the GraphiQL interface


## Install Graphene Django CRUDDALS

To install Graphene Django CRUDDALS, follow these steps:

1. Install Graphene Django CRUDDALS with the virtual environment activated and in the project folder

   `pip install graphene-django-cruddals`

2. In the schema.py file of the app, replace all content, import the CruddalsModel class, and create a class that inherits from it

   ```python
     from graphene_django_cruddals import CruddalsModel
     from .models import MyModel

     class CruddalsMyModel(CruddalsModel):
         class Meta:
             model = MyModel
   ```

3. In the root schema, import the class created in the previous step and add it to the Query class, and the mutations for your model also was added, so you now can create the Mutation class

   ```python
     from myapp.schema import CruddalsMyModel

     class Query(CruddalsMyModel.Query, graphene.ObjectType):
         pass

      class Mutation(CruddalsMyModel.Mutation, graphene.ObjectType):
          pass
      
      schema = graphene.Schema(query=Query, mutation=Mutation)
   ```

4. Run the server

   `python manage.py runserver`

5. Open your browser and go to `http://localhost:8000/graphql/`

6. You can now run queries and mutations that were created by the Graphene Django CRUDDALS package 🎉 🎊 🥳
