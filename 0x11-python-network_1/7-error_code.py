#!/usr/bin/python3
"""
This script sends a request to the URL
and displays the body of the response
"""

from sys import argv
import requests


if __name__ == "__main__":
    req = requests.get(argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
