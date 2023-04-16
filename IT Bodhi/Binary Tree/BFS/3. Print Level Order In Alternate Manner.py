"""
Print the Level Order in an Alternate Manner --> BFS
Data Structure = Queue

Approach 1: Putting None Value for each level.

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

        # Edge Case
        if root is None:
            return levelOrderDict, level

        levelArr = []
        levelOrderQueue = [root, None]
        while levelOrderQueue:
            node = levelOrderQueue.pop(0)

            if node:
                levelArr.append(node.val)
                if node.left:
                    levelOrderQueue.append(node.left)
                if node.right:
                    levelOrderQueue.append(node.right)
            else:
                levelOrderDict[level+1] = levelArr
                level += 1
                levelArr = []
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
            if minLevel == maxLevel:
                print(levelOrderDict.get(minLevel))
            else:
                print(levelOrderDict.get(minLevel))
                print(levelOrderDict.get(maxLevel))
            minLevel += 1
            maxLevel -= 1


"""
TC: O(N) + O(N/2) ~ O(N)
SC: O(N)
"""