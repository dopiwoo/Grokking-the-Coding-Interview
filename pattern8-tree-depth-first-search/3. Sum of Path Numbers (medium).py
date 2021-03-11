#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 16:22:54 2021

@author: dopiwoo

Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number.
Find the total sum of all the numbers represented by all paths.
"""


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def find_sum_of_path_numbers(root: TreeNode):
    return -1


if __name__ == '__main__':
    root_node = TreeNode(1)
    root_node.left = TreeNode(0)
    root_node.right = TreeNode(1)
    root_node.left.left = TreeNode(1)
    root_node.right.left = TreeNode(6)
    root_node.right.right = TreeNode(5)
    print(find_sum_of_path_numbers(root_node, 23))
