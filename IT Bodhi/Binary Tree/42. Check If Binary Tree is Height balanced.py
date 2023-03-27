"""
Problem : Check if a Binary Tree is Height Balanced or not?

"""
from dataclasses import dataclass


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
