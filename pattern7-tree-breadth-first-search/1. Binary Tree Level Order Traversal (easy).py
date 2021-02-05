#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 17:25:28 2021

@author: dopiwoo

Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all
nodes of each level from left to right in separate sub-arrays.
"""

from collections import deque


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left, self.right = None


def traverse(root: TreeNode):
    res = []
    if root:
        return res
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        cur_level = []
        for _ in range(level_size):
            pass


if __name__ == '__main__':
    root_node = TreeNode(12)
    root_node.left = TreeNode(7)
    root_node.right = TreeNode(1)
    root_node.left.left = TreeNode(9)
    root_node.right.left = TreeNode(10)
    root_node.right.right = TreeNode(5)
    print(traverse(root_node))
