"""

Solution
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the 
linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

"""


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        # Go until end of list
        idx = 0
        hash_set = set()
        while head is not None and head.next is not None:
            if head in hash_set:
                return head
            hash_set.add(head)
            head = head.next      
        return None

    
    
# Follow Up: Can you solve it without using extra space?
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode: 
        dummy = ListNode(-1)
        dummy.next = head
        slow = fast = dummy
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            # If cylce is present
            if slow == fast:
                while dummy:
                    if dummy == slow:
                        return dummy
                    slow = slow.next
                    dummy = dummy.next
            return None
