"""
Problem -: Serialize and Deserialize a Binary Tree

Approach 1: Take the InOrder and PreOrder Traversal of the BT and then create the BT again.

Follow Up -: Can we do this using only string or array
Approach 2: Take any Order Traversal i.e, --> Pre Order Traversal

Serialize : Convert the BT into string
Deserialize: Convert the string into exact BT structure.
Approach 1: PreOrder
PreOrder -> abNcNNdNefgNNhiNNNN

Approach 2: LevelOrder


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
    @staticmethod
    def createStringFromBT(self, root: TreeNode) -> str:
        finalString = ""
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                finalString += "N"
            else:
                finalString += node.val

            stack.append(node.right)
            stack.append(node.left)
        return finalString

    def createBTWithMarker(self, preOrderTraversalString: str, pi: PreIndex) -> TreeNode | None:  # Deserialize
        # Base Case
        if preOrderTraversalString[pi.index] == "N":
            pi.index += 1
            return None

        node = TreeNode(preOrderTraversalString[pi.index])
        pi.index += 1
        node.left = self.createBTWithMarker(preOrderTraversalString, pi)
        node.right = self.createBTWithMarker(preOrderTraversalString, pi)

        return node

    @staticmethod
    def serializeUsingLevelOrder(root: TreeNode) -> str:
        finalString = ""
        # Base Case
        if root is None:
            return finalString

        levelQueue = [root, None]
        while levelQueue:
            node = levelQueue.pop(0)
            if node is None:
                finalString += "N"
                continue
            else:
                finalString += f"{node.val} "  # Adding " " is needed in levelOrder

            levelQueue.append(node.left)
            levelQueue.append(node.right)
        return finalString

    @staticmethod
    def deserializeUsingLevelOrder(data: str) -> TreeNode | None:
        if data == "":
            return None
        values = data.split(" ")
        root = TreeNode(val=int(values[0]))
        levelQueue = [root]
        for i in range(len(values)):
            parent = levelQueue.pop(0)
            if values[i] != "N":
                left = TreeNode(val=int(values[i]))
                parent.left = left
                levelQueue.append(left)
            if values[i+1] != "N":
                right = TreeNode(val=int(values[i+1]))
                parent.right = right
                levelQueue.append(right)
        return root


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

