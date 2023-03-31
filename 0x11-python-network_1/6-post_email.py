#!/usr/bin/python3
"""
This script sends a POST request to the passed URL with the email
as a parameter, and finally displays the body of the response.
"""

from sys import argv
import requests


if __name__ == "__main__":
    args = argv
    val = {"email": args[2]}
    req = requests.post(args[1], data=val)
    print(req.text)
