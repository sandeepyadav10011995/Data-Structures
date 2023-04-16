"""
Approach 1. Brute Force -: Using HashMap
            Reverse the list for level % 2 == 0
            TC: O(N)
            SC: O(N)--> Queue + O(N)--> Map of list + O(N)--> Output

Approach 2: Using Doubly Ended Queue
            TC: O(N)
            SC: O(N)--> Queue + O(N)--> Output

Approach 3. Using 2 Stack -> Optimized Space Complexity
            TC: O(N)
            SC: Optimized O(N) Because at any point of time max we will be storing N/2 nodes in stack

"""
from collections import deque
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


class Solution:
    @staticmethod
    def zigZagLevelOrderUsingDoublyEndedQueue(root: TreeNode) -> list[list[int]]:
        result = []
        # Base Case:
        if root is None:
            return result

        isLeftToRightOrder = True
        levelQueue = deque()
        levelOrderQueue = deque()
        # Insert the First Levels Initials
        levelOrderQueue.append(root)
        levelOrderQueue.append(None)

        while levelOrderQueue:
            node = levelOrderQueue.popleft()
            if node:
                if isLeftToRightOrder:
                    levelQueue.append(node.val)
                else:
                    levelQueue.appendleft(node.val)

                if node.left:
                    levelOrderQueue.append(node.left)
                if node.right:
                    levelOrderQueue.append(node.right)
            else:
                result.append(list(levelQueue))
                levelQueue = deque()
                if levelOrderQueue:
                    levelOrderQueue.append(None)
                # Change the direction
                isLeftToRightOrder = not isLeftToRightOrder

        return result

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