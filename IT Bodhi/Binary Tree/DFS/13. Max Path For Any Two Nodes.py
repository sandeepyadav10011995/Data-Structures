"""
Approach 1: Brute Force -: Try it on Every Node
            TC: O(N^2)
            SC: O(N)

Approach 2: Top Down --> Update the globalValue and return the localValue
            TC: O(N)
            SC: O(N)

Approach 3: Bottom Up Approach -:  therefore, will need a special return type i.e, PathDetails
            TC: O(N)
            SC: O(N)

"""
import math
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None

class SolutionBruteForce:
    MIN = -math.inf
    maxPath = -math.inf

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

        # Explore
        LMS = self.getMaxPath(root.left)
        RMS = self.getMaxPath(root.right)

        return max(CV, LMS, RMS)

    def getMaxPathTopDown(self, root: TreeNode) -> int:  # TC: O(N)
        # Base Case
        if root is None:
            return 0

        leftSum = max(self.getMaxPathTopDown(root.left), 0)
        rightSum = max(self.getMaxPathTopDown(root.right), 0)

        maxAtNode = root.val + leftSum + rightSum
        self.maxPath = max(self.maxPath, maxAtNode)

        return max(leftSum, rightSum) + root.val


@dataclass
class PathDetails:
    msp: int = -math.inf  # Max Sum Path
    rmp: int = -math.inf  # Root Max Path


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
