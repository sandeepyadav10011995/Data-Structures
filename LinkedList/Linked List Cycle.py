"""
Given a linked list, determine if it has a cycle in it.To represent a cycle in the given linked list, we use an integer pos which 
represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, 
then there is no cycle in the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

"""
# Brute Force Solution: Using a Hash Table --> Time Complexity : O(N) and Space Complexity : O(N)

# Optimized Solution : Using Two Pionter Technique -->  Time Complexity : O(N) and Space Complexity : O(1)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Begin both pointers at the head node
        slow = head
        fast = head
        # Go until end of list
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
