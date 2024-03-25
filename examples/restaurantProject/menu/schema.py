from graphene_django_cruddals.main import CruddalsModel
import graphene
from .models import *


class CruddalsMenu(CruddalsModel):
    class Meta:
        model = Menu


schema = graphene.Schema(query=CruddalsMenu.Query, mutation=CruddalsMenu.Mutation)
