#!/usr/bin/python3
"""
This module `1-my_list` defines a class
"""


class MyList(list):
    """This is a child of the parent class `list`"""

    def print_sorted(self):
        """a public instance method that prints the list
        but sorted (ascending sort)"""
        print(sorted(self))
