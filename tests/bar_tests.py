import unittest

from src.bar import Bar
from src.guests import Guest

class TestBar(unittest.TestCase):
    def setUp(self):
        self.test_drinks_list = [{"Vodka" : 3.00}, {"Beer" : 5.50}, {"Gin" : 2.50}]
        self.test_bar = Bar("McSammys", 1000, self.test_drinks_list)

    def test_get_drink_price(self):
        self.assertEqual(5.50, self.test_bar.get_drink_price({"Beer" : 5.50}))
    
    def test_choose_drink(self):
        self.assertEqual({"Beer" : 5.50}, self.test_bar.choose_drink("Beer"))

    def test_customer_charged(self):
        self.test_customer = Guest('Margaret', 35, 10.50, "Hollaback Girl")
        self.test_bar.charge_customer(self.test_customer, self.test_drinks_list[1])
        self.assertEqual(5.00 , self.test_customer.money)
