"""
Maximum Subarray : Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

"""
def maxSubArray(self, nums: List[int]) -> int:
        # Approach 1 : Find the index of negative numbers and find all the sums between them.
        # Approach 2
        # if len(nums) == 0:
        #     return 0
        # max_sum = cur_sum = nums[0]
        # for num in nums[1:]:
        #     # Set cur sum
        #     cur_sum = max(cur_sum + num, num)
        #     # Set max sum
        #     max_sum = max(cur_sum, max_sum)
        # return max_sum
        
        # Approach 3 : Kadane’s Algorithm
        cur_sum, max_sum = 0, 0
        start, end, s = 0, 0, 0
        for i, num in enumerate(nums):
            cur_sum += num
            if max_sum < cur_sum:
                max_sum = cur_sum
                start = s
                end = i
            if cur_sum < 0:
                cur_sum = 0
                s = i + 1
        # print(start, end)
        return max_sum
