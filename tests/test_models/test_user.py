#!/usr/bin/python3
"""define unittest for the user class"""

import models
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """testing the User class."""

    def test_no_args(self):
        self.assertEqual(User, type(User()))

    def test_store_new(self):
        self.assertIn(User(), models.storage.all().values())


if __name__ == "__main__":
    unittest.main()

