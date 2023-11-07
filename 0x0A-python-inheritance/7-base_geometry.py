#!/usr/bin/python3
"""define the BaseGeometry class"""


class BaseGeometry:
    """representation of the class"""

    def area(self):
        """no implementation"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate the value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
