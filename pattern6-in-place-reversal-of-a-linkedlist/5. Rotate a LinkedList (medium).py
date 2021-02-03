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
    if not head:
        return None
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
