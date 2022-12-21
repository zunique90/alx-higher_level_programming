#!/usr/bin/python3
"""class Square that defines a square by: (based on 5-square.py)"""


class Square:
    """represents a square"""

    def __init__(self, sizei=0, position=(0, 0)):
        """Initializes the square class"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """retrieves current position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position value"""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the current area of the square"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return

        [print() for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print("#", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print()
