"""
Level Order Traversal --> BFS
Data Structure = Queue

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
    def levelOrderTraversalOne(root: TreeNode) -> list[int]:
        levelOrderResult = []
        # Base Case
        if root is None:
            return levelOrderResult

        levelOrderQueue = [root]
        while levelOrderQueue:
            node = levelOrderQueue.pop(0)
            levelOrderResult.append(node.val)

            if node.left:
                levelOrderQueue.append(node.left)
            if node.right:
                levelOrderQueue.append(node.right)

        return levelOrderResult

    @staticmethod
    def levelOrderTraversalTwo(root: TreeNode) -> list[int]:
        levelOrderResult = []
        # Base Case
        if root is None:
            return levelOrderResult

        levelOrderQueue = [root]
        while levelOrderQueue:
            node = levelOrderQueue.pop(0)
            levelOrderResult.append(node.val)

            if node.right:
                levelOrderQueue.append(node.right)
            if node.left:
                levelOrderQueue.append(node.left)

        return levelOrderResult


"""
TC: O(N)
SC: O(N)
"""
