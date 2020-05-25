"""
Solution : Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

"""
# Recursive Approach
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
		# Base Case
		if head is None or head.next is None:
			return head
		rev = self.reverseList(head.next)
		head.next.next = head
		head.next = None
		return rev

# Iterative Approach
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Iterative Approach --> Using Three pointers
        # Edge Case
        if head == None:
            return None
        cur = head
        pre = None
        nextNode = None
        
        while cur != None:
            nextNode = cur.next
            cur.next = pre
            pre = cur
            cur = nextNode
        return pre
#         # Iterative Approach --> Using Two pointers
#         # Edge Case
#         if head == None:
#             return None
#         cur = head
#         pre = None
#         while cur:
#             cur.next, pre, cur = pre, cur, cur.next
#         return pre
            
        
