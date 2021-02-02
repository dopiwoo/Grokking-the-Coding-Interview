#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:34:40 2021

@author: dopiwoo

Given the head of the Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the reversed
LinkedList.
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


def reverse(head: Node) -> Node:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)

    Parameters
    ----------
    head : Node
        Input head of a Singly LinkedList.

    Returns
    -------
    prev : Node
        The new head of the reversed LinkedList.

    """
    prev = None
    while head is not None:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev


if __name__ == '__main__':
    a = Node(2)
    a.next = Node(4)
    a.next.next = Node(6)
    a.next.next.next = Node(8)
    a.next.next.next.next = Node(10)
    print(a)
    result = reverse(a)
    print(result)
