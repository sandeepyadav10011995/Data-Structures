"""
The Fast & Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that uses two
pointers which move through the array (or sequence/LinkedList) at different speeds. This approach is quite useful when
dealing with cyclic LinkedLists or arrays.

By moving at different speeds (say, in a cyclic LinkedList), the algorithm proves that the two pointers are bound to
meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.

One of the famous problems solved using this technique was Finding a cycle in a LinkedList. Let’s jump onto this problem
to understand the Fast & Slow pattern.

Question: Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or
          not?

"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedListCycle:
    @staticmethod
    def has_cycle(head: Node) -> bool:
        # Two Pointers --> Slow and Fast Pointer
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # Found the cycle
                return True
        return False


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

"""
Problem 1: Given the head of a LinkedList with a cycle, find the length of the cycle.
Solution: We can use the above solution to find the cycle in the LinkedList. Once the fast and slow pointers meet, we 
          can save the slow pointer and iterate the whole cycle with another pointer until we see the slow pointer again 
          to find the length of the cycle.

"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedListCycleLength:
    @staticmethod
    def find_cycle_length(head: Node) -> int:
        # Two Pointers --> Slow and Fast Pointer
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # Found the cycle
                return LinkedListCycleLength.calc_cycle_length(slow)
        return 0

    @staticmethod
    def calc_cycle_length(slow: Node) -> int:
        cur = slow
        cycle_length = 0
        while True:
            cur = cur.next
            cycle_length += 1
            if cur == slow:
                break
        return cycle_length


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    llcl = LinkedListCycleLength()
    print("LinkedList has cycle: " + str(llcl.find_cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(llcl.find_cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(llcl.find_cycle_length(head)))


main()

"""
Time Complexity: O(N)
Space Complexity: O(1)
"""

