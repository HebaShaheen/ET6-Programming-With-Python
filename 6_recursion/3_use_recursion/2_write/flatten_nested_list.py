#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def flatten_nested_list(thelist: list, result=None) -> list:
    """Flattens a nested list into a single list with all elements.

    Args:
        thelist (list): A potentially nested list of elements to be flattened.
        result (list, optional): An accumulator for flattened elements. Defaults to None.

    Returns:
        list: A flat list containing all elements of the input list in order.
    Raises:
        TypeError: If the input is not a list.
    """
    if not isinstance(thelist, list):
        raise TypeError("Input must be a list")
    if result is None:  # Base_case 1
        result = []  # Turn_around 1

    for item in thelist:
        if isinstance(item, list):
            flatten_nested_list(item, result)  # recursive call
        else:
            result.append(item)  # Build_up

    return result


print(flatten_nested_list([1, [2, 3, [4, 5]], 6]))
