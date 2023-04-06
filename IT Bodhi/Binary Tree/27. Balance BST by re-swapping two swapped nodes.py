"""
Balance BST by re-swapping two swapped nodes. These two nodes can be any two nodes.

Solution 1: Inorder Traversal --> We will get two values which are swap them.
            => 15 and 25 is Swapped
            8, 10, 12, 25, 18, 20, 21, 15, 28, 30, 36, 40, 55
                            |           |
            We will find out the two values where the value is less than the prev value
            Important Points while finding out the two swapped nodes -:
                Exception 1: Found at node 18, therefore First node would be previous node = 25
                Exception 2: Found at node 15, therefore Second node would be current node = 15

            Note : There is one Edge Case where this will not work, when we swap two consecutive values.
            Example --> 15 and 12 is Swapped
            8, 10, 15, 12, 18, 20, 21, 25, 28, 30, 36, 40, 55

            Exception : Found at node 12, therefore in consecutive swaps we will get only ONE EXCEPTION.
            Therefore;
                    First Node --> Previous Node = 15
                    Second Node --> Current Node = 12

            And then create a Balanced BST from the sorted inorder.
"""
import math
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


@dataclass
class SwapPair:
    prev: TreeNode = None
    first: TreeNode = None
    last: TreeNode = None


class Solution:
    def _inOrder(self, root: TreeNode, sp: SwapPair) -> None:
        if root is None:
            return
        self._inOrder(root.left, sp)
        if sp.prev and root.val < sp.prev.val:
            if sp.first is None:
                sp.first = sp.prev
            sp.last = root
        sp.prev = root
        self._inOrder(root.right, sp)

    def recoverBST(self, root: TreeNode) -> None:
        sp = SwapPair()
        sp.prev = TreeNode(val=-math.inf)
        self._inOrder(root, sp)

        if sp.first and sp.last:
            sp.first.val, sp.last.val = sp.last.val, sp.first.val



sol = Solution()
root1 = TreeNode(val=2, left=TreeNode(val=1), right=TreeNode(val=3, left=TreeNode(val=4)))
sol.recoverBST(root=root1)
print(root1)
