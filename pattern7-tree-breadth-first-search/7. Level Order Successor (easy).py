#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 17:29:12 2021

@author: dopiwoo

Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor
is the node that appears right after the given node in the level order traversal.
"""

from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def find_successor(root: TreeNode, key: int) -> TreeNode or None:
    """
    Time Complexity: O(N)
    Space Complexity: O(N)

    Parameters
    ----------
    root : TreeNode
        Input binary tree.
    key : int
        Input node.

    Returns
    -------
    TreeNode or None
        The level order successor of the given node in the given tree.

    """
    if not root:
        return None
    queue = deque([root])
    while queue:
        cur_node = queue.popleft()
        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)
        if cur_node.val == key:
            break
    return queue[0] if queue else None


if __name__ == '__main__':
    root_node = TreeNode(12)
    root_node.left = TreeNode(7)
    root_node.right = TreeNode(1)
    root_node.left.left = TreeNode(9)
    root_node.right.left = TreeNode(10)
    root_node.right.right = TreeNode(5)
    print(find_successor(root_node, 12))
    print(find_successor(root_node, 9))
