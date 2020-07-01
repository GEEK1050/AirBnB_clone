#!/usr/bin/python3
"""Defines the amenity test class"""

import models
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_args(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_store_new(self):
        self.assertIn(Amenity(), models.storage.all().values())


if __name__ == "__main__":
    unittest.main()
