#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
import json
import os
import uuid
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from datetime import datetime
from time import sleep


class TestCity(unittest.TestCase):
    """Test Cases for the City class."""

    def setUp(self):
        """Sets up test resources"""
        self.u1 = City()
        self.u1.state_id = "LA-jhbdhbad-213561"
        self.u1.name = "LA"

    def tearDown(self):
        """Tears down test resources"""
        self.u1 = None
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_IsInstanceOf(self):
        """Test instance"""
        self.assertEqual(str(type(self.u1)), "<class 'models.city.City'>")
        self.assertIsInstance(self.u1, City)
        self.assertTrue(issubclass(type(self.u1), BaseModel))

    def test_attributes(self):
        """Test attributes existence"""
        u1_dict = self.u1.__dict__
        self.assertIn('id', u1_dict)
        self.assertIn('created_at', u1_dict)
        self.assertIn('updated_at', u1_dict)
        self.assertIn('name', u1_dict)
        self.assertIn('state_id', u1_dict)


if __name__ == '__main__':
    unittest.main()
