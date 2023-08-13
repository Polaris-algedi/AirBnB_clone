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

    def setUp(self):
        """Sets up test resources"""
        self.u1 = Place()
        self.u1.city_id = str(uuid.uuid4())
        self.u1.user_id = str(uuid.uuid4())
        self.u1.name = "a place"
        self.u1.description = "a Beach"
        self.u1.number_rooms = 5
        self.u1.number_bathrooms = 3
        self.u1.max_guest = 10
        self.u1.price_by_night = 100
        self.u1.latitude = 40.7128
        self.u1.longitude = -74.0060
        self.u1.amenity_ids = ["amenity_id1", "amenity_id2"]

    def tearDown(self):
        """Tears down test resources"""
        self.u1 = None
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_IsInstanceOf(self):
        """Test instance"""
        self.assertEqual(str(type(self.u1)), "<class 'models.place.Place'>")
        self.assertIsInstance(self.u1, Place)
        self.assertTrue(issubclass(type(self.u1), BaseModel))

    def test_attributes(self):
        """Test attributes existence"""
        u1_dict = self.u1.__dict__
        self.assertIn('id', u1_dict)
        self.assertIn('created_at', u1_dict)
        self.assertIn('updated_at', u1_dict)
        self.assertIn('city_id', u1_dict)
        self.assertIn('user_id', u1_dict)
        self.assertIn('name', u1_dict)
        self.assertIn('description', u1_dict)
        self.assertIn('number_rooms', u1_dict)
        self.assertIn('number_bathrooms', u1_dict)
        self.assertIn('max_guest', u1_dict)
        self.assertIn('price_by_night', u1_dict)
        self.assertIn('latitude', u1_dict)
        self.assertIn('longitude', u1_dict)
        self.assertIn('amenity_ids', u1_dict)


if __name__ == '__main__':
    unittest.main()
