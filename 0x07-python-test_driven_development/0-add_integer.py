#!/usr/bin/python3
"""Defines an addition function"""


def add_integer(a, b=98):
    """Returns the integer addition of a and b"""
    if a is None or (type(a) != int and type(a) != float):
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
