#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review
        user = User(email="email", password="password")
        user.save()
        state = State(name="name")
        state.save()
        city = City(name="name", state_id=state.id)
        city.save()
        place = Place(name="name", user_id=user.id, city_id=city.id)
        place.save()
        self.x = Review(text="text", place_id=place.id, user_id=user.id)
        self.x.save()

    def test_place_id(self):
        """ """
        self.assertEqual(type(self.x.place_id), str)

    def test_user_id(self):
        """ """
        self.assertEqual(type(self.x.user_id), str)

    def test_text(self):
        """ """
        self.assertEqual(type(self.x.text), str)
