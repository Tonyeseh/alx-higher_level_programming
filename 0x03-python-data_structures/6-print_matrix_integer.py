#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for sublist in matrix:
        for j in range(len(sublist)):
            if j == len(sublist) - 1:
                print("{:d}".format(sublist[j]), end='')
            else:
                print("{:d}".format(sublist[j]), end=" ")
        print()
