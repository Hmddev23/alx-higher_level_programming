#!/usr/bin/python3
"""define a function for reading from a text file"""


def read_file(filename=""):
    """read a given file and print its content"""
    with open(filename, "r", encoding='utf-8') as file:
    print(file.read(), end="")
