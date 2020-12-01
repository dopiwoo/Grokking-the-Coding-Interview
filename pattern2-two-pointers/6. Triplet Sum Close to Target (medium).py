#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:31:29 2020

@author: dopiwoo

Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target
number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the
triplet with the smallest sum.

Example 1:
Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
"""

from typing import List


def triplet_sum_close_to_target(arr: List[int], target_sum: int) -> int:
    arr.sort()
    min_diff = float('inf')
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            diff = target_sum - arr[i] - arr[left] - arr[right]
            if diff == 0:
                return target_sum - diff
            if abs(diff) < abs(min_diff) or (abs(diff) == abs(min_diff) and diff > min_diff):
                min_diff = diff
            if diff > 0:
                left += 1
            else:
                right -= 1
    return target_sum - min_diff


if __name__ == '__main__':
    print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
    print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
    print(triplet_sum_close_to_target([1, 0, 1, 1], 100))
    print(triplet_sum_close_to_target([-1, 2, 1, -4], 1))
