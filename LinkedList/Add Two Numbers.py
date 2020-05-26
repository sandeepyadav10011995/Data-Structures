"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list. 
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # output = ListNode()
        # head = output
        # carry = 0
        # while l1 and l2:
        #     node_sum = l1.val + l2.val + carry
        #     if node_sum > 9:
        #         carry = node_sum // 10
        #         node = ListNode(node_sum % 10)
        #     else:
        #         node = ListNode(node_sum)
        #         carry = 0
        #     head.next = node
        #     head = head.next
        #     l1 = l1.next
        #     l2 = l2.next
        # if carry > 0:
        #     node = ListNode(carry)
        #     head.next = node
        # return output.next
        
        # Recursion Solution
        def helper(carry, l1=None, l2=None):
            if l1 and l2:
                value = l1.val + l2.val + carry
                carry = value // 10
                val = value % 10
                node = ListNode(val)
                node.next = helper(carry, l1.next, l2.next)
                return node
            if l1:
                value = l1.val + carry
                carry = value // 10
                val = value % 10
                return ListNode(val, helper(carry, l1.next, None))
            if l2:
                value = l2.val + carry
                carry = value // 10
                val = value % 10
                return ListNode(val, helper(carry, None, l2.next))
            if carry:
                return ListNode(carry)
        return helper(0, l1, l2)


