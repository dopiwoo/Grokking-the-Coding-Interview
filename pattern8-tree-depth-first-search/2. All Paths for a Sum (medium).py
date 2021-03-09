#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 17:00:08 2021

@author: dopiwoo

Given a binary tree and a number 'S', find all paths from root-to-leaf such that the sum of all the node values of
each path equals 'S'.
"""


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def find_paths(root: TreeNode, required_sum: int):
    all_paths = []
    cur_path = [root.val]
    if root.val == required_sum and not root.left and not root.right:
        all_paths.append(list(cur_path))
    else:
        find_paths()
    return all_paths


if __name__ == '__main__':
    root_node = TreeNode(12)
    root_node.left = TreeNode(7)
    root_node.right = TreeNode(1)
    root_node.left.left = TreeNode(4)
    root_node.right.left = TreeNode(10)
    root_node.right.right = TreeNode(5)
    print(find_paths(root_node, 23))
