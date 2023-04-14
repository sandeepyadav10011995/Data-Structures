"""
Problem : Binary Tree Diameter

Approach : Bottom-Up: therefore, will need a special return type i.e, RecAns

"""
from collections import deque
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


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
        _subTreeHeight = max(LV.subTreeHeight, RV.subTreeHeight) + 1

        rt.bestDiameter = _bestDiameter
        rt.subTreeHeight = _subTreeHeight

        return rt

    def driverFun(self, root):
        finalAns = self._diameterBinaryTree(root)
        return finalAns.bestDiameter


def main():
    node = TreeNode(val=6)

    node.left = TreeNode(val=2)
    node.right = TreeNode(val=3)

    node.left.left = TreeNode(val=1)
    node.left.right = TreeNode(val=4)

    node.right.left = TreeNode(val=5)
    node.right.right = TreeNode(val=2)

    node.left.left.left = TreeNode(val=8)
    node.left.right.left = TreeNode(val=2)
    node.right.left.right = TreeNode(val=3)

    node.left.left.left.left = TreeNode(val=10)
    node.left.left.left.right = TreeNode(val=4)
    node.left.right.left.right = TreeNode(val=5)

    node.left.right.left.right.left = TreeNode(val=12)
    node.left.right.left.right.right = TreeNode(val=2)

    sol = Solution()
    print(sol.driverFun(root=node))

main()
