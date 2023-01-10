#!/usr/bin/python3
"""Defines the function `pascal_triangle`"""


def pascal_triangle(n):
    """ returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triList = []
    for i in range(n):
        triList.append([])
        triList[i].append(1)

        for j in range(1, i):
            triList[i].append(triList[i - 1][j - 1] + triList[i - 1][j])
        if i != 0:
            triList[i].append(1)

    return triList
