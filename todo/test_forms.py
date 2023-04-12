from django.test import TestCase
from .forms import ItemForm

# Create your tests here.


class TestItemForm(TestCase):
    # Inherits all testing functionality.
    def test_item_name_is_required(self):
        form = ItemForm({"name": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors.keys())
        # Remember punctuation is important, the string has to match exactly.
        # If any errors are found, the form will return a dictionary of errors.
        # [0] ensures that the first index is the string with error msg.
        self.assertEqual(form.errors["name"][0], "This field is required.")

    def test_done_field_is_not_required(self):
        form = ItemForm({"name": "Test Item Name"})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ["name", "done"])
