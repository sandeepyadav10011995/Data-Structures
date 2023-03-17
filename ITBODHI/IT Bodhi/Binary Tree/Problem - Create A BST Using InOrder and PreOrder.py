"""



"""
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode2:
    val: str = None
    left: Any = None
    right: Any = None


class Solution:
    def __init__(self, preOrder: str, inOrder: str) -> None:
        self.preOrder = preOrder
        self.idxMap = {val: idx for idx, val in enumerate(inOrder)}
        self.preIndex = 0

    def createBST(self) -> TreeNode2:
        return self._createBSTUtil(start=0, end=len(self.preOrder)-1)

    def _createBSTUtil(self, start: int, end: int) -> TreeNode2:
        # Base Case
        if start > end:
            return None

        root = TreeNode2(self.preOrder[self.preIndex])
        self.preIndex += 1
        root.left = self._createBSTUtil(start, self.idxMap[root.val] - 1)
        root.right = self._createBSTUtil(self.idxMap[root.val] + 1, end)
        return root


def main():
    preOrder = "abcdefgh"
    inOrder = "badgfhec"
    sol = Solution(preOrder=preOrder, inOrder=inOrder)
    print(sol.createBST())


main()
