"""
Approach 1. Using K distance from a given node
            1. Do it for N and increment the count if ay node is getting printed.
            2. Return the minimum count

Approach 2. Using BFS Approach
            1. To get the information about parent create a ParentMap HashMap
            2. Now push the given node in queue
            3. Pop the node from the queue for this level, While poping, pop the nodes at the same level
            4. Burn the immediate three nodes --> Push them in the queue if not visited already
            5. Increment the count only if some node is burnt
            6. Repeat Steps 3-5
            7. Return the count

"""
from dataclasses import dataclass
from typing import Any


@dataclass
class TreeNode:
    val: int = None
    left: Any = None
    right: Any = None


class Solution:
    def _printAtkDistance(self, node: TreeNode, K: int) -> None:
        # Base Cases
        if node is None:
            return
        if K == 0:
            print(node.val)
            return

        # Explore
        self._printAtkDistance(node.left, K-1)
        self._printAtkDistance(node.right, K - 1)

    def allNodesAtKDistance(self, root: TreeNode, K: int, p: TreeNode) -> int:
        # Base Cases
        if root is None:
            return -1

        if root == p:
            print(root.val)
            return 1

        LV = self.allNodesAtKDistance(root.left, K, p)
        if LV > 0:
            if LV > K:
                return LV
            if LV == K:
                print(root.val)
                return LV+1
            self._printAtkDistance(root.right, K-LV-1)
            return LV+1

        RV = self.allNodesAtKDistance(root.right, K, p)
        if RV > 0:
            if RV > K:
                return RV
            if RV == K:
                print(root.val)
                return RV+1
            self._printAtkDistance(root.left, K-RV-1)
            return RV+1

        return -1


class BurnTree:
    @staticmethod
    def _bfsToParentMap(root: TreeNode, mpp: dict[TreeNode: TreeNode], start: int) -> TreeNode:
        # Base Case
        res = TreeNode(-1)
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.val == start:
                res = node
            if node.left:
                mpp[node.left] = node
                queue.append(node.left)
            if node.right:
                mpp[node.right] = node
                queue.append(node.right)
        return res

    @staticmethod
    def _findMaxDistance(mpp: dict[TreeNode: TreeNode], target: TreeNode) -> int:
        # Push the target in the queue and start burning
        queue = [target]
        # Create a visitedMap to keep a track on the visited TreeNode's
        vis: dict[TreeNode: int] = []
        maxi: int = 0

        while queue:
            sz: int = len(queue)
            fl: int = 0

            for _ in range(sz):
                node = queue.pop(0)
                # Explore the left, right and parent nodes
                if node.left is not None and node.left not in vis:
                    fl = 1
                    vis[node.left] = 1
                    queue.append(node.left)

                if node.right is not None and node.right not in vis:
                    fl = 1
                    vis[node.right] = 1
                    queue.append(node.right)

                if mpp.get(node) is not None and mpp.get(node) not in vis:
                    fl = 1
                    vis[mpp.get(node)] = 1
                    queue.append(mpp.get(node))

            if fl == 1:
                maxi += 1
        return maxi

    def minTimeToBurnBT(self, root: TreeNode, start: int) -> int:
        mpp: dict[TreeNode: TreeNode] = {}
        # Create a Parent-Child Map
        target = self._bfsToParentMap(root, mpp, start)
        return self._findMaxDistance(mpp, target)


"""
TC: O(N) --> Map + O(N) --> Burn ==> O(2N) ~ O(N)
SC: O(N)Map + O(N)Vis + O(N)Queue => O(3N) ~ O(N)
"""
