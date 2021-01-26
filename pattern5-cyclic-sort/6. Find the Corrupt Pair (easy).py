#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:19:21 2021

@author: dopiwoo

We are given an unsorted array containing 'n' numbers taken from the range 1 to 'n'. The array originally contained all
the numbers from 1 to 'n', but due to a data error, one of the numbers got duplicated which also resulted in one number
going missing. Find both these numbers.

Example 1:
Input: [3, 1, 2, 5, 2]
Output: [2, 4]
Explanation: '2' is duplicated and '4' is missing.

Example 2:
Input: [3, 1, 2, 3, 6, 4]
Output: [3, 5]
Explanation: '3' is duplicated and '5' is missing.
"""

from typing import List


def find_corrupt_numbers(nums: List[int]) -> List[int]:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)

    Parameters
    ----------
    nums : List[int]
        Input unsorted array.

    Returns
    -------
    List[int]
        The corrupt pair in the given array.

    """
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return [nums[i], i + 1]


if __name__ == '__main__':
    print(find_corrupt_numbers([3, 1, 2, 5, 2]))
    print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))
