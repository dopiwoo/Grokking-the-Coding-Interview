#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 17:25:28 2021

@author: dopiwoo

Given a binary tree, populate an array to represent its level-by-level traversal. You should populate the values of all
nodes of each level from left to right in separate sub-arrays.
"""

from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def traverse(root: TreeNode) -> List[List[int]]:
    """
    Time Complexity: O(N)
    Space Complexity: O(N)

    Parameters
    ----------
    root : TreeNode
        Input binary tree.

    Returns
    -------
    res : List[List[int]]
        Array representing the level-by-level traversal of the given binary tree.

    """
    res = []
    if not root:
        return res
    queue = deque([root])
    while queue:
        cur_level = []
        for _ in range(len(queue)):
            cur_node = queue.popleft()
            cur_level.append(cur_node.val)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        res.append(cur_level)
    return res


if __name__ == '__main__':
    root_node = TreeNode(12)
    root_node.left = TreeNode(7)
    root_node.right = TreeNode(1)
    root_node.left.left = TreeNode(9)
    root_node.right.left = TreeNode(10)
    root_node.right.right = TreeNode(5)
    print(traverse(root_node))
