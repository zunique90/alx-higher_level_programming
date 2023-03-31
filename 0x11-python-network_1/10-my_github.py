#!/usr/bin/python3
"""
Python script that takes Github Credentials and displays user id
using the GitHub API
"""

from sys import argv
import requests as r
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    userAuth = HTTPBasicAuth(argv[1], argv[2])
    response = r.get("https://api.github.com/user", auth=userAuth)
    userId = response.json()
    print(userId.get("id"))
