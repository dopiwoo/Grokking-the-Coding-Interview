#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 17:50:35 2021

@author: dopiwoo

We are given an unsorted array containing 'n+1' numbers taken from the range 1 to 'n'. The array has only one duplicate
but it can be repeated multiple times. Find that duplicate number without using any extra space. You are, however,
allowed to modify the input array,

Example 1:
Input: [1, 4, 4, 3, 2]
Output: 4

Example 2:
Input: [2, 1, 3, 3, 5, 4]
Output: 3

Example 3:
Input: [2, 4, 1, 4, 4]
Output: 4
"""

from typing import List


def find_duplicate(nums: List[int]) -> int:
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
        The duplicate number in the given array.

    """
    i = 0
    while i < len(nums):
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                return nums[i]
        else:
            i += 1


def find_duplicate_pointers(arr: List[int]) -> int:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)

    Parameters
    ----------
    arr : List[int]
        Input unsorted array.

    Returns
    -------
    ptr1 ： int
        The duplicate number in the given array.

    """
    fast, slow = arr[arr[0]], arr[0]
    while fast != slow:
        fast = arr[arr[fast]]
        slow = arr[slow]
    curr = arr[arr[slow]]
    cycle_length = 1
    while curr != arr[slow]:
        curr = arr[curr]
        cycle_length += 1
    ptr1, ptr2 = arr[0], arr[0]
    while cycle_length > 0:
        ptr2 = arr[ptr2]
        cycle_length -= 1
    while ptr1 != ptr2:
        ptr1 = arr[ptr1]
        ptr2 = arr[ptr2]
    return ptr1


if __name__ == '__main__':
    print(find_duplicate_pointers([1, 4, 4, 3, 2]))
    print(find_duplicate_pointers([2, 1, 3, 3, 5, 4]))
    print(find_duplicate_pointers([2, 4, 1, 4, 4]))
