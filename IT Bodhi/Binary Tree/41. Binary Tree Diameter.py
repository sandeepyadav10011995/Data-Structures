"""
Problem : Binary Tree Diameter

Approach : Bottom-Up; therfore will need a special return type i.e, RecAns

"""
from dataclasses import dataclass


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
        _subTreeHeight = max(LV.subTreeHeight, RV.subTreeHeight)

        rt.bestDiameter = _bestDiameter
        rt.subTreeHeight = _subTreeHeight

        return rt

    def driverFun(self, root):
        finalAns = self._diameterBinaryTree(root)
        return finalAns.bestDiameter
