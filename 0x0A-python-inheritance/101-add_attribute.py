#!/usr/bin/python3
"""define a function that accumulate object attributes"""


def add_attribute(obj, attr, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (any): Object attribute to be added.
        attr (str): Name of the attribute to be added.
        value (any): Value of attr.

    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
