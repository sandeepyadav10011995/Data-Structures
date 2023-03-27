"""




"""
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


class Solution:
    def _printAtkDistance(self, node: TreeNode, K: int) -> None:
        # Base Cases
        if node is None:
            return
        if K == 0:
            print(node.val)
            return

        # Explore
        self._printAtkDistance(node.left, K-1)
        self._printAtkDistance(node.right, K - 1)

    def allNodesAtKDistance(self, root: TreeNode, K: int, p: TreeNode) -> int:
        # Base Cases
        if root is None:
            return -1

        if root == p:
            print(root.val)
            return 1

        LV = self.allNodesAtKDistance(root.left, K, p)
        if LV > 0:
            if LV > K:
                return LV
            if LV == K:
                print(root.val)
                return LV+1
            self._printAtkDistance(root.right, K-LV-1)
            return LV+1

        RV = self.allNodesAtKDistance(root.right, K, p)
        if RV > 0:
            if RV > K:
                return RV
            if RV == K:
                print(root.val)
                return RV+1
            self._printAtkDistance(root.left, K-RV-1)
            return RV+1

        return -1
