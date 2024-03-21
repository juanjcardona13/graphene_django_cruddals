from django.contrib import admin

from core.admin import RestaurantEmployeeProfileInline, ScheduleInline
from menu.admin import MenuInline
from .models import Restaurant, Table
import nested_admin

# Register your models here.
class TableInline(nested_admin.NestedTabularInline):
    model = Table
    extra = 0

@admin.register(Restaurant)
class RestaurantAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        TableInline,
        MenuInline,
        RestaurantEmployeeProfileInline,
        ScheduleInline,
    ]
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
                    ("email", "phone_number", ),
                    "website",
                    ("logo",),
                    "document",
                    ("created_at", "slug"),
                    # ("employees",),
                )
            },
        ),
    )
    exclude = ("employees",)
    readonly_fields = ("slug", "created_at",)

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display_links = ("id", "identifier",)
    list_display = ("id", "identifier", "status", "capacity", "is_active")
    search_fields = ("identifier", "status", "is_active")
    list_filter = ("id", "identifier")

    fieldsets = (
        (
            "Main",
            {
                "fields": (
                    ("identifier", "status", "capacity",),
                    ("restaurant",  "is_active"),
                )
            },
        ),
    )
