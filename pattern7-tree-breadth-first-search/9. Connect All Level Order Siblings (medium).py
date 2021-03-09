#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 16:58:14 2021

@author: dopiwoo

Given a binary tree, connect each node with its level order successor. The last node of each level should point to the
first node of the next level.
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

    def print_tree(self):
        cur = self
        while cur:
            print(str(cur.val) + ' ', end='')
            cur = cur.next


def connect_all_siblings(root: TreeNode):
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
    prev_node = None
    queue = deque([root])
    while queue:
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
    connect_all_siblings(root_node)
    root_node.print_tree()
