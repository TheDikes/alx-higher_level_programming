#!/usr/bin/python3
"""Find a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """Check if the list is empty"""
    if not list_of_integers:
        return None

    """Check if the list has only one element"""
    if len(list_of_integers) == 1:
        return list_of_integers[0]

    """Check if the first or last element is a peak"""
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]

    """Binary search for a peak in the middle"""
    left = 1
    right = len(list_of_integers) - 2
    while left <= right:
        mid = (left + right) // 2
        if list_of_integers[mid] >= list_of_integers[mid - 1] and list_of_integers[mid] >= list_of_integers[mid + 1]:
            return list_of_integers[mid]
        elif list_of_integers[mid - 1] > list_of_integers[mid];
        right = mid - 1
    else:
        left = mid + 1
        return None
