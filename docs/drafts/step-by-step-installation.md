# 🛠️ Installation




##   🔧 Install Graphene Django CRUDDALS

To install Graphene Django CRUDDALS, follow these steps:

Install Graphene Django CRUDDALS with the virtual environment activated and in the project folder
  `pip install graphene-django-cruddals`

In the schema.py file of the app, replace all content, import the DjangoModelCruddals class, and create a class that inherits from it

```python
  from graphene_django_cruddals import DjangoModelCruddals
  from .models import MyModel

  class CruddalsMyModel(DjangoModelCruddals):
      class Meta:
          model = MyModel
```

In the root schema, import the class created in the previous step and add it to the Query class, and the
mutations for your model also was added, so you now can create the Mutation class
```python
  from myapp.schema import CruddalsMyModel

  class Query(CruddalsMyModel.Query, graphene.ObjectType):
      pass

  class Mutation(CruddalsMyModel.Mutation, graphene.ObjectType):
      pass

  schema = graphene.Schema(query=Query, mutation=Mutation)
```

Run the server
  `python manage.py runserver`

Open your browser and go to `http://localhost:8000/graphql/`

You can now run queries and mutations that were created by the Graphene Django CRUDDALS package 🎉 🎊 🥳

