class TreeNode:
    def __init__(self, val):
        self.val =val
        self.left = None
        self.right= None

class Solution:
    def recoverBST(self, root):
        # Inorder Traversal --> sorted Array
        x = y = pred = None
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pred and root.val < pred.val:
                y = root
                if x is None:
                    x = pred
            pred = root
            root = root.right
        x.val, y.val = y.val, x.val


