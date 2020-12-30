#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 09:43:53 2020

@author: dopiwoo

Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted
on their start time.

Example 1:
Input: arr1 = [[1, 3], [5, 6], [7, 9]], arr2 = [[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.

Example 2:
Input: arr1 = [[1, 3], [5, 7], [9, 12]], arr2 = [[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists.
"""

from typing import List


def merge(intervals_a: List[List[int]], intervals_b: List[List[int]]) -> List[List[int]]:
    """
    The algorithm will be to iterate through both the lists together to see if any two intervals overlap. If two
    intervals overlap, we will insert the overlapped part into a result list and move on to the next interval which is
    finishing early.

    Time Complexity: O(N)
    Space Complexity: O(1)

    Parameters
    ----------
    intervals_a : List[List[int]]
        input interval a
    intervals_b : List[List[int]]
        input interval b

    Returns
    -------
    result : List[List[int]]
        intersection of a and b

    """
    i, j = 0, 0
    result = []
    while i < len(intervals_a) and j < len(intervals_b):
        if not intervals_a[i][0] < intervals_b[j][1] or intervals_a[i][1] > intervals_b[j][0]:
            result.append([max(intervals_a[i][0], intervals_b[j][0]), min(intervals_a[i][1], intervals_b[j][1])])
        if intervals_a[i][1] < intervals_b[j][1]:
            i += 1
        else:
            j += 1
    return result


if __name__ == '__main__':
    print(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]]))
    print(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]]))
