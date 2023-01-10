#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """class Student"""

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if type(attrs) is list and all(type(i) is str for i in attrs):
            return{j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__

    def __init__(self, first_name, last_name, age):
        """initializes the student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
