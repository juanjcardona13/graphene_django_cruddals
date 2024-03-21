from django.contrib import admin
from django.forms import Textarea
from django.db import models
from .models import Menu, MenuItem
import nested_admin

# Register your models here.
class MenuItemInline(nested_admin.NestedTabularInline):
    model = MenuItem
    extra = 0
    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(
                attrs={'rows': 2, 'cols': 30}
            )
        }
    }

class MenuInline(nested_admin.NestedTabularInline):
    inlines = [MenuItemInline]
    model = Menu
    extra = 0

@admin.register(Menu)
class MenuAdmin(nested_admin.NestedModelAdmin):
    inlines = [MenuItemInline]
    list_display_links = ("id", "name",)
    list_display = ("id", "name", "is_active")
    list_filter = ("name", "is_active")
    search_fields = ("id", "name")

    fieldsets = (
        (
            "Main",
            {
                "fields": (
                    ("name", "is_active"),
                    "restaurant",
                )
            },
        ),
    )

@admin.register(MenuItem)
class MenuItemAdmin(nested_admin.NestedModelAdmin):
    list_display_links = ("id", "name",)
    list_display = ("id", "name", "price", "is_active")
    list_filter = ("name", "price", "is_active")
    search_fields = ("id", "name")

    fieldsets = (
        (
            "Main",
            {
                "fields": (
                    ("menu", "name", "price", "is_active"),
                    "description",
                )
            },
        ),
    )
