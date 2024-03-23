from django.test import TestCase
from menu.models import Menu


class MenuTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(
            name="menu1",
            is_active=True
        )

    def test_menus_can_speak(self):
        """Menus that can speak are correctly identified"""
        menu1 = Menu.objects.get(name="menu1")
        self.assertEqual(menu1.name, 'menu1')