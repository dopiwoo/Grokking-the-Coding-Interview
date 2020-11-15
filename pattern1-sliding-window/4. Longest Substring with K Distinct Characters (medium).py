# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 09:28:28 2020

@author: dopiwoo

Given a string, find the length of the longest substring in it with no more than K distinct characters.
"""


def longest_substring_with_k_distinct(str1: str, k: int) -> int:
    """
    First, we will insert characters from the beginning of the string until we have ‘K’ distinct characters in the
    HashMap.
    These characters will constitute our sliding window. We are asked to find the longest such window having no more
    than ‘K’ distinct characters. We will remember the length of this window as the longest window so far.
    After this, we will keep adding one character in the sliding window (i.e., slide the window ahead) in a stepwise
    fashion.
    In each step, we will try to shrink the window from the beginning if the count of distinct characters in the HashMap
    is larger than ‘K.’ We will shrink the window until we have no more than ‘K’ distinct characters in the HashMap.
    This is needed as we intend to find the longest window.
    While shrinking, we’ll decrement the character’s frequency going out of the window and remove it from the HashMap if
    its frequency becomes zero.
    At the end of each step, we’ll check if the current window length is the longest so far, and if so, remember its
    length.

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
