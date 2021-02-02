#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 14:32:59 2021

@author: dopiwoo

Given an unsorted array containing numbers and a number 'k', find the first 'k' missing positive numbers in the array.

Example 1:
Input: [3, -1, 4, 5, 5], k = 3
Output: [1, 2, 6]
Explanation: The smallest missing positive numbers are 1, 2 and 6.

Example 2:
Input: [2, 3, 4], k = 3
Output: [1, 5, 6]
Explanation: The smallest missing positive numbers are 1, 5 and 6.

Example 3:
Input: [-2, -3, 4], k = 2
Output: [1, 2]
Explanation: The smallest missing positive numbers are 1 and 2.
"""

from typing import List


def find_first_k_missing_positive(nums: List[int], k: int) -> List[int]:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)

    Parameters
    ----------
    nums : List[int]
        Input unsorted array.
    k : int
        Input number 'k'.

    Returns
    -------
    List[int]
        The first 'k' missing positive numbers in the given array.

    """
    i = 0
    len_nums = len(nums)
    res = []
    seen = set()
    while i < len_nums:
        j = nums[i] - 1
        if 0 <= j < len_nums and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(len_nums):
        if len(res) < k and nums[i] != i + 1:
            res.append(i + 1)
            seen.add(nums[i])
    additional_num = len_nums + 1
    while len(res) < k:
        if additional_num not in seen:
            res.append(additional_num)
        additional_num += 1
    return res


if __name__ == '__main__':
    print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print(find_first_k_missing_positive([2, 3, 4], 3))
    print(find_first_k_missing_positive([-2, -3, 4], 2))
    print(find_first_k_missing_positive([2, 1, 3, 6, 5], 2))
