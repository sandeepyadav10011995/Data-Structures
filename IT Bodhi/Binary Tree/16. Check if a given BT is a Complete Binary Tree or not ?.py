"""
--------------------- Complete Binary Tree --------------------------
Case 1: LH == RH + 1
        Right SubTree should be a Perfect Binary Tree
        Left SubTree should be a Complete Binary Tree

Case 2: LH == RH
        Left SubTree should be a Perfect Binary Tree
        Right SubTree should be a Complete Binary Tree

Approach -: Bottom Up; To hold answer we would need a special Return Type i.e, BTStatus

"""
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


@dataclass
class BTStatus:
    isPBT: bool = False
    isCBT: bool = False
    height: int = 0
    size: int = 0
    node: TreeNode = None


class Solution:
    def maxCBT(self, root: TreeNode) -> BTStatus:
        rt = BTStatus()
        # Base Case
        if root is None:
            rt.isPBT = True
            rt.isCBT = True
            return rt

        # Explore Left and Right
        LV = self.maxCBT(root.left)
        RV = self.maxCBT(root.right)

        #  Case 1: LH == RH + 1 OR Case 2: LH == RH
        if (LV.height == RV.height + 1 and LV.isCBT and RV.isPBT) or \
                (LV.height == RV.height and LV.isPBT and RV.isCBT):
            rt.isCBT = True
            rt.isPBT = (LV.isPBT and RV.isPBT and LV.height == RV.height)
            rt.height = LV.height + 1
            rt.size = LV.size + RV.size + 1
            rt.node = root
        else:
            # Carry Forward the answer
            rt.isCBT = False
            rt.isPBT = False
            rt.height = LV.height + 1
            rt.size = max(LV.size, RV.size)
            rt.node = LV.node if LV.size > RV.size else RV.node

        return rt

