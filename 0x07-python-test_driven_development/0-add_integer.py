#!/usr/bin/python3
"""
This is the '0-add_integer' module

it defines an addition function 'add_integer'
"""


def add_integer(a, b=98):
    """Returns the integer addition of a and b

    Raises:
        TypeError: if either a or b is not an int or float
    """
    if a is None or (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
