# Quick start

## Installation

For installing graphene_django_cruddals, just run this command in your shell

> `pip install graphene_django_cruddals`

## Basic usage

To use it, simply create a new class that inherits "`CruddalsModel`"
Suppose we have the following model.

```python
  class Restaurant(models.Model):
    name = models.CharField(
        max_length=100,
        help_text='The name of the restaurant'
    )
    slug = models.SlugField(
        help_text='The slug of the restaurant',
        blank=True,
        null=True,
        unique=True,
        editable=False,
        max_length=100
    )
```

Then we can create a complete CRUD+DALS with the following code

```python
class CruddalsRestaurant(CruddalsModel):
    class Meta:
        model = Restaurant
```

Now you can use the `schema` that was generated for you,

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

and this is it, now you can go to Graphiql and see the new queries and mutations that graphene django cruddals made for you

## Documentation

Coming soon!
