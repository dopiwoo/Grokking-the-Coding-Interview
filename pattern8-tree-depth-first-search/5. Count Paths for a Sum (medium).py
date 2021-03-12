#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 15:20:44 2021

@author: dopiwoo

Given a binary tree and a number 'S', find all paths in the tree such that the sum of all the node values of each path
equals 'S'. Please note that the paths can start or end at any node but all paths must follow direction from parent to
child (top to bottom).
"""

from typing import List


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def count_paths(root: TreeNode, s: int) -> int:
    """
    Time Complexity: O(N^2)
    Space Complexity: O(N)

    Parameters
    ----------
    root : TreeNode
        Input binary tree.
    s : int
        Input number 'S'.

    Returns
    -------
    int
        Number of paths in the tree such that the sum of all the node values of each path equals 'S'.

    """
    def count_paths_recursive(cur_node: TreeNode, cur_s: int, cur_path: List[int]) -> int:
        if not cur_node:
            return 0
        cur_path.append(cur_node.val)
        path_count = 0
        path_sum = 0
        for i in range(len(cur_path) - 1, -1, -1):
            path_sum += cur_path[i]
            if path_sum == cur_s:
                path_count += 1
        return path_count + count_paths_recursive(cur_node.left, cur_s, cur_path) + count_paths_recursive(
            cur_node.right, cur_s, cur_path)

    return count_paths_recursive(root, s, [])


if __name__ == '__main__':
    root_node = TreeNode(12)
    root_node.left = TreeNode(7)
    root_node.right = TreeNode(1)
    root_node.left.left = TreeNode(4)
    root_node.right.left = TreeNode(10)
    root_node.right.right = TreeNode(5)
    print(count_paths(root_node, 11))
