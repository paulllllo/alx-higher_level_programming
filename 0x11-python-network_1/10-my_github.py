#!/usr/bin/python3

"""
Consumes the Github API
"""

import requests
from requests.auth import HTTPBasicAuth
import sys


def main():
    username = sys.argv[1]
    token = sys.argv[2]
    url = 'https://api.github.com/user'
    res = requests.get(url, auth=HTTPBasicAuth(username, token))
    try:
        data = res.json()
        print(data.get('id'))
    except Exception as e:
        print('')


if __name__ == '__main__':
    main()
