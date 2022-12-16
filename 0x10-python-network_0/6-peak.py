#!/usr/bin/python3
""" module contains the find_peak function"""


def find_peak(list_of_integers):
    """Find a peak in a list of unsorted integers"""
    size = len(list_of_integers)
    if size == 0:
        return
    mid = int(size / 2)
    if (mid == 0 or (list_of_integers[mid] >= list_of_integers[mid - 1])) and (mid == size - 1 or (list_of_integers[mid] >= list_of_integers[mid + 1])):
        return list_of_integers[mid]
    if list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
