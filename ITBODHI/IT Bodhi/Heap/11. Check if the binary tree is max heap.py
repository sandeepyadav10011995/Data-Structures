"""
Problem: Check if the binary tree is max heap

If BT is a maxHeap
    - Child-Parent Relationship
    - CBT -> Level Order
        -   HL -- HR
            - LH == RH then HL should be Full Tree
            - LH = RH + 1 then HR should be Full tree
            - resultant would be isHeap --> LH == RH

"""


class Node:
    def __init__(self, val=None, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def isChildParentRelationshipCorrect(root: Node) -> bool:
    # Base Case
    if root is None:
        return True

    # Check the left child
    if root.left is not None and root.left.val > root.val:
        return False

    # Check the right child
    if root.right is not None and root.right.val > root.val:
        return False

    return isChildParentRelationshipCorrect(root.left) and isChildParentRelationshipCorrect(root.right)


def isCBT(root: Node) -> bool:
    queue = [root]
    isNullChildAdded = False

    while queue:
        element = queue.pop(0)
        if element.left is None and queue:
            return False
        else:
            if element.left and not isNullChildAdded:
                queue.append(element.left)
                #
        if element.right:
            queue.append(element.right)

    return True


class ReturnType:
    def __init__(self, isHeap=False, isFull=False, height=0):
        self.isHeap = isHeap
        self.isFull = isFull
        self.height = height


class MaxHeap:
    def isMaxHeap(self, root: Node) -> bool:
        rt = ReturnType()

        # Base Case
        if root is None:
            rt.isHeap = True
            rt.isFull = True
            rt.height = 0
            return rt

        # Child-Parent Check
        if root.left is not None and root.left.val > root.val:
            return rt

        # Check the right child
        if root.right is not None and root.right.val > root.val:
            return rt

        lv = self.isMaxHeap(root.left)
        rv = self.isMaxHeap(root.right)

        if (lv.isHeap and rv.isHeap
                and (
                        (lv.height == rv.height and lv.isFull)
                        or (lv.height == rv.height + 1 and rv.isFull)
                )
        ):
            rt.isHeap = True
            rt.height = lv.height + 1
            rt.isFull = lv.isFull and rv.isFull and lv.height == rv.height
            return rt

        return rt
