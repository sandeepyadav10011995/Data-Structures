import sys

class Solution:
    def isValidBSTRecursive(self, node: TreeNode, min, max): # Recursive Approach
        if min >= node.val or max <= node.val:
            return False

        return self.isValidBST(node.left, min, node.val) and self.isValidBST(nodr.right, node.val, max)

    def isValidBSTBFS(self, root): # Iterative Approach
        max = sys.maxsize
        min = -sys.maxsize - 1
        queue = [AugmentedTreeNode(root, min, max)]
        while queue:
            augmented_node = queue.pop()
            if augmented_node:
                node_value = augmented_node.node.val
                if node_value <= augmented_node.min or node_value >= augmented_node.max:
                    return False

                queue.append(AugmentedTreeNode(augmented_node.left, augmented_node.min, node_value))
                queue.append(AugmentedTreeNode(augmented_node.left, node_value, augmented_node.max))
        return True

# Ques. Why BFS why not DFS.
# Ans. BFS will be able to catch the error more faster --> Asymptotically faster

    def isValidBST(self, root: TreeNode):
        # Recursive Approach
        # max = sys.maxsize
        # min = -sys.maxsize - 1
        # return self.isValidBSTRecursive(root, min, max)

        # Iterative Approach
        return self.isValidBSTBFS(root)

class AugmentedTreeNode:
    def __init__(self, node, min, max):
        self.node = node
        self.min = min
        self.max = max

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None  # Points to another TreeNode object
        self.right = None  # Points to another TreeNode object
