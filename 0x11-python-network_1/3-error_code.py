#!/usr/bin/python3
"""A script that prints the response from a request from cmd arguement"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    try:
        response = urllib.request.urlopen(sys.argv[1])
        the_header = response.read()
        print(the_header.decode())
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
