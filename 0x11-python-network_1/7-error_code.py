#!/usr/bin/python3
"""A script that post a request with some data"""

import requests
import sys

if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
