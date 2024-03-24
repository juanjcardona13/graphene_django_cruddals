# -*- coding: utf-8 -*-
import graphene

from .cruddals_model.schema import (
    Query as cruddalsModelQuery,
    Mutation as cruddalsModelMutation,
)

class Query(
    cruddalsModelQuery,
    graphene.ObjectType,
):
    pass


class Mutation(
    cruddalsModelMutation,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
schema_no_camelcase = graphene.Schema( query=Query, mutation=Mutation, auto_camelcase=False )
