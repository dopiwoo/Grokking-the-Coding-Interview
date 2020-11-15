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
    This problem follows the Sliding Window pattern, and we can use a similar dynamic sliding window strategy as
    discussed in No-repeat Substring. We can use a HashMap to count the frequency of each letter.
    We’ll iterate through the string to add one letter at a time in the window.
    We’ll also keep track of the count of the maximum repeating letter in any window (let’s call it
    maxRepeatLetterCount).
    So, at any time, we know that we can have a window which has one letter repeating maxRepeatLetterCount times; this
    means we should try to replace the remaining letters.
    If we have more than ‘k’ remaining letters, we should shrink the window as we are not allowed to replace more than
    ‘k’ letters.
    While shrinking the window, we don’t need to update maxRepeatLetterCount (which makes it global count; hence, it is
    the maximum count for ANY window). Why don’t we need to update this count when we shrink the window? The answer: In
    any window, since we have to replace all the remaining letters to get the longest substring having the same letter,
    we can’t get a better answer from any other window even though all occurrences of the letter with frequency
    maxRepeatLetterCount is not in the current window.

    Time Complexity: O(N)
    Space Complexity: O(1)

    :param str1: input string
    :param k: maximum number of replacement
    :return: the length of the longest substring having the same letters after replacement
    """
    max_repeat = 0
    max_length = 0
    seen = {}
    window_start = 0
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in seen:
            seen[right_char] = 1
        else:
            seen[right_char] += 1
        max_freq_count = max(max_repeat, seen[right_char])
        if window_end - window_start + 1 - max_freq_count > k:
            seen[str1[window_start]] -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


if __name__ == '__main__':
    print(length_of_longest_substring('aabccbb', 2))
    print(length_of_longest_substring('abbcb', 1))
    print(length_of_longest_substring('abccde', 1))
