#!/usr/bin/python3
"""A script that prints the response from a request from cmd arguement"""

import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    the_header = response.info()

print(the_header.get('X-Request-Id'))
