#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = len(tuple_a)
    b = len(tuple_b)

    if a < 2:
        if a == 0:
            tuple_a = (0, 0)
        else:
            tuple_a = (tuple_a[0], 0)
    if b < 2:
        if b == 0:
            tuple_b = (0, 0)
        else:
            tuple_b = (tuple_b[0], 0)

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
