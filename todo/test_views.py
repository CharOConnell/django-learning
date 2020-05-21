from django.test import TestCase
from .models import Item


class TestViews(TestCase):
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        # checks that the page object is running
        self.assertTemplateUsed(page, "todo_list.html")

    def test_get_add_item_page(self):
        page = self.client.get("/add")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")

    def test_get_edit_item_page(self):
        item = Item(name='Create a Test')
        item.save()
        # this saves to the test database, not our real database

        page = self.client.get("/edit/{0}".format(item.id))
        # need to pass in the ID value
        # the object is numeric hence {0}
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "item_form.html")

    def test_get_edit_page_for_item_that_does_not_exist(self):
        page = self.client.get("/edit/1")
        self.assertEqual(page.status_code, 404)
        # check that if it doesn't exist, it throws up the 404
        # we used the get_object_or_404
