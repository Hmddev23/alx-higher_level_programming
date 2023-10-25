#!/usr/bin/python3
"""define the class Square"""


class Square:
    """define class Square constructor"""

    def __init__(self, size=0):
        """initialization of the new square

        Args:
            size (int): Size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """get or set the square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the Square area"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
