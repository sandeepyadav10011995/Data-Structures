"""
Approach 1. Using Level order traversal
            TC: O(N)
            SC: O(N/2) --> Queue ~ O(N)

Approach 2: Recursive Approach
            TC: O(N)
            SC: O(H) --> In worst Case --> O(N) --> Call Stack

"""
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


class Solution:
    leftView = []
    rightView = []
    def generateLeftViewUsingRecursiveApproach(self, root: TreeNode, level: int) -> None:
        # Base Case
        if root is None:
            return

        if level == len(self.leftView):
            self.leftView.append(root.val)

        self.generateRightViewUsingRecursiveApproach(root.left, level + 1)
        self.generateRightViewUsingRecursiveApproach(root.right, level + 1)

    def generateRightViewUsingRecursiveApproach(self, root: TreeNode, level: int) -> None:  # Root -> Right --> Left
        # Base Case
        if root is None:
            return

        if level == len(self.rightView):
            self.rightView.append(root.val)

        self.generateRightViewUsingRecursiveApproach(root.right, level+1)
        self.generateRightViewUsingRecursiveApproach(root.left, level+1)

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

    @staticmethod
    def generateRightViewOfBinaryTree(root: TreeNode) -> list[int]:
        rightView = []
        # Base Case
        if root is None:
            return rightView

        levelOrderQueue = [root, None]

        while levelOrderQueue:
            node = levelOrderQueue.pop(0)

            if node is not None:
                if levelOrderQueue[0] is None:
                    rightView.append(node.val)
                if node.left:
                    levelOrderQueue.append(node.left)
                if node.right:
                    levelOrderQueue.append(node.right)
            else:
                # To avoid Never Ending Infinite Loop
                if levelOrderQueue:
                    levelOrderQueue.append(None)

        return rightView

"""
TC: O(N)
SC: O(N)
"""
