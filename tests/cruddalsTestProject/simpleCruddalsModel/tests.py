import datetime

from django.test import TestCase
from django.utils import timezone

from .models import ModelF


class ModelFModelTests(TestCase):

    def test_model_f(self):
        """
        text returns time
        """
        time = timezone.now() + datetime.timedelta(days=30)
        model_f = ModelF(text="time")
        self.assertIs(model_f.text, "time")
