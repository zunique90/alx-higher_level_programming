#!/usr/bin/python3
"""This module defines the class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry"""

    def area(self):
        """a public instance method that is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a public instance method that validates value"""
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
