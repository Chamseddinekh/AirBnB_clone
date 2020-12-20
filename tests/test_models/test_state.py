#!/usr/bin/python3
"""
test module for testing state models
"""
import unittest
import os
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """test the Place class"""
    def test_subclass_state(self):
        """Place subclass test"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)
