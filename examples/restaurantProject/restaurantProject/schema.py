import graphene
from graphene_django import DjangoObjectType

from menu.schema import CruddalsMenu
from restaurant.models import Restaurant, Table

class RestaurantType(DjangoObjectType):
    class Meta:
        model = Restaurant

class TableType(DjangoObjectType):
    class Meta:
        model = Table

# class Query(CruddalsMenu.Query, graphene.ObjectType):
class Query(graphene.ObjectType):
    # for field_name, graphene_field in CruddalsMenu.operation_fields_for_queries.items():
    #     locals()[field_name] = graphene_field

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