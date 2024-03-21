from django.contrib import admin

from restaurant.models import Restaurant
from .models import EmployeeProfile, TimeSlot, Schedule
import nested_admin
from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.


class TimeSlotInline(nested_admin.NestedTabularInline):
    model = TimeSlot
    extra = 0

class RestaurantEmployeeProfileInline(nested_admin.NestedTabularInline):
    model = Restaurant.employees.through
    extra = 0

class ScheduleInline(GenericTabularInline, nested_admin.NestedTabularInline, ):
    inlines = [TimeSlotInline]
    model = Schedule
    extra = 0
    ct_field = 'content_type'
    ct_fk_field = 'object_id'

@admin.register(EmployeeProfile)
class EmployeeProfileAdmin(nested_admin.NestedModelAdmin):
    inlines = [RestaurantEmployeeProfileInline]
    list_display_links = ("id", "user",)
    list_display = ("id", "user", "hire_date", "is_active")
    list_filter = ("user", "hire_date", "is_active")
    search_fields = ("id", "user")

    fieldsets = (
        (
            "Main",
            {
                "fields": (
                    ("user", "hire_date", "is_active"),
                    ("extra_info"),
                )
            },
        ),
    )

@admin.register(Schedule)
class ScheduleAdmin(nested_admin.NestedModelAdmin):
    inlines = [TimeSlotInline]
    list_display_links = ("id", "day_of_week",)
    list_display = ("id", "day_of_week", "is_active")
    list_filter = ("day_of_week", "is_active")
    search_fields = ("id", "day_of_week")

    fieldsets = (
        (
            "Main",
            {
                "fields": (
                    ("day_of_week", "is_active"),
                    ("content_type", "object_id",)
                    
                )
            },
        ),
    )

@admin.register(TimeSlot)
class TimeSlotAdmin(nested_admin.NestedModelAdmin):
    list_display_links = ("id",)
    list_display = ("id", "start_time", "end_time", "is_active")
    list_filter = ("start_time", "end_time", "is_active")
    search_fields = ("id", "start_time")

    fieldsets = (
        (
            "Main",
            {
                "fields": (
                    ("start_time", "end_time", ),
                    ("schedule", "is_active")
                )
            },
        ),
    )