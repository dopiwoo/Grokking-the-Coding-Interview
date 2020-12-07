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
    b1_cnt = 0
    b2_cnt = 0
    p1 = len(str1) - 1
    p2 = len(str2) - 1
    while p1 >= 0 or p2 >= 0:
        while p1 >= 0 and (str1[p1] == '#' or b1_cnt > 0):
            if str1[p1] == '#':
                b1_cnt += 1
            else:
                b1_cnt -= 1
            p1 -= 1
        while p2 >= 0 and (str2[p2] == '#' or b2_cnt > 0):
            if str2[p2] == '#':
                b2_cnt += 1
            else:
                b2_cnt -= 1
            p2 -= 1
        if p1 < 0 or p2 < 0:
            return p1 == p2
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
    print(backspace_compare('ab##', 'c#d#'))
    print(backspace_compare('bxj##tw', 'bxo#j##tw'))
    print(backspace_compare('aaa###a', 'aaaa###a'))
