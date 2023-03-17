"""
Problem 1: Max Of A Binary Tree
"""
import math


class BT11:
    MIN = -math.inf

    def getMax(self, root):
        # Base Case
        if root is None:
            return self.MIN
        return max(self.getMax(root.left), self.getMax(root.right), root.val)


"""
Optimization -: Leaf Node Check
"""


class BT12:
    MIN = -math.inf

    def getMax(self, root):
        # Base Case
        if root is None:
            return self.MIN
        isLeaf = root.left is None and root.right is None
        if isLeaf:
            return root.val

        return max(self.getMax(root.left), self.getMax(root.right))


"""
Problem 2: Max Of A Single Parent In Binary Tree
"""


class BT2:
    MIN = -math.inf

    @staticmethod
    def _isSingleParent(node):
        return (node.left is None and node.right is not None) or (
            node.left is not None and node.right is None
        )

    def getMaxSingleParent(self, root):
        # Base Case
        if root is None:
            return self.MIN
        val = self.MIN
        # Single Parent Condition
        if self._isSingleParent(root):
            val = root.val

        return max(self.getMaxSingleParent(root.left),
                   self.getMaxSingleParent(root.right),
                   val)
