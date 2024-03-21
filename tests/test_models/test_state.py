#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_cities_type(self):
        """Test if cities attribute is of type list"""
        self.assertIsInstance(self.state.cities, list)

    def test_cities_content(self):
        """Test if cities attribute contains City instances"""
        self.assertTrue(all(isinstance(city, BaseModel)
                            for city in self.state.cities))
