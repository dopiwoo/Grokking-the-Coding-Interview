#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 11:06:48 2020

@author: dopiwoo

Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

Example 1:
Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted.

Example 2:
Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted.
"""

from typing import List


def shortest_window_sort(arr: List[int]) -> int:
    arr_len = len(arr)
    low = 0
    high = arr_len - 1
    while low < arr_len - 1 and arr[low] <= arr[low + 1]:
        low += 1
    if low == arr_len - 1:
        return 0
    while high > 0 and arr[high] >= arr[high - 1]:
        high -= 1
    subarray = arr[low:high + 1]
    subarray_min = min(subarray)
    subarray_max = max(subarray)
    while low > 0 and arr[low - 1] > subarray_min:
        low -= 1
    while high < arr_len - 1 and arr[high + 1] < subarray_max:
        high += 1
    return high - low + 1


if __name__ == '__main__':
    print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
    print(shortest_window_sort([1, 2, 3]))
    print(shortest_window_sort([3, 2, 1]))
