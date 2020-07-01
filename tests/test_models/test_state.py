#!/usr/bin/python3
"""Define unittest fot the state class"""

import models
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """testing the State class"""

    def test_no_args(self):
        self.assertEqual(State, type(State()))

    def test_store_new(self):
        self.assertIn(State(), models.storage.all().values())


if __name__ == "__main__":
    unittest.main()
