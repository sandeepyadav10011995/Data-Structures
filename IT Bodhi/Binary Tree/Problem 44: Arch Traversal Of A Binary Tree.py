"""
Binary Tree Arch Traversal
Approach 1: Level Order Traversal
TC: O(N)
SC: O(N) --> Saving the answers

"""
from collections import deque
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


@dataclass
class LevelOrderNode:
    node: TreeNode = None
    leftMost: bool = False
    rightMost: bool = False


class ArchTraversal:
    @staticmethod
    def binaryTreeArchTraversal(root: TreeNode) -> list[int]:
        archTraversalAns = deque()
        # Base Case
        if root is None:
            return list(archTraversalAns)

        isFirstElementOfLevel = True
        isLastElementOfLevel = True
        levelOrderQueue = [LevelOrderNode(node=root), None]
        archTraversalAns.append(root.val)

        while levelOrderQueue:
            llNode = levelOrderQueue.pop(0)

            if llNode is not None:
                if isFirstElementOfLevel:
                    if llNode.leftMost:
                        archTraversalAns.appendleft(llNode.node.val)
                    if llNode.rightMost:
                        archTraversalAns.append(llNode.node.val)
                    isFirstElementOfLevel = False
                if isLastElementOfLevel and levelOrderQueue[0] is None:
                    if llNode.leftMost:
                        archTraversalAns.appendleft(llNode.node.val)
                    if llNode.rightMost:
                        archTraversalAns.append(llNode.node.val)
                    isLastElementOfLevel = False
                if llNode.node.left:
                    levelOrderQueue.append(LevelOrderNode(node=llNode.node.left, leftMost=True, rightMost=False))
                if llNode.node.right:
                    levelOrderQueue.append(LevelOrderNode(node=llNode.node.right, leftMost=False, rightMost=True))
            else:
                isFirstElementOfLevel = True
                isLastElementOfLevel = True
                # To avoid Never Ending Infinite Loop
                if levelOrderQueue:
                    levelOrderQueue.append(None)

        return list(archTraversalAns)


def main():
    root = TreeNode(val=6)

    root.left = TreeNode(val=2)
    root.right = TreeNode(val=3)

    root.left.left = TreeNode(val=1)
    root.left.right = TreeNode(val=4)

    root.right.left = TreeNode(val=5)
    root.right.right = TreeNode(val=2)

    root.left.left.left = TreeNode(val=8)
    root.left.right.left = TreeNode(val=2)

    root.right.left.right = TreeNode(val=3)

    root.left.left.left.left = TreeNode(val=10)
    root.left.left.left.right = TreeNode(val=4)
    root.left.right.left.right = TreeNode(val=5)

    root.left.right.left.right.left = TreeNode(val=12)
    root.left.right.left.right.right = TreeNode(val=2)

    at = ArchTraversal()
    print(at.binaryTreeArchTraversal(root))


main()
