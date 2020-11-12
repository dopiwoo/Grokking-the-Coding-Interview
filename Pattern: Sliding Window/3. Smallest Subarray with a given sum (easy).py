# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 19:09:28 2020

@author: dopiwoo

Given an array of positive numbers and a positive number ‘s’, find the length of the smallest contiguous subarray whose
sum is greater than or equal to ‘s’. Return 0 if no such subarray exists.
"""

from typing import List


def smallest_subarray_with_given_sum(s: int, arr: List[int]) -> int:
    """
    1. First, we will add-up elements from the beginning of the array until their sum becomes greater than or equal to
       ‘S’.
    2. These elements will constitute our sliding window. We are asked to find the smallest such window having a sum
       greater than or equal to ‘S.’ We will remember the length of this window as the smallest window so far.
    3. After this, we will keep adding one element in the sliding window (i.e., slide the window ahead) in a stepwise
       fashion.
    4. In each step, we will also try to shrink the window from the beginning. We will shrink the window until the
       window’s sum is smaller than ‘S’ again. This is needed as we intend to find the smallest window. This shrinking
       will also happen in multiple steps; in each step, we will do two things:
        Check if the current window length is the smallest so far, and if so, remember its length.
        Subtract the first element of the window from the running sum to shrink the sliding window.

    Time Complexity: O(N)
    Space Complexity: O(1)

    :param s: a positive number whose sum in the subarray is greater than or equal to
    :param arr: input array
    :return: the length of the smallest contiguous subarray
    """
    min_length = float('inf')
    window_start = 0
    window_sum = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    if min_length == float('inf'):
        return 0
    return min_length


if __name__ == '__main__':
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))
