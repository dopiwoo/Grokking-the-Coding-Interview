# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:48:11 2020

@author: dopiwoo

Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
"""

from typing import List


def pair_with_target_sum_pointer(arr: List[int], target: int) -> List[int]:
    """
    Time Complexity: O(len(arr))
    Space Complexity: O(1)

    :param arr: input array
    :param target: input target
    :return: indices of the two numbers that add up to target
    """
    left = 0
    right = len(arr) - 1
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum < target:
            left += 1
        elif curr_sum > target:
            right -= 1
        else:
            return [left, right]
    return [-1, -1]


def pair_with_target_sum_hashmap(arr: List[int], target: int) -> List[int]:
    """
    Time Complexity: O(len(arr))
    Space Complexity: O(len(arr))

    :param arr: input array
    :param target: input target
    :return: indices of the two numbers that add up to target
    """
    seen = {}
    for i, n in enumerate(arr):
        if n in seen:
            return [seen[n], i]
        seen[target - n] = i
    return [-1, -1]


if __name__ == '__main__':
    print(pair_with_target_sum_pointer([1, 2, 3, 4, 6], 6))
    print(pair_with_target_sum_pointer([2, 5, 9, 11], 11))
    print(pair_with_target_sum_hashmap([1, 2, 3, 4, 6], 6))
    print(pair_with_target_sum_hashmap([2, 5, 9, 11], 11))
