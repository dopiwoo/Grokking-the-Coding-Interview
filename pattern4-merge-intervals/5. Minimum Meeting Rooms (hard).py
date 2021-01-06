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
import heapq


def min_meeting_rooms(meetings: List[List[int]]) -> int:
    """
    Time Complexity: O(N * log(N))
    Space Complexity: O(N)

    Parameters
    ----------
    meetings : List[List[int]]
        input meetings

    Returns
    -------
    int
        the minimum number of rooms required to hold all the meetings

    """
    free_rooms = []
    meetings.sort(key=lambda x: x[0])
    heapq.heappush(free_rooms, meetings[0][1])
    for i in meetings[1:]:
        if free_rooms[0] <= i[0]:
            heapq.heappop(free_rooms)
        heapq.heappush(free_rooms, i[1])
    return len(free_rooms)


if __name__ == '__main__':
    print(min_meeting_rooms([[1, 4], [2, 5], [7, 9]]))
    print(min_meeting_rooms([[6, 7], [2, 4], [8, 12]]))
    print(min_meeting_rooms([[1, 4], [2, 3], [3, 6]]))
    print(min_meeting_rooms([[4, 5], [2, 3], [2, 4], [3, 5]]))
