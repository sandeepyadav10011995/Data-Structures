"""
Write a program to find the node at which the intersection of two singly linked lists begins.
"""



class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # p1 = headA
        # p2 = headB
        # # Edge Case --> Both are None
        # if p1 is None or p2 is None:
        #     return None
        # # Get the intersection point
        # while p1 and p2 and p1 != p2:
        #     p1 = p1.next
        #     p2 = p2.next
        #     # No Intersection Point
        #     if p1 is None and p2 is None:
        #         return None
        #     # If p1 reaches end
        #     if p1 is None:
        #         p1 = headB
        #     # If p2 reaches end
        #     if p2 is None:
        #         p2 = headA
        # return p1
        
        p1 = headA
        p2 = headB
        # Edge Case --> Both are None
        if p1 is None or p2 is None:
            return None
        while True:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
            # No Intersection Point
            if p1 is None and p2 is None:
                return None
            # If p1 reaches end
            if p1 is None:
                p1= headB
            # If p2 reaches end
            if p2 is None:
                p2 = headA


        
