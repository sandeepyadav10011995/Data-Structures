"""
Insert In A BST
    - Find the position where this val can be inserted
    - It will always be a leaf position

TC: O(LogN)
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
    def insertValInBST(root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val=val)

        cur = root
        while True:
            if cur.val <= val:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val=val)
                    break
            else:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val=val)
                    break
        return root
