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


def reverse_sub_list(head: Node, p: int, q: int) -> Node:
    if p == q:
        return head
    curr, prev = head, None
    i = 0
    while curr is not None and i < p - 1:
        prev = curr
        curr = curr.next
        i += 1
    last_node_of_first_part = prev
    last_node_of_sub_list = curr
    while curr is not None and i < q:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        i += 1
    if last_node_of_first_part is not None:
        last_node_of_first_part.next = prev
    else:
        head = prev
    last_node_of_sub_list.next = curr
    return head


if __name__ == '__main__':
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)
    a.next.next.next.next = Node(5)
    print(a)
    result = reverse_sub_list(a, 2, 4)
    print(result)
