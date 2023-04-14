from django.test import TestCase
from .models import Item

# Create your tests here.


class TestViews(TestCase):
    # Inherits all testing functionality.
    def test_get_todo_list(self):
        response = self.client.get("/")
        # 200 is successful http response.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/todo_list.html")

    def test_get_add_item_page(self):
        response = self.client.get("/add")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/add_item.html")

    def test_get_edit_item_page(self):
        # Create temp item.
        item = Item.objects.create(name="Test Item")
        # Simulate client response.
        response = self.client.get(f"/edit/{item.id}")
        # Check if successful.
        self.assertEqual(response.status_code, 200)
        # Check if correct template used.
        self.assertTemplateUsed(response, "todo/edit_item.html")

    def test_can_add_item(self):
        response = self.client.post("/add", {"name": "Test Posted Item"})
        self.assertRedirects(response, "/")

    def test_can_delete_item(self):
        item = Item.objects.create(name="New Test Item")
        response = self.client.get(f"/delete/{item.id}")
        self.assertRedirects(response, "/")
        # Check if item exists after deletion.
        # Create filter for existing item.
        existing_items = Item.objects.filter(id=item.id)
        # Check if it exists by comparing to zero.
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        # Create item with done=True
        item = Item.objects.create(name="New Test Item", done=True)
        response = self.client.get(f"/toggle/{item.id}")
        self.assertRedirects(response, "/")
        # Once updated, pull the toggled item.
        updated_item = Item.objects.get(id=item.id)
        # Check its done status.
        self.assertFalse(updated_item.done)