#!/usr/bin/python3
"""Unittest module for the Place Class."""

import unittest
import json
import os
import uuid
from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.engine.file_storage import FileStorage
from datetime import datetime
from time import sleep


class TestPlace(unittest.TestCase):
    """Test Cases for the Place class."""

    def test_IsInstanceOf(self):
        """Test instance"""
        place = Place()
        self.assertEqual(str(type(place)), "<class 'models.place.Place'>")
        self.assertIsInstance(place, Place)
        self.assertTrue(issubclass(type(place), BaseModel))

    def test_attributes_existence_and_type(self):
        """Test attributes existence"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(type(place.city_id) == str)

        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(type(place.user_id) == str)

        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(type(place.name) == str)

        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(type(place.description) == str)

        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(type(place.number_rooms) == int)

        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertTrue(type(place.number_bathrooms) == int)

        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(type(place.max_guest) == int)

        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(type(place.price_by_night) == int)

        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(type(place.latitude) == float)

        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(type(place.longitude) == float)

        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertTrue(type(place.amenity_ids) == list)


if __name__ == '__main__':
    unittest.main()
