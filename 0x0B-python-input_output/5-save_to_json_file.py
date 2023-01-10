#!/usr/bin/python3
"""This module defines the function `save_to_json_file`"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    obj = json.dumps(my_obj)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(obj)
