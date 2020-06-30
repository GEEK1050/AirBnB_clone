#!/usr/bin/python3
"""Module for BaseModel unittests."""

import os
import unittest
import models
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """test the Base class."""

    def test_init(self):
        """tests."""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_no_args_instantiates(self):
        """test passing no args"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_assert_is_instance(self):
        """test the type of instance"""
        b1 = BaseModel()
        self.assertIsInstance(b1.id, str)

    def test_is_not_instance(self):
        """test the type of instance"""
        b1 = BaseModel()
        self.assertNotIsInstance(b1.id, int)

    def test_attribute(self):
        b1 = BaseModel()
        b1.name = "Holberton"
        b1.my_number = 89
        self.assertEqual(b1.name, "Holberton")
        self.assertEqual(b1.my_number, 89)

    def test_None_args(self):
        b1 = BaseModel(None)
        self.assertNotIn(None, b1.__dict__)

    def test_two_models_different_created_at(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertLess(b1.created_at, b2.created_at)

    def test_two_models_different_updated_at(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertLess(b1.updated_at, b2.updated_at)

    def test_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_json(self):
      """json tests"""
      b1 = BaseModel()
      d = b1.to_dict()
      self.assertAlmostEqual(type(d), dict)

    def test_id_type_string(self):
        """
        test id of the basemodel is a string
        """
        b1 = BaseModel()
        self.assertEqual(type(b1.id), str)


if __name__ == '__main__':
    unittest.main()                                          
