"""
Pair with sum K in a Binary Search Tree

Approach 1: Inorder Traversal
            TC: O(N) + O(N) --> O(N)
            SC: O(N) + O(N) --> O(N)

Approach 2: Convert the BST into DLL --> O(N)
            Then convert the DLL into Balanced BST (BST structure can be changed.)
            TC: O(N) + O(N) + O(N)
            SC: O(logN) + O(1)


Approach 3: Using Iterative Inorder Traversal


"""
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


@dataclass
class RT:
    first: TreeNode = None
    second: TreeNode = None


class Solution:
    @staticmethod
    def BTPairWithSumK(root: TreeNode, K: int) -> RT:
        rt = RT()
        if root is None:
            return rt

        # To pick next low or high value depending on sum of low+high
        inOrderStack = []
        revInOrderStack = []

        # To keep the cur_sum and compare it with K
        low: TreeNode = root
        high: TreeNode = root
        curLow: TreeNode = None
        curHigh: TreeNode = None

        # To keep a track as in which node needs to moved low or high
        moveLeft: bool = True
        moveRight: bool = True

        while True:  # Infinite Loop
            # LEFT
            while moveLeft:
                while low is not None:
                    inOrderStack.append(low)
                    low = low.left
                curLow = inOrderStack.pop()
                moveLeft = False
                low = curLow.right

            # RIGHT
            while moveRight:
                while high is not None:
                    revInOrderStack.append(high)
                    high = high.right
                curHigh = revInOrderStack.pop()
                moveRight = False
                high = curHigh.left

            # No Solution exists
            if curLow.val > curHigh.val:
                break

            curSum = curLow.val + curHigh.val
            if curSum == K:
                rt.first = curLow
                rt.second = curHigh
                # Move left and right both if there are multiple answers but no repetitions.
                break
            elif curSum < K:
                moveLeft = True
            else:
                moveRight = True

        return rt


"""
TC: O(N)
SC: O(N) --> Unbalanced; O(logN) --> Balanced
"""