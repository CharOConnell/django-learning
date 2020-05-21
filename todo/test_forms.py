from django.test import TestCase


# Create your tests here.
class TestDjango(TestCase):

    def test_is_this_thing_on(self):
        # need to start with test or django won't find them
        self.assertEqual(1, 1)
        # asserts that 1 is equal to 0
