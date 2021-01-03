"""
Even Odd Partition
Given a singly linked list, arrange the nodes such that all even index nodes appear before the odd index nodes.

When we refer to "index" we are referring to the node's zero-indexed position in the input (original) list.

The relative ordering of the nodes within the same region must be maintained.

Example 1:
Input:  5 -> 1 -> 3 -> 7 -> 3 -> X
Output: 5 -> 3 -> 3 -> 1 -> 7 -> X
Explanation: All the even index nodes go first, followed by the odd. The relative ordering of the nodes is maintained.

Example 2:
Input:  1 -> 2 -> 3 -> 4 -> 5 -> X
Output: 1 -> 3 -> 5 -> 2 -> 4 -> X

Example 3:
Input:  4 -> 1 -> X
Output: 4 -> 1 -> X

Constraints:
The arrangement must be performed using O(1) space
"""

class Solution:
    def evenOddPartition(self, head):
        # Edge Case
        if head is None or head.next is None:
            return head

        odd = head
        even = head.next
        even_head = even
        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head

