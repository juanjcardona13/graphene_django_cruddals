from simpleCruddalsModel.schema import (
    CruddalsModelA,
    Mutation as simpleCruddalsModelMutation,
    Query as simpleCruddalsModelQuery,
)

import graphene


class Query(
    simpleCruddalsModelQuery,
    graphene.ObjectType,
):
    pass


class Mutation(
    simpleCruddalsModelMutation,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
    types=[CruddalsModelA.meta.model_as_input_object_type],
)
schema_no_camelcase = graphene.Schema(
    query=Query,
    mutation=Mutation,
    types=[CruddalsModelA.meta.model_as_input_object_type],
    auto_camelcase=False,
)
