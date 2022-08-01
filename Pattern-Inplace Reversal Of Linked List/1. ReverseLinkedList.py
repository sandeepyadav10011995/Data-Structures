"""
In a lot of problems, we are asked to reverse the links between a set of nodes of a LinkedList. Often, the constraint is
that we need to do this in-place, i.e., using the existing node objects and without using extra memory.

In-place Reversal of a LinkedList pattern describes an efficient way to solve the above problem. In the following
chapters, we will solve a bunch of problems using this pattern.

Problem Statement: Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new
                   head of the reversed LinkedList.

"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class ReverseLinkedList:
    @staticmethod
    def reverse(head: Node) -> Node:
        previous = None
        current = head
        future = None
        while current:
            future = current.next  # Temporarily store the next node
            current.next = previous  # Reverse the current node
            previous = current  # Before we move to next node, point previous to the current node
            current = future  # Move on the next node
        return previous

    @staticmethod
    def print_list(head: Node) -> None:
        temp = head
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    rll = ReverseLinkedList()

    print("Nodes of original LinkedList are: ", end='')
    rll.print_list(head)
    result = rll.reverse(head)
    print("Nodes of reversed LinkedList are: ", end='')
    rll.print_list(result)


main()


"""
Time Complexity: O(N)
Space Complexity: O(1)
"""
