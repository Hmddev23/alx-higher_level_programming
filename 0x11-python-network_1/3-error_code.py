#!/usr/bin/python3
"""
send a request to a URL and displays the body of the response.
"""

import sys
import urllib.request

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
    except:
        pass
