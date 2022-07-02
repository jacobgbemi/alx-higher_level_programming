#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            if element is not row[len(row) - 1]:
                print("{:d}".format(element), end=" ")
            else:
                print("{:d}".format(element), end="")
        print()
