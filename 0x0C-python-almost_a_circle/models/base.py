#!/usr/bin/python3
"""
This module defines the class `Base`
"""


class Base:
    """class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiation of a Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
