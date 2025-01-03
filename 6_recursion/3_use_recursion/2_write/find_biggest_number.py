#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def find_biggest_number(thelist: list[int]) -> int:
    """Find the biggest number in the list

    Args:
        thelist (list[int]): a list to search the biggest number in it

    Raises:
        ValueError: give value error if the list is empty
        AssertionError: gives error if it is not a list

    Returns:
        int: returns the biggest number

    >>> find_biggest_number([4, 8, 1])
    8

    >>> find_biggest_number([5, 90, 90])
    90

    >>> find_biggest_number([124, 403, 620])
    620
    """

    assert isinstance(thelist, list), "This should be a list"

    if not thelist:  # Base case 1
        # Turn_around 1
        raise ValueError("The list is empty. Cannot find the biggest number.")
    if len(thelist) == 1:  # Base case 2
        return thelist[0]  # Turn_around 2

    next_num = find_biggest_number(thelist[1:])  # Recursive call | Breack_down
    if thelist[0] > next_num:
        return thelist[0]
    else:
        return next_num
