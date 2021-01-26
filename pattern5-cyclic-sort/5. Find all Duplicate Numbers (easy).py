#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 11:07:51 2021

@author: dopiwoo

We are given an unsorted array containing 'n' numbers taken from the range 1 to 'n'. The array has come numbers
appearing twice. Find all these duplicate numbers without using any extra space.

Example 1:
Input: [3, 4, 4, 5, 5]
Output: [4, 5]

Example 2:
Input: [5, 4, 7, 2, 3, 5, 3]
Output: [3, 5]
"""

from typing import List


def find_all_duplicates(nums: List[int]) -> List[int]:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)

    Parameters
    ----------
    nums : List[int]
        Input unsorted array.

    Returns
    -------
    res : List[int]
        All duplicate numbers in the given array.

    """
    i = 0
    res = []
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(len(nums)):
        if nums[i] != i + 1:
            res.append(nums[i])
    return res


if __name__ == '__main__':
    print(find_all_duplicates([3, 4, 4, 5, 5]))
    print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))
