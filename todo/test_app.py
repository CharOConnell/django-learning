from django.apps import apps
from django.test import TestCase
from .apps import TodoConfig


class TestTodoConfig(TestCase):
    # all we can test is that it's named correctly
    def test_app(self):
        self.assertEqual("todo", TodoConfig.name)
        self.assertEqual("todo", apps.get_app_config("todo").name)
        # check we can get the app configuration from django
