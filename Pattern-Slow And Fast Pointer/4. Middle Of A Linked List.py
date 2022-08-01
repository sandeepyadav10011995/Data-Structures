"""
The Fast & Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that uses two
pointers which move through the array (or sequence/LinkedList) at different speeds. This approach is quite useful when
dealing with cyclic LinkedLists or arrays.

By moving at different speeds (say, in a cyclic LinkedList), the algorithm proves that the two pointers are bound to
meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.

Problem Statement : Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.
                    If the total number of nodes in the LinkedList is even, return the second middle node.


Algo : We can use the Fast & Slow pointers method such that the fast pointer is always twice the nodes ahead of the slow
       pointer. This way, when the fast pointer reaches the end of the LinkedList, the slow pointer will be pointing at
       the middle node.

Example 1:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
Output: 3

Example 2:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
Output: 4

Example 3:
Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
Output: 4

"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    @staticmethod
    def find_middle_of_linked_list(head: Node) -> Node:
        # Two Pointers --> Slow and Fast Pointer
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    ll = LinkedList()

    print("Middle Node: " + str(ll.find_middle_of_linked_list(head).value))

    head.next.next.next.next.next = Node(6)
    print("Middle Node: " + str(ll.find_middle_of_linked_list(head).value))

    head.next.next.next.next.next.next = Node(7)
    print("Middle Node: " + str(ll.find_middle_of_linked_list(head).value))


main()

"""
Time Complexity: O(N)
Space Complexity: O(1)
"""
