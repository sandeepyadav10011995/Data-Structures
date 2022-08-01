"""
The Fast & Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that uses two
pointers which move through the array (or sequence/LinkedList) at different speeds. This approach is quite useful when
dealing with cyclic LinkedLists or arrays.

By moving at different speeds (say, in a cyclic LinkedList), the algorithm proves that the two pointers are bound to
meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.

One of the famous problems solved using this technique was Finding a cycle in a LinkedList. Let’s jump onto this problem
to understand the Fast & Slow pattern.

Question: Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the
          cycle?

"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedListCycle:
    @staticmethod
    def has_cycle(head: Node) -> Node:
        # Two Pointers --> Slow and Fast Pointer With Dummy Node
        dummy = Node(-1)
        dummy.next = head
        slow = dummy
        fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # Found the cycle
                while dummy:
                    if dummy == slow:
                        return dummy
                    dummy = dummy.next
                    slow = slow.next

        return Node(value=None)


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    llc = LinkedListCycle()
    print("LinkedList has cycle: " + str(llc.has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(llc.has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(llc.has_cycle(head)))


main()

"""
Time Complexity: O(N)
Space Complexity: O(1)
"""
