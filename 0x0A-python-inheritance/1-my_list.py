#!/usr/bin/python3
"""1-my_list.py"""


class MyList(list):
    """Subclass of the list class with an additional methods"""

    def print_sorted(self):
        """
        Prints the list in sorted (ascending) order.
        """
        print(sorted(self))
