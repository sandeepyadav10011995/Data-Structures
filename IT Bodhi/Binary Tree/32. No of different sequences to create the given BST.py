"""
Problem -: No of different sequences to create the given BST

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
class RT:
    seqCount: int = None
    length: int = None


class Solution:
    def totalSequencesBST(self, root: TreeNode) -> RT:
        rt = RT()
        # Base Case
        if root is None:
            rt.seqCount = 1
            rt.length = 0
            return rt

        LV = self.totalSequencesBST(root.left)
        RV = self.totalSequencesBST(root.right)

        rt.length = LV.length + RV.length + 1
        # seqCount = Total Pairs * (Fact(LV.length + RV.length))/(Fact(LV.length) * Fact(RV.length))
        rt.seqCount = (LV.seqCount * RV.seqCount) * (
                    (math.factorial(LV.length + RV.length)) / math.factorial(LV.length) * math.factorial(RV.length))

        return rt
