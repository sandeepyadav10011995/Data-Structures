"""
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place, do not return anything from your function.

Example 1:
Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:
Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]

Note:
1 <= arr.length <= 10000
0 <= arr[i] <= 9
"""


class Solution:
    def duplicateZeros(self, nums):
        """
            Do not return anything, modify arr in-place instead.
        """
        # Using Queue
        queue = nums[:]
        last_index_is_zero = False
        for index in range(len(nums)):
            if last_index_is_zero:
                nums[index] = 0
                last_index_is_zero = False
                continue
            num = queue.pop(0)
            nums[index] = num
            if num == 0:
                last_index_is_zero = True
        del queue
        return nums



arr = [1,0,2,3,0,4,5,0]
sol = Solution()
print(sol.duplicateZeros(arr))
