#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 10:45:27 2021

@author: dopiwoo

We are given an array containing 'n' distinct numbers taken from the range 0 to 'n'. Since the array has only 'n'
numbers out of the total 'n+1' numbers, find the missing number.

Example 1:
Input: [4, 0, 3, 1]
Output: 2

Example 2:
Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7
"""

from typing import List


def find_missing_number(nums: List[int]) -> int:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)

    A better solution: Gauss' Formula

    Parameters
    ----------
    nums : List[int]
        Input array containing 'n' distinct numbers taken from the range 0 to 'n'.

    Returns
    -------
    int
        The missing number in the given array.

    """
    i = 0
    len_nums = len(nums)
    while i < len_nums:
        j = nums[i]
        if j < len_nums and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(len_nums):
        if nums[i] != i:
            return i
    return len_nums


if __name__ == '__main__':
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))
    print(find_missing_number([0, 1]))
