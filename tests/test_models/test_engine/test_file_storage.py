#!/usr/bin/python3
"""define a class FileStorage unittest"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import unittest
from datetime import datetime
import json


class TestFileStorage(unittest.TestCase):
    """Test Cases for the FileStorage class."""

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_two_models_unique_ids(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_two_models_different_created_at(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertLess(b1.created_at, b2.created_at)

    def test_two_models_different_updated_at(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertLess(b1.updated_at, b2.updated_at)

    def test_args_unused(self):
        b = BaseModel(None)
        self.assertNotIn(None, b.__dict__.values())

    def test_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)


class TestFileStorage_save(unittest.TestCase):
    """Test Cases for the save method"""

    def test_save_update(self):
        b = BaseModel()
        b.save()
        bid = "BaseModel." + b.id
        with open("file.json", "r") as f:
            self.assertIn(bid, f.read())

    def test_save_arg(self):
        b = BaseModel()
        with self.assertRaises(TypeError):
            b.save(None)


class TestBaseModel_to_dict(unittest.TestCase):
    """Test Cases for the to_dict method"""

    def test_type_to_dict(self):
        b = BaseModel()
        self.assertTrue(dict, type(b.to_dict()))


if __name__ == '__main__':
    unittest.main()
