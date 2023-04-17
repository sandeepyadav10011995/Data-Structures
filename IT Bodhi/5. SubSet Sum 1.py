"""
Sunset Sum1





"""

class Solution:
    def driver(self, nums: list[int]) -> list[int]:
        self.powerset = []
        self.sumSubset = []
        self.generatePowerset(nums, curIdx=0, subSetSum=0, subset=[])
        return self.sumSubset

    def generatePowerset(self, nums: list[int], curIdx: int, subSetSum: int, subset):
        # Base Case -> Our Goal
        if curIdx == len(nums):
            self.sumSubSet.append(subSetSum)
            self.powerset.append(subset[:])
            return

        # Two Choices
        # Pick the item
        subset.append(nums[curIdx])
        self.generatePowerset(nums, curIdx + 1, subSetSum + nums[curIdx], subset)
        subset.pop()

        # Do not pick the item
        self.generatePowerset(nums, curIdx + 1, subSetSum, subset)
