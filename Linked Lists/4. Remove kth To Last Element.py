"""
Remove kth To Last Element
Given a linked list, remove the k'th to last element, and return the head of the new linked list.

Example 1:
Input:
k = 2
1 -> 2 -> 5 -> 6 -> 7 -> X

Output: 1 -> 2 -> 5 -> 7 -> X

Explanation: Element 6 is the 2nd to last element, therefore removed.

Example 2:
Input:
k = 1
2 -> 3 -> 5 -> X

Output: 2 -> 3 -> X

Constraints:
1 <= k <= linked list size
"""
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class Solution:
    def removeKthFromLast(self, head, k): # Approach : Two Pointers
        dummy_head = Node(-1) # Reason : First Node needs to be removed --> To handle that edge case
        dummy_head.next = head

        left = dummy_head
        right = dummy_head.next
        # Create a k-size window between left and right pointer
        while k > 0:
            right = right.next
            k -= 1

        while right is not None:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy_head.next
