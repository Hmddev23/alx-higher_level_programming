#!/usr/bin/python3
"""define the class Square a subclass from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """representation of the Square class"""

    def __init__(self, size):
        """Initialization of a new square.

        Args:
            size (int): Size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
