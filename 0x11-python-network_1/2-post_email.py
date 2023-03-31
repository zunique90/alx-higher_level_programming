#!/usr/bin/python3
"""
This script sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response (decoded in utf-8)
"""

from sys import argv
from urllib.request import urlopen, Request
from urllib.parse import urlencode


if __name__ == "__main__":
    args = argv
    val = {"email": args[2]}
    data = urlencode(val)
    data = data.encode()
    req = Request(args[1], data)
    with urlopen(req) as response:
        print(response.read().decode("utf-8"))
