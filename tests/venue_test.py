import unittest
from src.venue import Venue

class TestVenue(unittest.TestCase):

    def setUp(self):
        self.venue = Venue("Tom's Karaoke Bar")

    def test_venue_has_name(self):
        self.assertEqual("Tom's Karaoke Bar", self.venue.name)