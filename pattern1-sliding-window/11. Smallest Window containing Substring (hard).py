# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 22:09:08 2020

@author: dopiwoo

Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given
pattern.

Example 1:
Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec".

Example 2:
Input: String="abdbca", Pattern="abc"
Output: "bca"
Explanation: The smallest substring having all characters of the pattern is "bca".

Example 3:
Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.
"""


def find_substring(str1: str, pattern: str) -> str:
    """
    Time Complexity: O(N)
    Space Complexity: O(N)

    Parameters
    ----------
    str1 : str
        input string
    pattern : str
        input pattern

    Returns
    -------
    str
        the smallest substring in the given string which has all the characters of the given pattern

    """
    matched = 0
    min_length = len(str1) + 1
    seen = {}
    window_start = 0
    for char in pattern:
        seen[char] = 1
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in seen:
            seen[right_char] -= 1
            if seen[right_char] >= 0:
                matched += 1
        while matched == len(pattern):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substr_start = window_start
            left_char = str1[window_start]
            window_start += 1
            if left_char in seen:
                if seen[left_char] == 0:
                    matched -= 1
                seen[left_char] += 1
    if min_length > len(str1):
        return ''
    return str1[substr_start:substr_start + min_length]


if __name__ == '__main__':
    print(find_substring("aabdec", "abc"))
    print(find_substring("abdbca", "abc"))
    print(find_substring("adcad", "abc"))
