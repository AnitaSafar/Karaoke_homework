import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room("70s", 50)
        # self.drink_1 = Drink("beer", 2.00)
        # self.drink_2 = Drink("wine", 3.00)
        # self.drink_3 = Drink("gin", 4.00)
        # self.pub = Pub("The Prancing Pony", 100.00)
        # self.customer = Customer("Frodo", 10.00)
    
    def test_room_has_name(self):
        self.assertEqual("70s", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(50, self.room.capacity)

    