"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

"""
# Definition of the binary tree.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursive Approach -- O(N^2)
class Solution:
    def getHeight(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        return max(left_height, right_height) + 1
        
    def diameterBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        # Left Diameter
        diaL = self.diameterBinaryTree(root.left)
        # Right Diameter
        diaR = self.diameterBinaryTree(root.right)
        # Get the left and right height for the node
        lg, rh = 0, 0
        if root.left:
            lh = self.getHeight(root.left)
        if root.right:
            rh = self.getHeight(root.right)
        return max(diaL, diaR, lh+rh)

# Opimized Recursive Approach --> O(N)
class Solution:
    diameter = 0
    def helper(self, root: TreeNode) -> int:
        if root is None:
            return 0
        # Left Side
        lh = self.helper(root.left)
        rh = self.helper(root.right)
        Solution.diameter = max(Solution.diameter, lh+rh)
        return max(lh, rh) + 1
    
    def diameterBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.helper(root)
        return Solution.diameter
        
          
