import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room("70s", 3)
        self.guest_1 = Guest("Anna", 34, 50)
        self.guest_2 = Guest("Lily", 32, 60)
        self.guest_3 = Guest("Hannah", 35, 80)
        self.guest_4 = Guest("Liam", 36, 100)
        self.song = Song("Don't stop me now", "Queen")

    def test_room_has_name(self):
        self.assertEqual("70s", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(3, self.room.capacity)

    def test_check_in_guest(self):
        self.room.check_in(self.guest_1)
        self.assertEqual(1, len(self.room.inside))


    def test_check_out(self):
        self.room.check_in(self.guest_1)
        self.room.check_out(self.guest_1)
        self.assertEqual(0, len(self.room.inside))
        

    def test_check_out_1_left(self):
        self.room.check_in(self.guest_1)        
        self.room.check_in(self.guest_2)
        self.room.check_out(self.guest_1)
        self.assertEqual(1, len(self.room.inside))
    

    def test_add_song_to_room(self):
        self.room.add_song(self.song)
        self.assertEqual("Don't stop me now", self.song.name)
    

    def test_all_guests(self):
        self.room.check_in(self.guest_1)
        self.room.check_in(self.guest_2)
        self.room.check_in(self.guest_3)
        self.assertEqual(3, len(self.room.inside))

    def test_full_house(self):
        self.room.check_in(self.guest_1)
        self.room.check_in(self.guest_2)
        self.room.check_in(self.guest_3)
        self.room.check_in(self.guest_4)
        self.assertEqual(3, len(self.room.inside))







