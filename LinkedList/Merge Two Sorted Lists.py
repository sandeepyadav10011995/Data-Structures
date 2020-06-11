"""
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # # Recursive Approach
		# def helper(p1, p2):
        #     # Base Case
        #     if p1 is None:
        #         return p2
        #     if p2 is None:
        #         return p1
        #     # Other Cases
        #     if p1.val <= p2.val:
        #         p1.next = helper(p1.next, p2)
        #         return p1
        #     else:
        #         p2.next = helper(p1, p2.next)
        #         return p2
        # return helper(l1, l2)
        
		# Iterative Approach --> Using Sentinel Node()
        prehead = ListNode(-1)
        prev = prehead
        
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        
        if l1 is not None:
            prev.next = l1
        else:
            prev.next = l2
        
        return prehead.next
        



