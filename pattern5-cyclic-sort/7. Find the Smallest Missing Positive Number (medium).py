#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 16:38:00 2021

@author: dopiwoo

Given an unsorted array containing numbers, find the smallest missing positive number in it.

Example 1:
Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'.

Example 2:
Input: [3, -2, 0, 1, 2]
Output: 4

Example 3:
Input: [3, 2, 5, 1]
Output: 4
"""

from typing import List


def find_first_smallest_missing_positive(nums: List[int]) -> int:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)

    Parameters
    ----------
    nums : List[int]
        Input unsorted array.

    Returns
    -------
    int
        The smallest missing positive number in the given array.

    """
    i = 0
    len_nums = len(nums)
    while i < len_nums:
        j = nums[i] - 1
        if 0 < nums[i] <= len_nums and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(len_nums):
        if nums[i] != i + 1:
            return i + 1


if __name__ == '__main__':
    print(find_first_smallest_missing_positive([-3, 1, 5, 4, 2]))
    print(find_first_smallest_missing_positive([3, -2, 0, 1, 2]))
    print(find_first_smallest_missing_positive([3, 2, 5, 1]))
