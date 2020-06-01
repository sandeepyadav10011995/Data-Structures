"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.

Example:
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false


"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.queue = []
        self._inorder(root)
    
    def _inorder(self, root):
        if root is None:
            return
        self._inorder(root.left)
        self.queue.append(root.val)
        self._inorder(root.right)
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.queue.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.queue) != 0


# Your BSTIterator object will be instantiated and called as such:
obj = BSTIterator(root)
param_1 = obj.next()
param_2 = obj.hasNext()
