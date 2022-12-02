import unittest

from src.rooms import Room
from src.guests import Guest
from src.songs import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.test_room = Room(7, 2, 23.00)
        self.test_guest = Guest("Herbert Farthingsworth", 38)
        self.test_song = Song("Number 9", "Moon Hooch", "Dirty Funk/Dance Fusion Jazz")

    def test_room_was_created(self):
        self.assertEqual(7, self.test_room.number)
        self.assertEqual(2, self.test_room.capacity)
        self.assertEqual(23.00, self.test_room.price)

    def test_guest_was_checked_in(self):
        self.test_room.check_in_guest(self.test_guest)
        self.assertEqual(True, self.test_room.return_if_customer_is_checked_in(self.test_guest))

    def test_guest_was_checked_out(self):
        self.test_room.check_in_guest(self.test_guest)
        self.test_room.check_out_guest(self.test_guest)
        self.assertEqual(False, self.test_room.return_if_customer_is_checked_in(self.test_guest))

    def test_song_was_added_to_room(self):
        self.test_room.add_song_to_room(self.test_song)
        self.assertEqual([self.test_song], self.test_room.songs_list)

    #Extensions:
    def test_customer_cant_check_into_full_room(self):
        self.test_room.check_in_guest(self.test_guest)
        self.test_room.check_in_guest(self.test_guest)
        self.assertEqual(False, self.test_room.check_room_has_space())

        
