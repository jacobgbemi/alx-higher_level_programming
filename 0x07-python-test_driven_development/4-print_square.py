#!/usr/bin/python3
"""
Defines a function that square with the character #.
"""


def print_square(size):
    """
    Prints square with #'s given int size
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("", end="")
    else:
        for rows in range(size):
            [print("#", end="") for i in range(size)]
            print("")
