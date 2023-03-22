"""




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
class PathDetails:
    msp: int = -math.inf
    rmp: int = -math.inf


class Solution:
    def getMaxPath(self, root: TreeNode) -> PathDetails:
        rt = PathDetails()
        # Base Case
        if root is None:
            return rt

        # Explore
        LV = self.getMaxPath(root.left)
        RV = self.getMaxPath(root.right)

        if root.left is None:
            CV = root.val + RV.rmp
        elif root.right is None:
            CV = root.val + LV.rmp
        elif LV.rmp > 0 and RV.rmp > 0:
            CV = LV.rmp + RV.rmp + root.val
        else:
            CV = root.val + max(LV.rmp, RV.rmp)

        rt.msp = max(LV.msp, RV.msp, CV)
        rt.rmp = max(LV.rmp, RV.rmp) + root.val if max(LV.rmp, RV.rmp) > 0 else root.val

        return rt
