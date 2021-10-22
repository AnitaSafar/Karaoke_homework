import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Don't stop me now", "Queen")

    def test_song_has_name(self):
        self.assertEqual("Don't stop me now", self.song.name)

    def test_song_has_artist(self):
        self.assertEqual("Queen", self.song.artist)