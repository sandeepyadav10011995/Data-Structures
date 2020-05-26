"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL

Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

"""
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        def helper(head):
            count = 1
            while head.next is not None:
                head = head.next
                count += 1
            return count
        if head is None:
            return head
        slow = head
        fast = head
        ln = helper(head)
        k = k % ln
        if k == 0:
            return head
        while k > 0:
            k -= 1
            fast = fast.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        new_head = slow.next
        slow.next = None
        fast.next = head
        return new_head

	
