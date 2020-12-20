#!/usr/bin/python3
"""
test module for testing city models
"""
import unittest
import os
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """test the city class"""
    def test_subclass_city(self):
        """city subclass test"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)
