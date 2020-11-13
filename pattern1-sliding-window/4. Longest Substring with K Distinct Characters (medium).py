# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 09:28:28 2020

@author: dopiwoo

Given a string, find the length of the longest substring in it with no more than K distinct characters.
"""


def longest_substring_with_k_distinct(str1: str, k: int) -> int:
    """
    Time Complexity: O(N)
    Space Complexity: O(k)

    :param str1: input string
    :param k: no more than K distinct characters
    :return: the length of the longest substring
    """
    max_length = 0
    seen = {}
    window_start = 0
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in seen:
            seen[right_char] = 1
        else:
            seen[str1[window_end]] += 1
        while len(seen) > k:
            left_char = str1[window_start]
            seen[left_char] -= 1
            if seen[left_char] == 0:
                del seen[left_char]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


if __name__ == '__main__':
    print('Length of the longest substring: ' + str(longest_substring_with_k_distinct('araaci', 2)))
    print('Length of the longest substring: ' + str(longest_substring_with_k_distinct('araaci', 1)))
    print('Length of the longest substring: ' + str(longest_substring_with_k_distinct('cbbebi', 3)))
