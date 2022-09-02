#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = [list(map((lambda x: x * x), i)) for i in matrix]
    return square_matrix
