import os
import sys

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT_PATH + "/tests/")

SECRET_KEY = 1

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "graphene_django",
    "tests",
    # "tests.test_project",
]

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "django_test.sqlite"}
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
    }
]

# GRAPHENE = {"SCHEMA": "tests.schema.schema"}

ROOT_URLCONF = "tests.settings.urls"


USE_TZ = True
