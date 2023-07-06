#!/usr/bin/python3
"""A script that post a request with some data"""

import requests
import sys

if __name__ == "__main__":
    try:
        letter = sys.argv[1]
    except IndexError:
        letter = ''
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})
    try:
        if r.json() != {}:
            data = r.json()
            print('[{}] {}'.format(data.get('id'), data.get('name')))
        else:
            print('No result')
    except requests.exceptions.JSONDecodeError as err:
        print('Not a valid JSON')
