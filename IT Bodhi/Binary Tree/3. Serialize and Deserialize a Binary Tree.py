"""
Problem -: Serialize and Deserialize a Binary Tree

Approach 1: Take the InOrder and PreOrder Traversal of the BT and then create the BT again.

Follow Up -: Can we do this using only string or array
Approach 2: Take any Order Traversal i.e, --> Pre Order Traversal

PreOrder -> abNcNNdNefgNNhiNNNN

"""
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: str = None
    left: Any = None
    right: Any = None


@dataclass
class PreIndex:
    index: int = 0


class Solution:
    def createBTWithMarker(self, preOrderTraversalString: str, pi: PreIndex) -> TreeNode | None:
        # Base Case
        if preOrderTraversalString[pi.index] == "N":
            pi.index += 1
            return None

        node = TreeNode(preOrderTraversalString[pi.index])
        pi.index += 1
        node.left = self.createBTWithMarker(preOrderTraversalString, pi)
        node.right = self.createBTWithMarker(preOrderTraversalString, pi)

        return node


"""
TC: O(N)
SC: O(2N) ~ O(N)

Important Question Why ?
Reason-: This helps in representing a Binary Tree in a unique signature form which can be used in many problems.

For Example-: We have to find whether T1 is a SubTree of T2 ?
              T1 --> S1
              T2 --> S2
              Then the problems totally drills down to just simple strings match which can be solved using KMP 
              Algorithms.
    
TC: O(S1+S2)
SC: O(S1+S2)

"""
