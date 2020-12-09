#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 09:48:11 2020

@author: dopiwoo

Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square
of all of its digits, leads us to number '1'. All other numbers will never reach '1'. Instead, they will be stuck in a
cycle of numbers which does not include'1'.
"""


def find_happy_number(num: int) -> bool:
    """
    Time complexity: O(logN)
    Space complexity: O(1)

    Parameters
    ----------
    num : int
        input number

    Returns
    -------
    bool
        whether the input is a happy number

    """
    def get_next(number: int) -> int:
        """
        Calculate the sum of the square of all of the digits in 'number'.

        Time complexity: O(243 * 3 + logN + loglogN + ...) = O(logN)
        Space complexity: O(1)

        Parameters
        ----------
        number : int
            input number

        Returns
        -------
        total_sum : int
            the sum of the square of all of the digits in 'number'.

        """
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit * digit
        return total_sum
    fast = get_next(num)
    slow = num
    while slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
        if fast == 1:
            return False
    return True


if __name__ == '__main__':
    print(find_happy_number(23))
    print(find_happy_number(12))
