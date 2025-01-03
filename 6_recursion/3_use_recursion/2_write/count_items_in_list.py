#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def count_items_in_list(thelist: list) -> int:
    """A function returns the length of a list

    Args:
        thelist (list): the list want to count its items

    Returns:
        int: the list length

    >>> count_items_in_list([1,2,3])
    3

    >>> count_items_in_list([5, 7, 8, 3, 6])
    5

    >>> count_items_in_list([4])
    1
    """
    assert isinstance(thelist, list), "it should be a list"
    # return len(thelist)
    if not thelist:
        return 0

    return 1 + count_items_in_list(thelist[1:])
