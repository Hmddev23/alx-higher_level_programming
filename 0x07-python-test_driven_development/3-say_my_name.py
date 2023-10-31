#!/usr/bin/python3
"""define the print_name function"""


def say_my_name(first_name, last_name=""):
    """Print the given name.

    Args:
        first_name (str): First name to print.
        last_name (str): Last name to print.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
