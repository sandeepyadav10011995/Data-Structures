class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.output = []

    def helper(self, i=0):
        # Base Case
        if i == len(self.nums):
            self.output.append(''.join(self.nums[:]))
            return
        # Loop
        for j in range(i, len(self.nums)):
            # Swap 1
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
            self.helper(i + 1)
            # Swap back
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def permute(self):
        self.helper()
        return self.output

nums_list = 'abc'
sol = Solution(list(nums_list))
print(sol.permute())
