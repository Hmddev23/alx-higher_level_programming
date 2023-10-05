#!/usr/bin/python3

import string

print(string.ascii_lowercase.translate(
    str.maketrans('', '', string.ascii_lowercase)
))
