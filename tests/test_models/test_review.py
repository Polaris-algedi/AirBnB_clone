#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
import json
import os
import uuid
from models import storage
from models.base_model import BaseModel
from models.review import Review
from models.engine.file_storage import FileStorage
from datetime import datetime
from time import sleep


class TestReview(unittest.TestCase):
    """Test Cases for the Review class."""

    def setUp(self):
        """Sets up test resources"""
        self.u1 = Review()
        self.u1.user_id = str(uuid.uuid4())
        self.u1.place_id = str(uuid.uuid4())
        self.u1.text = "Awesome"

    def tearDown(self):
        """Tears down test resources"""
        self.u1 = None
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_IsInstanceOf(self):
        """Test instance"""
        self.assertEqual(str(type(self.u1)), "<class 'models.review.Review'>")
        self.assertIsInstance(self.u1, Review)
        self.assertTrue(issubclass(type(self.u1), BaseModel))

    def test_attributes(self):
        """Test attributes existence"""
        u1_dict = self.u1.__dict__
        self.assertIn('id', u1_dict)
        self.assertIn('created_at', u1_dict)
        self.assertIn('updated_at', u1_dict)
        self.assertIn('user_id', u1_dict)
        self.assertIn('place_id', u1_dict)
        self.assertIn('text', u1_dict)


if __name__ == '__main__':
    unittest.main()
