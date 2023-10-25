#!/usr/bin/python3
"""define the MagicClass that does exactly what's provided in the bytecode"""

import math


class MagicClass:
    """representation of a circle"""

    def __init__(self, radius=0):
        """Initialization of the a MagicClass.

        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """return the MagicClass area"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """return The MagicClass circumference."""
        return (2 * math.pi * self.__radius)
