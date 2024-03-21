from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class EmployeeProfile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='employee_profile',
        help_text='The user that has this employee profile'
    ) #- employeeProfile = OneToOneRel
    hire_date = models.DateField(
        help_text='The date the employee was hired'
    )
    extra_info = models.JSONField(
        help_text='The extra information of the employee',
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        default=True,
        help_text='The status for enabling or disabling'
    )

    def __str__(self):
        return self.user.username

class Schedule(models.Model):
    day_of_week = models.PositiveSmallIntegerField(
        choices=[(i, j) for i, j in enumerate(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'], start=1)],
        help_text='The day of the week of the schedule'
    )
    content_type = models.ForeignKey(
        ContentType, 
        on_delete=models.CASCADE,
        help_text='The content type of the schedule item',
        limit_choices_to={'model__in': ('menu', 'employeeprofile', 'restaurant')},
        null=True,
        blank=True
    )
    object_id = models.PositiveIntegerField(
        help_text='The object id of the schedule item',
        null=True,
        blank=True
    )
    content_object = GenericForeignKey(
        'content_type', 
        'object_id'
    )
    is_active = models.BooleanField(
        default=True,
        help_text='The status for enabling or disabling'
    )

    # -menus = ReverseManyToOneRel

class TimeSlot(models.Model):
    start_time = models.TimeField(
        help_text='The start time of the time slot'
    )
    end_time = models.TimeField(
        help_text='The end time of the time slot'
    )
    schedule = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE,
        related_name='time_slots',
        help_text='The schedule that the time slot is a part of'
    )
    is_active = models.BooleanField(
        default=True,
        help_text='The status for enabling or disabling'
    )
