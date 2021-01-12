"""
A binary tree is "height-balanced" if at every node the left and right subtree height do not differ by more than 1.

Given a binary tree, determine if it is height-balanced.

Example 1:
Input:
           1
          / \
         2   3

Output: true
Explanation: The root node has a left subtree height of 1 and a right subtree height of 1. Each leaf node has left & right subtree heights of 0.

Example 2:
Input:
           1
          / \
         2   3
            / \
           4   5

Output: true
Explanation:
| Node{i} | left sub height | right sub height |
|    1    |        1        |         2        |
|    2    |        0        |         0        |
|    3    |        1        |         1        |
|    4    |        0        |         0        |
|    5    |        0        |         0        |

Example 3:
Input:
           1
          / \
         2   3
            / \
           4   5
                \
                 6
Output: false
Explanation: Breaks balance at root, |1 - 3| = 2 > 1.
| Node{i} | left sub height | right sub height |
|    1    |        1        |         3        |
|    2    |        0        |         0        |
|    3    |        1        |         2        |
|    4    |        0        |         0        |
|    5    |        0        |         1        |
|    6    |        0        |         0        |

"""
class BalanceStatusWithHeight:
    def __init__(self, is_balanced, height):
        self.is_balanced = is_balanced
        self.height = height

class Solution:
    def _checkBalanced(self, node):
        if node is None:
            return BalanceStatusWithHeight(True, -1)
        left_result = self._checkBalanced(node.left)
        if not left_result.is_balanced:
            return left_result

        right_result = self._checkBalanced(node.right)
        if not right_result.is_balanced:
            return right_result

        # Check both the heights --> Absolute heights diff
        subtree_is_balanced = abs(left_result.height - right_result.height) <= 1
        subtree_height = max(left_result.height, right_result.height) + 1

        return BalanceStatusWithHeight(subtree_is_balanced, subtree_height)

    def isBalanced(self, root):
        return self._checkBalanced(root).is_balanced
