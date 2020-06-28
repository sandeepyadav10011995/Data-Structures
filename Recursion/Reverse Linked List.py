Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    g_head = None
    def _recursiveTailApproach(self, prev, head):
        # Base Case
        if head is None:
            return prev
        
        cur = head
        future = head.next
        cur.next = prev
        return self._recursiveTailApproach(cur, future)
    
    def _recursiveHeadApproach(self, head):
        # Base Case
        if head.next is None:
            self.g_head = head
            return head
        new_head = self._recursiveHeadApproach(head.next)
        new_head.next = head
        return head
	
def reverseList(self, head: ListNode) -> ListNode:
#         # Iterative Approach --> Using Three pointers
#         # Edge Case
#         if head == None:
#             return None
#         cur = head
#         pre = None
#         nextNode = None
        
#         while cur != None:
#             nextNode = cur.next
#             cur.next = pre
#             pre = cur
#             cur = nextNode
#         return pre
#         # Iterative Approach --> Using Two pointers
#         # Edge Case
#         if head == None:
#             return None
#         cur = head
#         pre = None
#         while cur:
#             cur.next, pre, cur = pre, cur, cur.next
#         return pre
    
    # Recursive Approach --> Tail Recursion
        # return self._recursiveTailApproach(None, head)
    
    # Recursive Approach --> Head Recursion
        # Edge Case
        if head == None:
            return None
        self._recursiveHeadApproach(head).next = None
        return self.g_head
