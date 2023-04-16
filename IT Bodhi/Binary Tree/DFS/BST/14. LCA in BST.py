"""
LCA in Binary Search Tree
Approach 1: Recursive
        TC: O(H) -: H--> Height of the BST
        SC:
"""
from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


class Solution:
    def lowestCommonAncestor(self, root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> TreeNode | None:
        # Base Case
        if root is None:
            return root

        cur = root.val
        if cur > p.val and cur > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if cur < p.val and cur < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root
