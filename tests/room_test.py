import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Tokyo", 20, [], [], 100.00)
        self.guest = Guest("Angus", 15)
        self.song = Song("Blue Jeans Blues", "ZZ Top", "Rock")

    ## 1. Test room has a name

    def test_room_has_name(self):
        self.assertEqual("Tokyo", self.room.name)

    ## 2. Test room has a capacity

    def test_room_has_capacity(self):
        self.assertEqual(20, self.room.capacity)

    ## 3. Test guest_list is empty

    def test_guest_list_starts_empty(self):
        self.assertEqual(0, len(self.room.guest_list))


    ## 4. Test can add to guest_list

    def test_add_to_guest_list(self):
        self.room.add_to_guest_list(self.guest)
        self.assertEqual(1, len(self.room.guest_list))


    ## 5. Test can remove from guest_list

    def test_remove_from_guest_list(self):
        self.room.add_to_guest_list(self.guest)
        self.room.remove_from_guest_list(self.guest)
        self.assertEqual(0, len(self.room.guest_list))

    ## 6. Test playlist is empty

    def test_playlist_starts_empty(self):
        self.assertEqual(0, len(self.room.playlist))

    ## 7. Test can add to playlist

    def test_add_to_playlist(self):
        self.room.add_to_playlist(self.song)
        self.assertEqual(1, len(self.room.playlist))











        
    