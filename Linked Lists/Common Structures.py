# Graph Vertex
class GraphVertex:
    def __init__(self, val):
        self.val = val
        self.adjacents = []  # A list of adjacent GraphVertex's

# Singly Linked List Node
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None  # Points to another ListNode object

# Random List Node
class RandomListNode:
    def __init__(self, val):
        self.val = val
        self.next = None  # Points to another RandomListNode object
        self.random = None  # Points to another RandomListNode object

# Binary Tree Node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None  # Points to another TreeNode object
        self.right = None  # Points to another TreeNode object

# Doubly Linked List Node
class DLLNode:
    def __init__(self, val):
        self.val = val
        self.next = None  # Points to another DLLNode object
        self.prev = None  # Points to another DLLNode object

# Linked Binary Tree Node
class LinkedTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None  # Points to another LinkedTreeNode object
        self.right = None  # Points to another LinkedTreeNode object
        self.next = None  # Points to another LinkedTreeNode object
