# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:23:43 2020

@author: dopiwoo

Given an unsorted array of numbers and a target 'key', remove all instances of 'key' in-place and return the new length
of the array.
"""

from typing import List


def remove_element(arr: List[int], key: int) -> int:
    """
    Time Complexity: O(len(arr))
    Space Complexity: O(1)

    :param arr: input array
    :param key: target key
    :return: the new length of the array after removing all instances of 'key' in-place
    """
    p1 = 0
    for p2 in range(len(arr)):
        if arr[p2] != key:
            arr[p1] = arr[p2]
            p1 += 1
    return p1


if __name__ == '__main__':
    print(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3))
    print(remove_element([2, 11, 2, 2, 1], 2))
