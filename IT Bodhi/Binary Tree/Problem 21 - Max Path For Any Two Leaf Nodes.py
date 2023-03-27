"""
Approach 1. Using MaxPath Sum --> Top-Down Approach


Approach 2. Using Bottom-Up Approach

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
    MIN = -math.inf

    @staticmethod
    def _isSingleParent(node) -> bool:
        return (node.left is None and node.right is not None) or (
            node.left is not None and node.right is None
        )

    def _maxPathSum(self, node: TreeNode) -> int:
        # Base Case
        if node is None:
            return 0
        return node.val + max(self._maxPathSum(node.left), self._maxPathSum(node.right))

    def getMaxPath(self, root: TreeNode) -> int:
        # Base Case
        if root is None:
            return 0

        # Find the details at this node
        LV = self._maxPathSum(root.left)
        RV = self._maxPathSum(root.right)

        CV = LV + RV + root.val

        # To avoid Single Parent Issue to be considered as a starting root Node
        if self._isSingleParent(root):
            CV = self.MIN

        # Explore
        LMS = self.getMaxPath(root.left)
        RMS = self.getMaxPath(root.right)

        return max(CV, LMS, RMS)


"""
TC: O(N^2)
SC: O(1)
"""


@dataclass
class PathDetails:
    mps: int = 0  # mps: Max Path Sum
    rtlm: int = 0  # rtlm: Root To Leaf Max Sum


class Solution2:
    MIN = -math.inf

    @staticmethod
    def _isSingleParent(node) -> bool:
        return (node.left is None and node.right is not None) or (
                node.left is not None and node.right is None
        )

    def getMaxPathOptimized(self, root: TreeNode) -> PathDetails:
        rt = PathDetails()
        # Base Case
        if root is None:
            return rt

        # Explore
        LV = self.getMaxPathOptimized(root.left)
        RV = self.getMaxPathOptimized(root.right)

        CV = LV.rtlm + RV.rtlm + root.val
        # To avoid Single Parent Issue
        if self._isSingleParent(root):
            CV = self.MIN

        rt.mps = max(LV.mps, RV.mps, CV)
        rt.rtlm = max(LV.rtlm, RV.rtlm) + root.val

        return rt
