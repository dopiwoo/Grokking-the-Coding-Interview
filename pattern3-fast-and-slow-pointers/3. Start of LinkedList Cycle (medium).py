#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 15:31:02 2020

@author: dopiwoo

Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
"""


class Node:
    def __init__(self, value: int, next_node: 'Node' = None):
        self.value = value
        self.next = next_node


def find_cycle_start(head: Node) -> Node:
    """
    Floyd's Tortoise and Hare
    Floyd's algorithm is separated into two distinct phases. In the first phase, it determines whether a cycle is
    present in the list. If no cycle is present, it returns null immediately, as it is impossible to find the entrance
    to a nonexistent cycle. Otherwise, it uses the located "intersection node" to find the entrance to the cycle.

    Time Complexity: O(N)
    Space Complexity: O(1)

    Parameters
    ----------
    head : Node
        input LinkedList

    Returns
    -------
    slow : Node
        the starting node of the cycle

    """
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow


if __name__ == '__main__':
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)
    a.next.next.next.next = Node(5)
    a.next.next.next.next.next = Node(6)
    a.next.next.next.next.next.next = a.next.next
    print(find_cycle_start(a).value)
    a.next.next.next.next.next.next = a.next.next.next
    print(find_cycle_start(a).value)
    a.next.next.next.next.next.next = a
    print(find_cycle_start(a).value)
