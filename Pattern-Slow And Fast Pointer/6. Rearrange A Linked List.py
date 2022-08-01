"""
The Fast & Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that uses two
pointers which move through the array (or sequence/LinkedList) at different speeds. This approach is quite useful when
dealing with cyclic LinkedLists or arrays.

By moving at different speeds (say, in a cyclic LinkedList), the algorithm proves that the two pointers are bound to
meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.


Problem Statement: Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes
                   from the second half of the LinkedList are inserted alternately to the nodes from the first half in
                   reverse order. So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should
                   return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

Example 1:
Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null

Example 2:
Input: 2 -> 4 -> 6 -> 8 -> 10 -> null
Output: 2 -> 10 -> 4 -> 8 -> 6 -> null

"""


class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


class RearrangeLinkedList:
    def __init__(self):
        self.front = None
        self.dummy = Node(-1)
        self.dummy_head = None

    def reorder(self, head: Node) -> None:
        self.front = head
        self.dummy_head = self.dummy
        self._recursive(head)

    def _recursive(self, cur: Node):
        if cur is not None:
            if not self._recursive(cur.next):
                return False
            if self.front == cur:
                return False
            self.dummy.next = self.front
            self.dummy = self.dummy.next
            self.dummy.next = cur
            self.dummy = self.dummy.next
            self.front = self.front.next
        return True

    def print_list(self):
        temp = self.dummy_head
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    rll = RearrangeLinkedList()
    rll.reorder(head)
    rll.print_list()


main()


"""
Time Complexity: O(N)
Space Complexity: O(N) --> Only Call Stack
"""


from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()


def reorder(head):
    if head is None or head.next is None:
        return

    # find middle of the LinkedList
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    # slow is now pointing to the middle node
    head_second_half = reverse(slow)  # reverse the second half
    head_first_half = head

    # rearrange to produce the LinkedList in the required order
    while head_first_half is not None and head_second_half is not None:
        temp = head_first_half.next
        head_first_half.next = head_second_half
        head_first_half = temp

        temp = head_second_half.next
        head_second_half.next = head_first_half
        head_second_half = temp

    # set the next of the last node to 'None'
    if head_first_half is not None:
        head_first_half.next = None


def reverse(head):
    prev = None
    while head is not None:
    next = head.next
    head.next = prev
    prev = head
    head = next
    return prev


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reorder(head)
    head.print_list()


main()

