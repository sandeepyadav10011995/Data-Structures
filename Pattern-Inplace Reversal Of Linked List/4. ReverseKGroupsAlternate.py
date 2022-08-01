"""
In a lot of problems, we are asked to reverse the links between a set of nodes of a LinkedList. Often, the constraint is
that we need to do this in-place, i.e., using the existing node objects and without using extra memory.

In-place Reversal of a LinkedList pattern describes an efficient way to solve the above problem. In the following
chapters, we will solve a bunch of problems using this pattern.

Problem Statement : Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list
                    starting from the head?
If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class ReverseKGroupsAlternate:
    @staticmethod
    def reverse_k_groups(head: Node, k: int):
        # Edge Case
        if k <= 1 or head is None:
            return head

        current = head
        previous = None

        while current:
            last_node_of_previous_part = previous
            # After reversing the LinkedList "current" will be the last node of the sub-list.
            last_node_of_sub_list = current
            # Will be used temporarily to store the next node
            future = None
            i = 0
            while current and i < k:  # reverse k nodes
                future = current.next
                current.next = previous
                previous = current
                current = future
                i += 1

            # Connect the Previous Part
            if last_node_of_previous_part:
                last_node_of_previous_part.next = previous
            else:
                head = previous

            # Connect with the next part
            last_node_of_sub_list.next = current

            # Skip "k" nodes
            i = 0
            while current and i < k:
                previous = current
                current = current.next
                i += 1

        return head

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
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    rkg = ReverseKGroupsAlternate()
    print("Nodes of original LinkedList are: ", end='')
    rkg.print_list(head)
    result = rkg.reverse_k_groups(head, 2)
    print("Nodes of reversed LinkedList are: ", end='')
    rkg.print_list(result)


main()


"""
Time Complexity: O(N)
Space Complexity: O(1)
"""
