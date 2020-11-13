# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 10:59:12 2020

@author: dopiwoo

Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is
to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of
fruit.
You can start with any tree, but you can't skip a tree once you have started. You will pick one fruit from each tree
until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both the baskets.

Example 1:
Input: ['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C'].

Example 2:
Input: ['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 2 'B' in one basket and two 'C' in the other basket. This can be done if we start with the
second letter: ['B', 'C', 'B', 'B', 'C'].
"""

from typing import List


def fruits_into_baskets(fruits: List[str]) -> int:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)

    :param fruits:
    :return:
    """
    max_length = 0
    seen = {}
    window_end = 0
    window_start = 0
    for item in fruits:
        if item not in seen:
            seen[item] = 1
        else:
            seen[item] += 1
        while len(seen) > 2:
            left_char = fruits[window_start]
            seen[left_char] -= 1
            if seen[left_char] == 0:
                del seen[left_char]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
        window_end += 1
    return max_length


if __name__ == '__main__':
    print('Maximum number of fruits: ' + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print('Maximum number of fruits: ' + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))
