#!/usr/bin/python3
"""
Defines a function that prints my name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is [full name]"
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
