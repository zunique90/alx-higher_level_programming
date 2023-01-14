#!/usr/bin/python3
"""
unittest for base.py
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test class for Base class"""

    def setUp(self):
        """creates insstances of class Base"""
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()

    def teardown(self):
        """deletes instances of class Base"""
        del self.b1
        del self.b2
        del self.b3
        del self.b4
        del self.b5

    def test_objects(self):
        """tests instances"""
        self.assertIsInstance(self.b1, Base)
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 4)


if __name__ == "__main__":
    unittest.main()
