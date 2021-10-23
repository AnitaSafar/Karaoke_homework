import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Anna", 34, 50)

    def test_guest_has_name(self):
        self.assertEqual("Anna", self.guest.name)

    def test_guest_has_age(self):
        self.assertEqual(34, self.guest.age)

    def test_guest_has_money(self):
        self.assertEqual(50, self.guest.wallet)