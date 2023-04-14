"""
Problem : In an array which has only 1 & 0 values, count all the sub-array which has equal number of 1's and 0's

Example-:
arr = [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0]




----------------------------- COUNTS -----------------------------------
cumSum  1   0   1   0   1   2   1   0  -1   0  -1   0  -1   0   1   2   1   0   1   0
arr     1   0   1   0   1   1   0   0   0   1   0   1   0   1   1   1   0   0   1   0

count   0   1   1   2   2   0   3   3   0   4   1   5   2   6   6   1   5   7   6   8
prefixSumMap 0: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9
             1: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
             2: 1 -> 2
            -1: 1 -> 2 -> 3
--------------------------------- MAX LENGTH ---------------------------
cumSum  1   0   1   0   1   2   1   0  -1   0  -1   0  -1   0   1   2   1   0   1   0
arr     1   0   1   0   1   1   0   0   0   1   0   1   0   1   1   1   0   0   1   0
index   0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18 19

maxL    0   2   2   2   2   2   3   3   3   4   4   5   5   6   6   6   6   7   7   8
prefixSumMap<Key:CumSum, Value:Index>
             0: 1 ->
             1: 0 ->
             2:
            -1:

Approach 1: Brute Force explore all the sub-arrays
            TC: O(N^2)

Approach 2: Convert the problem into maxLengthSubarray of K sum where K = 0 by considering 0 as -1

"""


class SubArray:
    @staticmethod
    def longestSubArrayWithEqualZeroAndOne(nums: list[int], K: int) -> int:
        """
        Edge Case: When 0 is present in the array or duplicates are present nums = [2, 0, 0, 3], K = 3 ==> 3
        Solution: we don't need to override the first occurrence of the number
        """
        prefixSumMap = {0: 1}
        maxSubArrayLen = 0

        cumSum = 0
        for i in range(len(nums)):
            cumSum += -1 if nums[i] == 0 else nums[i]
            if cumSum == K:
                maxSubArrayLen = max(maxSubArrayLen, i + 1)
            remSum = cumSum - K
            if remSum in prefixSumMap:
                maxSubArrayLen = max(maxSubArrayLen, i - prefixSumMap[remSum])
            if cumSum not in prefixSumMap:
                prefixSumMap[cumSum] = i

        return maxSubArrayLen

    @staticmethod
    def countSubArrayWithEqualZeroAndOne(nums: list[int]) -> int:
        N = len(nums)
        count = 0
        cumSum = 0
        prefixSumMap = {0: 1}
        cumSumList = []
        for i in range(N):
            cumSum += -1 if nums[i] == 0 else nums[i]
            cumSumList.append(cumSum)
            if cumSum in prefixSumMap:
                count += prefixSumMap[cumSum]
                prefixSumMap[cumSum] += 1
            else:
                prefixSumMap[cumSum] = 1

        return count


arr = [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0]
arr1 = [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1]
sb = SubArray()
print(sb.countSubArrayWithEqualZeroAndOne(nums=arr))
print(sb.longestSubArrayWithEqualZeroAndOne(nums=arr1, K=0))
