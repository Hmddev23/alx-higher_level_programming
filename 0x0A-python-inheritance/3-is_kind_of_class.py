#!/usr/bin/python3
"""define class checker for a function"""


def is_kind_of_class(obj, a_class):
    """
    check if an object is an instance of a specific class.

    Args:
        obj: Object.
        a_class: Class to check.

    Returns:
        True if 'obj' is an instance of 'a_class', otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
