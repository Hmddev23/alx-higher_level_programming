#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    tmp_node = []
    for x in matrix:
        tmp_node.append(list(map(lambda x: x**2, x)))
    return (tmp_node)
