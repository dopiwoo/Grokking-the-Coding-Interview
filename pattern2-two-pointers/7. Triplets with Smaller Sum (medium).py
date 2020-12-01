#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 17:20:06 2020

@author: dopiwoo

Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] <
target where i, j, and k are three different indices. Write a function to return the count of such triplets.

Example 1:
Input: [-1, 0, 2, 3], target=3
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
"""

from typing import List


def triplet_with_smaller_sum(arr: List[int], target: int) -> int:
    arr.sort()
    arr_len = len(arr)
    count = 0
    for i in range(arr_len - 2):
        left = i + 1
        right = arr_len - 1
        while left < right:
            if arr[i] + arr[left] + arr[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1
    return count


if __name__ == '__main__':
    print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
    print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))
