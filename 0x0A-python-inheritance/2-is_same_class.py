#!/usr/bin/python3
"""define function checker class"""


def is_same_class(obj, a_class):
    """
    check if an object is exactly an instance of a specific class.

    Args:
        obj: Object.
        a_class: Class to check.

    Returns:
        True if 'obj' is an instance of 'a_class', otherwise False.
    """

    if type(obj) == a_class:
        return True
    else:
        return False
