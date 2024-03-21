from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.
class Menu(models.Model):
    name = models.CharField(
        max_length=100,
        help_text='The name of the menu'
    )
    restaurant = models.ForeignKey(
        "restaurant.Restaurant",
        on_delete=models.CASCADE,
        related_name='menus',
        help_text='The restaurant that the menu is a part of',
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        default=True,
        help_text='The status for enabling or disabling'
    )
    schedules = GenericRelation(
        'core.Schedule', 
        related_query_name='menus'
    )
    # -menu_items = ReverseManyToOneRel

class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='menu_items',
        help_text='The menu that this item is a part of'
    )
    name = models.CharField(
        max_length=100,
        help_text='The name of the menu item'
    )
    description = models.TextField(
        help_text='The description of the menu item'
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text='The price of the menu item'
    )
    is_active = models.BooleanField(
        default=True,
        help_text='The status for enabling or disabling'
    )

