# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 18:04:48 2020

@author: dopiwoo

Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size
‘k’.
"""

from typing import List


def find_averages_of_subarray_brute_force(k: int, arr: List[int]) -> List[float]:
    """
    A brute-force algorithm will calculate the sum of every k-element contiguous subarray of the given array and divide
    the sum by ‘k’ to find the average.
    Since for every element of the input array, we are calculating the sum of its next ‘k’ elements, the time complexity
    of the algorithm will be O(k * len(arr))

    Parameters
    ----------
    k : int
        window size
    arr : List[int]
        input array

    Returns
    -------
    result : List[float]
        average k-element contiguous subarray

    """
    result = []
    for i in range(len(arr) - k + 1):
        _sum = 0.0
        for j in range(i, i + k):
            _sum += arr[j]
        result.append(_sum / k)
    return result


def find_averages_of_subarray_sliding_window(k: int, arr: List[int]) -> List[float]:
    """
    The efficient way to solve this problem would be to visualize each contiguous subarray as a sliding window of ‘k’
    elements. This means that we will slide the window by one element when we move on to the next subarray. To reuse the
    sum from the previous subarray, we will subtract the element going out of the window and add the element now being
    included in the sliding window. This will save us from going through the whole subarray to find the sum and, as a
    result, the algorithm complexity will reduce to O(len(arr)).

    Parameters
    ----------
    k : int
        window size
    arr : List[int]
        input array

    Returns
    -------
    result : List[float]
        average k-element contiguous subarray

    """
    result = []
    window_start = 0
    window_sum = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k - 1:
            result.append(window_sum / k)
            window_sum -= arr[window_start]
            window_start += 1
    return result


if __name__ == '__main__':
    result_brute_force = find_averages_of_subarray_brute_force(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarray of size K (brute force): " + str(result_brute_force))
    result_sliding_window = find_averages_of_subarray_sliding_window(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarray of size K (sliding window): " + str(result_sliding_window))
