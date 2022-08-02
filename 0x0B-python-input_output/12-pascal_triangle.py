#!/usr/bin/python3
"""
Contains function that returns int lists of pascal triangle of any given size
"""


def pascal_triangle(n):
    """
    Return:
        empty list [] if n <= 0
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for rows in range(n - 1):
        line = [1]
        for i in range(rows):
            line.append(triangle[rows][i] + triangle[rows][i + 1])

        line.append(1)
        triangle.append(line)

    return triangle
