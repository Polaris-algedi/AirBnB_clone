#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
import json
import os
import uuid
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from datetime import datetime
from time import sleep


class TestUser(unittest.TestCase):
    """Test Cases for the User class."""

    def setUp(self):
        """Sets up test resources"""
        self.u1 = User()
        self.u1.email = "MP@example.com"
        self.u1.password = "123456"
        self.u1.first_name = "Mohammed"
        self.u1.last_name = "Polaris"

    def tearDown(self):
        """Tears down test resources"""
        self.u1 = None
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_IsInstanceOf(self):
        """Test instance"""
        self.assertEqual(str(type(self.u1)), "<class 'models.user.User'>")
        self.assertIsInstance(self.u1, User)
        self.assertTrue(issubclass(type(self.u1), BaseModel))

    def test_attributes(self):
        u1_dict = self.u1.__dict__
        self.assertIn('id', u1_dict)
        self.assertIn('created_at', u1_dict)
        self.assertIn('updated_at', u1_dict)
        self.assertIn('email', u1_dict)
        self.assertIn('password', u1_dict)
        self.assertIn('first_name', u1_dict)
        self.assertIn('last_name', u1_dict)


if __name__ == '__main__':
    unittest.main()
