"""
Next larger no in a BST for given no X

Approach 1: Inorder Traversal --> Return the first number greater than X.
            TC: O(N) + O(N)
            SC: O(N)

Approach 2: Optimize 1 using Binary Search
            TC: O(N) + O(logN)
            SC: O(N)

Approach 3: Simple Traversal of BST ---->  Similar to Inorder Successor
            1. Once we find a value which is equal to greater than X
                -> Then keep going left and last left is the Answer
            2. Once we find a value which is equal to smaller than X
                -> Then keep going right and last right is the Answer


            Case 1: If node has right child --> Hence it's successor is somewhere lower in the tree
                ===> Simply : Go Right and Then Left Till we can
            Case 2: If node has no right child -->  Hence it's successor is somewhere upper in the tree
                ===> Simply Do InOrder Traversal on root
"""
from collections import deque
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


class Solution:
    @staticmethod
    def inOrderSuccessor(root: TreeNode, p: TreeNode) -> TreeNode | None:
        # Case 1: Node has a right child: Go right and then left till we can
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p

        # Case 2: Node has no right Child -: Do an InOrder traversal on root
        stack, inOrder = [], p
        while stack or root:
            while root:
                stack.append(root.left)
                root = root.left

            temp = stack.pop()
            if inOrder == temp:
                return inOrder

            inOrder = temp
            if temp.right:
                root = temp.right

        return None
