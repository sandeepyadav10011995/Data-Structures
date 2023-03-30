"""
Problem : Find if any subset is making sum K, from a given integer array.

Case 1: Return True/False
Ex -: arr = [2, 5, 3, 4, 2], K = 8

Approach 1: Recursive
        TC: O(2^N)
        SC: O(N)

Approach 2: Top-Down Approach
        TC: O(Sum*N*2)
        SC: O(Sum*N)

What if we want to return the list of elements?
Then in the Base Cases --> we will return [] list when K == 0


    0   1   2   3   4   5   6   7   8
2   T
5   T
3   T
4   T
2   T

Case 2: If not possible then split the array in such a way that diff b/w groups is minimum
        Ex -: arr = [4, 5, 3, 4, 4], K = sum(arr)/2 = 20/2 = 10
        Not possible in half
F(i, j) = F(i-1, j) or F(i-1, j-arr[i-1])

    0   1   2   3   4   5   6   7   8   9   10  11
0   1   0   0   0   0   0   0   0   0   0   0   0
4   1   0   0   0   1   0   0   0   0   0   0   0
5   1   0   0   0   1   1   0   0   0   1   0   0
3   1   0   0   1   1   1   0   1   1   1   0   0
4   1   0   0   1   1   1   0   1   1   1   0   1
4   1   0   0   1   1   1   0   1   1   1   0   1

sum1 = i = 11
sum2 = 2*K -i == 20-11 = 9
diff = sum2-sum1 = 11-9 = 2
diff = |2*K - i -i| = |2(K-i)| = |2(10-11)| = 2*1 = 2

"""


class SolutionCase1:
    def subSetSumEqualToK(self, arr, K, index) -> bool:
        # Base Case
        if K == 0:
            return True
        if index < 0:
            return False

        return self.subSetSumEqualToK(arr, K, index-1) or \
            self.subSetSumEqualToK(arr, K-arr[index], index-1)
    """
    TC: O(2^N)
    SC: O(N)
    """

    def subSetSumEqualToKTopDown(self, arr, K, index) -> bool:
        # Base Case
        if K == 0:
            return True
        if index < 0:
            return False

        return self.subSetSumEqualToK(arr, K, index-1) or \
            self.subSetSumEqualToK(arr, K-arr[index], index-1)

    def subSetSumEqualToKList(self, arr, K, index) -> list[int] | None:
        # Base Case
        if K == 0:
            return []
        if index < 0:
            return None

        LV = self.subSetSumEqualToKList(arr, K, index-1)
        if LV is not None:
            return LV
        RV = self.subSetSumEqualToKList(arr, K-arr[index], index-1)
        if RV is not None:
            RV.append(arr[index])
        return RV

    @staticmethod
    def subSetSumEqualToKBottomUp(arr, K):
        size = len(arr)
        memo = [[0 for _ in range(K+1)] for _ in range(size+1)]
        for i in range(size+1):
            memo[i][0] = 1

        for i in range(1, size+1):
            for j in range(1, K+1):
                memo[i][j] = memo[i-1][j] or memo[i-1][j-arr[i-1]]

        return memo[-1][-1]


sol = SolutionCase1()
print(sol.subSetSumEqualToK(arr=[2, 5, 3, 4, 2], K=8, index=4))
print(sol.subSetSumEqualToKList(arr=[2, 5, 3, 4, 2], K=8, index=4))
print(sol.subSetSumEqualToKBottomUp(arr=[2, 5, 3, 4, 2], K=8))
# If not divisible then send K = Sum//2 + 1
print(sol.subSetSumEqualToKBottomUp(arr=[4, 5, 3, 4, 4], K=11))
