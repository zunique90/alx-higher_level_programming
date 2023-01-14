#!/usr/bin/python3
"""
unittest for rectangle.py
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unittests for Rectangle class"""

    def isBase(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def testId(self):
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(12, r.id)

    def isPrivate(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def testGetter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)
        self.assertEqual(7, r.height)
        self.assertEqual(7, r.x)
        self.assertEqual(5, r.y)

    def testSetter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 6
        self.assertEqual(6, r.width)
        r.height = 8
        self.assertEqual(8, r.height)
        r.x = 8
        self.assertEqual(8, r.x)
        r.y = 6
        self.assertEqual(6, r.y)

    def testAttr(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, "3", 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -3, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, "1")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def testArea(self):
        r = Rectangle(10, 2, 3, 1)
        self.assertEqual(20, r.area())
