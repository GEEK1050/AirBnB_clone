#!/usr/bin/python3
"""Defines unittests for city class"""

import models
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """testing of the City class."""

    def test_no_args(self):
        self.assertEqual(City, type(City()))

    def test_store_new(self):
        self.assertIn(City(), models.storage.all().values())


if __name__ == "__main__":
    unittest.main()
