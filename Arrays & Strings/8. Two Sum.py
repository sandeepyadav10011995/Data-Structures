class Solution:
    def twoSum1(self, nums, target): # If the array is not sorted --> Go with this approach
        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                return [hash_map[nums[i]], i]
            else:
                hash_map[target-nums[i]] = i
        return []

    def twoSum2(self, nums, target): # If the array is sorted --> Go with this approach(Two Pointers)
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left, right]
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return []
"""
questions:
    - sorted?
    - duplicates?
    - negative values?
    - multiple solutions?
"""
nums = [2,7,11,15]
target = 9
sol = Solution()
print(sol.twoSum1(nums, target))
print(sol.twoSum2(nums, target))
