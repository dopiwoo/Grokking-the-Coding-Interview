#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 14:49:04 2021

@author: dopiwoo

Given a binary tree, connect each node with its level order successor. The last node of each level should point to a
null node.
"""

from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = None

    def __repr__(self):
        return str(self.val)

    def print_level_order(self):
        string = ''
        next_level_root = self
        while next_level_root:
            cur = next_level_root
            next_level_root = None
            while cur:
                print(str(cur.val) + ' ', end='')
                if not next_level_root:
                    if cur.left:
                        next_level_root = cur.left
                    elif cur.right:
                        next_level_root = cur.right
                cur = cur.next
            print()
        return string


def connect_level_order_siblings(root: TreeNode):
    """
    Time Complexity: O(N)
    Space Complexity: O(N)

    Parameters
    ----------
    root : TreeNode
        Input binary tree.

    Returns
    -------
    None.

    """
    if not root:
        return None
    queue = deque([root])
    while queue:
        prev_node = None
        for _ in range(len(queue)):
            cur_node = queue.popleft()
            if prev_node:
                prev_node.next = cur_node
            prev_node = cur_node
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)


if __name__ == '__main__':
    root_node = TreeNode(12)
    root_node.left = TreeNode(7)
    root_node.right = TreeNode(1)
    root_node.left.left = TreeNode(9)
    root_node.right.left = TreeNode(10)
    root_node.right.right = TreeNode(5)
    connect_level_order_siblings(root_node)
    root_node.print_level_order()
