import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Miss Alice", 10.00)

    def test_guest_has_name(self):
        self.assertEqual("Miss Alice", self.guest.name)

    def test_guest_has_money(self):
        self.assertEqual(10.00, self.guest.money)