"""
Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

"""


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def helper(head):
            if head == None:
                return None
            cur = head
            pre = None
            while cur:
                cur.next, pre, cur = pre, cur, cur.next
            return pre
        # Base Case
        if head is None or head.next is None:
            return True
        
        slow = head
        fast = head
        # Important Traversal --> Increase slow pointer acc to fast pointer
        while fast is not None:
            fast = fast.next
            if fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next
        rev_head = helper(slow.next)
        while head is not None and rev_head is not None:
            if head.val == rev_head.val:
                head = head.next
                rev_head = rev_head.next
                continue
            else:
                return False
        return True
	
	
	
