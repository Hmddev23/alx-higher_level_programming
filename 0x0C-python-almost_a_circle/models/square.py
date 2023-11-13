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
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                self.width)
