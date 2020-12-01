#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 09:45:38 2020

@author: dopiwoo

Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:
Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
"""

from typing import List


def search_triplets(arr: List[int]) -> List[List[int]]:
    def search_pair(arr, target_sum, left, triplets):
        right = len(arr) - 1
        while left < right:
            curr_sum = arr[left] + arr[right]
            if curr_sum > target_sum:
                right -= 1
            elif curr_sum < target_sum:
                left += 1
            else:
                triplets.append([-target_sum, arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
        return triplets

    arr.sort()
    triplets = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        search_pair(arr, -arr[i], i + 1, triplets)
    return triplets


if __name__ == '__main__':
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))
