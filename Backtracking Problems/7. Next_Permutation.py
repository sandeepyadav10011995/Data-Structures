class Solution:
    def __init__(self, nums):
        self.nums = nums

    def _reverse(self, start):
        i = start
        j = len(self.nums) - 1
        # Reverse the Decreasing Order --> Increasing Order
        while i < j:
            self._swap(i, j)
            i += 1
            j -= 1

    def _swap(self, i, j):
        temp = self.nums[i]
        self.nums[i] = self.nums[j]
        self.nums[j] = temp

    def nextPermutation(self):
        i = len(self.nums) - 2
        # Looping to find the non-decreasing point !!
        while i >= 0 and self.nums[i + 1] <= self.nums[i]:
            i -= 1
        if i >= 0:
            j = len(self.nums) - 1
            # Find the next big number to ith position number
            while j >= 0 and self.nums[j] <= self.nums[i]:
                j -= 1
            # Swap
            self._swap(i, j)
        self._reverse(i + 1)


l = [6,2,1,5,4,3,0]
abc = Solution(l)
abc.nextPermutation()
print(abc.nums)
