"""
Problem : Binary Tree Diameter
        - The Longest Path Between Any Two Nodes
        - Path does not need to pass via root

Approach 1: Try it on Every Node (left max height + right max height) --> TopDown Approach
            TC: O(N^2)
            SC: O(N)

Approach 2: Top Down --> Update the globalValue and return the localValue
            TC: O(N)
            SC: O(N)

Approach 3: Bottom-Up: therefore, will need a special return type i.e, RecAns
            TC: O(N)
            SC: O(N)

"""
import datetime
import math
from collections import deque
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None

class SolutionBruteForce:
    maxDiameter: int = -math.inf
    def _findHeight(self, node: TreeNode):
        # Base Case
        if node is None:
            return 0

        leftHeight = self._findHeight(node.left)
        rightHeight = self._findHeight(node.right)

        return 1 + max(leftHeight, rightHeight)

    def maxDiameterBT(self, root: TreeNode) -> None:
        # Base Case
        if root is None:
            return

        leftHeight = self._findHeight(root.left)
        rightHeight = self._findHeight(root.right)

        self.maxDiameter = max(self.maxDiameter, leftHeight+rightHeight)

        self.maxDiameterBT(root.left)
        self.maxDiameterBT(root.right)

    def maxDiameterTopDown(self, root) -> int:
        # Base Case:
        if root is None:
            return 0

        leftHeight = self.maxDiameterTopDown(root.left)
        rightHeight = self.maxDiameterTopDown(root.right)

        self.maxDiameter = max(self.maxDiameter, leftHeight+rightHeight)

        return max(leftHeight, rightHeight) + 1


@dataclass
class RecursiveAnswer:
    bestDiameter: int = 0
    subTreeHeight: int = 0


class Solution:
    def _diameterBinaryTree(self, root) -> RecursiveAnswer:
        rt = RecursiveAnswer()
        # Base Case
        if root is None:
            return rt

        # Explore Left and Right
        LV = self._diameterBinaryTree(root.left)
        RV = self._diameterBinaryTree(root.right)

        _bestDiameter = max(LV.bestDiameter, RV.bestDiameter, LV.subTreeHeight + RV.subTreeHeight)
        _subTreeHeight = max(LV.subTreeHeight, RV.subTreeHeight) + 1

        rt.bestDiameter = _bestDiameter
        rt.subTreeHeight = _subTreeHeight

        return rt

    def driverFun(self, root):
        finalAns = self._diameterBinaryTree(root)
        return finalAns.bestDiameter


def main():
    node = TreeNode(val=6)

    node.left = TreeNode(val=2)
    node.right = TreeNode(val=3)

    node.left.left = TreeNode(val=1)
    node.left.right = TreeNode(val=4)

    node.right.left = TreeNode(val=5)
    node.right.right = TreeNode(val=2)

    node.left.left.left = TreeNode(val=8)
    node.left.right.left = TreeNode(val=2)
    node.right.left.right = TreeNode(val=3)

    node.left.left.left.left = TreeNode(val=10)
    node.left.left.left.right = TreeNode(val=4)
    node.left.right.left.right = TreeNode(val=5)

    node.left.right.left.right.left = TreeNode(val=12)
    node.left.right.left.right.right = TreeNode(val=2)

    t1 = datetime.datetime.now()
    sol1 = SolutionBruteForce()
    sol1.maxDiameterBT(root=node)
    print(sol1.maxDiameter)
    t2 = datetime.datetime.now()
    print(t2 - t1)

    sol11 = SolutionBruteForce()
    sol11.maxDiameterTopDown(root=node)
    print(sol11.maxDiameter)
    t3 = datetime.datetime.now()
    print(t3 - t2)

    sol = Solution()
    print(sol.driverFun(root=node))
    t4 = datetime.datetime.now()
    print(t4-t3)

main()
