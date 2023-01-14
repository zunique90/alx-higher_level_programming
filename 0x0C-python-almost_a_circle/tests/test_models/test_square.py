#!/usr/bin/python3
"""
unittest for square.py
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """unittests for Square class"""

    def isBase(self):
        self.assertIsInstance(Square(10), Base)

    def isRect(self):
        self.assertIsInstance(Square(10), Rectangle)

    def testGetter(self):
        s = Square(5)
        self.assertEqual(5, s.size)

    def testSetter(self):
        s = Square(5)
        s.size = 6
        self.assertEqual(6, s.size)

    def testAttr(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("10")

    def testArgs(self):
        s = Square(5)
        s.update(1, 2, 3)
        self.assertEqual("[Square] (1) 3/0 - 2", str(s))
        s.update(1, 2, 3, 4)
        self.assertEqual("[Square] (1) 3/4 - 2", str(s))

    def testKwargs(self):
        s = Square(5)
        s.update(x=12)
        self.assertEqual("[Square] (10) 12/0 - 5", str(s))
        s.update(size=7, y=1)
        self.assertEqual("[Square] (10) 12/1 - 7", str(s))
        s.update(size=7, id=89, y=1)
        self.assertEqual("[Square] (89) 12/1 - 7", str(s))

if __name__ == "__main__":
    unittest.main()
