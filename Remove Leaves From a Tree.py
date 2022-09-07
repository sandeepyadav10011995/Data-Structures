from collections import defaultdict
from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     @staticmethod
#     def findLeaves(root: TreeNode) -> List[List[int]]:
#         output = defaultdict(list)
#
#         def dfs(node, layer):
#             if not node: return layer
#             left = dfs(node.left, layer)
#             right = dfs(node.right, layer)
#             layer = max(left, right)
#
#             output[layer].append(node.val)
#
#             return layer + 1
#
#         dfs(root, 0)
#         return list(output.values())
#
#
# s = Solution()
#
# assert s.findLeaves(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))) == [[4, 5, 3], [2], [1]]
# assert s.findLeaves(TreeNode(1)) == [[1]]

# Follow-up 1: Simple modification with removing leaves first --> remove the leaves first


from collections import defaultdict


class Solution:
    @staticmethod
    def findLeaves(root: TreeNode) -> List[List[int]]:
        output = defaultdict(list)

        def dfs(node, layer):
            if not node:
                return layer

            left = dfs(node.left, layer)
            right = dfs(node.right, layer)
            layer = max(left, right)

            output[layer].append(node.val)

            # node.left, node.right = None, None

            del node.left
            del node.right

            return layer + 1

        dfs(root, 0)
        del root  # last node remaining
        return list(output.values())


s = Solution()
assert s.findLeaves(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))) == [[4, 5, 3], [2], [1]]
assert s.findLeaves(TreeNode(1)) == [[1]]

# Follow-up 2: Still DFS but deleting the root before children --> remove the root first

from collections import defaultdict


class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        output = defaultdict(list)

        def dfs(node, layer):
            if not node: return layer

            leftChild = node.left
            rightChild = node.right
            value = node.val

            del node

            left = dfs(leftChild, layer)
            right = dfs(rightChild, layer)
            layer = max(left, right)

            output[layer].append(value)

            return layer + 1

        dfs(root, 0)
        return list(output.values())


s = Solution()
assert s.findLeaves(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))) == [[4, 5, 3], [2], [1]]
assert s.findLeaves(TreeNode(1)) == [[1]]
