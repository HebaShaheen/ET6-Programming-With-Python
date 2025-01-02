#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def count_items_in_list(thelist: list) -> int:
    """A function returns the length of a list

    Args:
        thelist (list): the list want to count its items

    Returns:
        int: the list length
    """
    assert isinstance(thelist, list), "it should be a list"
    return len(thelist)
