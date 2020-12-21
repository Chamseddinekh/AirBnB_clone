#!/usr/bin/python3
"""
test module for testing amenity models
"""
import unittest
import os
from models.base_model import BaseModel
from models.amenity import Amenity


class TestCity(unittest.TestCase):
    """test the city class"""

    def test_subclass_amenity(self):
        """amenity subclass test"""
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)
