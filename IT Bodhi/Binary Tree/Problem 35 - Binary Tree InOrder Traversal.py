"""
INORDER -: LEFT --> ROOT --> RIGHT
Problem : Binary Tree PreOrder Traversal

Approach 1: Recursive Approach --> Can lead to Time Limit Exceeded !!

Approach 2: Iterative Approach

"""
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


class Solution:
    def __init__(self):
        self.output = []

    def _helper(self, root: TreeNode) -> None:
        # Base Case
        if root is None:
            return
        while root:
            self._helper(root.left)
            self.output.append(root.val)
            self._helper(root.right)

    def inOrderTraversalRecursive(self, root: TreeNode) -> list[int]:
        self._helper(root)
        return self.output

    def inOrderTraversalIterative(self, root: TreeNode) -> list[int]:
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            self.output.append(node.val)

            if node.right:
                root = node.right

        return self.output
