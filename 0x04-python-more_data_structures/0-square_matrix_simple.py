#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    tmp_matrix = []
    for x in matrix:
        tmp_matrix.append(list(map(lambda x: x**2, x)))
    return (tmp_matrix)
