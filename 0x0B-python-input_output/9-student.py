#!/usr/bin/python3
"""define the class Student"""


class Student:
    """ get the representation of a dictionary from a Student instance"""

    def __init__(self, first_name, last_name, age):
        """instantiation of the class attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """get the representation of a dictionary from a Student instance"""
        return self.__dict__
