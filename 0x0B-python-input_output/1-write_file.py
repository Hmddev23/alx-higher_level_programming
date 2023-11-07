#!/usr/bin/python3
"""define a function for writing in a file"""


def write_file(filename="", text=""):
    """write the string into the file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
