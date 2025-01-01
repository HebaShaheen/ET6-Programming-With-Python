#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Describe this solution by filling in the docstring and labeling each part.
> I did it in 1/1/2025

"""


def sum_digits_to_threshold(n, threshold):
    """
    This function recursively sums the digits of a number `n` until the result
    is less than a given 'threshold' or a base case is satisfied.

    Returns:
    int: The digit sum or the threshold, whichever is appropriate.

    Base case 1:
        If 'n' is a single-digit number (less than 10), return 'n'.

    Base case 2:
        If the digit sum exceeds the threshold, return the threshold.

    Recursive case:
        Sum the digits of 'n', and recursively call the function with this new sum.

    """
    if n < 10:  # Base case 1
        return n  # turn-around 1

    # Convert 'n' to a string, sum its digits.
    digit_sum = sum(int(digit) for digit in str(n))

    if digit_sum > threshold:  # Base case 2
        return threshold  # turn-around 2

    # Recursive case: Call the function again with the digit sum.
    return sum_digits_to_threshold(digit_sum, threshold)


# --- --- --- test cases --- --- ---

assert sum_digits_to_threshold(123, 7) == 6, "Test 1"
assert sum_digits_to_threshold(123, 5) == 5, "Test 2"
assert sum_digits_to_threshold(5, 3) == 5, "Test 3"
assert sum_digits_to_threshold(100, 99) == 1, "Test 4"
assert sum_digits_to_threshold(22, 10) == 4, "Test 5"
assert sum_digits_to_threshold(77, 10) == 10, "Test 6"
assert sum_digits_to_threshold(77, 77) == 5, "Test 7"
assert sum_digits_to_threshold(33, 33) == 6, "Test 8"
assert sum_digits_to_threshold(345, 33) == 3, "Test 9"
