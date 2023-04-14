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
    def __init__(self, postOrder: str, inOrder: str) -> None:
        self.postOrder = postOrder
        self.idxMap = {val: idx for idx, val in enumerate(inOrder)}
        self.postIndex = len(inOrder) - 1

    def createBST(self) -> TreeNode2:
        return self._createBSTUtil(start=0, end=len(self.postOrder) - 1)

    def _createBSTUtil(self, start: int, end: int) -> TreeNode2:
        # Base Case
        if start > end:
            return None

        root = TreeNode2(self.postOrder[self.postIndex])
        self.postIndex -= 1
        root.right = self._createBSTUtil(self.idxMap[root.val] + 1, end)
        root.left = self._createBSTUtil(start, self.idxMap[root.val] - 1)
        
        return root


def main():
    postOrder = "bghfedca"
    inOrder = "badgfhec"
    sol = Solution(postOrder=postOrder, inOrder=inOrder)
    print(sol.createBST())


main()
