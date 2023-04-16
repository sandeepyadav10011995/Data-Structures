"""
Problem -: Maximum Width of a Binary Tree

Width --> MAx number of nodes in a level between 2 nodes.

            0                           0                       0
        0      0                    0       0               0       0
    0      0        0            0                      0               0
                                                     0                      0
    Ans = 4                         Ans = 2                     Ans = 8

Approach: Level Order Traversal
            TC: O(N)
            SC: O(N)

            Segment Tree --> Indexing
            Ans = Second Node Index - First Node Index + 1

            Indexing -:
            0-Indexed -: Then left = 2*i+1 and right = 2*i+2
            1-Indexed -: Then left = 2*i and right = 2*i+1

            Problem -: If it is skewed tree then indexing would be wrong, i.e 2*i, 2*i+1 Also can lead to Integer
                       Overflow
            Solution -: Initialize the indexing from 0 - n for every level

"""
from collections import deque
from typing import Any
from dataclasses import dataclass

@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


@dataclass
class Pair:
    node: TreeNode = None
    num: int = None


class Solution:
    @staticmethod
    def getMaxWidthBT(root: TreeNode) -> int:
        ans = 0
        if root is None:
            return ans

        isFirstElementOfLevel = True
        levelQueue = deque([Pair(root, 0), Pair(None, None)])
        parentIdx = levelQueue[0].num
        firstIdx, lastIdx = 0, 0
        while levelQueue:
            pair = levelQueue.popleft()
            if pair.node:
                curIdx = pair.num - parentIdx
                if isFirstElementOfLevel:
                    firstIdx = curIdx
                    isFirstElementOfLevel = False
                if levelQueue[0].node is None:
                    lastIdx = curIdx
                if pair.node.left:
                    levelQueue.append(Pair(pair.node.left, curIdx*2+1))
                if pair.node.right:
                    levelQueue.append(Pair(pair.node.right, curIdx*2+2))
            else:
                ans = lastIdx-firstIdx+1
                firstIdx, lastIdx = 0, 0
                isFirstElementOfLevel = True
                if levelQueue:
                    parentIdx = levelQueue[0].num   # To make the starting Index from zero.
                    levelQueue.append(Pair(None, None))
        return ans


root1 = TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(val=4)), right=TreeNode(val=3, right=TreeNode(val=5)))
sol = Solution()
print(sol.getMaxWidthBT(root=root1))
