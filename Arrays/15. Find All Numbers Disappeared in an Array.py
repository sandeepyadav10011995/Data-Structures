"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""


class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        for i in range(n):
            index = abs(nums[i]) - 1
            nums[index] = abs(nums[index]) * -1
        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i+1)
        return res


arr = [4,3,2,7,8,2,3,1]
sol = Solution()
print(sol.findDisappearedNumbers(arr))
