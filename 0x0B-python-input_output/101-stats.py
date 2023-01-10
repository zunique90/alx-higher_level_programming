#!/usr/bin/python3
"""This script reads stdin line by line and computes metrics"""


import sys
from collections import defaultdict


def print_stats():
    """prints statistics"""
    print("File size: ", total_size)
    for status_code in sorted(status_codes.keys()):
        print(f"{status_code}: {status_codes[status_code]}")


if __name__ == "__main__":
    line_count = 0
    total_size = 0
    status_codes = defaultdict(int)

    try:
        for line in sys.stdin:
            line_count += 1

            fields = line.strip().split(" ")

            total_size += int(fields[-1])

            status_codes[fields[-2]] += 1

            if line_count % 10 == 0:
                print_stats()
    except KeyboardInterrupt:
        print_stats()
        raise
