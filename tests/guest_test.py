import unittest

from src.guests import Guest
from src.songs import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.test_song = Song("Jiggle Jiggle", "Louis Theroux", "Comedy Rap")
        self.test_customer = Guest("Bob", 19, 20.00, self.test_song)

        #Advanced Extensions
    def test_guest_has_favourite_song(self):
        self.assertEqual(self.test_song, self.test_customer.favourite_song)

    def test_person_can_cheer(self):
        self.assertEqual("Whoo!", self.test_customer.cheer())

