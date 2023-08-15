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

    def test_instance_and_inheritance(self):
        """
        Test the instance type and inheritance.
        """
        city = City()
        self.assertEqual(str(type(city)), "<class 'models.city.City'>")
        self.assertIsInstance(city, City)
        self.assertTrue(issubclass(type(city), BaseModel))

    def test_attributes_existence_and_type(self):
        """
        Test attributes existence and type
        """
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(type(city.state_id) == str)

        self.assertTrue(hasattr(city, "name"))
        self.assertTrue(type(city.name) == str)


if __name__ == '__main__':
    unittest.main()
