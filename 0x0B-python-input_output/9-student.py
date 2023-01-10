#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """class Student"""

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return self.__dict__

    def __init__(self, first_name, last_name, age):
        """initializes the student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
