"""
Problem : InOrder Successor Of BST

Algorithm:
        1. If Node has Right Child: Hence it's successor is somewhere lower in the tree
        2. If Node Has No Right Child: Hence it's successor is somewhere upper in the tree

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
    def inOrderSuccessor(root, p):
        # Case 1: Node has a Right Child -> Go right and then left till you can
        if p.right:
            p = p.right
            while p.left:
                p = p.left

            return p

        # Case 2: Node has no Right Child -> Then the inorder successor is the nearest ancestor for which the node is
        # in the left subtree.
        inOrderSuccessor = TreeNode()
        while root:
            if p.val < root.val:  # Keep going Left until less
                inOrderSuccessor = root
                root = root.left
            elif p.val > root.val:  # Keep going Right until great
                root = root.right
            else:  #  We have either found the successor or there is no successor at all
                break
        return inOrderSuccessor


sol = Solution()
node = TreeNode(val=20,
                left=TreeNode(val=10,
                              left=TreeNode(val=5),
                              right=TreeNode(val=15)
                              ),
                right=TreeNode(val=30,
                               left=TreeNode(val=25),
                               right=TreeNode(val=35)
                               )
                )

print(sol.inOrderSuccessor(root=node, p=TreeNode(val=10, left=TreeNode(val=5), right=TreeNode(val=15))).val)
print(sol.inOrderSuccessor(root=node, p=TreeNode(val=15)).val)
print(sol.inOrderSuccessor(root=node, p=TreeNode(val=35)).val)