"""
Problem 1: Find the Largest Subtree which is a Perfect Binary Tree

Approach -: Bottom Up; To hold answer we would need a special Return Type i.e,


"""
from dataclasses import dataclass
from typing import Any


class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


@dataclass
class BTStatus:
    isFullBT: bool = False
    node: TreeNode = None
    size: int = 0


class Solution:
    def largestFullSubTree(self, root: TreeNode) -> BTStatus:
        rt = BTStatus()
        # Base Case
        if root is None:
            rt.isFullBT = True
            return rt

        # Explore Left and Right
        LV = self.largestFullSubTree(root.left)
        RV = self.largestFullSubTree(root.right)

        # Case 1: Both and Right are FullTree and size are also equal
        if LV.isFullBT and RV.isFullBT and LV.size == RV.size:
            rt.isFullBT = True
            rt.node = root
            rt.size = 2 * LV.size + 1
        else:
            # Carry forward the answer
            rt.size = max(LV.size, RV.size)
            rt.node = LV.node if LV.size > RV.size else RV.node

        return rt


"""
TC: O(N)
SC: O(N) --> Call Stack
"""
