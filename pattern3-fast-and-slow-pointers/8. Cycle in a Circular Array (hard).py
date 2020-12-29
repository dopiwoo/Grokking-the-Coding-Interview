#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 16:58:15 2020

@author: dopiwoo

We are given an array containing positive and negative numbers. Suppose the array contains a number 'M' at a particular
index. Now, if 'M' is positive we will move forward 'M' indices and if 'M' is negative move backwards 'M' indices. You
should assume that the array is circular which means two things:

    1. If, while moving forward, we reach the end of the array, we will jump to the first element to continue the
       movement.
    2. If, while moving backward, we reach the beginning of the array, we will jump to the last element to continue the
       movement.

Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one
direction which means the cycle should not contain both forward and backward movements.

Example 1:
Input: [1, 2, -1, 2, 2]
Output: true
Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0

Example 2:
Input: [2, 2, -1, 2]
Output: true
Explanation: The array has a cycle among indices: 1 -> 3 -> 1

Example 3:
Input: [2, 1, -1, -2]
Output: false
Explanation: The array does not have any cycle.
"""

from typing import List


def circular_array_loop_exists(arr: List[int]) -> bool:
    """
    This problem involves finding a cycle in the array and, as we know, the Fast & Slow pointer method is an efficient
    way to do that. We can start from each index of the array to find the cycle. If a number does not have a cycle we
    will move forward to the next element. There are a couple of additional things we need to take care of:

    1. As mentioned in the problem, the cycle should have more than one element. This means that when we move a pointer
    forward, if the pointer points to the same element after the move, we have a one-element cycle. Therefore, we can
    finish our cycle search for the current element.
    2. The other requirement mentioned in the problem is that the cycle should not contain both forward and backward
    movements. We will handle this by remembering the direction of each element while searching for the cycle. If the
    number is positive, the direction will be forward and if the number is negative, the direction will be backward. So
    whenever we move a pointer forward, if there is a change in the direction, we will finish our cycle search right
    there for the current element.

    Time Complexity: O(N^2)
    Space Complexity: O(1)

    Parameters
    ----------
    arr : List[int]
        input array

    Returns
    -------
    bool
        whether the array have a cycle

    """
    def find_next_index(array: List[int], forward: bool, curr_idx: int):
        direction = array[curr_idx] >= 0
        if direction != forward:
            return -1
        next_idx = (curr_idx + array[curr_idx]) % len(array)
        if curr_idx == next_idx:
            return -1
        return next_idx

    for i in range(len(arr)):
        is_forward = arr[i] >= 0
        fast, slow = i, i
        while True:
            fast = find_next_index(arr, is_forward, fast)
            slow = find_next_index(arr, is_forward, slow)
            if fast != -1:
                fast = find_next_index(arr, is_forward, fast)
            if slow == -1 or fast == -1 or slow == fast:
                break
        if slow != -1 and slow == fast:
            return True
    return False


if __name__ == '__main__':
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))
