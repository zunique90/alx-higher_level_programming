#!/usr/bin/python3
"""This module defines a class Rectangle that is a subclass of BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""

    def __init__(self, width, height):
        """instantiation of the class attributes"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return the print() and str() representation of the object"""
        return f"[Rectangle] {self.__width}/{self.__height}"
