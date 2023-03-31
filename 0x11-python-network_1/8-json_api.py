#!/usr/bin/python3
"""
This script send a POST request
"""

import requests as r
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        args = argv
        val = {"q": args[1]}
    else:
        val = {"q": ""}
    try:
        req = r.post("http://0.0.0.0:5000/search_user", data=val)
        datas = req.json()
        if datas:
            print("[{}] {}".format(datas.get("id"), datas.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
