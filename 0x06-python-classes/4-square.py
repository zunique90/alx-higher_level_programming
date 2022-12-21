#!/usr/bin/python3
"""class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """Class that defines a square"""

    def __init(self, size=0):
        """Instantiation with optional size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """retrieves current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size and handles errors"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size ** 2
