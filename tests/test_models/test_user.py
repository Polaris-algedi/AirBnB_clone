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

    def test_instance_and_inheritance(self):
        """
        Test the instance type and inheritance.
        """
        user = User()
        self.assertEqual(str(type(user)), "<class 'models.user.User'>")
        self.assertIsInstance(user, User)
        self.assertTrue(issubclass(type(user), BaseModel))

    def test_attributes_existence_and_type(self):
        """
        Test attributes existence and type
        """
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(type(user.email) == str)

        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(type(user.password) == str)

        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(type(user.first_name) == str)

        self.assertTrue(hasattr(user, "last_name"))
        self.assertTrue(type(user.last_name) == str)


if __name__ == '__main__':
    unittest.main()
