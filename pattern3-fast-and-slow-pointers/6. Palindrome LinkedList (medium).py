#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 15:58:01 2020

@author: dopiwoo

Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.
Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is
finished. The algorithm should have O(N) time complexity where 'N' is the number of nodes in the LinkedList.

Example 1:
Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: True

Example 2:
Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
Output: False
"""


class Node:
    def __init__(self, value: int, next_node: 'Node' = None):
        self.value = value
        self.next = next_node

    def __repr__(self) -> str:
        string = ''
        temp_node = self
        while temp_node is not None:
            string += '->' + str(temp_node.value)
            temp_node = temp_node.next
        return string[2:]


def is_palindrome_linked_list(head: Node) -> bool:
    """
    Time complexity: O(N)
    Space complexity: O(1)

    Parameters
    ----------
    head : Node
        input head of a Singly LinkedList

    Returns
    -------
    bool
        whether the LinkedList is a palindrome or not

    """
    def reverse(curr_head: Node) -> Node:
        """
        Reverse a Singly LinkedList.

        Parameters
        ----------
        curr_head : Node
            input head of a Singly LinkedList

        Returns
        -------
        prev : Node
            the head of the reversed Singly LinkedList

        """
        prev = None
        while curr_head is not None:
            next_node = curr_head.next
            curr_head.next = prev
            prev = curr_head
            curr_head = next_node
        return prev

    # a single node LinkedList is a palindrome
    if head.next is None:
        return True

    # find middle of the LinkedList
    fast = head
    slow = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    # reverse the second half
    head_second_half = reverse(slow)

    # store the head of reversed part to revert back later
    copy_head_second_half = head_second_half

    # compare the first and the second half
    while head is not None and head_second_half is not None:
        if head.value != head_second_half.value:
            break
        head = head.next
        head_second_half = head_second_half.next

    # revert the reverse of the second half
    reverse(copy_head_second_half)

    # if both halves match
    if head is None or head_second_half is None:
        return True
    return False


if __name__ == '__main__':
    a = Node(2)
    print(is_palindrome_linked_list(a))
    a.next = Node(4)
    a.next.next = Node(6)
    a.next.next.next = Node(4)
    a.next.next.next.next = Node(2)
    print(is_palindrome_linked_list(a))
    a.next.next.next.next.next = Node(2)
    print(is_palindrome_linked_list(a))
