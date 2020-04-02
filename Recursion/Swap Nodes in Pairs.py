"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

"""
def swapPairs(self, head: ListNode) -> ListNode:
        def swap(head):
            # Edge Case
            if head == None or head.next == None:
                return head
            prev = head
            head = head.next
            prev.next = swap(head.next)
            head.next = prev
            return head
        return swap(head)
