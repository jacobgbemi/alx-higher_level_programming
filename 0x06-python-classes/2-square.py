#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Square Class"""
    def __init__(self, size=0):
        """Class instance"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size


if __name__ == "__main__":
    Square()
