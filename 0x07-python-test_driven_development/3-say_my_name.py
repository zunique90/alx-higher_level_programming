#!/usr/bin/python3
"""
This is the '3-say_my_name' module

It defines a function 'say_my_name' that prints a name
"""


def say_my_name(first_name, last_name=""):
    """Prints a name.

    Args:
        first_name: first name to print.
        last_name: optional last name to print
    Raises:
        TypeError: if either first_name or last_name is not a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
