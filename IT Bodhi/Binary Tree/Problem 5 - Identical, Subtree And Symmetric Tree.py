"""
Problem: Find if two tree are Identical or not?
"""


class Solution1:
    def isIdentical(self, p, q):
        # 3 Base Cases - 3 Golden Rules
        if p is None and q is None: return True
        if p is None or q is None: return False
        if p.val != q.val: return False

        return self.isIdentical(p.left, q.left) and self.isIdentical(p.right, q.right)


"""
Problem: Find if p is a subTree of q or not?
"""


class Solution2:
    def isSubtree(self, p, q):
        # 3 Base Cases - 3 Golden Rules
        if p is None and q is None: return True
        if p is None and q is not None: return True
        if p is not None and q is None: return False

        return self.isIdentical(p, q) or self.isSubtree(p, q.left) or self.isSubtree(p, q.right)

    def isIdentical(self, p, q):
        # 3 Base Cases - 3 Golden Rules
        if p is None and q is None: return True
        if p is None or q is None: return False
        if p.val != q.val: return False

        return self.isIdentical(p.left, q.left) and self.isIdentical(p.right, q.right)


"""
Problem: Find if tree is Symmetric Tree or not?
"""


class Solution3:
    def isSymmetric(self, root) -> bool:
        # Base Case
        if root is None:
            return True
        return self.isUtil(root.left, root.right)

    def isSymmetricUtil(self, p, q) -> bool:  # Helper or Util Method
        # 3 Base Cases - 3 Golden Rules
        if p is None and q is None: return True
        if p is None or q is None: return False
        if p.val != q.val: return False

        return self.isSymmetricUtil(p.left, q.right) and self.isSymmetricUtil(p.right, q.left)

    @staticmethod
    def isSymmetricIterative(root) -> bool:  # Iterative Approach : Using BFS Approach
        # Base Case
        if root is None:
            return True
        levelOrderQueue = [(root.left, root.right)]

        while levelOrderQueue:
            p, q = levelOrderQueue.pop(0)
            # 3 Base Cases - 3 Golden Rules
            if p is None and q is None: continue
            if p is None or q is None: return False
            if p.val != q.val: return False

            levelOrderQueue.append((p.left, q.right))
            levelOrderQueue.append((p.right, q.left))
        return True
