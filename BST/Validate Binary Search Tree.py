"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true


"""




# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # # Recursive Approach
        # # Edge Case
        # if root is None:
        #     return True
        # # Base Case
        # if root.left is None and root.right is None:
        #     return True
        # lh, rh = False, False
        # if root.left and root.val > root.left.val:
        #     lh = self.isValidBST(root.left)
        # if root.right and root.val > root.right.val:
        #     rh = self.isValidBST(root.left) 
        # return lh + rh
        
        def helper(node, lower=float('-inf'), upper=float('inf')):
            # Base Case
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)

