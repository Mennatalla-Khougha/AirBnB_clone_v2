#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User
        self.x = User(email="email", password="password")

    def test_first_name(self):
        """ """
        self.assertIsNone(self.x.first_name)

    def test_last_name(self):
        """ """
        self.assertIsNone(self.x.last_name)

    def test_email(self):
        """ """
        self.assertIsInstance(self.x.email, str)

    def test_password(self):
        """ """
        self.assertIsInstance(self.x.password, str)
