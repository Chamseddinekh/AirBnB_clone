#!/usr/bin/python3
"""
test module for testing review models
"""
import unittest
import os
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """test the Place class"""
    def test_subclass_review(self):
        """Place subclass test"""
        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)
