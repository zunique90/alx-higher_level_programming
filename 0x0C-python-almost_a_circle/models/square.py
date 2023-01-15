#!/usr/bin/python3
"""
This module defines the class `Square`
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """instantiation of a Square class"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """retrieves the size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the value of size"""
        self.width = value
        self.height = value

    def __str__(self):
        """return customized string repesentation of Square"""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
