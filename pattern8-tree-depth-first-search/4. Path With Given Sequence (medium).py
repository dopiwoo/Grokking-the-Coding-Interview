#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 09:27:57 2021

@author: dopiwoo

Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
"""

from typing import List


class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def find_path(root: TreeNode, sequence: List[int]) -> bool:
    """
    Time Complexity: O(N)
    Space Complexity: O(N)

    Parameters
    ----------
    root : TreeNode
        Input binary tree.
    sequence : List[int]
        Input number sequence.

    Returns
    -------
    bool
        Whether the sequence is present as a root-to-leaf path in the given tree.

    """
    def find_path_recursive(cur_node, seq, seq_index):
        if not cur_node:
            return False
        len_seq = len(seq)
        if seq_index >= len_seq or cur_node.val != seq[seq_index]:
            return False
        if not cur_node.left and not cur_node.right and seq_index == len_seq - 1:
            return True
        seq_index += 1
        return find_path_recursive(cur_node.left, seq, seq_index) or find_path_recursive(cur_node.right, seq, seq_index)

    if not root:
        return len(sequence) == 0
    return find_path_recursive(root, sequence, 0)


if __name__ == '__main__':
    root_node = TreeNode(1)
    root_node.left = TreeNode(0)
    root_node.right = TreeNode(1)
    root_node.left.left = TreeNode(1)
    root_node.right.left = TreeNode(6)
    root_node.right.right = TreeNode(5)
    print(find_path(root_node, [1, 0, 7]))
    print(find_path(root_node, [1, 1, 6]))
