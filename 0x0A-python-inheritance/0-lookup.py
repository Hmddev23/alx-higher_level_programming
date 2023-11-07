#!/usr/bin/python3
"""function to return a list"""


def lookup(obj):
    """return a list of methods and attributes"""
    return list(dir(obj))
