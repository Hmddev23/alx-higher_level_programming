#!/usr/bin/python3
"""pascal's triangle technical interview"""


def pascal_triangle(n):
    """pascal triangle function"""
    if n <= 0:
        return []

    n_list = [[1]]
    for _ in range(1, n):
        p_row = n_list[-1]
        n_row = [1]

        for i in range(1, len(p_row)):
            new_element = p_row[i - 1] + p_row[i]
            n_row.append(new_element)

        n_row.append(1)
        n_list.append(n_row)

    return n_list
