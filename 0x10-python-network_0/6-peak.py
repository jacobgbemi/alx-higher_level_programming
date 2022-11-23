#!/usr/bin/python3
"""
Function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    finds num that's greater than both left and right
    """
    if len(list_of_integers) == 0:
        return None

    lists = list_of_integers
    beg = 0
    end = len(lists)-1

    if lists[beg] > lists[beg+1]:
        return lists[beg]
    if lists[end] > lists[end-1]:
        return lists[end]

    mid = (beg+end)//2
    if lists[mid-1] < lists[mid] and lists[mid+1] < lists[mid]:
        return lists[mid]
    if lists[mid] < lists[mid-1]:
        return find_peak(lists[beg:mid+1])
    elif lists[mid] < lists[mid+1]:
        return find_peak(lists[mid:end+1])
    else:
        return lists[beg]
