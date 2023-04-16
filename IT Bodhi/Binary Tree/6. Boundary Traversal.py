"""
Boundary Traversal  --> AntiClockwise


                            1
                       2        7
                  3                  8
                     4            9
                  5     6      10   11

Boundary Traversal -: 1, 2, 3, 4, 5, 6, 10, 11, 9, 8, 7

Step 1: Generate Left Boundary Excluding Leaf Nodes
Step 2: Generate Leaf Nodes --> InOrder
Step 3: Generate Right Boundary Excluding Leaf Nodes

TC: O(H) + O(H) + O(N) ~ O(N)
SC: O(N) --> Call Stack
"""
from collections import deque
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


class Solution:
    @staticmethod
    def _isLeaf(node: TreeNode) -> bool:
        return node.left is None and node.right is None

    def addLeftBoundary(self, root: TreeNode, result: list[int]) -> None:
        cur = root.left
        while cur:
            if not self._isLeaf(cur):
                result.append(cur.val)
            else:
                cur = cur.right

    def addLeafNodes(self, root: TreeNode, result: list) -> None:  # Inorder
        if self._isLeaf(root):
            result.append(root.val)
            return
        if root.left:
            self.addLeafNodes(root.left, result)
        if root.right:
            self.addLeafNodes(root.right, result)

    def addRightBoundary(self, root: TreeNode, result: list) -> None:
        # Base Case
        cur = root
        tmp = []
        while cur:
            if not self._isLeaf(cur):
                tmp.append(cur.val)

            if cur.right:
                cur = cur.right
            else:
                cur = cur.left
        i = len(tmp)-1
        while i >= 0:
            result.append([tmp[i]])
            i -= 1


    def generateBoundaryTraversal(self, root: TreeNode) -> list[int]:
        result = []
        # Base Case
        if not self._isLeaf(root):
            result.append(root.val)
        # Add Left Boundary
        self.addLeftBoundary(root,result)
        # Add Leaf Nodes
        self.addLeafNodes(root, result)
        # Add Right Boundary
        self.addRightBoundary(root, result)

        return result
