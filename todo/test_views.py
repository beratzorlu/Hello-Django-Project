from django.test import TestCase

# Create your tests here.


class TestDjango(TestCase):
    # Inherits all testing functionality.
    def test_if_works(self):
        self.assertEqual(1, 1)
