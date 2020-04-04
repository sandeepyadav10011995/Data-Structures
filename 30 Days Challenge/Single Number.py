"""
Single Number : Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4

"""
# Approach : Using the Bitwise operator --> XOR
def singleNumber(nums: List[int]) -> int:
        # Edge case:
        if len(nums) == 1:
            return nums[-1]
        temp = nums[0]
        for i in range(1, len(nums)):
            temp = temp ^ nums[i]
        return temp
        
