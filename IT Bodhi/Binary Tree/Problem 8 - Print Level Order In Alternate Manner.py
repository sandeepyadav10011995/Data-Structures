"""
Print the Level Order in an Alternate Manner --> BFS
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
    def _levelOrderTraversal(root: TreeNode) -> (dict, int):
        level = 0
        levelOrderDict = {}

        # Base Case
        if root is None:
            return levelOrderDict, level

        arr = []
        levelOrderQueue = [root, None]
        while levelOrderQueue:
            node = levelOrderQueue.pop(0)

            if node:
                arr.append(node.val)
                if node.left:
                    levelOrderQueue.append(node.left)
                if node.right:
                    levelOrderQueue.append(node.right)
            else:
                levelOrderDict[level+1] = arr
                level += 1
                arr = []
                # To avoid Never Ending Infinite Loop and adding 1 to the answer all the time
                if levelOrderQueue:
                    levelOrderQueue.append(None)
        return levelOrderDict, level

    def printAlternateLevelOrder(self, root) -> None:
        # Base Case
        if root is None:
            return
        minLevel = 1
        levelOrderDict, maxLevel = self._levelOrderTraversal(root)

        while minLevel <= maxLevel:
            print(levelOrderDict.get(minLevel))
            print(levelOrderDict.get(maxLevel))
            minLevel += 1
            maxLevel -= 1


"""
TC: O(N) + O(N/2) ~ O(N)
SC: O(N)
"""