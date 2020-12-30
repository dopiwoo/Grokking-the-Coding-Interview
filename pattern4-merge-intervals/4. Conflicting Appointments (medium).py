#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 10:56:59 2020

@author: dopiwoo

Given an array of intervals representing 'N' appointments, find out if a person can attend all the appointments.

Example 1:
Appointments: [[1, 4], [2, 5], [7, 9]]
Output: False
Explanation: Since [1, 4] and [2, 5] overlap, a person cannot attend both of these appointments.

Example 2:
Appointments: [[6, 7], [2, 4], [8, 12]]
Output: True
Explanation: None of the appointments overlap, therefore a person can attend all of them.

Example 3:
Appointments: [[4, 5], [2, 3], [3, 6]]
Output: False
Explanation: Since [4, 5] and [3, 6] overlap, a person cannot attend both of these appointments.
"""

from typing import List


def can_attend_all_appointments(intervals: List[List[int]]) -> bool:
    """
    The problem follows the Merge Intervals pattern. We can sort all the intervals by start time and then check if any
    two intervals overlap. A person will not be able to attend all appointments if any two appointments overlap.

    Time Complexity: O(N * log(N))
    Space Complexity: O(N)

    Parameters
    ----------
    intervals : List[List[int]]
        input intervals

    Returns
    -------
    bool
        Whether a person can attend all the appointments.

    """
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True


if __name__ == '__main__':
    print(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]]))
    print(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]]))
    print(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]]))
