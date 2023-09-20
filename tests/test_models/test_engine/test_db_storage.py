#!/usr/bin/python3
"""unittests for models/engine/file_storage.py."""
import os
import models
import unittest
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


@unittest.skipIf(type(models.storage) != DBStorage, "FS")
class TestDBStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the DBStorage class."""

    @classmethod
    def setUp(self):
        self.classes = [
            BaseModel, User,
            State, City,
            Amenity, Place,
            Review
        ]

    def test_all_type(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        for cls in self.classes:
            obj = cls()
            obj.save()
            key = f"{cls.__name__}.{obj.id}"
            self.assertIn(key, models.storage.all().keys())
            self.assertIn(obj, models.storage.all().values())

    def test_save(self):
        for cls in self.classes:
            obj = cls()
            obj.save()
            key = f"{cls.__name__}.{obj.id}"
            self.assertIn(key, models.storage.all().keys())

    def test_reload(self):
        for cls in self.classes:
            obj = cls()
            obj.save()
            models.storage.reload()
            key = f"{cls.__name__}.{obj.id}"
            reloaded_obj = models.storage.all()[key]
            self.assertIn(key, models.storage.all())

    def test_reload_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload("Hello")
