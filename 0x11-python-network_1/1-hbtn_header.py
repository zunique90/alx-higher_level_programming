#!/usr/bin/python3
"""
Displays the value of the X-Request-Id header variable
found in the header of the response
"""

from sys import argv
import urllib.request as request


if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        print(response.headers.get("X-Request-Id"))
