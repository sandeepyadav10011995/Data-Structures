"""
Approach 1. Using Size of the Queue --> List[List[int]]

Approach 2. Using None Logic in Queue --> HashMap[int: List[int]]

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
    def layerByLayerLeftViewOfBinaryTree(root: TreeNode) -> list[list[int]]:
        lblLeftViewList = []
        # Base Case
        if root is None:
            return lblLeftViewList

        lvQueue = [root]
        lblLeftViewList.append([])
        while lvQueue:
            sz = len(lvQueue)
            for index in range(sz):
                node = lvQueue.pop(0)
                if len(lblLeftViewList) + 1 < index:
                    lblLeftViewList[index] = []
                lblLeftViewList[index].append(node.val)

                if node.left:
                    lvQueue.append(node.left)
                if node.right:
                    lvQueue.append(node.right)

        return lblLeftViewList

    @staticmethod
    def layerByLayerLeftViewOfBinaryTree2(root: TreeNode) -> dict[int: list[int]]:
        lblLeftViewMap = {}
        # Base Case
        if root is None:
            return lblLeftViewMap

        positionInLevel = 0
        lvQueue = [root, None]

        while lvQueue:
            node = lvQueue.pop(0)
            if node:
                positionInLevel += 1
                levelList = lblLeftViewMap.get(positionInLevel, [])
                levelList.append(node.val)
                lblLeftViewMap[positionInLevel] = levelList

                if node.left:
                    lvQueue.append(node.left)
                if node.right:
                    lvQueue.append(node.right)
            else:
                positionInLevel = 0
                if lvQueue:
                    lvQueue.append(None)

        return lblLeftViewMap
