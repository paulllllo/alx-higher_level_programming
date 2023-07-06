#!/usr/bin/python3
"""A script that prints the response from a request from cmd arguement"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            the_header = response.read()
            print(the_header.decode())
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
