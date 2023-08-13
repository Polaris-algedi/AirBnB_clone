#!/usr/bin/env python3
"""
This module defines the BaseModel class, which serves as a base model
with common attributes and methods for other classes to inherit from.
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Represents a base model with common attributes and methods.

    Attributes:
        id (str): Unique identifier for the instance.
        created_at (datetime): Creation timestamp of the instance.
        updated_at (datetime): Last update timestamp of the instance.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for field, value in kwargs.items():
                if field in ['created_at', 'updated_at']:
                    dt = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, field, dt)
                elif field != '__class__':
                    setattr(self, field, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: String representation of the instance.
        """
        str_base = f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
        return str_base

    def save(self):
        """
        Updates the `updated_at` attribute and saves the instance.

        This method updates the `updated_at` attribute to the current
        timestamp and triggers the saving of the instance using the
        storage system.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary.

        Returns:
            dict: Dictionary representation of the instance.
        """
        customized = self.__dict__.copy()
        customized['__class__'] = type(self).__name__
        customized['created_at'] = customized['created_at'].isoformat()
        customized['updated_at'] = customized['updated_at'].isoformat()

        return customized
