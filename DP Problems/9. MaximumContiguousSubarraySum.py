class Solution:
    def maxContiguousSubarraySum(self, nums):
        # Kadane's Algorithm
        global_sum = 0
        running_sum = 0
        for i in range(len(nums)):
            running_sum = max(running_sum+nums[i], nums[i])
            global_sum = max(global_sum, running_sum)

        return global_sum
sol = Solution()
print(sol.maxContiguousSubarraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
#      running_sum      -->         -2, 1, -2, 4,  3, 5, 6,  1, 5
