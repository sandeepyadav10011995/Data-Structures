"""
POSTORDER -: LEFT --> RIGHT --> ROOT
Problem : Binary Tree PostOrder Traversal

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
            self._helper(root.right)
            self.output.append(root.val)

    def postOrderTraversalRecursive(self, root: TreeNode) -> list[int]:
        self._helper(root)
        return self.output

    @staticmethod
    def postOrderTraversalIterativeWithTwoStacks(root: TreeNode) -> list[int]:
        stack1 = [root]
        stack2 = []
        while stack1:
            node = stack1.pop()
            stack2.append(node.val)

            if root.right:
                stack1.append(root.right)
            if root.left:
                stack1.append(root.left)

        return stack2[::-1]

    @staticmethod
    def _isLeaf(root: TreeNode) -> bool:
        return root.left is None and root.right is None

    def postOrderTraversalIterativeWithOneStack(self, root: TreeNode) -> list[int]:
        prev = None
        cur = root
        stack = []

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            # Three Cases: Leaf Node | prev Node is Right Node | prev Node is Left Node && Right Node is None
            if self._isLeaf(cur) or prev == cur.right or (prev == cur.left and cur.right is None):
                self.output.append(cur.val)
                prev = cur
                cur = None
            elif cur.right is not None:
                stack.append(cur)
                cur = cur.right

        return self.output
