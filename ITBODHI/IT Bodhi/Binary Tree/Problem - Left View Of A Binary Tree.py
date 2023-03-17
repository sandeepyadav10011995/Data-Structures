"""
Approach 1. Using Level order traversal

"""
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


class Solution:
    @staticmethod
    def generateLeftViewOfBinaryTree(root: TreeNode) -> list[int]:
        leftView = []
        # Base Case
        if root is None:
            return leftView

        queue = [root, None]
        isFirstElementOfLevel = True

        while queue:
            node = queue.pop(0)

            if node is not None:
                if isFirstElementOfLevel:
                    leftView.append(node.val)
                    isFirstElementOfLevel = False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                isFirstElementOfLevel = True
                if queue:
                    queue.append(None)

        return leftView
