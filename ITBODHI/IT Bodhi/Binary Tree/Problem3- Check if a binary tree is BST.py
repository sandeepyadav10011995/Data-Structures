"""
Problem : Check if a BT is a BST or not?
"""
import math


class BTTopDownApproach:
    def isValidBSTRecursive(self, root, MIN, MAX):
        # Base Case
        if root is None:
            return True
        # Check BST Condition
        if MIN >= root.val or MAX <= root.val:
            return False

        return self.isValidBSTRecursive(root.left, MIN, root.val) and \
            self.isValidBSTRecursive(root.right, root.val, MAX)

    def isValidBST(self, root):
        MIN = -math.inf
        MAX = math.inf
        return self.isValidBSTRecursive(root, MIN, MAX)


class RT:
    def __init__(self, isBST=False, MIN=math.inf, MAX=-math.inf):
        self.isBST = isBST
        self.MIN = MIN
        self.MAX = MAX


class BTBottomUpApproach:

    def isBST(self, root):
        # Base Case
        if root is None:
            return RT(isBST=True)

        # Explore
        LV = self.isBST(root.left)
        RV = self.isBST(root.right)

        # Check BST Condition
        if LV.isBST and RV.isBST and LV.MAX <= root.val < RV.MIN:
            return RT(isBST=True, MIN=min(LV.MIN, root.val), MAX=max(RV.MAX, root.val))
        else:
            return RT()
