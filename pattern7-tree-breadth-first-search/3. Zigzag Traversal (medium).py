#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 11:30:41 2021

@author: dopiwoo

Given a binary tree, populate an array to represent its zigzag level order traversal. You should populate the values of
all nodes of the first level from left to right, then right to left for the next level and keep alternating in the same
manner for the following levels.
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
        Array representing the zigzag level order traversal of the given binary tree.

    """
    if not root:
        return []
    queue = deque([root])
    res = []
    left_to_right = True
    while queue:
        cur_level = deque()
        for _ in range(len(queue)):
            cur_node = queue.popleft()
            if left_to_right:
                cur_level.append(cur_node.val)
            else:
                cur_level.appendleft(cur_node.val)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        res.append(list(cur_level))
        left_to_right = not left_to_right
    return res


if __name__ == '__main__':
    root_node = TreeNode(12)
    root_node.left = TreeNode(7)
    root_node.right = TreeNode(1)
    root_node.left.left = TreeNode(9)
    root_node.right.left = TreeNode(10)
    root_node.right.right = TreeNode(5)
    root_node.right.left.left = TreeNode(20)
    root_node.right.left.right = TreeNode(17)
    print(traverse(root_node))
