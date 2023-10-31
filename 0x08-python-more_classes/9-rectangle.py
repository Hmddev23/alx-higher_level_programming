#!/usr/bin/python3
"""define the class Rectangle"""


class Rectangle:
    """Representation of a rectangle

    attributes : number_of_instances (int): the number of rectangle intances.
    print_symbol (any): the symbol used for a string representation.
    """

    print_symbol = "#"
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializing the rectangle

        Args:
            width (int): Width of the rectangle. Defaults to 0.
            height (int): Height of the rectangle. Defaults to 0.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the rectangle width.

        Returns:
            Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set the rectangle width.

        Args:
            value (int): Width of the rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the rectangle height.

        Returns:
            Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set the rectangle height.

        Args:
            value (int): Height of the rectangle.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the rectangle area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """ return the rectangle perimetre."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        return the rectangle with equal or larger area between rect_1 and rect_2.

        Parameters:
            rect_1 (Rectangle): First rectangle for comparison.
            rect_2 (Rectangle): Second rectangle for comparison.

        Returns:
            Rectangle: The rectangle with the larger or equal area.

        Raises:
            TypeError: If either rect_1 or rect_2 are not instances of Rectangle class.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """
        return a rectangle string representation using '#' characters.
        If the rectangle's perimeter is 0, returns an empty string.

        Returns:
            A string representation of the rectangle using '#' characters.
        """
        if self.perimeter() == 0:
            return ("")
        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    @classmethod
    def square(cls, size=0):
        """
        return a new Rectangle instance with width == height == size
        """
        return cls(size, size)

    def __repr__(self):
        """return the rectangle string Representaion."""
        rect = "Rectangle(" + str(self.__width) + ", "
        rect += str(self.__height) + ")"
        return rect

    def __del__(self):
        """print the deletion message."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
