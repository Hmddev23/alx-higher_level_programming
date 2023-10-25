#!/usr/bin/python3
"""define the class Square"""


class Square:
    """Define class Square constructor"""
    def __init__(self, size=0):
        """initialization the new square

        Args:
        size (int): Size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    self.__size = size
