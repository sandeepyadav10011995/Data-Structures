from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.nums = nums
        self.generatePermutationWithDup([], Counter(nums))
        return self.ans
    
    def generatePermutationWithDup(self, comb, counter):
        # Base Case --> Our Goal
        if len(comb) == len(self.nums):
            self.ans.append(comb[:])
            return
        
        # Explore
        for num in counter:
            if counter[num] > 0:
                comb.append(num)
                counter[num] -= 1
                # continue the exploration
                self.generatePermutationWithDup(comb, counter)
                # Undo the Choice
                comb.pop()
                counter[num] += 1
