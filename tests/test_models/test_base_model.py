#!/usr/bin/python3
"""Unittest module for the BaseModel Class."""

import unittest
import json
import os
import uuid
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
from time import sleep


class TestBaseModel(unittest.TestCase):
    """Test Cases for the BaseModel class."""

    def setUp(self):
        """Sets up test resources"""
        self.b1 = BaseModel()
        self.b2 = BaseModel()

    def tearDown(self):
        """Tears down test resources"""
        self.b1 = None
        self.b2 = None
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_IsInstanceOf(self):
        """Tests instance"""
        self.assertIsInstance(self.b1, BaseModel)
        self.assertEqual(str(type(self.b1)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertTrue(issubclass(type(self.b1), BaseModel))

    def test_Id_exitstence_and_type(self):
        """Tests id attribute type"""
        self.assertTrue(hasattr(self.b1, "id"))
        self.assertEqual(type(self.b1.id), str)
        self.assertNotEqual(self.b1.id, self.b2.id)

    def test_Id_uniqueness(self):
        """Tests the uniqueness of ids"""
        ids = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(ids)), len(ids))

    def test_Id_validation(self):
        """Tests if id is a valid UUID"""
        uuid_obj = uuid.UUID(self.b1.id)
        self.assertEqual(str(uuid_obj), self.b1.id)

    def test_datetime_attributes_existence_and_type(self):
        """Checks datetime attributes existence"""
        self.assertTrue(hasattr(self.b1, "created_at"))
        self.assertTrue(hasattr(self.b1, "updated_at"))
        self.assertIsInstance(self.b1.created_at, datetime)
        self.assertIsInstance(self.b1.updated_at, datetime)
        self.assertEqual(self.b1.created_at, self.b1.updated_at)

    def test_datetime_time(self):
        """Tests datetime attributes' differences"""
        date_now = datetime.now()
        time_difference = date_now - self.b1.created_at
        self.assertEqual(time_difference.days, 0)
        self.assertEqual(time_difference.seconds, 0)
        updated_at_1 = self.b1.updated_at
        sleep(0.05)
        self.b1.save()
        updated_at_2 = self.b1.updated_at
        self.assertLess(updated_at_1, updated_at_2)

    def test_instance_string_representations(self):
        """Tests instance string representation"""
        b_str = f"[{type(self.b1).__name__}] ({self.b1.id}) {self.b1.__dict__}"
        self.assertEqual(str(self.b1), b_str)

    def test_instance_dictionary_representations(self):
        """Test instance dictionary representations"""
        b1_dict = self.b1.to_dict()
        self.assertTrue(dict, type(b1_dict))
        self.assertNotEqual(self.b1.__dict__, b1_dict)
        self.assertIn("id", b1_dict)
        self.assertIn("created_at", b1_dict)
        self.assertIn("updated_at", b1_dict)
        self.assertIn("__class__", b1_dict)
        self.assertEqual(b1_dict['__class__'], type(self.b1).__name__)
        self.assertEqual(b1_dict['created_at'], self.b1.created_at.isoformat())
        self.assertEqual(b1_dict['updated_at'], self.b1.updated_at.isoformat())

    def test_added_attributes(self):
        """Tests adding attributes an instance"""
        self.b1.name = "Alx"
        self.b1.number = 11
        self.assertIn("name", self.b1.to_dict())
        self.assertIn("number", self.b1.to_dict())

    def test_recreate_instance_using_dictionary(self):
        """Tests recreating an instace using a dictionary
        representation
        """
        self.b1.name = "Alx"
        self.b1.number = 11
        b1_json = self.b1.to_dict()
        b3 = BaseModel(**b1_json)
        self.assertEqual(b3.to_dict(), self.b1.to_dict())

    def test_to_dict_with_arg(self):
        """Tests passing argument to to_dict method"""
        with self.assertRaises(TypeError):
            self.b1.to_dict("Hi")

    def test_instantiation_with_args_and_kwargs(self):
        """Tests instantiation passing args and dictionary"""
        dt = datetime.now()
        b = BaseModel("y76d", 5, dt)
        self.assertNotEqual(b.id, "y76d")
        with self.assertRaises(TypeError):
            BaseModel(id="y76d", created_at=dt, updated_at=dt)


if __name__ == '__main__':
    unittest.main()
