import graphene
from graphene_django import DjangoObjectType

from restaurant.models import Restaurant, Table

class RestaurantType(DjangoObjectType):
    class Meta:
        model = Restaurant

class TableType(DjangoObjectType):
    class Meta:
        model = Table

class Query(graphene.ObjectType):
    all_tables = graphene.List(TableType)
    restaurant_by_name = graphene.Field(RestaurantType, name=graphene.String(required=True))

    def resolve_all_tables(self, info):
        # We can easily optimize query count in the resolve method
        return Table.objects.all() # select_related("restaurant")

    def resolve_restaurant_by_name(self, info, name):
        try:
            return Restaurant.objects.get(name=name)
        except Restaurant.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)

# print("=========>", Query)
# print("=========>", TableType)
# print("=========>", RestaurantType)
# print("=========>", schema)