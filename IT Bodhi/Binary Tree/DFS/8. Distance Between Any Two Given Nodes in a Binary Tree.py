"""
Problem -: Distance b/w any two given nodes in a binary tree.

"""
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


class Solution:
    def __init__(self):
        self.hasFound = None

    def getDistanceWithProblem(self, root: TreeNode, p: TreeNode, q: TreeNode) -> int:
        # Base Case
        if root is None:
            return -1

        # Explore Left and Right
        LV = self.getDistanceWithProblem(root.left)
        RV = self.getDistanceWithProblem(root.right)

        # Case 1: We have not found both the nodes
        if LV < 0 and RV < 0:
            return 1 if (root == p or root == q) else -1

        # Case 2: We have found both the nodes
        if LV > 0 and RV > 0:
            return LV + RV

        if root == p or root == q:
            return LV if LV > 0 else RV
        else:
            return LV + 1 if LV > 0 else RV + 1

        # Problem: The answer is correct, but we are not able to hold the answer

    def getDistance(self, root: TreeNode, p: TreeNode, q: TreeNode) -> int:
        # Base Case
        if root is None:
            return -1

        # Explore Left and Right
        LV = self.getDistance(root.left)
        RV = self.getDistance(root.right)

        # Case 1: We have not found both the nodes
        if LV < 0 and RV < 0:
            return 1 if (root == p or root == q) else -1

        # Case 2: We have found both the nodes
        if LV > 0 and RV > 0:
            self.hasFound = True
            return LV + RV

        if root == p or root == q:
            self.hasFound = True
            return LV if LV > 0 else RV
        else:
            if self.hasFound:
                return LV if LV > 0 else RV
            else:
                return LV + 1 if LV > 0 else RV + 1

