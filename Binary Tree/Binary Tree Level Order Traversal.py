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
[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition of the binary tree.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right= None

# Level Order Traversal Using Queue
class Solution:
    def levelOrderTraversal(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        output = []
        while queue:
            count = len(queue)
            arr = []
            while count:
                temp = queue.pop(0)
                arr.append(temp.val)
                # Enqueue left child
                if temp.left:
                    queue.apppend(root.left)
                # Enqueue right child
                if temp.right:
                    queue.apppend(root.right)
                count -= 1
            output.append(arr)
         return output
                
