"""
Problem : Root to Leaf Path Sum exists or not ?

Approach 1: Top Down --> Recursive Using DFS

Approach 2: Top Down --> Iterative

"""


class Solution:
    @staticmethod
    def _isLeaf(root) -> bool:
        return root.left is None and root.right is None

    def pathSumRecursive(self, root, targetSum) -> bool:
        # Base Case
        if root is None:
            return False

        # Leaf Node Check
        if self._isLeaf(root) and root.val == targetSum:
            return True

        # Explore Left OR Right
        return self.pathSumRecursive(root.left, targetSum - root.val) or \
            self.pathSumRecursive(root.right, targetSum - root.val)

    def countPathSumRecursive(self, root, targetSum) -> int:
        # Base Case
        if root is None:
            return 0

        # Leaf Node Check
        if self._isLeaf(root) and root.val == targetSum:
            return 1

        # Explore Left OR Right
        return self.pathSumRecursive(root.left, targetSum - root.val) + \
            self.pathSumRecursive(root.right, targetSum - root.val)

    def pathSumIterative(self, root, targetSum) -> bool:
        # Base Case
        if root is None:
            return False

        stack = [(root, targetSum)]
        while stack:
            node, remSum = stack.pop()

            # Leaf Node Check
            if self._isLeaf(node):
                return root.val == remSum

            if node.right:
                stack.append(node.right, remSum - root.val)
            if node.left:
                stack.append(node.left, remSum - root.val)

        return False
