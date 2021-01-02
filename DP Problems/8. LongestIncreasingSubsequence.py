class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0

        dp_table = [1] * len(nums)
        global_length = 1
        for i in range(1, len(dp_table)):
            running_length = 0
            for j in range(i):
                if nums[i] > nums[j]:
                    running_length = max(running_length, dp_table[j])
            dp_table[i] = running_length + 1
            global_length = max(global_length, dp_table[i])
        return global_length

sol = Solution()
print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101]))
