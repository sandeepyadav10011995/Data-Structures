"""
PREORDER -: ROOT --> LEFT --> RIGHT
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
            self.output.append(root.val)
            self._helper(root.left)
            self._helper(root.right)

    def preOrderTraversalRecursive(self, root: TreeNode) -> list[int]:
        self._helper(root)
        return self.output

    def preOrderTraversalIterative(self, root: TreeNode) -> list[int]:
        stack = [root]
        while stack:
            node = stack.pop()
            self.output.append(node.val)

            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

        return self.output
