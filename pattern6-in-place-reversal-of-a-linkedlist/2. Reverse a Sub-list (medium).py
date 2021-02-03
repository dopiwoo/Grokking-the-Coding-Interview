#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:45:31 2021

@author: dopiwoo

Given the head of a LinkedList and two positions 'p' and 'q', reverse the LinkedList from position 'p' to 'q'.
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


def reverse_sub_list(head: Node, p: int, q: int) -> Node or None:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)

    Parameters
    ----------
    head : Node
        Input head of a LinkedList.
    p : int
        Input start position 'p'.
    q : int
        Input end position 'p'.

    Returns
    -------
    Node or None
        The LinkedList reversed from position 'p' to 'q'.

    """
    if not head:
        return None
    cur, prev = head, None
    while p > 1:
        prev = cur
        cur = cur.next
        p -= 1
        q -= 1
    tail, con = cur, prev
    while q:
        third = cur.next
        cur.next = prev
        prev = cur
        cur = third
        q -= 1
    if con:
        con.next = prev
    else:
        head = prev
    tail.next = cur
    return head


if __name__ == '__main__':
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)
    a.next.next.next.next = Node(5)
    print(a)
    print(reverse_sub_list(a, 2, 4))
    b = Node(7)
    b.next = Node(9)
    b.next.next = Node(8)
    b.next.next.next = Node(1)
    b.next.next.next.next = Node(10)
    b.next.next.next.next.next = Node(2)
    b.next.next.next.next.next.next = Node(6)
    print(b)
    print(reverse_sub_list(b, 3, 6))
