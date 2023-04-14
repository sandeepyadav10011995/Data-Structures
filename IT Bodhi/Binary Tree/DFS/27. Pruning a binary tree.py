"""
Problem : Pruning a binary tree
How to avoid dangling pointer or memory wastage while pruning the tree?
deleteBT(root: Node):
    deleteBT(root.left)
    deleteBT(root.right)
    free(root)

This will make sure that all the children nodes are deleted first before deleting parent node;
As deleting the root node first --> Will lead to the condition of inaccessible of the child nodes

Variant 1: Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree
so that all its elements lies in [low, high].
Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any
node's descendant should remain a descendant).
It can be proven that there is a unique answer.
Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.


Variant 2: Prune all remaining nodes if path_sum is greater than K from root to nodes

"""
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


class Solution:
    def _trimBST(self, node, low, high):
        # Base Case
        if node is None:
            return None

        elif node.val < low:
            # Free the left nodes
            return self._trimBST(node.right, low, high)
        elif node.val > high:
            # Free the right nodes
            return self._trimBST(node.left, low, high)
        else:
            node.left = self._trimBST(node.left, low, high)
            node.right = self._trimBST(node.right, low, high)
            return node

    def driverTrim(self, root, low, high):
        return self._trimBST(root, low, high)


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

print(sol.driverTrim(root=node, low=6, high=34))

