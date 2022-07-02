#!/usr/bin/python3

def no_c(my_string):
    copy = [alpha for alpha in my_string if alpha != 'c' and alpha != 'C']
    return ("".join(copy))
