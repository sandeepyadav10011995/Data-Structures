"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a 
file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another 
computer environment.

Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"


"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # Base Case
        if root is None:
            return "X,"
        leftSerialize = self.serialize(root.left)
        rightSerialize = self.serialize(root.right)
        
        return str(root.val) + "," + leftSerialize + rightSerialize
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(data):
            val = data.pop(0)
            if val == "X": return None
            node = TreeNode(int(val))
            node.left = helper(data)
            node.right = helper(data)
            return node
        
        data = data.split(",")
        return helper(data)
        
        
        


cod = Codec()
cod.deserialize(cod.serialize(root))



