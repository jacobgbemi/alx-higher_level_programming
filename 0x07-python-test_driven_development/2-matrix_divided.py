#!/usr/bin/python3
"""
Defines a function tht divides all the elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Returns new matrix with dividends
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if type(div) is bool:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(msg)

    new_matrix = []
    list_len = len(matrix[0])
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(msg)
        for element in lists:
            if isinstance(element, bool):
                raise TypeError(msg)
        if len(lists) != list_len:
            raise TypeError("Each row of the matrix must have the same size")
        newlist = []
        for element in lists:
            if type(element) is not int and type(element) is not float:
                raise TypeError(msg)
            newlist.append(round(element/div, 2))
        new_matrix.append(newlist)
    return new_matrix
