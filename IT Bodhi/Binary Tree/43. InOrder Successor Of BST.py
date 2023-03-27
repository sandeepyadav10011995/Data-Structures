"""
Problem : InOrder Successor Of BST

Algorithm:
        1. If Node has Right Child: Hence it's successor is somewhere lower in the tree
        2. If Node Has No Right Child: Hence it's successor is somewhere upper in the tree

"""


class Solution:
    @staticmethod
    def inOrderSuccessor(root, p):
        # Case 1: Node has a Right Child -> Go right and then left till you can
        if p.right:
            p = p.right
            while p.left:
                p = p.left

            return p.val

        # Case 2: Node has no Right Child -> Do InOrder Traversal on root
        stack = []
        inOrderSuccessor = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            # Logic: If the prev node was equal to p then current node will be its successor.
            node = stack.pop()
            if inOrderSuccessor == node.val:
                return node.val

            inOrderSuccessor = node.val
            root = node.right

        return None  # There is no successor

