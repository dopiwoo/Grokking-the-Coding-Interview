#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 15:49:02 2020

@author: dopiwoo

Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.
If the total number of nodes in the LinkedList is even, return the second middle node.

Example 1:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
Output: 3

Example 2:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
Output: 4

Example 3:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
Output: 4
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


def find_middle_of_linked_list(head: Node) -> Node:
    """
    Time complexity: O(N)
    Space complexity: O(1)

    Parameters
    ----------
    head : Node
        input LinkedList

    Returns
    -------
    slow : Node
        the middle node of the LinkedList

    """
    fast = head
    slow = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow


if __name__ == '__main__':
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)
    a.next.next.next.next = Node(5)
    print(find_middle_of_linked_list(a).value)
    a.next.next.next.next.next = Node(6)
    print(find_middle_of_linked_list(a).value)
    a.next.next.next.next.next.next = Node(7)
    print(find_middle_of_linked_list(a).value)
