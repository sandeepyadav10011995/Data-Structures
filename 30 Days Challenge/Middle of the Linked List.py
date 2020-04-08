"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.

Example 2:
Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.

"""

def middleNode(head: ListNode) -> ListNode:
    slow = head
    fast = head
    while fast.next != None:
        slow = slow.next
        if fast.next.next:
            fast = fast.next.next
        else:
            fast = fast.next
    return slow
    
