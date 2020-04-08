"""
Given a binary tree, return the inorder traversal of its nodes' values.
Inorder Traversal --> Left - Root - Right 
Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

"""
# Definition for a binary tree node.
class TreeNode:
   def __init__(self, x):
      self.val = x
      self.left = None
      self.right = None
     

# Recursive Approach
class Solution:
   def inorderTraversal(self, root: TreeNode) -> List[int]:
      output = []
      while root:
         self.inorderTraversal(root.left)
         output.append(root.val)
         self.inorderTraversal(root.right)
      return output
   
   
# Iterative Approach
class Solution:
   def inorderTraversal(self, root: TreeNode) -> List[int]:
      output = []
      stack = []
      while stack or root:
         while root:
            stack.append(root)
            root = root.left
         temp = stack.pop()
         output.append(root.val)
         if temp.right:
            root = temp.right
      return output
   
            
            
         
