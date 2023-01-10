#!/usr/bin/python3
"""This module defines the function `read_file`"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename) as f:
        print(f.read(), end="")
