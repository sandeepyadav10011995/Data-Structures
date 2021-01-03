"""
Design a linked list that implements the following api:

get(int index) --> O(n)
Gets the item at index index in the linked list
The list is 0 indexed
If the item does not exist return -1

addToHead(int value) --> O(1)
Adds a node to the head of the linked list with the value value

addToTail(int value) --> O(n)
Adds a node to the tail of the linked list with the value value

addAtIndex(int index, int value) --> O(n)
Adds a node with value value after the node at index index
If the index index is invalid do not perform any operation

deleteAtIndex(int index) --> O(n)
Deletes the node at index index
If the index index is invalid do not perform any operation

size() --> O(1)
Returns the total nodes in the linked list

isEmpty() --> O(1)
Returns true if the linked list is empty, false otherwise

Constraints:
The linked list will not be longer than 1,000 nodes
"""


class Node:
    def __init__(self, val=None):
        sel.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        # Edge Case
        if index < 0 or index > self.size:
            return -1
        dummy_head = self.head
        for _ in range(index):
            dummy_head = dummy_head.next
        return dummy_head.val

    def addToHead(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addToTail(self, val):
        cur = self.head
        new_node = Node(val)
        while cur.next:
            cur = cur.next
        cur.next = new_node
        self.size += 1

    def deleteAtIndex(self, index):
        # Edge Case
        if index < 0  or index > self.size:
            return
        cur = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(index-1):
                cur = cur.next
            cur.next = cur.next.next
        self.size -= 1

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

