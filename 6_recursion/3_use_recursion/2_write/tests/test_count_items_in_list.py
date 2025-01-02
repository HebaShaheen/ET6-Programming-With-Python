#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from ..count_items_in_list import count_items_in_list

"""Test the count_items_in_list function """


class TestCountItemsInList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_items_in_list([]), 0)

    def test_single_element_list(self):
        self.assertEqual(count_items_in_list([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(count_items_in_list([1, 2, 3]), 3)
