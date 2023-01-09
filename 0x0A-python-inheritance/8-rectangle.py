#!/usr/bin/python3
"""This module defines the class BaseGeometry
    and a class Rectangle that is a subclass of BaseGeometry
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
