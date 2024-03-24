

from graphene_django_cruddals.main import CruddalsModel
import graphene
from .models import *


class CruddalsMenu(CruddalsModel):
    class Meta:
        model = Menu




class CruddalsModelA(CruddalsModel):
    class Meta:
        model = ModelA

class CruddalsModelB(CruddalsModel):
    class Meta:
        model = ModelB

class CruddalsModelC(CruddalsModel):
    class Meta:
        model = ModelC

class CruddalsModelD(CruddalsModel):
    class Meta:
        model = ModelD

class CruddalsModelE(CruddalsModel):
    class Meta:
        model = ModelE

class CruddalsModelF(CruddalsModel):
    class Meta:
        model = ModelF


class Query(
    CruddalsModelA.Query,
    CruddalsModelB.Query,
    CruddalsModelC.Query,
    CruddalsModelD.Query,
    CruddalsModelE.Query,
    CruddalsModelF.Query,
    graphene.ObjectType,
):
    pass


class Mutation(
    CruddalsModelA.Mutation,
    CruddalsModelB.Mutation,
    CruddalsModelC.Mutation,
    CruddalsModelD.Mutation,
    CruddalsModelE.Mutation,
    CruddalsModelF.Mutation,
    graphene.ObjectType,
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation, types=[CruddalsModelA.meta.model_as_input_object_type])