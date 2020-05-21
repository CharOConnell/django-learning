from django.test import TestCase
from .models import Item


class TestItemModel(TestCase):
    def test_done_defaults_to_False(self):
        # if we create a new item without specifying the done,
        # it auto sets to false as we specified on our model
        item = Item(name="Create a Test")
        item.save()
        self.assertEqual(item.name, "Create a Test")
        # check the name is set
        self.assertFalse(item.done)
        # check it's set to false

    def test_can_create_an_item_with_a_name_and_status(self):
        # check that if we manually set it to done, it is true
        # we've checked it auto sets to false
        item = Item(name="Create a Test", done=True)
        item.save()
        self.assertEqual(item.name, "Create a Test")
        self.assertTrue(item.done)
