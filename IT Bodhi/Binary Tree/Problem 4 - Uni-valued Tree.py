"""
Uni-valued Tree -: A BT is uni-valued if every node in the tree has the same value. Return True if and only if the given
                   tree is uni-valued.
"""


class Solution:
    def isUnivalTree(self, root):
        # Base Case
        if root is None:
            return True
        return self.isUtil(root, root.val)

    def isUtil(self, root, val):
        # Base Case
        if root is None: return True
        if root.val != val: return False

        return self.isUtil(root.left, val) and self.isUtil(root.right, val)


"""
Follow Up : Count the no. of Unival Trees
"""


class Solution2:
    def countUnival(self, root):
        isUnival = self.isUnivalTree(root)
        return self.countUnival(root.left) + self.countUnival(root.right) + (1 if isUnival else 0)

    def isUnivalTree(self, root):
        # Base Case
        if root is None:
            return True
        return self.isUtil(root, root.val)

    def isUtil(self, root, val):
        # Base Case
        if root is None: return True
        if root.val != val: return False

        return self.isUtil(root.left, val) and self.isUtil(root.right, val)
