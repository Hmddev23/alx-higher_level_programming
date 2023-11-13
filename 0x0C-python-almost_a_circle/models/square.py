#!/usr/bin/python3
"""define the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """representation of a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialization of a new square

        Args:
            size (int): Size of the new Square.
            x (int): X coordinate of the new Square.
            y (int): Y coordinate of the new Square.
            id (int): ID of the new Square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return the print() and str() representation of the square"""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """get or set the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """system method that updates instance attributes via */**args"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """update the square

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

