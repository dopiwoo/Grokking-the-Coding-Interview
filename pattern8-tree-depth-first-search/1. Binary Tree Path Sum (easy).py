#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 17:29:02 2021

@author: dopiwoo

Given a binary tree and a number 'S', find if the tree has a path from root-to-leaf such that the sum of all the node
values of that path equals 'S'.
"""


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def has_path(root: TreeNode, path_sum: int):
    """
    Time Complexity: O(N)
    Space Complexity: O(N)

    Parameters
    ----------
    root : TreeNode
        Input binary tree.
    path_sum : int
        Input number 'S'.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if not root:
        return False
    if path_sum == root.val and not root.left and not root.right:
        return True
    return has_path(root.left, path_sum - root.val) or has_path(root.right, path_sum - root.val)


if __name__ == '__main__':
    root_node = TreeNode(12)
    root_node.left = TreeNode(7)
    root_node.right = TreeNode(1)
    root_node.left.left = TreeNode(9)
    root_node.right.left = TreeNode(10)
    root_node.right.right = TreeNode(5)
    print(has_path(root_node, 23))
    print(has_path(root_node, 16))
