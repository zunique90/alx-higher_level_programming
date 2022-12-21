#!/usr/bin/python3
"""class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """represents a square"""

    def __init__(self, size):
        """Initializes the square class"""
        self.size = size

    @property
    def size(self):
        """retrieves current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current area of the square"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print()
        if self.__size == 0:
            print()
