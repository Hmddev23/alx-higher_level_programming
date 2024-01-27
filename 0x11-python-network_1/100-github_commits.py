#!/usr/bin/python3
"""
list 10 repository_commits from the most recent to the oldest
of the repository "rails" by the user rails
"""

import sys
import requests

if __name__ == "__main__":
    repository_name = sys.argv[1]
    repository_owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/repository_commits'.format(repository_owner, repository_name)

    request = requests.get(url)
    repository_commits = request.json()

    try:
        for i in range(10):
            print('{}: {}'.format(
                repository_commits[i].get('sha'),
                repository_commits[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
