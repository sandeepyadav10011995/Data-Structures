"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between 
two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
		
		
# Recusive Approach
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base Case
        if root is None:
            return root
        if root.val == p.val or root.val == q.val:
            return root
        
        leftSearchResult = self.lowestCommonAncestor(root.left, p, q)
        rightSearchResult = self.lowestCommonAncestor(root.right, p, q)
        
        # Check the results
        if leftSearchResult is None: return rightSearchResult
        if rightSearchResult is None: return leftSearchResult
        
        return root
			
