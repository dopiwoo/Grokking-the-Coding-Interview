#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 17:47:11 2020

@author: dopiwoo

Given two strings containing backspaces (identified by the character '#'), check if the two strings are equal.

Example 1:
Input: str1="xy#z", str2="xzz#"
Output: True
Explanation: After applying backspaces the string become "xz" and "xz" respectively.
"""


def backspace_compare(str1: str, str2: str) -> bool:
    b1_count = 0
    b2_count = 0
    p1 = len(str1) - 1
    p2 = len(str2) - 1
    while p1 >= 0 or p2 >= 0:
        while str1[p1] == '#':
            b1_count += 1
            p1 -= 1
        p1 -= b1_count
        b1_count = 0
        while str2[p2] == '#':
            b2_count += 1
            p2 -= 1
        p2 -= b2_count
        b2_count = 0
        if str1[p1] == str2[p2]:
            p1 -= 1
            p2 -= 1
        else:
            return False
    return True


if __name__ == '__main__':
    print(backspace_compare('xy#z', 'xzz#'))
    print(backspace_compare('xy#z', 'xyz#'))
    print(backspace_compare('xp#', 'xyz##'))
    print(backspace_compare('xywrrmp', 'xywrrmu#p'))
