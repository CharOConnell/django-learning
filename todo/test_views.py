from django.test import TestCase
from django.shortcuts import get_object_or_404
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

    def test_post_create_an_item(self):
        response = self.client.post("/add", {"name": "Create a Test"})
        # create a response from a form posted to add, 
        # dictionary passed through
        item = get_object_or_404(Item, pk=1)
        # make sure our get_object_or_404 is working
        self.assertEqual(item.done, False)

    def test_post_edit_an_item(self):
        item = Item(name="Createa Test")
        # create new item
        item.save()
        id = item.id
        # store the id of that item

        response = self.client.post("/edit/{0}".format(id), {"name": "A different name"})
        # pass in the id value
        item = get_object_or_404(Item, pk=id)
        # check get_object_or_404 is working

        self.assertEqual("A different name", item.name)

    def test_toggle_status(self):
        item = Item(name="Create a Test")
        item.save()
        id = item.id

        response = self.client.post("/toggle/{0}".format(id))

        item = get_object_or_404(Item, pk=id)
        self.assertEqual(item.done, True)
        # we don't set it so it's false, but when we run it, 
        # it'll change to true
