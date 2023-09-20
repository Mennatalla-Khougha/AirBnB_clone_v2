#!/usr/bin/python3
"""Defines unittests for console.py."""
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class TestHBNB_create(unittest.TestCase):
    """Unittests for testing create from the HBNB command interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "filetest.json")
        except IOError:
            pass
        FileStorage.__objects = {}
        self.user = User(email="email", password="password")
        self.state = State(name="name")
        self.city = City(name="name", state_id=self.state.id)
        self.place = Place(
            name="name",
            user_id=self.user.id,
            city_id=self.city.id
        )
        self.amenity = Amenity(name="name")
        self.review = Review(
            text="text",
            place_id=self.place.id,
            user_id=self.user.id
        )

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("filetest.json", "file.json")
        except IOError:
            pass

    def test_missing_class(self):
        text = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(text, output.getvalue().strip())

    def test_invalid_class(self):
        text = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create khougha"))
            self.assertEqual(text, output.getvalue().strip())

    def test_invalid_syntax1(self):
        text = "*** Unknown syntax: khougha.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("khougha.create()"))
            self.assertEqual(text, output.getvalue().strip())

    def test_invalid_syntax2(self):
        text = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(text, output.getvalue().strip())

    def test_BaseModeld(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            key1 = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(key1, storage.all().keys())

    def test_User(self):
        cmd = 'create User email="email" password="password"'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertLess(0, len(output.getvalue().strip()))
            key1 = "User.{}".format(output.getvalue().strip())
            self.assertIn(key1, storage.all().keys())

    def test_State(self):
        cmd = "create State name=\"California\""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertLess(0, len(output.getvalue().strip()))
            key1 = "State.{}".format(output.getvalue().strip())
            self.assertIn(key1, storage.all().keys())

    def test_City(self):
        cmd = f'create City name="city" state_id={self.state.id}'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertLess(0, len(output.getvalue().strip()))
            key1 = "City.{}".format(output.getvalue().strip())
            self.assertIn(key1, storage.all().keys())

    def test_Amenity(self):
        cmd = 'create Amenity name="TV"'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertLess(0, len(output.getvalue().strip()))
            key1 = "Amenity.{}".format(output.getvalue().strip())
            self.assertIn(key1, storage.all().keys())

    def test_Place(self):
        cmd = f'create Place name="name" city_id={self.city.id}'
        cmd += f' user_id={self.user.id}'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertLess(0, len(output.getvalue().strip()))
            key1 = "Place.{}".format(output.getvalue().strip())
            self.assertIn(key1, storage.all().keys())

    def test_Review(self):
        cmd = f'create Review text="text" place_id={self.place.id}'
        cmd += f' user_id={self.user.id}'
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(cmd))
            self.assertLess(0, len(output.getvalue().strip()))
            key1 = "Review.{}".format(output.getvalue().strip())
            self.assertIn(key1, storage.all().keys())
