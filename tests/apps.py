# -*- coding: utf-8 -*-
from django.apps import AppConfig


class AppTestConfig(AppConfig):
    label = "app_test"
    name = "tests"

    def ready(self):
        from . import signals
