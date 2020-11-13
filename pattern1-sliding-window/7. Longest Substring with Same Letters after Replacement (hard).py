# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:07:27 2020

@author: dopiwoo

Given a string with lowercase letters only, if you are allowed to replace no more than 'k' letters with any letter, find
the length of the longest substring having the same letters after replacement.

Example 1:
Input: 'aabccbb', k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring 'bbbbb'.

Example 2:
Input: 'abbcb', k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring 'bbbb'.
"""


def length_of_longest_substring(str1: str, k: int) -> int:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)

    :param str1: input string
    :param k:
    :return:
    """
    max_freq_count = 0
    max_length = 0
    seen = {}
    window_start = 0
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in seen:
            seen[right_char] = 1
        else:
            seen[right_char] += 1
        max_freq_count = max(max_freq_count, seen[right_char])
        if window_end - window_start + 1 - max_freq_count > k:
            left_char = str1[window_start]
            seen[left_char] -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


if __name__ == '__main__':
    print(length_of_longest_substring('aabccbb', 2))
    print(length_of_longest_substring('abbcb', 1))
    print(length_of_longest_substring('abccde', 1))
