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

        isFirstElementOfLevel = True
        levelOrderQueue = [root, None]

        while levelOrderQueue:
            node = levelOrderQueue.pop(0)

            if node is not None:
                if isFirstElementOfLevel:
                    leftView.append(node.val)
                    isFirstElementOfLevel = False
                if node.left:
                    levelOrderQueue.append(node.left)
                if node.right:
                    levelOrderQueue.append(node.right)
            else:
                isFirstElementOfLevel = True
                # To avoid Never Ending Infinite Loop
                if levelOrderQueue:
                    levelOrderQueue.append(None)

        return leftView


"""
TC: O(N)
SC: O(N)
"""
