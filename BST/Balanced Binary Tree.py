"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
A binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:
Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(root):
            if root is None:
                return True, -1
            lbalanced, lh = helper(root.left)
            if not lbalanced:
                return False, 0
            rbalanced, rh = helper(root.right)
            if not rbalanced:
                return False, 0
            # Final Balance Check Check
            balance_check = abs(lh-rh) < 2
            return balance_check, 1+max(lh, rh)
        return helper(root)[0]
