#!/usr/bin/python3
"""
send a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]

    data = {'q': letter}

    request = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        response = request.json()
        if response == {}:
            print('No result')
        else:
            print('[{}] {}'.format(response.get('id'), response.get('name')))
    except ValueError:
        print('Not a valid JSON')
