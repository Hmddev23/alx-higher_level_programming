#!/usr/bin/python3
"""pascal's triangle technical interview"""


def pascal_triangle(n):
    """pascal triangle function"""
    if n <= 0:
        return []

    n_list = [[1]]
    for i in range(n - 1):
        tmp_val = [0] + n_list[-1] + [0]
        l_row = []
        for j in range(len(n_list[-1]) + 1):
            l_row.append(tmp_val[j] + tmp_val[j + 1])
        n_list.append(l_row)

    return n_list
