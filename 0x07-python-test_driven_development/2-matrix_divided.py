#!/usr/bin/python3
"""
"2-matrix_divided" module.
function that
divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix
    """
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    lenght = None
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if lenght is None:
            lenght = len(row)
        elif lenght != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(case / div, 2) for case in row] for row in matrix]
