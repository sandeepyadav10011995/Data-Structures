"""
Problem: Print or return the Top View of a binary tree
        -> Horizontal Distance
        -> Level Order
        Do a level order and store in the HaspMap w.r.t Horizontal Distance as key in the Hash Map

"""
import math
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


class Solution:
    @staticmethod
    def generateTopViewOfBinaryTree(root: TreeNode) -> dict[int: list[int]]:
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
            if node is not None:
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

    def topViewBT(self, root: TreeNode) -> list[int]:
        topViewMap, minHD, maxHD = self.generateTopViewOfBinaryTree(root)
        return [topViewMap[i][0] for i in range(minHD, maxHD+1)]

    def bottomViewBT(self, root: TreeNode) -> list[int]:
        topViewMap, minHD, maxHD = self.generateTopViewOfBinaryTree(root)
        return [topViewMap[i][-1] for i in range(minHD, maxHD+1)]


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
    print(sol.topViewBT(root1))


def main12():
    sol = Solution()
    bt = BT()
    bt.createBT()
    root1 = bt.root
    print(sol.bottomViewBT(root1))


main11()
print("*"*100)
main12()
