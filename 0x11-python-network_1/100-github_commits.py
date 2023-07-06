#!/usr/bin/python3

"""
Consumes the github api and prints some commits from a user
"""

import requests
import sys

def main():
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass


if __name__ == '__main__':
    main()
