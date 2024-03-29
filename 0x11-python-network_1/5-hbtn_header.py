#!/usr/bin/python3
"""A script that prints the headers from a request using the request module"""

import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
