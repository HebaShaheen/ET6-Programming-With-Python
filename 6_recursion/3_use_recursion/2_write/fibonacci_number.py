#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fibonacci_number(n: int) -> int:
    """
    Calculates the n'th number in the Fibonacci Sequence.

    base case 1:  n <= 0      -> 0

    base case 2:  n == 1      -> 1

    base case 3:  n in memo  -> memo[n]   if the argument in memo -> return the value stored in that key

    recursive case: n > 1    -> ƒ(n - 1) + ƒ(n - 2)

    >>> fibonacci_number(1)
    1

    >>> fibonacci_number(5)
    5

    >>> fibonacci_number(8)
    21

    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_number(n - 1) + fibonacci_number(n - 2)
