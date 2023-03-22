"""
Problem : Binary Tree Maximum Path Sum

"""
import math


class Solution:
    gmax = -math.inf

    def _getMaxPath(self, node):
        # Base Case
        if node is None:
            return 0

        leftMax = max(self._getMaxPath(node.left), 0)
        rightMax = max(self._getMaxPath(node.right), 0)

        maxAtNode = node.val + leftMax + rightMax
        self.gmax = max(self.gmax, maxAtNode)

        return max(leftMax, rightMax) + node.val

    def maxPathSum(self, root):
        self._getMaxPath(root)
        return self.gmax
