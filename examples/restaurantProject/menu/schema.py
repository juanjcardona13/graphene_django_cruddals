

from graphene_django_cruddals.main import CruddalsModel
from menu.models import Menu


class CruddalsMenu(CruddalsModel):
    class Meta:
        model = Menu


schema = CruddalsMenu.schema
