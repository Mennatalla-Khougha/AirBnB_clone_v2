#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.engine.db_storage import DBStorage
from models import storage
from models.user import User
from models.place import Place
from models.city import City
from models.state import State


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place
        user = User(email="email", password="password")
        user.save()
        state = State(name="name")
        state.save()
        city = City(name="name", state_id=state.id)
        city.save()
        self.x = Place(city_id=city.id, user_id=user.id, name="name")
        self.x.save()

    def test_city_id(self):
        """ """
        self.assertEqual(type(self.x.city_id), str)

    def test_user_id(self):
        """ """
        self.assertEqual(type(self.x.user_id), str)

    def test_name(self):
        """ """
        self.assertEqual(type(self.x.name), str)

    def test_description(self):
        """ """
        self.assertIsNone(self.x.description)

    @unittest.skipIf(type(storage) != DBStorage, "DB")
    def test_numbers(self):
        """ """
        self.assertTrue(self.x.number_rooms == 0)
        self.assertTrue(self.x.number_bathrooms == 0)
        self.assertTrue(self.x.max_guest == 0)
        self.assertTrue(self.x.price_by_night == 0)

    @unittest.skipIf(type(storage) == DBStorage, "DB")
    def test_numbers(self):
        """ """
        self.assertIsNone(self.x.number_rooms)
        self.assertIsNone(self.x.number_bathrooms)
        self.assertIsNone(self.x.max_guest)
        self.assertIsNone(self.x.price_by_night)

    def test_latitude(self):
        """ """
        self.assertIsNone(self.x.latitude)

    def test_longitude(self):
        """ """
        self.assertIsNone(self.x.latitude)

    def test_amenity_ids(self):
        """ """
        self.assertEqual(type(self.x.amenity_ids), list)
