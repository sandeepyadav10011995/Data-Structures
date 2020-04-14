"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.

"""
# Cumulative Sum Approach
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        # Convert the 0 to -1 so that cumulative sum becomes zero
        for i in range(N):
            if nums[i] == 0:
                nums[i] = -1
    
        # Required Inputs
        hash_map = {}
        cum_sum = 0
        max_len = 0
        end_idx = -1
        # Traverse the nums list
        for i in range(N):
            cum_sum += nums[i]
            if cum_sum == 0:
                max_len = i+1
                end_idx = i
            if cum_sum in hash_map:
                if max_len < i - hash_map[cum_sum]:
                    max_len = i - hash_map[cum_sum]
            else:
                hash_map[cum_sum] = i
                
         return max_len
        
