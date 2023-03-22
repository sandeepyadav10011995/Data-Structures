"""
Approach 1. using HashMap

Approach 2. Using 2 Stack -> Optimized Space Complexity

"""
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


class Solution:
    @staticmethod
    def zigZagLevelOrder(root: TreeNode) -> None:
        currentStack = [root]
        nextStack = []
        isLeftToRightOrder = False

        while True:
            while currentStack:
                node = currentStack.pop()
                print(f"{node.val} ")

                if isLeftToRightOrder:
                    if node.left:
                        nextStack.append(node.left)
                    if node.right:
                        nextStack.append(node.right)
                else:
                    if node.right:
                        nextStack.append(node.right)
                    if node.left:
                        nextStack.append(node.left)

            if not nextStack:
                break
            # Change the direction
            isLeftToRightOrder = not isLeftToRightOrder
            # Swap currentStack and nextStack
            currentStack, nextStack = nextStack, currentStack
            print("-"*100)


"""
TC: O(N)
SC: O(N)
"""