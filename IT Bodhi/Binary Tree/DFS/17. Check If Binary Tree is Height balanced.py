"""
Problem : Check if a Binary Tree is Height Balanced or not?

Approach 1: BruteForce : Check On Every Node
            TC: O(N^2)
            SC: O(N)

Approach 2: Optimized Approach -> Remember the answer while going up --> Bottom Up Approach
            TC: O(N)
            SC: O(N)

"""
from collections import deque
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


class SolutionBruteForce:
    def _findHeight(self, node):
        # Base Case
        if node is None:
            return 0

        leftHeight = self._findHeight(node.left)
        rightHeight = self._findHeight(node.right)

        return 1 + max(leftHeight, rightHeight)


    def checkForNode(self, node: TreeNode) -> bool:
        # Base Case
        if node is None:
            return True

        leftHeight = self._findHeight(node.left)
        rightHeight = self._findHeight(node.right)

        if abs(leftHeight-rightHeight) > 1:
            return False

        left = self.checkForNode(node.left)
        right = self.checkForNode(node.right)

        if not left or not right:
            return False

        return True


@dataclass
class BalancedStatusWithHeight:
    isBalanced: bool = False
    height: int = 0


class Solution:
    def _checkBalanced(self, node):
        rt = BalancedStatusWithHeight()
        # Base Case
        if node is None:
            rt.isBalanced = True
            return rt

        # Explore Left
        LV = self._checkBalanced(node.left)
        if not LV.isBalanced:
            return LV

        # Explore Right
        RV = self._checkBalanced(node.right)
        if not RV.isBalanced:
            return RV

        subTreeIsBalanced = abs(LV.height - RV.height) <= 1
        subTreeHeight = max(LV.height, RV.height) + 1

        rt.isBalanced = subTreeIsBalanced
        rt.height = subTreeHeight

        return rt

    def driver(self, root: TreeNode):
        return self._checkBalanced(root).isBalanced
