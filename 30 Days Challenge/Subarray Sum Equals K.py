"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

"""
# Brute Force Solution --> Iterating all the sub-arrays
class Solution:
    def subarraySum(nums: List[int], k: int) -> int:
        N = len(nums)
        count = 0
        for i in range(N):
            cum_sum = 0
            for j in range(i, N):
                cum_sum += nums[j]
                if cum_sum == k:
                    count += 1
        return count
    
 # Note : This solution time complexity is O(n^2) --> Will lead to Time Limit Exceeded Warning

    
