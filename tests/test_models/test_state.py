#!/usr/bin/python3
"""Unittest module for the State Class."""

import unittest
import json
import os
import uuid
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage
from datetime import datetime
from time import sleep


class TestState(unittest.TestCase):
    """Test Cases for the State class."""

    def test_instance_and_inheritance(self):
        """
        Test the instance type and inheritance.
        """
        state = State()
        self.assertEqual(str(type(state)), "<class 'models.state.State'>")
        self.assertIsInstance(state, State)
        self.assertTrue(issubclass(type(state), BaseModel))

    def test_attributes_existence_and_type(self):
        """
        Test attributes existence and type
        """
        self.assertTrue(hasattr(state, "name"))
        self.assertTrue(type(place.name) == str)


if __name__ == '__main__':
    unittest.main()
