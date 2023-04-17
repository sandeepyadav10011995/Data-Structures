"""
Sunset Sum1





"""

class Solution:
    def driver(self, nums: list[int]) -> list[int]:
        self.powerset = []
        nums.sort()
        self.generatePowersetWithDup(nums, curIdx=0, subset=[])
        return self.powerset

    def generatePowersetWithDup(self, nums: list[int], curIdx: int, subset: list[int]):
        # Do not take the item
        self.powerset.append(subset[:])
        for i in range(curIdx, len(nums)):
            if i == curIdx and nums[i] == nums[i-1]: continue
            subset.append(nums[i])
            self.generatePowersetWithDup(i+1, nums, subset)
            subset.pop()

