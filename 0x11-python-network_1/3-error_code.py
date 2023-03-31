#!/usr/bin/python3
"""
This script sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""

from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError


if __name__ == "__main__":
    req = Request(argv[1])
    try:
        with urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
