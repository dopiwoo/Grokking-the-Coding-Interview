# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:13:32 2020

@author: dopiwoo

Given a string and a list of words, find all the starting indices of substrings in the given string that are a
concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of
the same length.

Example 1:
Input: String="catfoxcat", words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".

Example 2:
Input: String="catcatfoxfox", words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox".
"""

from typing import List


def find_word_concatenation(str1: str, words: List[str]) -> List[int]:
    """
    Time Complexity: O(len(str1) + len(pattern))
    Space Complexity: O(len(pattern))

    :param str1: input string
    :param words: input words
    :return:
    """
    word_length = len(words[0])
    words_count = len(words)
    if words_count == 0 or word_length == 0:
        return []
    freq = {}
    result = []
    for word in words:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1
    for i in range(len(str1) - word_length * words_count + 1):
        seen = {}
        for j in range(0, words_count):
            next_word_index = i + j * word_length
            word = str1[next_word_index:next_word_index + word_length]
            if word not in freq:
                break
            if word not in seen:
                seen[word] = 1
            else:
                seen[word] += 1
            if seen[word] > freq.get(word, 0):
                break
            if j + 1 == words_count:
                result.append(i)
    return result


if __name__ == '__main__':
    print(find_word_concatenation('catfoxcat', ['cat', 'fox']))
    print(find_word_concatenation('catcatfoxfox', ['cat', 'fox']))
