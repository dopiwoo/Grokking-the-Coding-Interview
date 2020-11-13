# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 11:44:55 2020

@author: dopiwoo

Given a string, find the length of the longest substring, which has no repeating characters.

Example 1:
Input: 'aabccbb'
Output: 3
Explanation: The longest substring without any repeating characters is 'abc'.

Example 2:
Input: 'abbbb'
Explanation: The longest substring without any repeating characters is 'ab'.
"""


def non_repeating_substring(str1: str) -> int:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)

    :param str1: input string
    :return: the length of the longest substring without any repeating character
    """
    max_length = 0
    seen = {}
    window_start = 0
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in seen:
            window_start = max(window_start, seen[right_char] + 1)
        seen[right_char] = window_end
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


if __name__ == '__main__':
    print('Length of the longest substring: ' + str(non_repeating_substring('aabccbb')))
    print('Length of the longest substring: ' + str(non_repeating_substring('abbbb')))
    print('Length of the longest substring: ' + str(non_repeating_substring('abccde')))
