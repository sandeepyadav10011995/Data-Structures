"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right,
and replace the last element with -1. After doing so, return the array.

Example 1:
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]

Constraints:
1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5
"""


class Solution:
    def replaceElements(self, nums):
        n = len(nums)
        res = [0] * n
        res[-1] = -1
        j = n-2
        while j >= 0:
            res[j] = max(res[j+1], nums[j+1])
            j -= 1
        return res

nums = [17,18,5,4,6,1]
sol = Solution()
print(sol.replaceElements(nums))
