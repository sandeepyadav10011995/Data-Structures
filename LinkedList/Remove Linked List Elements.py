"""
Remove all elements from a linked list of integers that have value val.

Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

"""
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # Edge Case
        if not head:
            return head
        curr_node = head
        prev_node = head
        while curr_node:
            if curr_node.val == val:
                prev_node.next = curr_node.next
                if head.val == val:
                    head = head.next
            else:
                prev_node = curr_node
            curr_node = curr_node.next
        return head
        
		
