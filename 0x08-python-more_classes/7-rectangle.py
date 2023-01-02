#!/usr/bin/python3
"""This module defines the class Rectangle"""


class Rectangle:
    """class Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """prints the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Returns a string representation of Rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints message for every Rectangle deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
