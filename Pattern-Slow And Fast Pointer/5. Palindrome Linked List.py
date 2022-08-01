"""
The Fast & Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that uses two
pointers which move through the array (or sequence/LinkedList) at different speeds. This approach is quite useful when
dealing with cyclic LinkedLists or arrays.

By moving at different speeds (say, in a cyclic LinkedList), the algorithm proves that the two pointers are bound to
meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.


Problem Statement: Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or
                   not?

Example 1:
Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true

Example 2:
Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
Output: false

"""


class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


class PalindromeLinkedList:
    def __init__(self):
        self.front = None

    def is_palindromic_linked_list(self, head: Node) -> bool:
        self.front = head
        return self._recursive(head)

    def _recursive(self, cur: Node) -> bool:
        if cur is not None:
            if not self._recursive(cur.next):
                return False
            if self.front.value != cur.value:
                return False
            self.front = self.front.next

        return True


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    pll = PalindromeLinkedList()

    print("Is palindrome: " + str(pll.is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(pll.is_palindromic_linked_list(head)))


main()


"""
Time Complexity: O(N)
Space Complexity: O(N) --> Only Call Stack
"""
