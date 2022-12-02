#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lists in matrix:
        j = len(lists) - 1
        for row in lists:
            i = 0
            if i == j:
                print("{:d}".format(row))
            else:
                print("{:d}".format(row), end=" ")
            i += 1
        print()
