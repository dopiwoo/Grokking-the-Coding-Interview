#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 11:12:48 2021

@author: dopiwoo

For 'K' employees, we are given a list of intervals representing the working hours of each employee. Our goal is to find
out if there is a free interval that is common to all employees. You can assume that each list of employee working hours
is sorted on the start time.

Example 1:
Input: Employee working hours = [[[1, 3], [5, 6]], [[2, 3], [6, 8]]]
Output: [3, 5]
Explanation: Both the employees are free between [3, 5].

Example 2:
Input: Employee working hours = [[[1, 3], [9, 12]], [[2, 4], [6, 8]]]
Output: [4, 6], [8, 9]
Explanation: All employees are free between [4, 6] and [8, 9].

Example 3:
Input: Employee working hours = [[[1, 3], [2, 4]], [[3, 5], [7, 9]]]
Output: [5, 7]
Explanation: All employees are free between [5, 7].
"""

from typing import List
import heapq


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

    def __repr__(self):
        return 'Interval(' + str(self.start) + ', ' + str(self.end) + ')'


def find_employee_free_time(schedule: List[List[Interval]]) -> List[Interval]:
    """
    Time Complexity: O(N * log(N))
    Space Complexity: O(N)

    Parameters
    ----------
    schedule : List[List[Interval]]
        input list of intervals representing the working hours of each employee

    Returns
    -------
    ans : List[Interval]
        free interval that is common to all employees

    """
    ans = []
    pq = [(employee[0].start, i, 0) for i, employee in enumerate(schedule)]
    heapq.heapify(pq)
    anchor = min(interval.start for employee in schedule for interval in employee)
    while pq:
        t, employee_id, job_number = heapq.heappop(pq)
        if anchor < t:
            ans.append(Interval(anchor, t))
        anchor = max(anchor, schedule[employee_id][job_number].end)
        if job_number + 1 < len(schedule[employee_id]):
            heapq.heappush(pq, (schedule[employee_id][job_number + 1].start, employee_id, job_number + 1))
    return ans


if __name__ == '__main__':
    print(find_employee_free_time([[Interval(1, 3), Interval(5, 6)], [Interval(2, 3), Interval(6, 8)]]))
    print(find_employee_free_time([[Interval(1, 3), Interval(9, 12)], [Interval(2, 4), Interval(6, 8)]]))
    print(find_employee_free_time([[Interval(1, 3), Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]))
