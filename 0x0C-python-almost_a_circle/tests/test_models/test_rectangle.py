#!/usr/bin/python3
"""
unittest for rectangle.py
"""

import sys
import io
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
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)
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

    def testStr(self):
        r = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual("[Rectangle] (1) 10/10 - 10/10", str(r))

    @staticmethod
    def capture_stdout(rect, method):
        """captures and returns output printed to stdout"""
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def testDisplay(self):
        r = Rectangle(2, 3, 0, 0, 0)
        disp = self.capture_stdout(r, "display")
        self.assertEqual("##\n##\n##\n", disp.getvalue())

    def testDisplayxy(self):
        r = Rectangle(2, 4, 3, 2, 0)
        disp = self.capture_stdout(r, "display")
        self.assertEqual("\n\n   ##\n   ##\n   ##\n   ##\n", disp.getvalue())

    def testArgs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update()
        self.assertEqual("[Rectangle] (10) 10/10 - 10/10", str(r))
        r.update(89)
        self.assertEqual("[Rectangle] (89) 10/10 - 10/10", str(r))
        r.update(89, 2)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(r))
        r.update(89, 2, 3)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/3", str(r))
        r.update(89, 2, 3, 4)
        self.assertEqual("[Rectangle] (89) 4/10 - 2/3", str(r))
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (89) 4/5 - 2/3", str(r))

    def test_arg_order_width(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(1, "2", "3")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(1, "2", 3, "4")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(1, "2", 3, 4, "5")

    def test_arg_order_height(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(1, 2, "3", "4")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(1, 2, "3", 4, "5")

    def test_arg_order_x(self):
        r = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(1, 2, 3, "4", "5")

    def testKwargs(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual("[Rectangle] (11) 10/10 - 10/1", str(r))
        r.update(width=1, x=2)
        self.assertEqual("[Rectangle] (11) 2/10 - 1/1", str(r))
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual("[Rectangle] (89) 3/1 - 2/1", str(r))
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (89) 1/3 - 4/2", str(r))

    def testToDict(self):
        r = Rectangle(10, 2, 1, 9, 1)
        d = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertDictEqual(d, r.to_dictionary())

    def test_save_to_file(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())


if __name__ == "__main__":
    unittest.main()
