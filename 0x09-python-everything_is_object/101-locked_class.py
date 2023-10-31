#!/usr/bin/python3
"""define the locked class"""


class LockedClass:
    """
    This class restricts the instantiation of new attributes for LockedClass,
    allowing only attributes named 'first_name' to be created.
    """

    __slots__ = ["first_name"]
