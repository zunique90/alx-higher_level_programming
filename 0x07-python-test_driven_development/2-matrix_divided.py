#!/usr/bin/python3
"""Defines a division function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements of matrix by div, returns a new matrix"""

    if div is None or (type(div) != int and type(div) != float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    if matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    length = None
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if length is None:
            length = len(row)
        elif length != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    return [[round(i / div, 2) for i in row] for row in matrix]
