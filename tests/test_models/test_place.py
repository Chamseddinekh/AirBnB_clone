#!/usr/bin/python3
"""
test module for testing place models
"""
import unittest
import os
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """test the Place class"""
    def test_subclass_place(self):
        """Place subclass test"""
        self.assertTrue(issubclass(self.Place.__class__, BaseModel), True)