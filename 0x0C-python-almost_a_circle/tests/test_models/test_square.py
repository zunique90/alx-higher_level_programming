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

    def testStr(self):
        r = Square(10, 10, 10, 10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(r))

    def testAttr(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("10")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

    def testArgs(self):
        s = Square(5)
        s.update(1, 2)
        self.assertEqual("[Square] (1) 0/0 - 2", str(s))
        s.update(1, 2, 3)
        self.assertEqual("[Square] (1) 3/0 - 2", str(s))
        s.update(1, 2, 3, 4)
        self.assertEqual("[Square] (1) 3/4 - 2", str(s))

    def test_arg_order_size(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(1, "2", "3")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(1, "2", 3, "4")

    def test_arg_order_x(self):
        s = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(1, 2, "3", "4")

    def testKwargs(self):
        s = Square(5)
        s.update(x=12)
        self.assertEqual("[Square] (14) 12/0 - 5", str(s))
        s.update(size=7, y=1)
        self.assertEqual("[Square] (14) 12/1 - 7", str(s))
        s.update(size=7, id=89, y=1)
        self.assertEqual("[Square] (89) 12/1 - 7", str(s))

    def testToDict(self):
        r = Square(10, 2, 1, 1)
        d = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(d, r.to_dictionary())

    def test_save_to_file(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())


if __name__ == "__main__":
    unittest.main()
