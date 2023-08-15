#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
import json
import os
import uuid
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from datetime import datetime
from time import sleep


class TestAmenity(unittest.TestCase):
    """Test Cases for the Amenity class."""

    def test_instance_and_inheritance(self):
        """
        Test the instance type and inheritance.
        """
        amenity = Amenity()
        self.assertEqual(str(type(amenity)),
                         "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(issubclass(type(amenity), BaseModel))

    def test_attributes_existence_and_type(self):
        """
        Test attributes existence and type
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertTrue(type(amenity.name) == str)


if __name__ == '__main__':
    unittest.main()
