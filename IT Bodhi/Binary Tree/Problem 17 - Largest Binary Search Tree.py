"""
Problem -: Largest Binary Search Tree

Approach -: Bottom Up; To hold answer we would need a special Return Type i.e,  BTStatus

"""
import math
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


@dataclass
class BTStatus:
    isBST: bool = False
    MIN: int = math.inf
    MAX: int = -math.inf
    size: int = 0
    node: TreeNode = None


class Solution:
    def largestBST(self, root: TreeNode) -> BTStatus:
        rt = BTStatus()
        # Base Case
        if root is None:
            rt.isBST = True
            return rt

        # Explore Left and Right
        LV = self.largestBST(root.left)
        RV = self.largestBST(root.right)

        # Case 1: Both Left and Right are BST
        if LV.isBST and RV.isBST and LV.MAX <= root.val <= RV.MIN:
            rt.isBST = True
            rt.MIN = min(LV.MIN, root.val)
            rt.MAX = max(RV.MAX, root.val)
            rt.size = LV.size + RV.size + 1
            rt.node = root
        else:
            # Carry Forward the answer
            rt.isBST = False
            rt.size = max(LV.size, RV.size)
            rt.node = LV.node if LV.size > RV.size else RV.node

        return rt
