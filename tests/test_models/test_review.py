#!/usr/bin/python3
""" Test module for TestReview class"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class TestReview(test_basemodel):
    """ Tests for TestReview class"""

    def __init__(self, *args, **kwargs):
        """ Initialize TestReview """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ test for review place_id """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ test for review user_id """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ test for review text """
        new = self.value()
        self.assertEqual(type(new.text), str)
