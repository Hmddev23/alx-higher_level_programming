#!/usr/bin/python3
"""define the MyInt class that inherits from int"""


class MyInt(int):
    """convert int operators == and !=."""

    def __eq__(self, value):
        """change == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """change != operator with == behavior."""
        return self.real == value
