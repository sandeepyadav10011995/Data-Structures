"""
Problem : Path Sum : All Unique Paths with Target Sum

Variant 1: Return all The Root to Leaf Paths

Variant 2: Path does not need to start or end at the root or leaf, but it must go downwards.
Bruteforce Solution: Try on every node as if it is a root node and return the count
1st Flavour -: Prefix Sum; return the count

"""


# Variant 1: Return all The Root to Leaf Paths #


class Variant1Solution:
    @staticmethod
    def _isLeaf(root) -> bool:
        return root.left is None and root.right is None

    def _pathSumUtil(self, node, remSum, pathNodes, pathsList) -> None:
        # Base Case
        if node is None:
            return

        pathNodes.append(node.val)  # Our Choice
        if self._isLeaf(node) and node.val == remSum:  # Goal
            pathsList.append(pathNodes[:])
        else:  # Explore
            self._pathSumUtil(node.left, remSum - node.val, pathNodes, pathsList)
            self._pathSumUtil(node.right, remSum - node.val, pathNodes, pathsList)

        pathNodes.pop()  # Undo

    def pathsWithTargetSum(self, root, targetSum) -> list[list[int]]:
        pathsList = []
        self._pathSumUtil(root, targetSum, [], pathsList)
        return pathsList


# Variant 2: Path does not need to start or end at the root or leaf, but it must go downwards #


class BrutForceSolution:
    def pathSum(self, root, targetSum) -> int:
        """
        We will traverse the whole tree and do a "pathSum" query for each node serving as a root to a Subtree of the
        overarching tree.

        1. Find the totalPathSums with root of the overarching tree as the "root" to the subtree.
        2. Ask LeftSubtree: How many paths can you yield? Keeping the original "targetSum" intact.
        3. Ask RightSubtree: How many paths can you yield? Keeping the original "targetSum" intact.

        Reason: We keep the "targetSum" intact because it is the original query we are asking every node in the whole
                tree.
        """
        # Base Case
        if root is None:
            return 0

        return self._totalPathsFromThisNode(root, targetSum) + \
            self.pathSum(root.left, targetSum) + \
            self.pathSum(root.right, targetSum)

    def _totalPathsFromThisNode(self, node, remSum) -> int:
        # Base Case
        if node is None:
            return 0

        totalPathsCompletedFromThisNode = 1 if remSum == node.val else 0
        totalPathsCompletedFromThisNode += self._totalPathsFromThisNode(node.left, remSum - node.val) + \
                                           self._totalPathsFromThisNode(node.right, remSum - node.val)

        return totalPathsCompletedFromThisNode


# Logic: 1st Flavor -: Prefix Sum


class Solution1:
    def findPathSum(self, node, rootToNodeSum, targetSum, prefixSumMapping):
        # Base Case
        if node is None:
            return 0

        # Calculate the new prefixSum till this node
        rootToNodeSum += node.val

        # Sum that needs to be compensated
        sumToCompensatedFor = rootToNodeSum - targetSum

        totalPathsEndingAtThisNode = prefixSumMapping.get(sumToCompensatedFor, 0)
        totalPathsWithThisPathSum = prefixSumMapping.get(rootToNodeSum, 0)

        prefixSumMapping[rootToNodeSum] = totalPathsWithThisPathSum + 1

        totalCompletePathsInThisSubTree = totalPathsEndingAtThisNode + \
                                          self.findPathSum(node.left, rootToNodeSum, targetSum, prefixSumMapping) + \
                                          self.findPathSum(node.right, rootToNodeSum, targetSum, prefixSumMapping)

        prefixSumMapping[rootToNodeSum] = prefixSumMapping.get(rootToNodeSum, 0) - 1
        return totalCompletePathsInThisSubTree


# Logic: 2st Flavor -: Prefix Sum


class Solution2:
    count = 0
    mapping = {}

    def preOrder(self, node, curSum, targetSum):
        # Base Case
        if node is None:
            return 0

        # Add the node to cur_sum
        curSum += node.val

        # Scenario 1: The tree path starts from the root up-to this node => prefixSum == target
        if curSum == targetSum:
            self.count += 1

        # Scenario 2: The tree path starts from this node to downwards => prefixSum == curSum-targetSum
        self.count += self.mapping.get(curSum - targetSum, 0)

        # Add it to the mapping
        self.mapping[curSum] += 1

        self.preOrder(node.left, curSum, targetSum)
        self.preOrder(node.right, curSum, targetSum)

        self.mapping[curSum] -= 1
