#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 17:14:14 2021

@author: dopiwoo

Given a binary tree, return an array containing nodes in its right view. The right view of a binary tree is the set of
nodes visible when the tree is seen from the right side.
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


def tree_right_view(root: TreeNode) -> List[int]:
    """
    Time Complexity: O(N)
    Space Complexity: O(N)

    Parameters
    ----------
    root : TreeNode
        Input binary tree.

    Returns
    -------
    res : List[int]
        An array containing nodes in the right view of the given binary tree.

    """
    res = []
    if not root:
        return res
    queue = deque([root])
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            cur_node = queue.popleft()
            if i == level_size - 1:
                res.append(cur_node.val)
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
    return res


if __name__ == '__main__':
    root_node = TreeNode(12)
    root_node.left = TreeNode(7)
    root_node.right = TreeNode(1)
    root_node.left.left = TreeNode(9)
    root_node.right.left = TreeNode(10)
    root_node.right.right = TreeNode(5)
    root_node.left.left.left = TreeNode(3)
    print(tree_right_view(root_node))
