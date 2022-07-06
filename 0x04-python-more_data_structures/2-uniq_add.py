#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    for element in set(my_list):
        total += element
    return(total)
