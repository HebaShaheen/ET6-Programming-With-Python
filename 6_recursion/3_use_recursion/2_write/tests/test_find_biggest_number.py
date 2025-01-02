#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from ..find_biggest_number import find_biggest_number


class TestFindBiggestNumber(unittest.TestCase):
    """Test the biggest number fumction"""

    def test_single_element_list(self):
        self.assertEqual(find_biggest_number([42]), 42)

    def test_sorted_list(self):
        self.assertEqual(find_biggest_number([5, 1, 2, 3, 4]), 5)

    def test_unsorted_list(self):
        self.assertEqual(find_biggest_number([3, 1, 4, 9, 1, 5]), 9)

    def test_empty(self):
        """It should raise ValueError if the list empty"""
        with self.assertRaises(ValueError):
            find_biggest_number([])

    def test_invalid(self):
        """It should raise AssertionError"""
        with self.assertRaises(AssertionError):
            find_biggest_number("1 2 3")
