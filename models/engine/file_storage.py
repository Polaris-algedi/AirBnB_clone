#!/usr/bin/env python3

"""
This module defines the FileStorage class responsible for managing
and persisting instances of various classes to a JSON file.
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class_dict = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class FileStorage:
    """
    Manages and persists instances to a JSON file.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary to store instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieves all stored instances.

        Returns:
            dict: Dictionary containing all instances.
        """
        return type(self).__objects

    def new(self, obj):
        """
        Adds a new instance to the dictionary.

        Args:
            obj: The instance to be added.
        """
        key = f"{type(obj).__name__}.{obj.id}"
        type(self).__objects[key] = obj

    def save(self):
        """
        Saves instances to the JSON file.
        """
        with open(type(self).__file_path, 'w', encoding='UTF-8') as f:
            d = {k: v.to_dict() for k, v in type(self).__objects.items()}
            json.dump(d, f)

    def reload(self):
        """
        Loads instances from the JSON file, if it exists.
        """
        if os.path.exists(type(self).__file_path):
            with open(type(self).__file_path, 'r', encoding='UTF-8') as f:
                d = json.load(f)
                for key, val in d.items():
                    obj = class_dict[val['__class__']](**val)
                    type(self).__objects[key] = obj
