#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    fnl_matrix = [[0 for _ in range(len(row))] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            fnl_matrix[i][j] = matrix[i][j] ** 2

    return (fnl_matrix)
