"""
No Two Pumps At K Km
Distance:   5   10  15  21  28  35  42  51  59
Costs:      10  12  20  8   31  18  60  8   25
Profit:     10  12  20  20  43  43  80  80  105

K = 15
Find the MaxProfit we can gain by constructing Pumps

F(i) = max(F(i-1), # Don't build pump at i th
            Costs[i] + firstEligibleFrom F(j) where j < i and j>=0 and Distance[i]-Distance[j] >= K
"""


class Solution2:
    @staticmethod
    def maxProfitSimpleLeftToRight(pumps, k):
        N = len(pumps[0])
        profits = [-1 for _ in range(N)]
        profits[0] = pumps[1][0]

        for i in range(1, N):
            # Build a pump
            maxProfitAtIthPump = pumps[1][i]
            for j in range(i-1, -1, -1):
                if pumps[0][i] - pumps[0][j] > k:
                    maxProfitAtIthPump += profits[j]
                    break
            profits[i] = max(maxProfitAtIthPump, profits[i-1])

        return profits[-1]
    """
    TC: O(N*LogN) --> Because the array is sorted w.r.t distance else if the distance diff is very low in that case you 
                      always fo back i.e, O(N^2)
    SC: O(N)
    """


sol2 = Solution2()
pumpsInfo = [[5, 10, 15, 21, 28, 35, 42, 51, 59],
             [10, 12, 20, 8, 31, 18, 60, 8, 25]]
print(sol2.maxProfitSimpleLeftToRight(pumps=pumpsInfo, k=15))
