#!/usr/bin/python3
"""define a function that append text is a file"""


def append_write(filename="", text=""):
    """append the text into the end of a file"""
    with open(filename, "a", encoding="utf8") as fi:
        return fi.write(text)
