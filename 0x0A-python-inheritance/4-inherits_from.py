#!/usr/bin/python3
"""define an inherited class-checking function"""


def inherits_from(obj, a_class):
    """check if an object is an inherited instance of a class.

    Args:
        obj (any): Object to check.
        a_class (type): Class that match the type of the obj.

    Returns:
        True if 'obj' is an inherited instance of 'a_class'
        otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
