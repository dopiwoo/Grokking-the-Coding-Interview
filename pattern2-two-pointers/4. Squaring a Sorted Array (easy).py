# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 16:21:26 2020

@author: dopiwoo

Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

Example 1:
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
"""

from typing import List


def make_squares(arr: List[int]) -> List[int]:
    """
    Time Complexity: O(len(arr))
    Space Complexity: O(len(arr))

    :param arr: input array
    :return: new array containing squares of all the number of the input array in the sorted order
    """
    n = len(arr)
    p1 = 0
    p2 = n - 1
    idx = p2
    squares = [0] * n
    while p1 < p2:
        left_square = arr[p1] * arr[p1]
        right_square = arr[p2] * arr[p2]
        if left_square < right_square:
            squares[idx] = right_square
            p2 -= 1
        else:
            squares[idx] = left_square
            p1 += 1
        idx -= 1
    return squares


if __name__ == '__main__':
    print(make_squares([-2, -1, 0, 2, 3]))
    print(make_squares([-3, -1, 0, 1, 2]))
