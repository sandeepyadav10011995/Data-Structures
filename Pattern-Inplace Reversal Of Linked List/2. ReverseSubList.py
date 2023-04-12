"""
In a lot of problems, we are asked to reverse the links between a set of nodes of a LinkedList. Often, the constraint is
that we need to do this in-place, i.e., using the existing node objects and without using extra memory.
In-place Reversal of a LinkedList pattern describes an efficient way to solve the above problem. In the following
chapters, we will solve a bunch of problems using this pattern.
Problem Statement: Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position
                   ‘p’ to ‘q’?
Algo : The problem follows the In-place Reversal of a LinkedList pattern. We can use a similar approach as discussed in
       Reverse a LinkedList. Here are the steps we need to follow:
        1. Skip the first p-1 nodes, to reach the node at position p.
        2. Remember the node at position p-1 to be used later to connect with the reversed sub-list.
        3. Next, reverse the nodes from p to q using the same approach discussed in Reverse a LinkedList.
        4. Connect the p-1 and q+1 nodes to the reversed sub-list.
"""


class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next


class ReverseSubList:
    @staticmethod
    def reverse_sub_list(head: Node, p: int, q: int) -> Node:
        if p == q:
            return head

        # After skipping "p-1" nodes current will point to the pth node
        previous = None
        current = head
        i = 0
        while current and i < p-1:
            previous = current
            current = current.next
            i += 1

        # We are interested in three parts of the Linked List, the part before index "p", the part between "p" and "q",
        # and the part after index "q".
        last_node_of_first_part = previous
        # After reversing the LinkedList "current" will become the last node of the sub-list
        last_node_of_sub_list = current

        future = None  # Will be used to store the next node
        i = 0
        # Reverse nodes between "p" and "q"
        while current and i < q-p+1:
            future = current.next
            current.next = previous
            previous = current
            current = future
            i += 1

        # Connect the first part
        if last_node_of_first_part:
            # "previous" is now the first node of the sub-list
            last_node_of_first_part.next = previous
        else:  # This means p == 1; i.e., we are changing the first node of the LinkedList.
            head = previous

        # Connect the last part
        last_node_of_sub_list.next = current
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
    rsl = ReverseSubList()
    print("Nodes of original LinkedList are: ", end='')
    result = rsl.reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    rsl.print_list(result)


main()


"""
Time Complexity: O(N)
Space Complexity: O(1)
"""


"""
Second Approach : Using Swap Module
"""


class ReverseSubList2:
    @staticmethod
    def reverse_sub_list(head: Node, p: int, q: int) -> Node:
        # Edge Case
        if p == q:
            return head

        dummy_head = Node(-1)
        dummy_head.next = head
        nbrs = dummy_head  # nbrs: Node Before Reversed Sub List
        pos = 1
        while pos < p:
            nbrs = nbrs.next
            pos += 1

        swp = nbrs.next  # swp: Sub-list Working Pointer
        # Throw the items in sub-list to the front one by one.
        while p < q:
            # Cut of the sub-list
            temp = swp.next
            swp.next = temp.next

            # Wire into sub-list head
            temp.next = nbrs.next
            nbrs.next = temp

            p += 1

        return dummy_head.next

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
    rsl = ReverseSubList2()
    print("Nodes of original LinkedList are: ", end='')
    result = rsl.reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    rsl.print_list(result)


# main()


"""
Time Complexity: O(N)
Space Complexity: O(1)
"""