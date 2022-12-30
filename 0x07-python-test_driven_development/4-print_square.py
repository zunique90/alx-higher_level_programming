#!/usr/bin/python3
"""
This is the '4-print_square' module

It defines a function 'print_square'
"""


def print_square(size):
    """prints a square

    Args:
        size: the size length of the square to be printed
    Raises:
        TypeError: if size is not an int, or is a negative float
        ValueError: if size is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print()
