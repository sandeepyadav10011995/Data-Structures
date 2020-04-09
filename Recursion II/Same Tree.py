"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]
Output: true

"""
# Definition of the binary tree.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
# Recursive Approach
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
# Iterative Approach
from collections import deque
class Solution:
    def check(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return True

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if root is None:
            return True
        # Using Queue
        queue = deque([(p, q)])
        while queue:
            p, q = queue.popleft()
            if not self.check(p, q):
                return False
            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
        return True

