"""
Approach 1: Level Order Traversal
            Step 1: Generate Parent Map
            Step 2: Keep moving 1 distance in all three directions
            Step 3: Stop if dist == K
            TC: O(N) + O(N)
            SC: O(N)-> ParentTrack + O(N)--> Visited + O(N) -> Queue

Approach 2: Recursive Approach
            TC: O(N)
            SC: O(N) --> Call Stack

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
    def _bfsToParentMap(root: TreeNode, mpp: dict[TreeNode: TreeNode], start: int) -> TreeNode:
        # Base Case
        res = TreeNode(-1)
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.val == start:
                res = node
            if node.left:
                mpp[node.left.val] = node
                queue.append(node.left)
            if node.right:
                mpp[node.right.val] = node
                queue.append(node.right)
        return res

    @staticmethod
    def _findNodesAtKDistance(mpp: dict[TreeNode: TreeNode], target: TreeNode, K: int) -> list[int]:
        # Push the target in the queue and start burning
        queue = [target]
        # Create a visitedMap to keep a track on the visited TreeNode's
        vis: dict[TreeNode: int] = {}
        currDist: int = 0
        while queue:
            sz: int = len(queue)
            if currDist == K:
                break
            currDist += 1
            for _ in range(sz):
                node = queue.pop(0)
                # Explore the left, right and parent nodes
                if node.left is not None and node.left.val not in vis:
                    vis[node.left.val] = 1
                    queue.append(node.left)

                if node.right is not None and node.right.val not in vis:
                    vis[node.right.val] = 1
                    queue.append(node.right)

                if mpp.get(node.val) is not None and mpp.get(node.val).val not in vis:
                    vis[mpp.get(node.val).val] = 1
                    queue.append(mpp.get(node.val))
        return [_node.val for _node in queue]

    def getAllNodesAtKDistBT(self, root: TreeNode, start: int, K: int) -> list[int]:
        mpp: dict[TreeNode: TreeNode] = {}
        # Create a Parent-Child Map
        target = self._bfsToParentMap(root, mpp, start)
        return self._findNodesAtKDistance(mpp, target, K)

    def _printAtkDistance(self, node: TreeNode, K: int) -> None:
        # Base Cases
        if node is None:
            return
        if K == 0:
            print(node.val)
            print("_______")
            return

        # Explore
        self._printAtkDistance(node.left, K-1)
        self._printAtkDistance(node.right, K - 1)

    def allNodesAtKDistance(self, root: TreeNode, K: int, p: TreeNode) -> int:
        # Base Cases
        if root is None:
            return -1

        if root.val == p.val:
            print(root.val)
            print("_______")
            self._printAtkDistance(root, K)
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


sol = Solution()
node = TreeNode(val=1,
                left=TreeNode(val=2,
                              left=TreeNode(val=4,
                                            left=TreeNode(val=8),
                                            right=None),
                              right=TreeNode(val=5,
                                             left=TreeNode(val=9),
                                             right=TreeNode(val=10)
                              )
                ),
                right=TreeNode(val=3,
                               left=TreeNode(val=6),
                               right=TreeNode(val=7))
                )

sol.allNodesAtKDistance(root=node, K=2, p=TreeNode(val=2))

print(sol.getAllNodesAtKDistBT(root=node, start=2, K=2))