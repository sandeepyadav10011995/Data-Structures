"""
Problem: Print or return the Top View of a binary tree
        -> Horizontal Distance --> X-axis
        -> Level Order
        Do a level order and store in the HaspMap w.r.t Horizontal Distance as key in the Hash Map


                                                  a
                            b                                                   c
                d                        e                           f                    j
         n            g                                                   i           k       m
             o     p     h                                            l           t
                       q    r                                             s

"""
import math
from dataclasses import dataclass
from typing import Any


@dataclass
class LLNode:
    key: int = None
    next: Any = None


@dataclass
class TreeNode:
    val: str = None
    left: Any = None
    right: Any = None
    verticalChildren: Any = None


class Solution1:  # Layer By Layer Vertical View
    @staticmethod
    def _generateLayerByLayerVerticalViewOfBinaryTree(root: TreeNode) -> dict[int: list[int]]:
        topViewMap = {}
        # Base Case
        if root is None:
            return topViewMap

        maxHD = -math.inf
        minHD = math.inf
        horizontalDistance = 0
        queue = [(root, horizontalDistance), (None, None)]
        while queue:
            node, hd = queue.pop(0)
            if node:
                levelList = topViewMap.get(hd, [])
                levelList.append(node.val)
                topViewMap[hd] = levelList

                if hd > maxHD:
                    maxHD = hd
                if hd < minHD:
                    minHD = hd

                if node.left:
                    queue.append((node.left, hd-1))
                if node.right:
                    queue.append((node.right, hd+1))
            else:
                if queue:
                    queue.append((None, None))
        return topViewMap, minHD, maxHD

    def layerByLayerVerticalViewBT(self, root: TreeNode) -> list[int]:
        topViewMap, minHD, maxHD = self._generateLayerByLayerVerticalViewOfBinaryTree(root)
        return [topViewMap[i] for i in range(minHD, maxHD+1)]


@dataclass
class QueueObject:
    node: TreeNode = None
    level: int = 0
    horizontalDistance: int = 0


@dataclass
class VerticalListObject:
    level: int = 0
    bte: TreeNode = None


class Solution:  # Layer By Layer Vertical View -> Connect Vertical Children
    @staticmethod
    def generateVerticalViewOfBinaryTree(root: TreeNode):
        verticalOrderMap = {}
        # Base Case
        if root is None:
            return verticalOrderMap

        maxHD = -math.inf
        minHD = math.inf

        levelQueue = [QueueObject(node=root, level=1), QueueObject(None)]
        while levelQueue:
            currentQueueObj = levelQueue.pop(0)

            if currentQueueObj.node is not None:
                verticalList = verticalOrderMap.get(currentQueueObj.horizontalDistance)
                if verticalList:
                    lastVList = verticalList[-1]
                    if lastVList[0].level == currentQueueObj.level:
                        lastVList.append(VerticalListObject(level=currentQueueObj.level, bte=currentQueueObj.node))
                        verticalList[-1] = lastVList
                    else:
                        newVListObj = [VerticalListObject(level=currentQueueObj.level, bte=currentQueueObj.node)]
                        verticalList.append(newVListObj)
                else:
                    newVListObj = [VerticalListObject(level=currentQueueObj.level, bte=currentQueueObj.node)]
                    verticalList = [newVListObj]

                verticalOrderMap[currentQueueObj.horizontalDistance] = verticalList

                if currentQueueObj.horizontalDistance > maxHD:
                    maxHD = currentQueueObj.horizontalDistance
                if currentQueueObj.horizontalDistance < minHD:
                    minHD = currentQueueObj.horizontalDistance

                if currentQueueObj.node.left:
                    levelQueue.append(QueueObject(node=currentQueueObj.node.left, level=currentQueueObj.level + 1,
                                                  horizontalDistance=currentQueueObj.horizontalDistance - 1))
                if currentQueueObj.node.right:
                    levelQueue.append(QueueObject(node=currentQueueObj.node.right, level=currentQueueObj.level + 1,
                                                  horizontalDistance=currentQueueObj.horizontalDistance + 1))
            elif levelQueue:
                levelQueue.append(QueueObject(node=None))
        return verticalOrderMap, minHD, maxHD

    def setVerticalChildrenForEveryNodeOfBT(self, root: TreeNode):  # Connect List --> List
        verticalOrderMap, minHD, maxHD = self.generateVerticalViewOfBinaryTree(root)
        for i in range(minHD, maxHD+1):
            verticalView: list[list[VerticalListObject]] = verticalOrderMap.get(i)
            for j, listObject in enumerate(verticalView):
                nextListObject = None if len(verticalView) <= j+1 else verticalView[j+1]
                for btObj in listObject:
                    btObj.bte.verticalChildren = nextListObject

        return root


class BT:
    def __init__(self):
        self.root = None

    def createBT(self):
        # Create a BT
        root = TreeNode("a")

        root.left = TreeNode("b")
        root.right = TreeNode("c")

        root.left.left = TreeNode("d")
        root.left.right = TreeNode("e")

        root.left.left.left = TreeNode("n")
        root.left.left.right = TreeNode("g")

        root.left.left.left.right = TreeNode("o")

        root.left.left.right.left = TreeNode("p")
        root.left.left.right.right = TreeNode("h")

        root.left.left.right.right.left = TreeNode("q")
        root.left.left.right.right.right = TreeNode("r")

        root.right.left = TreeNode("f")
        root.right.left.right = TreeNode("i")
        root.right.left.right.left = TreeNode("l")
        root.right.left.right.left.right = TreeNode("s")

        root.right.right = TreeNode("j")
        root.right.right.left = TreeNode("k")
        root.right.right.left.right = TreeNode("m")
        root.right.right.left.right.left = TreeNode("t")
        self.root = root


def main11():
    sol = Solution()
    bt = BT()
    bt.createBT()
    root1 = bt.root
    print(sol.setVerticalChildrenForEveryNodeOfBT(root1))


def main12():
    sol = Solution1()
    bt = BT()
    bt.createBT()
    root1 = bt.root
    print(sol.layerByLayerVerticalViewBT(root1))


# print("*"*100)
# main11()
print("*"*100)
main12()
print("*"*100)
