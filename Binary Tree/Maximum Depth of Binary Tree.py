"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.
Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
   
Ans = 3
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
		
# Recursive Approach --> Bottom-Up Approach
class Solution:
	def maxDepth(self, root: TreeNode) -> int:
        # Base Case
        if root is None:
            return 0
        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)
        return max(lh, rh) + 1
	
	
# Recursive Approach --> Top-Down Approach
class Solution:
	def maxDepth(self, root: TreeNode) -> int:
		def helper(root, depth):
			nonlocal answer
			# Base Case
			if root is None:
				return
			# If node is a leaf node
			if root.left is None and root.right is None:
				answer = max(answer, depth)
			helper(root.left, depth+1)
			helper(root.right, depth+1)
		answer = 0
		helper(root, 1)
		return answer
	
