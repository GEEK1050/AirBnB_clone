#!/usr/bin/python3

"""Module for Base unit tests."""
import unittest
from datetime import datetime

from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """test the Base class."""

    def test_init(self):
        """tests."""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_assert_is_instance(self):
        """test id instance"""
        self.assertIsInstance(b1.id, str)

    def test_is_not_instance(self):
        """test id is not int"""
        self.assertNotIsInstance(b1.id, int)

    def test_attribute(self):
        """test attributes"""
        b1.name = "Holberton"
        b1.my_number = 89
        self.assertEqual(b1.name, "Holberton")
        self.assertEqual(b1.my_number, 89)

    def test_json(self):
      """json tests"""
      d = b1.to_dict()
      self.assertAlmostEqual(type(d), dict)
