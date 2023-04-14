from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        # Create temp item.
        item = Item.objects.create(name="Test Item")
        # Check if item is false by default.
        self.assertFalse(item.done)
