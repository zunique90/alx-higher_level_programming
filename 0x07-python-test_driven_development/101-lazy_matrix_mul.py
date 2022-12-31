#!/usr/bin/python3
"""
This is the '101-lazy_matrix_mul' module.

It defines the function 'lazy_matrix_mul'.
"""


import numpy


def lazy_matrix_mul(m_a, m_b):
    """multiplies two matrices using the module numpy.

    Args:
        m_a: first matrix
        m_b: second matrix
    Returns:
        A new matrix containing the results of the multiplication
    """
    return numpy.matmul(m_a, m_b)
