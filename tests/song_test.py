import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Loch Lomond", "Runrig", "Folk Rock")

    ## 1. Test song has a name.

    def test_song_has_name(self):
        self.assertEqual("Loch Lomond", self.song.title)

    ## 2. Test song has an artist.

    def test_song_has_artist(self):
        self.assertEqual("Runrig", self.song.artist)

    ## 3. Test song has a genre.

    def test_song_has_genre(self):
        self.assertEqual("Folk Rock", self.song.genre)