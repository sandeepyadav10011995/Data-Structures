"""
Sum of multiples of values of same level for a Binary Tree --> BFS
Data Structure = Queue

Approach 1: Do a level order traversal, store the result as list[list[int]] and then calculate the sum of multiples.
            Drawback -: Using Extra Space i.e, O(N)

Approach 2: Putting None Value for each level. --> SC: O(1)

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
    def mulTree(root: TreeNode) -> int:
        # Edge Case
        if root is None:
            return -1

        levelMul = 1
        levelsSum = 0
        levelOrderQueue = deque([root, None])
        while levelOrderQueue:
            node = levelOrderQueue.popleft()

            if node:
                levelMul *= node.val
                if node.left:
                    levelOrderQueue.append(node.left)
                if node.right:
                    levelOrderQueue.append(node.right)
            else:
                levelsSum += levelMul
                levelMul = 1
                # To avoid Never Ending Infinite Loop and adding 1 to the answer all the time
                if levelOrderQueue:
                    levelOrderQueue.append(None)

        return levelsSum


sol = Solution()
sol.mulTree(root=TreeNode(1))

"""
TC: O(N)
SC: O(N)
"""
