#!/usr/bin/python3
"""
list 10 commits from the most recent to the oldest
of the repository "rails" by the user rails
"""

import sys
import requests

if __name__ == "__main__":
    repo_name = sys.argv[1]
    repo_owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        repo_owner,
        repo_name
    )

    request = requests.get(url)
    repo_commits = request.json()
    try:
        for i in range(10):
            print('{}: {}'.format(
                repo_commits[i].get('sha'),
                repo_commits[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
