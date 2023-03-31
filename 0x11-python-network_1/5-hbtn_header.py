#!/usr/bin/python3
"""
Displays the value of the X-Request-Id header variable
in the header of the response
"""

from sys import argv
import requests


if __name__ == "__main__":
    with requests.get(argv[1]) as response:
        print(response.headers.get("X-Request-Id"))
