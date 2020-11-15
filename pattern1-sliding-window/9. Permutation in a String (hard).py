# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 14:17:23 2020

@author: dopiwoo

Given a string and a pattern, find out if the string contains any permutation of the pattern.
Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six
permutations:
    1. abc
    2. acb
    3. bac
    4. bca
    5. cab
    6. cba
If a string has ‘n’ distinct characters, it will have n! permutations.

Example 1:
Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

Example 2:
Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

Example 3:
Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.

Example 4:
Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
"""


def find_permutation(str1: str, pattern: str) -> bool:
    """
    Create a HashMap to calculate the frequencies of all characters in the pattern.
    Iterate through the string, adding one character at a time in the sliding window.
    If the character being added matches a character in the HashMap, decrement its frequency in the map. If the
    character frequency becomes zero, we got a complete match.
    If at any time, the number of characters matched is equal to the number of distinct characters in the pattern (i.e.,
    total characters in the HashMap), we have gotten our required permutation.
    If the window size is greater than the length of the pattern, shrink the window to make it equal to the pattern’s
    size. At the same time, if the character going out was part of the pattern, put it back in the frequency HashMap.

    Time Complexity: O(N)
    Space Complexity: O(1)

    :param str1: input string
    :param pattern: input pattern
    :return: if the string contains any permutation of the pattern
    """
    matched = 0
    seen = {}
    window_start = 0
    for char in pattern:
        if char not in seen:
            seen[char] = 1
        else:
            seen[char] += 1
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in pattern:
            seen[right_char] -= 1
            if seen[right_char] == 0:
                matched += 1
        if matched == len(seen):
            return True
        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            if left_char in seen:
                if seen[left_char] == 0:
                    matched -= 1
                seen[left_char] += 1
            window_start += 1
    return False


if __name__ == '__main__':
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))
