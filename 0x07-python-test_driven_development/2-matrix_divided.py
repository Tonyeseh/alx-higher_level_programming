#!/usr/bin/python3
""" Module defines a matrix division function """


def matrix_divided(matrix, div):
    """ Divide all elements of a matrix.

        Args:
            matrix (list): list of lists containing ints or floats
            div (int/float): the divisor

        Raises:
            TypeError: If the contains an non-int or float element
            TypeError: If the rows of the matrix is not of same size
            TypeError: If div is not a float or int
            ZeroDivisionError: If div is 0.

        Returns:
            A new matrix that divided by div.
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(x, list) for x in matrix) or
            not all((isinstance(y, int) or isinstance(y, float))
                    for y in [z for x in matrix for z in x])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    return [list(map(lambda x: round(x / div, 2), row))for row in matrix]
