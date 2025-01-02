#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from ..check_palindrome import check_palindrome


class TestCheckPalindrome(unittest.TestCase):
    """Test palindrome function"""

    def test_empty_string(self):
        self.assertTrue(check_palindrome(""), True)

    def test_single_character(self):
        self.assertTrue(check_palindrome("a"), True)

    def test_palindrome_even_length(self):
        self.assertTrue(check_palindrome("abba"), True)

    def test_palindrome_odd_length(self):
        self.assertTrue(check_palindrome("madam"), True)

    def test_not_a_palindrome(self):
        self.assertFalse(check_palindrome("hello"), False)
