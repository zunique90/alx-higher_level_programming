#!/usr/bin/python3
"""
This is the '2-matrix_divided' module

It defines a division function
"""


def matrix_divided(matrix, div):
    """Divides all elements of matrix by div.

    Raises:
        TypeError: if matrix is not a lists of list of integers or floats
        TypeError: if rows in the matrix are not of same size
        TypeError: if div is not an integer or float
        ZeroDivisionError: if div == 0

    Returns a new matrix containing the results rounded to 2 decimal places
    """

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
