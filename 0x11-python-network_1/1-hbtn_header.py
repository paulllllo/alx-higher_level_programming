#!/usr/bin/python3
"""A script that prints the response from a request from cmd arguement"""

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        the_headers = response.info()
        header_value = the_headers.get('X-Request-Id')

        print(header_value)
