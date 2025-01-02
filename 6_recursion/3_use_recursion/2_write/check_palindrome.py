#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def check_palindrome(word: str) -> bool:
    """A function checks if the word is palindrome returns yes if not returns no
    palindrome means the reverse and orginal word the same.

    Args:
        word (str): the word to check it is palindrome or not

    Returns:
        bool: return True if it is palindrome and False if not
    """
    # reverse = "".join(reversed(word))  # Convert the reversed iterator to a string

    # if word == reverse:
    #    return True
    # else:
    #    return False
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return check_palindrome(word[1:-1])


print(check_palindrome(""))  # Output: True
print(check_palindrome("r"))  # Output: True
print(check_palindrome("hello"))  # Output: False
