#!/usr/bin/python3
"""This module defines the function `add_attribute`"""


def add_attribute(obj, att, value):
    """adds attrubute to object if possible"""
    if hasattr(obj, '__dict__'):
        setattr(obj, att, value)
    else:
        raise TypeError("can't add new attribute")
