#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 09:51:54 2020

@author: dopiwoo

Given an array with positive numbers and a target number, find all of its contiguous subarray whose product is less than
the target number.

Example 1:
Input: [2, 5, 3, 10], target=30
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarray whose product is less than the target.
"""

from typing import List


def find_subarray(arr: List[int], target: int) -> List[List[int]]:
    arr_len = len(arr)
    left = 0
    product = 1
    result = []
    for right in range(arr_len):
        product *= arr[right]
        while product >= target and left < arr_len:
            product /= arr[left]
            left += 1
        temp_list = []
        for i in range(right, left - 1, -1):
            temp_list.insert(0, arr[i])
            result.append(temp_list.copy())
    return result


if __name__ == '__main__':
    print(find_subarray([2, 5, 3, 10], 30))
    print(find_subarray([8, 2, 6, 5], 50))
