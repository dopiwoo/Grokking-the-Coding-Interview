#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:49:08 2021

@author: dopiwoo

Pre-order Traversal
Pre-order traversal is to visit the root first. Then traverse the left subtree. Finally, traverse the right subtree.

In-order Traversal
In-order traversal is to traverse the left subtree first. Then visit the root. Finally, traverse the right subtree.

Post-order Traversal
Post-order traversal is to traverse the left subtree first. Then traverse the right subtree. Finally, visit the root.

Level-order traversal
Level-order traversal is to traverse the tree level by level.
Breadth-First Search is an algorithm to traverse or search in data structures like a tree or a graph. The algorithm
starts with a root node and visit the node itself first. Then traverse its neighbors, traverse its second level
neighbors, traverse its third level neighbors, so on and so forth.
When we do breadth-first search in a tree, the order of the nodes we visited is in level order.
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


class Recursive:
    @staticmethod
    def preorderTraversal(root: TreeNode) -> List[int]:
        return [root.val] + Recursive.preorderTraversal(root.left) + Recursive.preorderTraversal(
            root.right) if root else []

    @staticmethod
    def inorderTraversal(root: TreeNode) -> List[int]:
        return Recursive.inorderTraversal(root.left) + [root.val] + Recursive.inorderTraversal(
            root.right) if root else []

    @staticmethod
    def postorderTraversal(root: TreeNode) -> List[int]:
        return Recursive.postorderTraversal(root.left) + Recursive.postorderTraversal(root.right) + [root.val
                                                                                                     ] if root else []


class Iterative:
    @staticmethod
    def preorderTraversal(root: TreeNode) -> List[int]:
        if not root:
            return []
        stack, output = [root], []
        while stack:
            root = stack.pop()
            if root:
                output.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return output

    @staticmethod
    def inorderTraversal(root: TreeNode) -> List[int]:
        if not root:
            return []
        stack, output = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return output
            node = stack.pop()
            output.append(node.val)
            root = node.right

    @staticmethod
    def postorderTraversal(root: TreeNode) -> List[int]:
        if not root:
            return []
        stack, output = [root], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return output[::-1]

    @staticmethod
    def levelOrder(root: TreeNode) -> List[List[int]]:
        output = []
        if not root:
            return output
        queue = deque([root])
        while queue:
            cur_level = []
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                cur_level.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            output.append(cur_level)
        return output


if __name__ == '__main__':
    root_node = TreeNode(12)
    root_node.left = TreeNode(7)
    root_node.right = TreeNode(1)
    root_node.left.left = TreeNode(9)
    root_node.right.left = TreeNode(10)
    root_node.right.right = TreeNode(5)
    print(Recursive().preorderTraversal(root_node))
    print(Iterative().preorderTraversal(root_node))
    print(Recursive().inorderTraversal(root_node))
    print(Iterative().inorderTraversal(root_node))
    print(Recursive().postorderTraversal(root_node))
    print(Iterative().postorderTraversal(root_node))
    print(Iterative().levelOrder(root_node))
