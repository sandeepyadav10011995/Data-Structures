"""
Merge 2 BSTs -:
            1. Convert both the BST to Sorted DLL(Doubly Linked List). --> Medium
            2. Merge 2 Sorted DLLs. -> Easy
            3. Create a BST from a Sorted DLL. --> Hard

1. Convert both the BST to Sorted DLL(Doubly Linked List)
     DLL -: left --> prev
            right --> next

    Create a return type class -: INOP
                                    - Node previous
                                    - Node head


"""
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


@dataclass
class INOP:
    previous: TreeNode = None
    head: TreeNode = None


@dataclass
class DLT:
    current: TreeNode


class Solution:
    def convertBSTToDLL(self, root: TreeNode, inop: INOP):
        # Base Case
        if root is None:
            return
        # Inorder Traversal --> Left
        self.convertBSTToDLL(root.left, inop)

        if inop.previous is None:
            inop.head = root
        else:
            # Parent --> Child
            inop.previous.right = root
            # Child --> Parent
            root.left = inop.previous

        # Move the previous
        inop.previous = root
        # Call on the right side
        self.convertBSTToDLL(root.right, inop)

    def mergeTwoDLL(self, head1: TreeNode, head2: TreeNode) -> TreeNode:
        # Base Case:
        if head1 is None:
            return head2
        if head2 is None:
            return head1

        # No recursion --> Call Stack space complexity
        # Do it iteratively
        newHead = head1 if head1.val > head2.val else head2
        cur = newHead

        # Edge case --> Move the head to next
        if cur == head1:
            head1 = head1.right

        if cur == head2:
            head2 = head2.right

        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                head1.left = cur
                cur.right = head1
                cur = head1
                head1 = head1.right
            else:
                head2.left = cur
                cur.right = head2
                cur = head2
                head2 = head2.right

        if head1 is None:
            head2.left = cur
            cur.right = head2
        else:
            head1.left = cur
            cur.right = head1

        return newHead

    def createBSTFromDLL(self, dlt: DLT, count: int) -> TreeNode | None:  # TC: O(N)
        # Base Case
        if count < 1:
            return None

        leftCount = count-1//2
        leftBST = self.createBSTFromDLL(dlt, leftCount)
        currentRoot = dlt.current
        currentRoot.left = leftBST
        dlt.current = dlt.current.right
        rightBST = self.createBSTFromDLL(dlt, count-leftCount-1)
        currentRoot.right = rightBST

        return currentRoot
