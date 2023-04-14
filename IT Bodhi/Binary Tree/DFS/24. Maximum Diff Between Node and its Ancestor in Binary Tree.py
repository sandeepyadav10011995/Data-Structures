"""
Problem : Maximum difference between node and its ancestor in Binary Tree.
A is ancestor of B
a-b ==> Max                         4
                        2                       7
                1                          3          16
            3       8                   6      2          5

TC: O(N)
SC: O(N) --> Call Stack

"""
import math
from dataclasses import dataclass


@dataclass
class Answer:
    minSoFar: int = math.inf
    maxAns: int = 0


class Solution:
    def findMaxDiff(self, root) -> Answer:
        ans = Answer()
        # Base Case:
        if root is None:
            return ans

        LV = self.findMaxDiff(root.left)
        RV = self.findMaxDiff(root.right)

        ans.maxAns = root.val - min(LV.minSoFar, RV.minSoFar)
        ans.minSoFar = min(LV.minSoFar, RV.minSoFar, root.val)

        return ans
 