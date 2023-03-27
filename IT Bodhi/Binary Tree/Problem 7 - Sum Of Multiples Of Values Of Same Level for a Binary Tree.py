"""
Sum of multiples of values of same level for a Binary Tree --> BFS
Data Structure = Queue

Approach 1: Do a level order traversal, store the result as list[list[int]] and then calculate the sum of multiples.
            Drawback -: Using Extra Space i.e, O(N)

Approach 2: Putting None Value for each level. --> SC: O(1)

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
    def mulTree(root: TreeNode) -> int:
        # Base Case
        if root is None:
            return -1

        levelMul = 1
        levelsSum = 0
        levelOrderQueue = [root, None]
        while levelOrderQueue:
            node = levelOrderQueue.pop(0)

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


"""
TC: O(N)
SC: O(N)
"""
