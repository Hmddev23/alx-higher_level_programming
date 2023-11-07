#!/usr/bin/python3
"""implementing of the BaseGeometry class"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """representation of a Rectangle class"""

    def __init__(self, width, height):
        """concontructor and width, height"""
        self.integer_validator("height", height)
        self.integer_validator("width", width)

        self.__width = width
        self.__height = height

    def area(self):
        """return the rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """return the rectangle description"""
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
