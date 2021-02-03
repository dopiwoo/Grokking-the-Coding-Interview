#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 16:59:33 2021

@author: dopiwoo

Given the head of a LinkedList and a number 'k', reverse every alternating 'k' sized sub-list starting from the head.
If, in the end, you are left with a sub-list with less than 'k' elements, reverse it too.
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


def reverse_alternative_k_elements(head: Node, k: int) -> Node or None:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)

    Parameters
    ----------
    head : Node
        Input head of a LinkedList.
    k : int
        Input number 'k'.

    Returns
    -------
    Node or None
        The LinkedList reversed every alternating 'k' sized sub-list starting from the head.

    """
    if not head:
        return None
    cur, prev = head, None
    while cur:
        i = 0
        tail, con = cur, prev
        while cur and i < k:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            i += 1
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        i = 0
        while cur and i < k:
            prev = cur
            cur = cur.next
            i += 1
    return head


if __name__ == '__main__':
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)
    a.next.next.next.next = Node(5)
    a.next.next.next.next.next = Node(6)
    a.next.next.next.next.next.next = Node(7)
    a.next.next.next.next.next.next.next = Node(8)
    print(a)
    print(reverse_alternative_k_elements(a, 2))
