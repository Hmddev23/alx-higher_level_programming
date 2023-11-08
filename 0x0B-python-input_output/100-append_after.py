#!/usr/bin/python3
"""define a function that append text file"""


def append_after(filename="", search_string="", new_string=""):
    """insert a line of text to a file"""
    txt = ""
    with open(filename) as r:
        for ln in r:
            txt += ln
            if search_string in ln:
                txt += new_string

    with open(filename, "w") as w:
        w.write(txt)
