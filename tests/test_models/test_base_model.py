#!/usr/bin/python3
""" This module handles miscellaneous unit testing """

import os
import models
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """
    Class defines a series of test
    for the Airbnb console
    """

    my_model = BaseModel()

    def test_BaseModelTest_1(self):
        """
        This test ascertains the attributes
        value of a given instance in the BaseModel
        """

        self.my_model.name = "SomeDude"
        self.my_model.my_number = 25
        self.my_model.save()
        my_model_json = self.my_model.to_dict()

        self.assertEqual(self.my_model.name, my_model_json['name'])
        self.assertEqual(self.my_model.my_number, my_model_json['my_number'])
        self.assertEqual('BaseModel', my_model_json['__class__'])
        self.assertEqual(self.my_model.id, my_model_json['id'])


if __name__ == '__main__':
    unittest.main()
