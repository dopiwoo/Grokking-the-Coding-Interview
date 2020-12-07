#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 14:59:28 2020

@author: dopiwoo

Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
"""


class Node:
    def __init__(self, value: int, next_node: 'Node' = None) -> None:
        self.value = value
        self.next = next_node


def has_cycle(head: Node) -> bool:
    """
    Time Complexity: O(N) where 'N' is the total number of nodes in the LinkedList
    Space Complexity: O(1)

    Parameters
    ----------
    head: Node
        input LinkedList

    Returns
    -------
    bool
        whether the LinkedList has a cycle in it or not
    """
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


if __name__ == '__main__':
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)
    a.next.next.next.next = Node(5)
    a.next.next.next.next.next = Node(6)
    print(has_cycle(a))
    a.next.next.next.next.next.next = a.next.next
    print(has_cycle(a))
    a.next.next.next.next.next.next = a.next.next.next
    print(has_cycle(a))
