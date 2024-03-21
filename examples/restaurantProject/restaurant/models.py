from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(
        max_length=100,
        help_text='The name of the restaurant'
    )
    slug = models.SlugField(
        help_text='The slug of the restaurant',
        blank=True,
        null=True,
        unique=True,
        editable=False,
        max_length=100
    )
    logo = models.ImageField(
        help_text='The logo of the restaurant',
        blank=True,
        null=True,
        upload_to='media/restaurant/logos/'
    )
    email = models.EmailField(
        help_text='The email of the restaurant',
        unique=True,
    )
    phone_number = models.CharField(
        max_length=20,
        help_text='The phone number of the restaurant',
        blank=True,
        null=True
    )
    website = models.URLField(
        help_text='The website of the restaurant',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text='The date and time the restaurant was created'
    )
    document = models.FileField(
        help_text='The document of the restaurant',
        blank=True,
        null=True,
        upload_to='media/restaurant/documents/'
    )
    is_active = models.BooleanField(
        default=True,
        help_text='The status for enabling or disabling'
    )
    employees = models.ManyToManyField(
        'core.EmployeeProfile', 
        related_name='restaurants', 
        help_text='The employees that work at the restaurant'
    )
    schedules = GenericRelation(
        'core.Schedule',
        related_query_name='restaurant',
        help_text='The schedules of the restaurant'
    )
    # -tables = ManyToOneRel
    # -menus = ManyToManyRel
    

class Table(models.Model):
    
    class TableStatus(models.TextChoices):
        OCCUPIED = ("OCCUPIED", "OCCUPIED")
        AVAILABLE = ("AVAILABLE", "AVAILABLE")
        RESERVED = ("RESERVED", "RESERVED")
        UNAVAILABLE = ("UNAVAILABLE", "UNAVAILABLE")

    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='tables',
        help_text='The restaurant that the table is a part of'
    )
    identifier = models.CharField(
        max_length=100,
        help_text='The identifier of the table'
    )
    capacity = models.IntegerField(
        help_text='The capacity of the table'
    )
    status = models.CharField(
        help_text='The status of the table',
        max_length=15,
        choices=TableStatus.choices, 
        default=TableStatus.AVAILABLE, 
        blank=True, 
        null=True
    ) #-choices
    is_active = models.BooleanField(
        default=True,
        help_text='The status for enabling or disabling'
    )
