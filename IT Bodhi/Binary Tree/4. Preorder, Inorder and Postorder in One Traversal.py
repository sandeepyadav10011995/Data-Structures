"""
Preorder, Inorder and Postorder in One Traversal
Insert Item in Stack
Item -: node, num where num = 1-3

TC: O(3N) ~ O(N)
SC: O(4N) ~ O(N)
"""
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None

@dataclass
class Item:
    node: TreeNode = None
    num: int = 1

class Solution:
    def allTraversalInOne(self, root: TreeNode) -> dict:
        result = {}
        # Edge Case
        if root is None:
            return result

        preOrder = []
        inOrder = []
        postOrder = []

        stack = [Item(node=root)]
        while stack:
            it = stack.pop()
            if it.num == 1:  # This is a part of PreOrder
                preOrder.append(it.node.val)
                it.num += 1
                stack.append(it)
                if it.node.left:
                    stack.append(Item(it.node.left, num=1))

            elif it.num == 2:  # This is a part of InOrder
                inOrder.append(it.node.val)
                it.num += 1
                stack.append(it)
                if it.node.right:
                    stack.append(Item(node=it.node.right, num=1))

            else:  # This is a part of PostOrder
                postOrder.append(it.node.val)

        result["preOrder"] = preOrder
        result["inOrder"] = inOrder
        result["postOrder"] = postOrder

        return result





