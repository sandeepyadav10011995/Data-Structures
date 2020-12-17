"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        # # Edge Case
        # if not nums:
        #     return 0
        # max_ones = 0
        # count = 0
        # for i in range(len(nums)):
        #     if nums[i] == 1:
        #         count += 1
        #     else:
        #         count = 0
        #     if count > max_ones:
        #         max_ones = count
        # return max_ones

        # Edge Case
        if not nums:
            return 0
        i , j = 0, 0
        max_ones = 0
        while j < len(nums):
            if nums[j] == 1:
                j += 1
                if j == len(nums) or nums[j] != 1:
                    max_ones = max(max_ones, j-i)
            else:
                j += 1
                i = j
        return max_ones


sol = Solution()
arr = [1,0,1,1,0,1]
print(sol.findMaxConsecutiveOnes(arr))
