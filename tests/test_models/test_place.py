#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place
        self.x = Place(city_id="id", user_id="id", name="name")

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

    def test_number_rooms(self):
        """ """
        self.assertIsNone(self.x.number_rooms)

    def test_number_bathrooms(self):
        """ """
        self.assertIsNone(self.x.number_bathrooms)

    def test_max_guest(self):
        """ """
        self.assertIsNone(self.x.max_guest)

    def test_price_by_night(self):
        """ """
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
