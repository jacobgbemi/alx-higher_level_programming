#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        squares = []
        for rows in matrix:
            squares.append(list(map(lambda x: x**2, rows)))
        return (squares)
    return None
