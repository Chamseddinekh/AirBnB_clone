#!/usr/bin/python3
"""
test module for testing user models
"""
import unittest
import os
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """test the Place class"""
    def test_subclass_user(self):
        """Place subclass test"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)
