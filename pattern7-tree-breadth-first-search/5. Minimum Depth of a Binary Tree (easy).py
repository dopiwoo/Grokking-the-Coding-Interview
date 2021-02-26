#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 10:11:06 2021

@author: dopiwoo

Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root
node to the nearest leaf node.
"""

from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def find_minimum_depth(root: TreeNode) -> int:
    """
    Time Complexity: O(N)
    Space Complexity: O(N)

    Parameters
    ----------
    root : TreeNode
        Input binary tree.

    Returns
    -------
    min_depth : int
        The minimum depth of the given binary tree.

    """
    if not root:
        return 0
    min_depth = 0
    queue = deque([root])
    while queue:
        min_depth += 1
        for _ in range(len(queue)):
            cur_node = queue.popleft()
            if not cur_node.left and not cur_node.right:
                return min_depth
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)


if __name__ == '__main__':
    root_node = TreeNode(12)
    root_node.left = TreeNode(7)
    root_node.right = TreeNode(1)
    root_node.right.left = TreeNode(10)
    root_node.right.right = TreeNode(5)
    print(find_minimum_depth(root_node))
    root_node.left.left = TreeNode(9)
    root_node.right.left.left = TreeNode(11)
    print(find_minimum_depth(root_node))
