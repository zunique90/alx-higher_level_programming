#!/usr/bin/python3
"""This module defines the class BaseGeometry
    and a class Rectangle that is a subclass of BaseGeometry
"""


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

class Rectangle(BaseGeometry):
    """class Rectangle"""

    def __init__(self, width, height):
        """instantiation of the class attributes"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
