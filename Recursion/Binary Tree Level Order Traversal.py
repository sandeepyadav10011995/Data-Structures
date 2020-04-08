"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
Output = 
[
  [3],
  [9,20],
  [15,7]
]

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Level Order Using BFS
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        output = []
        queue = [root]
        while queue:
            root = queue[0]
            output.append(root.val)
            if root.right:
                queue.append(root.right)
            if root.left:
                queue.append(root.left)
        return output
    
        
    
    
    


