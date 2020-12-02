#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 17:00:25 2020

@author: dopiwoo

Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the
target number.

Example 1:
Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.
"""

from typing import List


def search_quadruplets(arr: List[int], target: int) -> List[List[int]]:
    arr.sort()
    arr_len = len(arr)
    quadruplets = []
    for i in range(arr_len - 3):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        for j in range(i + 1, arr_len - 2):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            # search pairs
            left = j + 1
            right = arr_len - 1
            while left < right:
                quad_sum = arr[i] + arr[j] + arr[left] + arr[right]
                if quad_sum == target:
                    quadruplets.append([arr[i], arr[j], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left - 1]:
                        left += 1
                    while left < right and arr[right] == arr[right + 1]:
                        right -= 1
                elif quad_sum < target:
                    left += 1
                else:
                    right -= 1
    return quadruplets


if __name__ == '__main__':
    print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
