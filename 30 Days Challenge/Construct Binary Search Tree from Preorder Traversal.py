"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  
Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

Example 1:
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

"""

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(arr):
            # Base Case
            if len(arr) == 0:
                return None
            
            # Other Cases
            root = TreeNode(arr.pop(0))
            left_arr = [i for i in arr if i < root.val]
            right_arr = [i for i in arr if i > root.val]
            root.left = helper(left_arr)
            root.right = helper(right_arr)
            
            return root
        return helper(preorder)
