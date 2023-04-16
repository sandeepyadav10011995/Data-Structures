"""
Delete In A BST
    - Search the key to be deleted
    - Delete it by attaching the rightChild to the right of rightMost child of left Child.

TC: O(H) -: H--> Height of the Tree/
SC: O(H)
"""
from dataclasses import dataclass
from typing import Any

@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


class Solution:
    def _findLastRight(self, node: TreeNode) -> TreeNode:
        if node.right is None:
            return node
        else:
            return self._findLastRight(node.right)

    def _helper(self, node: TreeNode) -> TreeNode:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            rightChild = node.right
            lastRight = self._findLastRight(node.left)
            lastRight.right = rightChild
            return node.left


    def deleteNode(self, root: TreeNode, key: int) -> TreeNode | None:
        # Base Case
        if root is None:
            return root

        if root.val == key:
            return self._helper(root)

        dummy = root
        while root:
            if root.val > key:
                if root.left and root.left == key:
                    root.left = self._helper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right and root.right == key:
                    root.right = self._helper(root.right)
                    break
                else:
                    root = root.right

        return dummy
