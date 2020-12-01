#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 15:24:13 2020

@author: dopiwoo

Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array os objects,
hence, we can't count 0s, 1s and 2s to recreate the array.

Example 1:
Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]
"""

from typing import List


def dutch_flag_sort(arr: List[int]):
    i = 0
    low = 0
    high = len(arr) - 1
    while i <= high:
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            i += 1
            low += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[high] = arr[high], arr[i]
            high -= 1


if __name__ == '__main__':
    arr1 = [1, 0, 2, 1, 0]
    dutch_flag_sort(arr1)
    print(dutch_flag_sort(arr1))
    arr2 = [2, 2, 0, 1, 2, 0]
    dutch_flag_sort(arr2)
    print(dutch_flag_sort(arr2))
