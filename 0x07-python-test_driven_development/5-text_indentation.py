#!/usr/bin/python3
"""
This is '5-text_indentation' module

It defines a function 'text_indentation'
"""


def text_indentation(text):
    """prints a text with 2 new lines

    after each of these characters: `.`,`?` and `:`

    Raises:
        TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for i in text:
        if flag == 0:
            if i == " ":
                continue
            else:
                flag = 1
        if flag == 1:
            if i == "?" or i == "." or i == ":":
                print(i)
                print()
                flag = 0
            else:
                print(i, end="")
