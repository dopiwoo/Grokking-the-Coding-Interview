#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 17:14:02 2021

@author: dopiwoo

We are given a list of jobs. Each job has a start time, an end time, and a CPU load when it is running. Our goal is to
find the maximum CPU load at any time if all the jobs are running on the same machine.

Example 1:
Jobs: [[1, 4, 3], [2, 5, 4], [7, 9, 6]]
Output: 7
Explanation: Since [1, 4, 3] and [2, 5, 4] overlap, their maximum CPU load (3 + 4 = 7) will be when both the jobs are
running at the same time i.e., during the time interval (2, 4).

Example 2:
Jobs: [[6, 7, 10], [2, 4, 11], [8, 12, 15]]
Output: 15
Explanation: None of the jobs overlap, therefore we will take the maximum load of any job which is 15.

Example 3:
Jobs: [[1, 4, 2], [2, 4, 1], [3, 6, 5]]
Output: 8
Explanation: Maximum CPU load will be 8 as all jobs overlap during the time interval [3, 4].
"""

from typing import List
import heapq


def find_max_cpu_load(jobs: List[List[int]]) -> int:
    jobs.sort(key=lambda x: x[0])
    min_heap = []
    heapq.heappush(min_heap, jobs[0][1])
    curr_cpu_load = jobs[0][2]
    max_cpu_load = jobs[0][2]
    for i in jobs[1:]:
        if min_heap[0] <= i[0]:
            heapq.heappop(min_heap)
            curr_cpu_load -= i[2]
        heapq.heappush(min_heap, i[1])
        curr_cpu_load += i[2]
        max_cpu_load = max(max_cpu_load, curr_cpu_load)
    return max_cpu_load


if __name__ == '__main__':
    print(find_max_cpu_load([[1, 4, 3], [2, 5, 4], [7, 9, 6]]))
    print(find_max_cpu_load([[6, 7, 10], [2, 4, 11], [8, 12, 15]]))
    print(find_max_cpu_load([[1, 4, 2], [2, 4, 1], [3, 6, 5]]))
