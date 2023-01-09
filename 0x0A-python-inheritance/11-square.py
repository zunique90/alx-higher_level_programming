#!/usr/bin/python3
"""This module defines a class Square that is a subclass of Rectangle
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size):
        """instantiation of the class attributes"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
