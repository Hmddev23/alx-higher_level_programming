#!/usr/bin/python3
"""
take a GitHub user credentials (username and password)
and uses the GitHub API to display the id.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    authToken = HTTPBasicAuth(username, password)
    request = requests.get('https://api.github.com/user', auth=authToken)
    print(request.json().get('id'))
