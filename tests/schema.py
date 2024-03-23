# -*- coding: utf-8 -*-
import graphene

from .generate_schema.schema import (
    Query as generateSchemaQuery,
    Mutation as generateSchemaMutation,
)

class Query(
    generateSchemaQuery,
    graphene.ObjectType,
):
    pass


class Mutation(
    generateSchemaMutation,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
schema_no_camelcase = graphene.Schema( query=Query, mutation=Mutation, auto_camelcase=False )
