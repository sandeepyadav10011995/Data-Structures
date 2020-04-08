"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]

"""

# Definition for a binary tree node.
class TreeNode:
   def __init__(self, x):
      self.val = x
      self.left = None
      self.right = None

# Recursive Approach 
class Solution:
   def postorderTraversal(self, root: TreeNode) -> List[int]:
      output = []
      while root:
         self.postorderTraversal(root.left)
         self.postorderTraversal(root.right)
         output.append(root.val)
      return output
   
# Iterative Approach
class Solution:
   def postorderTraversal(self, root: TreeNode) -> List[int]:
      stack_1 = [root]
      stack_2 = []
      while stack_1:
         root = stack_1.pop()
         stack_2.append(root.val)
         if root.right:
            stack_1.append(root.right)
         if root.left:
            stack_1.append(root.left)
      
      output = []
      while stack_2:
         output.append(stack_2.pop())
      return output
   
 
