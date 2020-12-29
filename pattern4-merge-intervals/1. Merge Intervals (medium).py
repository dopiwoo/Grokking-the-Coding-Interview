#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 01:13:21 2020

@author: dopiwoo

Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive
intervals.

Example 1:
Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into
one [1,5].

Example 2:
Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].

Example 3:
Intervals: [[1,4], [2,6], [3,5]]
Output: [[1,6]]
Explanation: Since all the given intervals overlap, we merged them into one.
"""

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Time complexity: O(N * log(N))
    Space complexity: O(N)

    Parameters
    ----------
    intervals : List[List[int]]
        input intervals

    Returns
    -------
    merged : List[List[int]]
        merged intervals

    """
    merged = []
    intervals.sort(key=lambda x: x[0])
    for i in range(len(intervals)):
        if not merged or intervals[i][0] > intervals[i - 1][1]:
            merged.append(intervals[i])
        else:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
    return merged


if __name__ == '__main__':
    print(merge([[1, 4], [2, 5], [7, 9]]))
    print(merge([[6, 7], [2, 4], [5, 9]]))
    print(merge([[1, 4], [2, 6], [3, 5]]))
