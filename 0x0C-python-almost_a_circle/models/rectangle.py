#!/usr/bin/python3
"""defines the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """representation of a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialization a new rectangle.

        Args:
            width (int): Width of the new rectangle.
            height (int): Height of the new rectangle.
            x (int): X coordinate of the new rectangle.
            y (int): Y coordinate of the new rectangle.
            id (int): Id of the new rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set or get the rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set or get the rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set or get the rectangle x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set or get the rectangle y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        """method for value validation"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """return the rectangle area"""
        return self.width * self.height

    def display(self):
        """print the rectangle using the `#` character"""
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        """return the print() and str() representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
            self.x, self.y,
            self.width, self.height)
