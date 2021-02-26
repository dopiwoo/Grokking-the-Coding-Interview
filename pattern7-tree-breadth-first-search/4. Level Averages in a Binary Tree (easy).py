#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 10:02:53 2021

@author: dopiwoo

Given a binary tree, populate an array to represent the averages of all of its levels.
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


def find_level_averages(root: TreeNode) -> List[float]:
    """
    Time Complexity: O(N)
    Space Complexity: O(N)

    Parameters
    ----------
    root : TreeNode
        Input binary tree.

    Returns
    -------
    res : List[float]
        Array representing the averages of all levels of the given binary tree.

    """
    res = []
    if not root:
        return res
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level_sum = 0.0
        for _ in range(level_size):
            cur_node = queue.popleft()
            level_sum += cur_node.val
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
        res.append(level_sum / level_size)
    return res


if __name__ == '__main__':
    root_node = TreeNode(12)
    root_node.left = TreeNode(7)
    root_node.right = TreeNode(1)
    root_node.left.left = TreeNode(9)
    root_node.left.right = TreeNode(2)
    root_node.right.left = TreeNode(10)
    root_node.right.right = TreeNode(5)
    print(find_level_averages(root_node))
