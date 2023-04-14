"""
Problem : Count of all sub-array having sum as K
Example -: arr = [2, 4, -1, -1, 2, 1, 1, -1, 3, 4, -2, 1, -2, 1, 3], K=2

Approach 1: Brute Force
            TC: O(N)*O(N^2) ~ O(N^3)
            SC: O(1)

Approach 2: Prefix Sum
            TC: O(N)
            SC: O(N)

Example -:
K = 2
cumSum  2   6   5   4   6   7   8   7   10  14  12  13  11  12  15
arr     2   4   -1  -1  2   1   1   -1  3   4   -2  1   -2  1   3
count   1   0   0   1   1   1   2   1   1   0   1   0   0   1   1
prefixSum = {0: 1, 2: 1, 6: 2, 5: 1, 4: 1, 7: 2, 8: 1, 10: 1, 14: 1,
             12: 2, 13: 1, 11: 1}

Approach 3:
"""

class Solution:
    @staticmethod
    def countSubArrayWithSumK1(nums: list[int], K: int) -> int:
        """
        Edge Case: When 0 is present in the array or duplicates are present nums = [2, 0, 0, 3], K = 3 ==> 3
        Solution: we don't need to override the first occurrence of the number
        """
        N = len(nums)
        prefixCountMap = {0: 1}
        count = 0
        cumSum = 0
        for i in range(N):
            if nums[i] == 0:
                prefixCountMap[0] += 1
            cumSum += nums[i]
            if cumSum == K:
                count += 1
            remSum = cumSum - K
            if remSum in prefixCountMap:
                count += prefixCountMap[remSum]
            if cumSum not in prefixCountMap:
                prefixCountMap[cumSum] = 1
            else:
                prefixCountMap[cumSum] += 1

        return count

    @staticmethod
    def countSubArrayWithSumK2(nums: list[int], K: int) -> int:
        N = len(nums)
        count = 0
        windowStart = 0
        windowSum = 0

        for windowEnd in range(N):
            windowSum += nums[windowEnd]

            while windowSum > K:
                windowSum -= nums[windowStart]
                windowStart += 1

            while windowSum == K:
                windowSum -= nums[windowStart]
                windowStart += 1
                count += 1

        return count


sol = Solution()
print(sol.countSubArrayWithSumK1(nums=[2, 0, 0, 3], K=3))
print(sol.countSubArrayWithSumK2(nums=[2, 0, 0, 3], K=3))
arr = [2, 4, -1, -1, 2, 1, 1, -1, 3, 4, -2, 1, -2, 1, 3]
print(sol.countSubArrayWithSumK1(nums=arr, K=2))
