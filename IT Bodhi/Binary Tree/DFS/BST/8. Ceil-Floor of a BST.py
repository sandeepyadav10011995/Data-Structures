"""
Ceil in a BST?

Ceil -: key is present then return key else return it's successor
If not present return -1

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
    def ceilBST(root: TreeNode, key: int) -> int:
        ceil = -1
        while root:
            if root.val == key:
                return root.val

            if key > root.val:
                root = root.right
            else:
                ceil = root.val
                root = root.left

        return ceil

    @staticmethod
    def floorBST(root: TreeNode, key: int) -> int:
        floor = -1
        while root:
            if root.val == key:
                return root.val

            if key > root.val:
                floor = root.val
                root = root.right
            else:
                root = root.left

        return floor