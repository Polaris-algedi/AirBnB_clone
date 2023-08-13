#!/usr/bin/env python3
"""
Unit tests for the FileStorage class
"""
import unittest
import os
from models.engine.file_storage import FileStorage
import models.engine.file_storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class TestFileStorage(unittest.TestCase):
    """Test suite for the FileStorage class"""

    file_path = "file.json"

    def setUp(self):
        """Set up test environment before each test case"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

        self.storage = FileStorage()

    def tearDown(self):
        """Clean up test environment after each test case"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_type(self):
        """Tests type of FileStorage class."""

        self.assertEqual(str(type(self.storage)),
                         "<class 'models.engine.file_storage.FileStorage'>")
        self.assertIsInstance(self.storage, FileStorage)
        self.assertFalse(issubclass(type(self.storage), BaseModel))

    def test_module_and_class_documentation(self):
        """Test the documentation of the module and the FileStorage class"""
        self.assertIsNotNone(models.engine.file_storage.__doc__)
        self.assertIsNotNone(FileStorage.__doc__)

    def test_initial_attributes(self):
        """Test the initial attributes of the FileStorage instance"""
        self.assertEqual(self.storage._FileStorage__file_path, self.file_path)
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_get_all_objects(self):
        """Test the 'all' method of FileStorage"""
        dict1 = self.storage.all()
        self.assertIsInstance(dict1, dict)
        self.assertIs(dict1, self.storage._FileStorage__objects)

    def test_add_new_object(self):
        """Test adding a new object using the 'new' method"""
        u1 = User()
        self.storage.new(u1)
        key = f"{type(u1).__name__}.{u1.id}"
        self.assertIn(key, self.storage._FileStorage__objects)

    def test_reload_from_file(self):
        """Test reloading objects from the JSON file"""
        b = BaseModel()
        self.storage.new(b)
        self.storage.save()
        key = f"{type(b).__name__}.{b.id}"

        FileStorage._FileStorage__objects = {}
        self.storage.reload()
        self.assertIn(key, self.storage._FileStorage__objects)

    def test_reload_with_nonexistent_file(self):
        """Test reloading when the JSON file doesn't exist"""
        try:
            self.storage.reload()
        except FileNotFoundError:
            self.fail("FileNotFoundError raised unexpectedly")


if __name__ == "__main__":
    unittest.main()
