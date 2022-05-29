import unittest
from item import *
class TestItem(unittest.TestCase):
    def test__init_(self):
        itm = Item("name",1,"test")
        self.assertIsNotNone(itm.name)
        self.assertIsNotNone(itm.quantity)
        self.assertIsNotNone(itm.description)
    