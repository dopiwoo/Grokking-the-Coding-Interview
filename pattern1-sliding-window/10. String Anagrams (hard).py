# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 10:51:29 2020

@author: dopiwoo

Given a string and a pattern, find all anagrams of the pattern in the given string.
Anagram is actually a Permutation of a string. For example, "abc" had the following six anagrams:
    1. abc
    2. acb
    3. bac
    4. bca
    5. cab
    6. cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:
Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

Example 2:
Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
"""

from typing import List


def find_string_anagrams(str1: str, pattern: str) -> List[int]:
    """
    This problem follows the Sliding Window pattern and is very similar to Permutation in a String. In this problem, we
    need to find every occurrence of any permutation of the pattern in the string. We will use a list to store the
    starting indices of the anagrams of the pattern in the string.

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
    result : List[int]
        the list of starting indices of the anagrams of the pattern in the given string

    """
    matched = 0
    result = []
    seen = {}
    window_start = 0
    for char in pattern:
        if char not in seen:
            seen[char] = 1
        else:
            seen[char] += 1
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in seen:
            seen[right_char] -= 1
            if seen[right_char] == 0:
                matched += 1
        if matched == len(seen):
            result.append(window_start)
        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            if left_char in seen:
                if seen[left_char] == 0:
                    matched -= 1
                seen[left_char] += 1
            window_start += 1
    return result


if __name__ == '__main__':
    print(find_string_anagrams('ppqp', 'pq'))
    print(find_string_anagrams('abbcabc', 'abc'))
