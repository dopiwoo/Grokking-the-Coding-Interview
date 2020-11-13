# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 18:04:48 2020

@author: dopiwoo

Given an array of positive numbers and a positive number ‘k’ find the maximum sum of any contiguous subarray of size
‘k’.
"""

from typing import List, Union


def max_sub_array_of_size_k(k: int, arr: List[Union[float, int]]) -> List[Union[float, int]]:
    """
    Sliding window approach:
    1. Subtract the element going out of the sliding window.
    2. Add the new element getting included in the sliding window.
    Time Complexity: O(N)
    Space Complexity: O(1)

    :param k: window size
    :param arr: input array
    :return: maximum sum of any contiguous subarray of size ‘k’
    """
    max_sum = 0
    window_start = 0
    window_sum = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum


if __name__ == '__main__':
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))
