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

    def test_instance_and_inheritance(self):
        """
        Test the instance type and inheritance.
        """
        review = Review()
        self.assertEqual(str(type(review)), "<class 'models.review.Review'>")
        self.assertIsInstance(review, Review)
        self.assertTrue(issubclass(type(review), BaseModel))

    def test_attributes_existence_and_type(self):
        """
        Test attributes existence and type
        """
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(type(review.place_id) == str)

        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(type(review.user_id) == str)

        self.assertTrue(hasattr(review, "text"))
        self.assertTrue(type(review.text) == str)


if __name__ == '__main__':
    unittest.main()
