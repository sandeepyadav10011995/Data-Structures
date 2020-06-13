"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive Solution
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # Base Case
        if root is None:
            return True
        def helper(p, q):
            # Case 1: Leaf Node.
			if not p and not q:
                return True
			# Case 2: If one of left or right child is not present.
            if not p or not q:
                return False
			# Case 3: If the neighbours values are not equal.
            if p.val != q.val:
                return False
            return helper(p.left, q.right) and helper(p.right, q.left)
        return helper(root.left, root.right)


# Iterative Approach --> BFS
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # Base Case
        if root is None:
            return True
        queue = [(root, root)]
        while queue:
            p, q = queue.pop()
            if not p and not q:
                continue
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            queue.append((p.left, q.right))
            queue.append((p.right, q.left))
        return True
