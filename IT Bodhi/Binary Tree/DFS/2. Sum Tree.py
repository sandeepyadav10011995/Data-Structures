"""
Problem : Sum Tree:: Root Value = Sum Of the left and right subtree
"""


class SumTree:
    def __init__(self, sum: int = 0, isSumT: bool = False):
        self.sum = sum
        self.isSumT = isSumT


class BTBottomUpApproach:
    @staticmethod
    def isLeaf(node):
        return node.left is None and node.right is None

    def isSumTree(self, root):
        # Base Case
        if root is None:
            return SumTree(0, True)
        # Leaf Condition Check
        if self.isLeaf(root):
            return SumTree(root.val, True)

        # Explore
        LV = self.isSumTree(root.left)
        RV = self.isSumTree(root.right)

        if LV.isSumT and RV.isSumT and (LV.sum + RV.sum == root.val):
            return SumTree(2 * root.val, True)
        else:
            return SumTree()


class BTTopDownApproach:
    @staticmethod
    def isLeaf(node):
        return node.left is None and node.right is None

    def isSumTree(self, root):
        # Base Case
        if root is None:
            return True
        # Leaf Condition Check
        if self.isLeaf(root):
            return True
        LV = root.left.val if self.isLeaf(root.left) else 2 * root.left.val
        RV = root.right.val if self.isLeaf(root.right) else 2 * root.right.val

        # Explore
        if LV + RV == root.val:
            return self.isSumTree(root.left) and self.isSumTree(root.right)
        return False
