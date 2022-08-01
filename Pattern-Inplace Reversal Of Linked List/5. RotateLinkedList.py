"""
In a lot of problems, we are asked to reverse the links between a set of nodes of a LinkedList. Often, the constraint is
that we need to do this in-place, i.e., using the existing node objects and without using extra memory.

In-place Reversal of a LinkedList pattern describes an efficient way to solve the above problem. In the following
chapters, we will solve a bunch of problems using this pattern.

Problem Statement : Given the head of a Singly LinkedList and a number ‘k’, rotate the LinkedList to the right by ‘k’
                    nodes.

"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class RotateLinkedList:
    @staticmethod
    def rotate(head: Node, rotations: int) -> Node:
        # Edge Case
        if head is None or head.next is None or rotations <= 0:
            return head

        tail = head
        size = 1
        while tail.next:
            tail = tail.next
            size += 1

        rotations %= size
        if rotations == 0:
            return head

        # Create a cycle
        tail.next = head
        rev_tail = tail
        steps_to_new_tail = size - rotations
        while steps_to_new_tail > 0:
            rev_tail = rev_tail.next
            steps_to_new_tail -= 1
        rev_head = rev_tail.next
        rev_tail.next = None

        return rev_head

    @staticmethod
    def print_list(head: Node) -> None:
        temp = head
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    rll = RotateLinkedList()
    print("Nodes of original LinkedList are: ", end='')
    rll.print_list(head)
    result = rll.rotate(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    rll.print_list(result)


main()

"""
Time Complexity: O(N)
Space Complexity: O(1)
"""
