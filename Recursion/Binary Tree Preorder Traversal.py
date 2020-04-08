"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]

Notice : Do it both Recursively and Iteratively.

"""
# Definition for a binary tree node.
clas TreeNode:
   def __init__(self, x):
      self.val = x
      self.left = None
      self.right = None

# Recursive Approach
class Solution:
   def preorderTraversal(self, root: TreeNode) -> List[int]:
      output = []
      while root:
         output.append(root)
         self.preorderTraversal(root.left)
         self.preorderTraversal(root.right)
      return output

   
# Iterative Approach
class Solution:
   def preorderTraversal(self, root: TreeNode) -> List[int]:
      output = []
      stack = [root]
      while stack:
         root = stack.pop()
         output.append(root.val)
         if root.right:
            stack.append(root.right)
         if root.left:
            stack.append(root.left)
     return output
    
         
         
         
         
         
