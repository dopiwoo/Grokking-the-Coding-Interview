#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:19:43 2021

@author: dopiwoo

Given a binary tree, populate an array to represent its level-by-level traversal in reverse order, i.e., the lowest
level comes first. You should populate the values of all nodes in each level from left to right in separate sub-arrays.
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
    List[List[int]]
        Array representing the level-by-level traversal in reverse order of the given binary tree.

    """
    if not root:
        return []
    queue = deque([root])
    res = deque()
    while queue:
        cur_level = []
        for _ in range(len(queue)):
            cur_node = queue.popleft()
            cur_level.append(cur_node.val)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        res.appendleft(cur_level)
    return list(res)


if __name__ == '__main__':
    root_node = TreeNode(12)
    root_node.left = TreeNode(7)
    root_node.right = TreeNode(1)
    root_node.left.left = TreeNode(9)
    root_node.right.left = TreeNode(10)
    root_node.right.right = TreeNode(5)
    print(traverse(root_node))
