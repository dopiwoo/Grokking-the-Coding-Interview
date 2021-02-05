#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:52:46 2021

@author: dopiwoo

Given the head of a Singly LinkedList and a number 'k', rotate the LinkedList to the right by 'k' nodes.
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


def rotate(head: Node, rotations: int) -> Node or None:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)

    Parameters
    ----------
    head : Node
        Input head of a Singly LinkedList.
    rotations : int
        Input number 'k'.

    Returns
    -------
    Node or None
        The LinkedList rotated to the right by 'k' nodes.

    """
    if not head:
        return None
    cur = head
    length = 1
    while cur.next is not None:
        cur = cur.next
        length += 1
    cur.next = head
    tail = head
    for i in range(length - rotations % length - 1):
        tail = tail.next
    head = tail.next
    tail.next = None
    return head


if __name__ == '__main__':
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)
    a.next.next.next.next = Node(5)
    a.next.next.next.next.next = Node(6)
    print(a)
    print(rotate(a, 3))
