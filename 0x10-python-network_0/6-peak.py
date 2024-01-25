#!/usr/bin/python3
"""
find a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    find a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None

    bottom, top = 0, len(list_of_integers) - 1

    while bottom < top:
        midd = (bottom + top) // 2

        if list_of_integers[midd] > list_of_integers[midd + 1]:
            top = midd
        else:
            bottom = midd + 1

    return list_of_integers[bottom]
