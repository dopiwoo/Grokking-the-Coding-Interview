#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 17:00:08 2021

@author: dopiwoo

Given a binary tree and a number 'S', find all paths from root-to-leaf such that the sum of all the node values of
each path equals 'S'.
"""

from typing import List


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def find_paths(root: TreeNode, required_sum: int) -> List[List[int]]:
    """
    Time Complexity: O(N^2)
    Space Complexity: O(N)

    Parameters
    ----------
    root : TreeNode
        Input binary tree.
    required_sum : int
        Input number 'S'.

    Returns
    -------
    all_paths : List[List[int]]
        All paths from root-to-leaf such that the sum of all the node values of each path equals 'S'.

    """
    def find_paths_recursive(cur_node, path_sum, cur_path, ins_all_paths):
        if not cur_node:
            return
        cur_path.append(cur_node.val)
        if cur_node.val == path_sum and not cur_node.left and not cur_node.right:
            ins_all_paths.append(cur_path.copy())
        else:
            find_paths_recursive(cur_node.left, path_sum - cur_node.val, cur_path, ins_all_paths)
            find_paths_recursive(cur_node.right, path_sum - cur_node.val, cur_path, ins_all_paths)
        del cur_path[-1]

    all_paths = []
    find_paths_recursive(root, required_sum, [], all_paths)
    return all_paths


if __name__ == '__main__':
    root_node = TreeNode(12)
    root_node.left = TreeNode(7)
    root_node.right = TreeNode(1)
    root_node.left.left = TreeNode(4)
    root_node.right.left = TreeNode(10)
    root_node.right.right = TreeNode(5)
    print(find_paths(root_node, 23))
