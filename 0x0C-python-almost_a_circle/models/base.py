#!/usr/bin/python3
"""
This module defines the class `Base`
"""

import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list represented by json_string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1, 1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        listDict = []
        listInst = []

        if os.path.exists(filename):
            with open(filename, "r") as f:
                listDict = cls.from_json_string(f.read())
                for dicts in listDict:
                    listInst.append(cls.create(**dicts))
        return listInst
