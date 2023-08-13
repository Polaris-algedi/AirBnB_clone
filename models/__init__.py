#!/usr/bin/env python3
"""
This module initializes the storage mechanism for the application.

It imports the `FileStorage` class from the `models.engine.file_storage` module
and creates an instance of it to provide a persistent storage mechanism.

"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
