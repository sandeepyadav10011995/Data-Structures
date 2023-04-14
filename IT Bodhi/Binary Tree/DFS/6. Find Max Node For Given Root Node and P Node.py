"""
Problem -: Find the Max Node for the given root node and p node
"""
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


class Solution:
    def getMaxNode(self, root: TreeNode, p: TreeNode) -> TreeNode | None:
        # Base Case
        if root is None:
            return None

        if root == p:  # Return from the Root or P node
            return root

        # Explore Left
        LV = self.getMaxNode(root.left)
        if LV is not None:
            return root if root.val > LV.val else LV
        # Explore Right if p not found in left subtree
        RV = self.getMaxNode(root.right)
        # Case 2: When RV is not None
        if RV is not None:
            return root if root.val > RV.val else RV
        else:
            return None
