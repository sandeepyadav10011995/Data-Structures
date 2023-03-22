"""
Problem -: First Common Ancestors / Lowest Common Ancestor of node p and q

CASE 1: It's guaranteed that both the nodes exists in Tree


CASE 2: When existence of p and q is not guaranteed.
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
        self.lcaFound = None

    def lcaCase1(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode | None:
        # Base Case
        if root is None:
            return root

        # Case 1: root == p or root == q
        if root.val == p.val or root.val == q.val:
            return root

        # Explore the left and right
        leftAnswer = self.lcaCase1(root.left, p, q)
        rightAnswer = self.lcaCase1(root.right, p, q)

        if leftAnswer is None:
            return rightAnswer
        if rightAnswer is None:
            return leftAnswer

        return root

    def lcaCase2(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode | None:
        # Base Case
        if root is None:
             return root

        # Explore the left and right
        LV = self.lcaCase2(root.left, p, q)
        RV = self.lcaCase2(root.right, p, q)

        # Case 1: When we are not found both the nodes on either sides
        if LV is None and RV is None:
            return root if (root.val == p.val or root.val == q.val) else None

        # Case 2: When we have found both the nodes
        if LV and RV:
            self.lcaFound = True
            return root

        # Case 3: When we have found one node and other node is root node
        if p.val == root.val or q.val == root.val:
            self.lcaFound = True
            return root
        else:
            return LV if LV else RV


"""
TC: O(N)
SC: O(N)
"""
