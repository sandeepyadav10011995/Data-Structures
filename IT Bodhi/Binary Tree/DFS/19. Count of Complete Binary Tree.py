"""
Formula for total nodes = 2^height - 1 -: IF we are given Complete Binary Tree

TC: O(LogN)^2 --> O(N)
SC: O(logN) --> Call Stack
"""
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


class Solution:
    @staticmethod
    def _getLeftHeight(node: TreeNode) -> int:
        count = 0
        while node.left:
            count += 1
            node = node.left

        return count

    @staticmethod
    def _getRightHeight(node: TreeNode) -> int:
        count = 1
        while node.right:
            count += 1
            node = node.right

        return count

    def countCompleteBTNodes(self, root: TreeNode) -> int:
        # Base Case
        if root is None:
            return 0

        leftHeight = self._getLeftHeight(root)
        rightHeight = self._getRightHeight(root)

        if leftHeight == rightHeight:
            return 2>>leftHeight - 1  # math.pow(2, leftHeight) - 1
        else:
            return 1 + self.countCompleteBTNodes(root.left) + self.countCompleteBTNodes(root.right)

"""
TC: O(N)
SC: O(N) --> Call Stack
"""
@dataclass
class Answer:
    count: int = 0
    height: int = 0
    isCBT: bool = False


class SolutionBottomUp:  # Works well for normal BT also!!
    def countCompleteBTNodes(self, root) -> Answer:
        rt = Answer()
        # Base Case
        if root is None:
            rt.isCBT = True
            return rt

        LV = self.countCompleteBTNodes(root.left)
        RV = self.countCompleteBTNodes(root.right)

        if LV.isCBT and RV.isCBT and abs(LV.height-RV.height) <= 1:
            rt.isCBT = True
            rt.count = LV.count + RV.count + 1
            rt.height = max(LV.height, RV.height) + 1
        else:
            # Carry Forward the Answer
            rt.count = LV.count + RV.count
            rt.height = max(LV.height, RV.height) + 1

        return rt
