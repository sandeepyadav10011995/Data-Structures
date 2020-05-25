"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example: Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note: Given n will always be valid.
Follow up: Could you do this in one pass?

"""
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Intialize a dummy node and attach head to it
        dummy = ListNode()
        # Note : Edge Case --> When we want to delete first node.
        dummy.next = head
        # Assign two pointers and advance 2nd pointer by n
        slow = dummy
        fast = dummy 
        while n > 0:
            fast = fast.next
            n -= 1
        # Traverse the Linked List
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        # Delete the nth node
        slow.next = slow.next.next
        return dummy.next
      
      
