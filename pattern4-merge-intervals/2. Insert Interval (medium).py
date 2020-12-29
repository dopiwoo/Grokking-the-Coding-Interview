#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 01:29:50 2020

@author: dopiwoo

Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position
and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

Example 1:
Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

Example 2:
Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].

Example 3:
Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
"""

from typing import List


def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    """
    1. Skip all intervals which end before the start of the new interval, i.e., skip all intervals with the following
    condition: intervals[i][1] < new_interval[0].
    2. Let’s call the last interval ‘b’ that does not satisfy the above condition. If ‘b’ overlaps with the new interval
    (a) (i.e. b.start <= a.end), we need to merge them into a new interval ‘c’: new_interval[0] = min(new_interval[0],
    intervals[i][0]), new_interval[1] = max(new_interval[1], intervals[i][1]).
    3. We will repeat the above two steps to merge ‘c’ with the next overlapping interval.

    Time Complexity: O(N)
    Space Complexity: O(N)

    Parameters
    ----------
    intervals : List[List[int]]
        input intervals
    new_interval : List[int]
        input new interval

    Returns
    -------
    merged : List[List[int]]
        merged intervals

    """
    i = 0
    merged = []
    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        merged.append(intervals[i])
        i += 1
    while i < len(intervals) and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    merged.append(new_interval)
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1
    return merged


if __name__ == '__main__':
    print(insert([[1, 3], [5, 7], [8, 12]], [4, 6]))
    print(insert([[1, 3], [5, 7], [8, 12]], [4, 10]))
    print(insert([[2, 3], [5, 7]], [1, 4]))
