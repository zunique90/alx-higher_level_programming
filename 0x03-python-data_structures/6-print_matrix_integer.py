#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for dup in matrix:
        for i in dup:
            print("{:d} ".format(i), end="")
        print()
