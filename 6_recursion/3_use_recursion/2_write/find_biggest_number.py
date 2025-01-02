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
    """

    assert isinstance(thelist, list), "This should be a list"

    if not thelist:  # Check if the list is empty
        raise ValueError("Please provide a non-empty list.")

    biggest = thelist[0]
    for item in thelist:
        assert isinstance(item, int), "items should be integer"
        if item > biggest:
            biggest = item
    return biggest
