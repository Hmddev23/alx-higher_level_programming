#!/usr/bin/python3
"""define the class Square"""


class Square:
    """define class Square constructor"""
    def __init__(self, size=0):
        """initialization of the new square

        Args:
            size (int): Size of the square
        """
        self.__size = size

    @property
    def size(self):
        """get or set the square current size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the square area."""
        return (self.__size ** 2)
