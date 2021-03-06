"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

"""
# Recursive Approach With Slicing --> i.e. Using Extra Space
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def helper(self, inorder: List[int], postorder[int]) -> TreeNode:
        if inorder == [] or postorder == []:
            return None
        root = TreeNode(postorder[-1])
        idx = inorder.index(root.val)
        root.left = self.helper(inorder[:idx], postorder[:idx])
        root.right = self.helper(inorder[idx+1:], postorder[idx:-1])
        return root
    
    def buildTree(self, inorder: List[int], postorder[int]) -> TreeNode:
        return self.helper(inorder, postorder)
    

# Optimized Recursive Approach --> i.e. No Extra Space
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        def helper(start, end):
            if start > end:
                return None
            root = TreeNode(postorder.pop())
            root.right = helper(idx_map[root.val] + 1, end)
            root.left = helper(start, idx_map[root.val] - 1)
            return root
        return helper(0, len(inorder) - 1)
        
        
        
