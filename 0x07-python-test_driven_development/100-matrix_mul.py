#!/usr/bin/python3
"""
This is the '100-matrix_mul' module.

It defines the 'matrix_mul' function.
"""


def matrix_mul(m_a, m_b):
    """multiplies 2 matrices
    Args:
        m_a: first matrix
        m_b: second matrix
    Raises:
        TypeError: if either m_a or m_b is not a list
        TypeError: if either m_a or m_b is not a list of lists
        ValueError: if either m_a or m_b is empty
        TyperError: if either m_a or m_b contains a non int/float
        TypeError: if rows in lists is not of same size
        ValueError: if m_a and m_b can't be multiplied
    Returns:
        A new matrix containing the results of the multiplication
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    lenmatrixa = len(m_a)
    lenrowa = len(m_a[0])
    lenmatrixb = len(m_b)
    lenrowb = len(m_b[0])
    for i in range(lenmatrixa):
        if len(m_a[i]) != lenrowa:
            raise TypeError("each row of m_a must be of the same size")
    for i in range(lenmatrixb):
        if len(m_b[i]) != lenrowb:
            raise TypeError("each row of m_b must be of the same size")
    for i in range(lenmatrixa):
        for j in range(lenrowa):
            if type(m_a[i][j]) is not int and type(m_a[i][j]) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for i in range(lenmatrixb):
        for j in range(lenrowb):
            if type(m_b[i][j]) is not int and type(m_b[i][j]) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if lenrowa != lenmatrixb:
        raise ValueError("m_a and m_b can't be multiplied")
    matrix = []
    result = 0
    for i in range(lenmatrixa):
        row = []
        for j in range(lenrowb):
            result = 0
            for k in range(lenrowa):
                result += m_a[i][k] * m_b[k][j]
            row.append(result)
        matrix.append(row)
    return matrix
