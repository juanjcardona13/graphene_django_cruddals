
#  🏁  Quick start

## Install

Hey there! Ready to start your project with graphene_django_cruddals? Awesome! Installing it is a easy. Just follow these steps:

1. Open up your favorite terminal.

2. Copy and paste the following command:
  `pip install graphene_django_cruddals`

***Everything is ready!***

## Basic usage

To use it, simply create a new class that inherits "`DjangoModelCruddals`"
Suppose we have the following model.

```python
  class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
```

Then we can create a complete CRUD+DALS with the following code

```python
class CruddalsRestaurant(DjangoModelCruddals):
    class Meta:
        model = Restaurant
```

Now you can use the `schema` that was generated for you

```python
schema = CruddalsRestaurant.Schema
```

or use in your root `Query` and `Mutation`

```python
class Query(
    # ... your others queries
    CruddalsRestaurant.Query,
    graphene.ObjectType,
):
    pass


class Mutation(
    # ... your others mutations
    CruddalsRestaurant.Mutation,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema( query=Query, mutation=Mutation, )
```

and this is it, now you can go to Graphiql or your favorite graphql client and see the new queries and mutations that graphene django cruddals made for you

## Not working?

1. Don't forget to set the `graphene_django` in your project
2. Don't forget to set the url for the graphql view in your project


