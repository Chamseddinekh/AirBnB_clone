#!usr/bin/python3
"""
base model test
"""
import unittest
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    base model test
    """
    def test_save(self):
        """test save func"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

if __name__ == '__main__':
    unittest.main()
