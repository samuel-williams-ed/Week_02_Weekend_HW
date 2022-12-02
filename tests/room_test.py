import unittest

from src.rooms import Room
from src.guests import Guest
from src.songs import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.test_room = Room(7, 2, 23.00)
        self.test_song = Song("Number 9", "Moon Hooch", "Dirty Funk/Dance Fusion Jazz")
        self.test_guest = Guest("Herbert Farthingsworth", 38, 200.00, self.test_song)

    def test_room_was_created(self):
        self.assertEqual(7, self.test_room.number)
        self.assertEqual(2, self.test_room.capacity)
        self.assertEqual(23.00, self.test_room.price)

    def test_guest_was_checked_in(self):
        self.test_room.check_in_guest(self.test_guest)
        self.assertEqual(True, self.test_guest.checked_in)

    def test_guest_was_checked_out(self):
        self.test_room.check_in_guest(self.test_guest)
        self.test_room.check_out_guest(self.test_guest)
        self.assertEqual(False, self.test_guest.checked_in)

    def test_song_was_added_to_room(self):
        self.test_room.add_song_to_room(self.test_song)
        self.assertEqual([self.test_song], self.test_room.songs_list)

    #Extensions:
    def test_customer_cant_check_into_full_room(self):
        self.test_room.check_in_guest(self.test_guest)
        self.test_room.check_in_guest(self.test_guest)
        self.assertEqual(False, self.test_room.check_room_has_space())

    def test_customer_has_been_charged_entry(self):
        self.test_room.check_in_guest(self.test_guest)
        self.assertEqual(177.00, self.test_guest.money)

    #Advanced Extensions
    def test_customers_fav_song_is_in_room(self):
        self.test_room.add_song_to_room(self.test_song)
        self.assertEqual(True, self.test_room.check_playlist_for_customer_fav(self.test_guest))

    #bar tab property in room
    #list of dictionaries
    #dictionaries hold customer_object : tab (int)
    #build Bar class with .charge() method
    # def test_guests_can_have_tab(self):
    #     self.assertEqual([{self.test_guest : 5.50}], )
