# Generated by Django 4.2 on 2024-03-17 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_employeeprofile_restaurant_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeprofile',
            name='restaurants',
        ),
    ]