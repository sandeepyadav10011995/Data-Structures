"""
Given a binary tree :
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Follow up:
You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.


"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
# Iterative Approach
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # Iterative Approach
        if root is None:
            return root
        queue = [root]
        while queue:
            count = len(queue)
            while count:
                node = queue.pop(0)
                if count != 1:
                    node.next = queue[0]
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                count -= 1
        return root
	
	
