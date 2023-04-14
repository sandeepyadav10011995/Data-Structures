"""
Problem : Minimum cost to paint N fences by C colours. No more than 2 consecutive fences with same colours
F(N) = Last two colors are same(F(N-2)*(X-1)) + Last two colors are different(F(N-1)*(X-1))

F(N, C, K)
Input-:
        0  1  2  3  4  5
0   R:  2, 3, 1, 2, 7, 4
1   G:  3, 5, 2, 3, 6, 1
2   B:  4, 6, 5, 8, 2, 2

Output-:
        0  1  2  3  4  5
0   R:  2, 6, 8, 10, 18, 16
1   G:  3, 7, 8, 11, 16, 13
2   B:  4, 8, 11, 16, 12, 18

F(i, j) : ith Fence painted with jth Color cost = costs[j][i]
F(i, R) = Costs[0][i] + min(F(i-1, B), F(i-1, G))

M: Colors
N: Fences
Therefore generalised F(i, j) = Costs[i][j] + for(k: 1-->C and k != i)min(F(k, j-1))

"""
import math


class Solution:
    @staticmethod
    def minCostToPaintNFencesByCColors(costs):
        # Base Case
        colors = len(costs)
        fences = len(costs[0])
        minCosts = costs[:]

        for fence in range(1, fences):
            for color in range(colors):
                minCostsForFence = math.inf
                for k in range(0, colors):
                    if k != color:
                        minCostsForFence = min(minCostsForFence, minCosts[k][fence-1]+minCosts[color][fence])
                minCosts[color][fence] = minCostsForFence

        return min(minCosts[i][-1] for i in range(colors))
    """
    Assumptions:
        M: Colors
        N: Fences
    TC: O(N*M*M) + O(M) ~ O(N*M^2)
    SC: O(N*M)
    """


sol = Solution()
Costs = [[2, 3, 1, 2, 7, 4],
         [3, 5, 2, 3, 6, 1],
         [4, 6, 5, 8, 2, 2]]
print(sol.minCostToPaintNFencesByCColors(costs=Costs))
