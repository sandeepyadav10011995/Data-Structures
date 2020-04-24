"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Example :
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

Output :
    3
   / \
  9  20
    /  \
   15   7
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        def helper(start, end):
            if start > end:
                return None
            root = TreeNode(preorder.pop(0))
            root.left = helper(start, idx_map[root.val] - 1)
            root.right = helper(idx_map[root.val] + 1, end)
            
            return root
        
        return helper(0, len(inorder) - 1)
