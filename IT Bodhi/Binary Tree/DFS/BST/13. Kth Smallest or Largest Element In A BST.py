"""
K-th Smallest/Largest Element in BST

Approach 1: Brute Force
            Any Traversal other than Inorder and store it in an array
            Sort the array and return Kth element from it
            TC: O(N) + O(NlogN) ~ O(NlogN)
            SC: O(N) -> Array
Approach 2: Inorder Traversal --> Making use of BST property
            Inorder--> Store it in an array
            Return Kth element from it
            TC: O(N)
            SC: O(N) --> Array
Approach 3: Return the val during traversal only.
            Using counter we can keep a counter
            Recursive and Iterative
            TC: O(N)
            SC: O(N) --> Call Stack

            Morris Traversal
            TC: O(N)
            SC: O(1)

Logic for the Kth Largest
With One Traversal --> We can get the total number of nodes  -> N
Then just convert this question into N-Kth smallest element in a BST --> Simple

"""
from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


class Solution:
    count = 0
    def kthSmallestElementBST(self, root: Optional[TreeNode], k: int) -> TreeNode | None:
        if root is None:
            return root

        LV = self.kthSmallestElementBST(root.left, k)
        if LV:
            return LV
        k -= 1
        if k == 0:
            return root

        return self.kthSmallestElementBST(root.right, k)
