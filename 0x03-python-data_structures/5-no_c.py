#!/usr/bin/python3
def no_c(my_string):
    copy = ""
    for char in my_string:
        if char != "c" and char != "C":
            copy += char

    return copy
