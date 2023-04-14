"""



"""
from dataclasses import dataclass
from typing import Any


@dataclass
class Node2:
    val: int = None
    next: Any = None


class Node:
    def __init__(self, val=None, _next=None) -> None:
        self.val = val
        self.next = _next


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BBST:
    def __init__(self, root: Node):
        self.curNode = root

    def createBST(self, start, end):
        # Base Case
        if start > end:
            return None

        # Create a New Node
        newNode = TreeNode()
        mid = (start+end)//2
        newNode.left = self.createBST(start, mid-1)
        newNode.val = self.curNode.val
        self.curNode = self.curNode.next
        newNode.right = self.createBST(mid+1, end)

        return newNode


class BBST2:
    def __init__(self, array=None):
        if array is None:
            array = []
        self.arrIndex = 0
        self.array = array

    def createBST(self, start, end):
        # Base Case
        if start > end:
            return None

        # Create a New Node
        curNode = TreeNode()
        mid = (start+end)//2
        leftBST = self.createBST(start, mid-1)
        curNode.left = leftBST
        curNode.val = self.array[self.arrIndex]
        self.arrIndex += 1
        rightBST = self.createBST(mid+1, end)
        curNode.right = rightBST

        return curNode


def main():
    # Create a Linked List
    head = Node2(1)
    head.next = Node2(2)
    head.next.next = Node2(3)
    head.next.next.next = Node2(4)
    head.next.next.next.next = Node2(5)
    head.next.next.next.next.next = Node2(6)

    # Create a BST
    bst = BBST(head)
    treeNode = bst.createBST(0, 5)
    print(treeNode)

    arr = [5, 10, 12, 15, 25, 35, 45, 65, 89]
    # Create a BST
    bst2 = BBST2(arr)
    treeNode = bst2.createBST(0, 8)
    print(treeNode)


main()

"""
TC: O(N)
SC: O(1)
"""
