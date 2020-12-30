#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 11:13:05 2020

@author: dopiwoo

Given a list of intervals representing the start and end of 'N' meetings, find the minimum number of rooms required to
hold all the meetings.

Example 1:
Meetings: [[1, 4], [2, 5], [7, 9]]
Output: 2
Explanation: Since [1, 4] and [2, 5] overlap, we need two rooms to hold these two meetings, [7, 9] can occur in any of
the two rooms later.

Example 2:
Meetings: [[6, 7], [2, 4], [8, 12]]
Output: 1
Explanation: None of the meetings overlap, therefore we only need one room to hold all meetings.

Example 3:
Meetings: [[1, 4], [2, 3], [3, 6]]
Output: 2
Explanation: Since [1, 4] overlaps with the other two meetings [2, 3] and [3, 6], we need two rooms to hold these all
the meetings.

Example 4:
Meetings: [[4, 5], [2, 3], [2, 4], [3, 5]]
Output: 2
Explanation: We will need one room for [2, 3] and [3, 5], and another room for [2, 4] and [4, 5].
"""

from typing import List


def min_meeting_rooms(meetings: List[List[int]]):
    meetings.sort(key=lambda x: x[0])
    min_rooms = 0
    min_heap = []
    for i in range(len(meetings)):
        pass


if __name__ == '__main__':
    print(min_meeting_rooms([[1, 4], [2, 5], [7, 9]]))
    print(min_meeting_rooms([[6, 7], [2, 4], [8, 12]]))
    print(min_meeting_rooms([[1, 4], [2, 3], [3, 6]]))
    print(min_meeting_rooms([[4, 5], [2, 3], [2, 4], [3, 5]]))
