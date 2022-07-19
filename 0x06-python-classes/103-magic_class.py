#!/usr/bin/python3

"""Define a class MagicClass"""

import math


class MagicClass:
    """MagicClass class"""
    def __init__(self, radius=0):
        """Initialize a new class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Circumference"""
        return 2 * math.pi * self.__radius
