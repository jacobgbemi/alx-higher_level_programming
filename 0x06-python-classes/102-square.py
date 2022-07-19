#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Initialize a new class"""
        self.size = size

    @property
    def size(self):
        """Getter for square size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Area of the square"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """ == comparision """
        return self.area() == other.area()

    def __ne__(self, other):
        """ != comparison """
        return self.area() != other.area()

    def __lt__(self, other):
        """ < comparison """
        return self.area() < other.area()

    def __le__(self, other):
        """ <= comparison """
        return self.area() <= other.area()

    def __gt__(self, other):
        """ > comparison """
        return self.area() > other.area()

    def __ge__(self, other):
        """ >= compmarison """
        return self.area() >= other.area()


if __name__ == "__main__":
    Square()
