#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 17:29:59 2020

@author: dopiwoo

Given the head of a LinkedList with a cycle, find the length of the cycle.
"""


class Node:
    def __init__(self, value: int, next_node: 'Node' = None):
        self.value = value
        self.next = next_node


def find_cycle_length(head: Node) -> int:
    """
    Time Complexity: O(N) where 'N' is the total number of nodes in the LinkedList
    Space Complexity: O(1)

    Parameters
    ----------
    head: Node
        input LinkedList

    Returns
    -------
    int
        the length of the cycle

    """
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            length = 0
            while True:
                slow = slow.next
                length += 1
                if fast == slow:
                    return length
    return 0


if __name__ == '__main__':
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)
    a.next.next.next.next = Node(5)
    a.next.next.next.next.next = Node(6)
    print(find_cycle_length(a))
    a.next.next.next.next.next.next = a.next.next
    print(find_cycle_length(a))
    a.next.next.next.next.next.next = a.next.next.next
    print(find_cycle_length(a))
