# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 14:45:54 2020

@author: dopiwoo

Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the
duplicates in-place return the length of the subarray that has no duplicate in it.

Example 1:
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
"""

from typing import List


def remove_duplicates(arr: List[int]) -> int:
    """
    Time Complexity: O(len(arr))
    Space Complexity: O(1)

    :param arr: input array
    :return: the length of the subarray that has no duplicate in it
    """
    p1 = 1
    p2 = 1
    while p2 < len(arr):
        if arr[p1 - 1] != arr[p2]:
            arr[p1] = arr[p2]
            p1 += 1
        p2 += 1
    return p1


if __name__ == '__main__':
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))
