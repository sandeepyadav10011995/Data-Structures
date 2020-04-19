"""
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Recursive Approach
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def helper(p1, p2):
            # Base Cases
            if p1 is None:
                return p2
            if p2 is None:
                return p1
            # Other Cases
            if p1.val <= p2.val:
                p1.next = helper(p1.next, p2)
            else:
                p2.next = helper(p1, p2.next)
        
        return helper(l1, l2)
        
        
        
# Iterative Approach --> Using Dummay Variable Concept
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Edge Cases
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        # Other Cases
        head = ListNode()
        prev = head
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        if l1 is None:
            prev.next = l2
        if l2 is None:
            prev.next = l1
        
        return head.next
