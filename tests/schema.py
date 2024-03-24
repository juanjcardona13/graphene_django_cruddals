# -*- coding: utf-8 -*-
import graphene

from .cruddals_model.schema import (
    CruddalsModelA,
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


schema = graphene.Schema(query=Query, mutation=Mutation, types=[CruddalsModelA.meta.model_as_input_object_type])
schema_no_camelcase = graphene.Schema( query=Query, mutation=Mutation, types=[CruddalsModelA.meta.model_as_input_object_type], auto_camelcase=False )
