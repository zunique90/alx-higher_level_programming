#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest) of the given repository
"""

from sys import argv
from requests import get


if __name__ == "__main__":
    arg = argv
    url = "https://api.github.com/repos/{}/{}/commits".format(arg[2], arg[1])

    with get(url) as r:
        for commits in r.json()[:10]:
            print(
                    "{}: {}".format(
                        commits.get("sha"), commits.get("commit").get(
                            "author").get("name")))
