class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n):
        if n == 0: return [], 1
        # Recursion Approach
        return self._recursive(1, n)
        # DP Approach --> Catalan Number - Cartesian Product
        # return self._dynamic(n)

    def _dynamic(self, n):
        G = [0] * (n+1)
        G[0], G[1] = 1, 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]
        return G[n]

    def _recursive(self, start, end):
        """
          Imagine the iteration for n = 5, we need to generate trees 5 nodes in size. Here is
          how the calls would compose themselves.
          Top level stack frame:
            start = 1
            end = 5
          i = 1
                    1
                /       \
          gen(1, 0)  gen(2, 5)
          i = 2
                    2
                /       \
          gen(1, 1)  gen(3, 5)
          i = 3
                    3
                /       \
          gen(1, 2)  gen(4, 5)
          i = 4
                    4
                /       \
          gen(1, 3)  gen(5, 5)
          i = 5
                    5
                /       \
          gen(1, 4)  gen(6, 5)
        """
        if start > end:
            return [None]
        ans = []
        count = 0
        for i in range(start, end + 1):
            left_tree = self._recursive(start, i - 1)
            right_tree = self._recursive(i + 1, end)
            for l_child in left_tree:
                for r_child in right_tree:
                    root = TreeNode(i)
                    root.left = l_child
                    root.right = r_child
                    ans.append(root)
                count += 1
        # print(count)
        return ans, count

n = 5
sol = Solution()
# sol.generateTrees(n)
for i in range(1, n+1):
    print(sol.generateTrees(i)[1])
