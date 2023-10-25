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
        """return the square area"""
        return (self.__size ** 2)

    def my_print(self):
        """Print square with the character #"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.size == 0:
            print("")
