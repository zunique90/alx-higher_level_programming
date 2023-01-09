#!/usr/bin/python3
"""This module defines a class MyInt that is a subclass if int"""


class MyInt(int):
    """a rebel class that inverts == and != operators"""

    def __eq__(self, num):
        """inverts the == operator"""
        return self.real != num

    def __ne__(self, num):
        """inverts the != operator"""
        return self.real == num
