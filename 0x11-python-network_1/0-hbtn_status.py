#!/usr/bin/python3
"""This script fetches https://alx-intranet.hbtn.io/status"""

import urllib.request as request


if __name__ =="__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))
