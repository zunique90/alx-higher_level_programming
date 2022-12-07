#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for d in sorted(a_dictionary):
        print(d, a_dictionary[d], sep=": ")
