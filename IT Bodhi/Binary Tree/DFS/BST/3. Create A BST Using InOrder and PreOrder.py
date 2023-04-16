"""



"""
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: str = None
    left: Any = None
    right: Any = None


class Solution:
    def __init__(self, preOrder: str, inOrder: str) -> None:
        self.preOrder = preOrder
        self.idxMap = {val: idx for idx, val in enumerate(inOrder)}
        self.preIndex = 0

    def createBST(self) -> TreeNode:
        return self._createBSTUtil(start=0, end=len(self.preOrder)-1)

    def _createBSTUtil(self, start: int, end: int) -> TreeNode:
        # Base Case
        if start > end:
            return None

        root = TreeNode(self.preOrder[self.preIndex])
        self.preIndex += 1
        root.left = self._createBSTUtil(start, self.idxMap[root.val] - 1)
        root.right = self._createBSTUtil(self.idxMap[root.val] + 1, end)
        return root


"""
TC: O(N)
SC: O(N) --> Map + O(N) --> Call Stack ~ O(N)

"""

def main():
    preOrder = "abcdefgh"
    inOrder = "badgfhec"
    sol = Solution(preOrder=preOrder, inOrder=inOrder)
    print(sol.createBST())


main()
