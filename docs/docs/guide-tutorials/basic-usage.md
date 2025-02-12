## 💡 Basic usage

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

and this is it, now you can go to Graphql and see the new queries and mutations that graphene django cruddals made for you