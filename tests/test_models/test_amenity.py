#!/usr/bin/python3
""" This module handles miscellaneous unit testing """

import models
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        
        amenity.name = "Wifi"
        self.assertEqual(amenity.name, "Wifi")
        
if __name__ == '__main__':
    unittest.main()
