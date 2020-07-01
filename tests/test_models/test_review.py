#!/usr/bin/python3
"""Defines unittests review class"""

import models
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """testing the Review class."""

    def test_no_args(self):
        self.assertEqual(Review, type(Review()))

    def test_store_new(self):
        self.assertIn(Review(), models.storage.all().values())


if __name__ == "__main__":
    unittest.main()
