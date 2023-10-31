#!/usr/bin/python3
"""defines a print_square function"""


def print_square(size):
    """print a square with the # character.

    Args:
        size (int): Height/Width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
    print("")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
