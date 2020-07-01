#!/usr/bin/python3
"""Defines unittests for place class"""

import models
import unittest
from datetime import datetime
from models.place import Place


class TestPlace(unittest.TestCase):
    """testing Place class."""

    def test_no_args(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), models.storage.all().values())


if __name__ == "__main__":
    unittest.main()
